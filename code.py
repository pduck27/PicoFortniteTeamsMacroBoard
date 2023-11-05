# Support for Spritesheet creation: https://gist.github.com/todbot/99ee476b600e19da7793a94155ff3805

import board
import digitalio
import time
import usb_hid
import random
import busio
import displayio
import terminalio
from adafruit_displayio import adafruit_displayio_sh1106
from adafruit_display_text import label
from adafruit_display_text import scrolling_label
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

MODE_INIT = "Start"
MODE_NONE = "None"
MODE_FORTNITE = "Fortnite"
MODE_TEAMS = "Teams"
SUBMODE_F_CIRCLE = "Fortnite Circle"
SUBMODE_F_FORWARD = "Fortnite Forward"
SUBMODE_F_RANDOM = "Fortnite Random" # not in use
SUBMODE_T_MIC = "Teams Microphone"
SUBMODE_T_VIDEO = "Teams Video"

keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

button1 = digitalio.DigitalInOut(board.GP0)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP1)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.GP2)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

nextDirection = 0
ignoreButtonState = False
prevMode = MODE_INIT
currMode = MODE_NONE
prevSubMode = MODE_INIT
currSubMode = MODE_NONE

def showDebugInfo(blinkNo):
    print(f'Mode: {currMode}')
    print(f'Submode: {currSubMode}')
    print(f'Button1: {button1.value}')
    print(f'Button2: {button2.value}')
    print(f'Button3: {button3.value}')
    blink(blinkNo)
   
def blink(blinks):
    ignoreButtonState = True
    led.value = False
    i = 0
    
    while i < blinks:
       led.value = True
       time.sleep(0.1)
       led.value = False
       time.sleep(0.1)
       i += 1
       
    ignoreButtonState = False
    
def modeSwitch():   
    global sprite
    
    if (currMode != prevMode) or (currSubMode != prevSubMode):
        print(f'Switching to Mode {currMode} with Submode {currSubMode}.')
    
        if currMode == MODE_FORTNITE:
            sprite[0] = 4
            sprite[1] = 5
            sprite[2] = 3
        elif currMode == MODE_TEAMS:
            sprite[0] = 6
            sprite[1] = 7
            sprite[2] = 3
        else:
            sprite[0] = 1
            sprite[1] = 2
            sprite[2] = 3         
    

def clearSubMode():
    global prevSubMode
    global currSubMode
    
    prevSubMode = MODE_INIT
    currSubMode = MODE_NONE   
    
    clearModeFinal()
    
def clearMainMode():
    global currMode
    
    clearSubMode()
    currMode = MODE_INIT
    clearModeFinal()
    
def clearModeFinal():
    keyboard.release_all()
    modeSwitch()
    

# Teams Microphone
def teamsSwitchMicrophone():    
    keyboard.release_all()
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.M)        
    time.sleep(0.5)
    
# Teams Microphone
def teamsSwitchVideo():
    keyboard.release_all()
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.SHIFT, Keycode.O)    
    time.sleep(0.5)

# Fortnite moves with cancel possibility
def moveAndWaitForCancel(sec):
    for i in range(sec * 10):
        time.sleep(sec / 100)
        if button3.value:
            showDebugInfo(3)                        
            clearSubMode()
            return

# Fortnite random movement. Not used yet.
def fortniteRandom():     
    keyboard.release_all()
    
    nextDirection = random.randint(0, 8)
    if nextDirection == 0:
        print("do nothing")
    elif nextDirection == 1:
        print("go forward")
        keyboard.press(Keycode.W)
    elif nextDirection == 2:
        print("go right")
        keyboard.press(Keycode.D)
    elif nextDirection == 3:
        print("go back")
        keyboard.press(Keycode.S)
    elif nextDirection == 4:
        print("go left")
        keyboard.press(Keycode.A)
    elif nextDirection == 5:
        print("go left")
        keyboard.press(Keycode.SPACEBAR)
    elif nextDirection == 6:
        print("emote")
        keyboard.press(Keycode.B)
        time.sleep(2)
        keyboard.release(Keycode.B)
    elif nextDirection == 7:
        print("left click")
        mouse.move(0,0,random.randint(1,10))
        mouse.press(Mouse.LEFT_BUTTON)
        time.sleep(2)
        mouse.release(Mouse.LEFT_BUTTON)        
    elif nextDirection == 8:
        print("mouse move")
        mouse.move(random.randint(-500,500), random.randint(-50,50),0)        
        
    time.sleep(random.randint(2,8))
    
    keyboard.release_all()    
     
# Fortnite circle movement
def fortniteCircle():              
     keyboard.release_all()
     sec = random.randint(2,8)
     
     keyboard.press(Keycode.W)
     moveAndWaitForCancel(sec)
     keyboard.release_all()     
    
     keyboard.press(Keycode.D)
     moveAndWaitForCancel(sec)
     keyboard.release_all()     
     
     keyboard.press(Keycode.S)
     moveAndWaitForCancel(sec)
     keyboard.release_all()
          
     keyboard.press(Keycode.A)
     moveAndWaitForCancel(sec)
     keyboard.release_all()
     
     keyboard.release_all()  
    
     
# Fortnite straight forward 
def fortniteStraightForward():      
    keyboard.release_all()
    
    keyboard.press(Keycode.W, Keycode.SHIFT)
    moveAndWaitForCancel(5)
    keyboard.release(Keycode.SHIFT)
    
    keyboard.release_all()
    time.sleep(1)
    
    keyboard.press(Keycode.W, Keycode.SHIFT)    
    moveAndWaitForCancel(8)    
    keyboard.release(Keycode.SHIFT)
    
    keyboard.release_all()
     

# Init Display
displayio.release_displays()
i2c = busio.I2C(scl=board.GP17, sda=board.GP16) # This RPi Pico way to call I2C
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)

WIDTH = 132
HEIGHT = 64
BORDER = 5
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

### SPRITE START
sprite_fname = "spritesheet.bmp"
sprite_cnt = 3*1
sprite_w,sprite_h = 40,40

sprite_sheet = displayio.OnDiskBitmap(open(sprite_fname, "rb"))
sprite_palette = sprite_sheet.pixel_shader
# this below will be faster than OnDiskBitmap, but not all boards have enough RAM
# import adafruit_imageload
# sprite_sheet, sprite_palette = adafruit_imageload.load(sprite_fname)

sprite_palette.make_transparent(0)  # make background color transparent

sprite = displayio.TileGrid(sprite_sheet, pixel_shader=sprite_palette,
                            width = 3, height = 1,
                            tile_width = sprite_w, tile_height = sprite_h)

maingroup = displayio.Group(scale=1) # make 4x big
maingroup.append(sprite)
display.show(maingroup)
sprite[0] = 1
sprite[1] = 2
sprite[2] = 3
maingroup.x = 6
maingroup.y = ((HEIGHT - sprite_h) // 2 - 1) + 3
### SPRITE END

# Start main loop
print("Wait for button press.")


while True:       
    
    prevSubMode = currSubMode
    prevMode = currMode
    
    if not ignoreButtonState:
        led.value = False
        
        if currMode == MODE_FORTNITE:
            if button1.value:
                showDebugInfo(1)
                currSubMode = SUBMODE_F_CIRCLE                       
                
            elif button2.value:
                showDebugInfo(2)
                currSubMode = SUBMODE_F_FORWARD                
                
            elif button3.value:
                showDebugInfo(3)
                clearSubMode()
            
        elif currMode == MODE_TEAMS:
            if button1.value:
                showDebugInfo(1)
                currSubMode = SUBMODE_T_MIC                          
                
            elif button2.value:
                showDebugInfo(2)
                currSubMode = SUBMODE_T_VIDEO
                
            elif button3.value:
                showDebugInfo(3)
                clearSubMode()
                
        else: # main menu
            if button1.value:
                showDebugInfo(1)
                currMode = MODE_FORTNITE                          
                
            elif button2.value:
                showDebugInfo(2)
                currMode = MODE_TEAMS
                
            elif button3.value:
                showDebugInfo(3)
                clearMainMode()
            
            
    modeSwitch()    
 
    # Repeating SubMode runs
    if currSubMode == SUBMODE_F_CIRCLE:
        sprite[1] = 0
        fortniteCircle()
    elif currSubMode == SUBMODE_F_FORWARD:      
        sprite[0] = 0
        fortniteStraightForward()      
    elif currSubMode == SUBMODE_T_MIC:
        sprite[0] = 8
        teamsSwitchMicrophone()
        clearSubMode()
    elif currSubMode == SUBMODE_T_VIDEO:
        sprite[1] = 8
        teamsSwitchVideo()
        clearSubMode()      
           
    time.sleep(0.1) 
