# Pico Fortnite and Teams Macro Board

This project is about a typical macro keyboard based on Raspberry Pi Pico connected via USB to my PC. It emulates keyboard strokes and can be used for two scenarios. 
First I use it to collect some XP points in Fortnite by emulating several movements to glitch in special XP levels. So I don't need to be present at my PC. 
Second it is used for Home Office and works with Microsoft Teams. I can (un-)mute microphone and camera with it.
A couple of buttons and a display make it easier to control. The _red button_ resets the board, the other three buttons are for navigation in the menu.

Main menu when connecting the board or reset:

![mainmenu](/githubresource/MainMenu.jpg)

Fortnite menu with two modes _walk in circles_ and _run forward_. These are the most common movesets I use for the several XP levels:

![mainmenu](/githubresource/FortniteMenu.jpg)

Teams menu with two modes _(un)mute microphone_ and _(un)mute camera_:

![mainmenu](/githubresource/TeamsMenu.jpg)

The three buttons are assigned to the shown tiles on the menu and switch the modes or return to previous menu. The Teams modes are momentary (mute / unmute) and the Fortnite modes are permanent. 

![mainmenu](/githubresource/FortniteRunning.jpg)

The Fortnite modes can be canceled with the _return button_ (here green). ⚠️ But it could happen that some of the still send keystrokes will be executed anyway until it stops. If you are totally lost then push the _reset button_ (here red).

# Requirements
You need the following by now:
 - A [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) connected via USB
 - A separate Display. I used a [1,3" OLED I2C 128 x 64 Pixel Display with a SSH 1106 controller](https://www.az-delivery.de/products/1-3zoll-i2c-oled-display). ⚠️ If you use another display you must adjust the display settings in the code.
 - A couple of momentary switches.
 - For development I used [Thonny GUI](https://thonny.org/) and [Circuit Python](https://circuitpython.org/board/raspberry_pi_pico/) because it supports the Keyboard HID better. You must add the [following libraries from Adafruit](https://docs.circuitpython.org/projects/display_text/en/latest/index.html) then manually:
   - _adafruit_display_text_
   - _adafruit_displayio_
   - _adafruit_hid_
   - For adjusting the spritesheets / icons I recommend this [Emoji Flipper project from todbot](https://gist.github.com/todbot/99ee476b600e19da7793a94155ff3805). It helps to understand the logic and find the right tool to create spritesheets.
  
# Wiring
To check and change the wired GPIO pins please also have a look in the code.
   - The three menu buttons are connected to GPIO 0, 1 and 2 and soldered with a resistor to ground.
   - The reset button is connected to the RUN pin [as described here](https://www.raspberrypi.com/news/how-to-add-a-reset-button-to-your-raspberry-pi-pico/).
   - Display I2C is on GPIO 16 and 17. Power and ground are connected to the Pico pins. 
 
# Not used random mode
There is also an implemented _Fortnite Random mode_ which is not in use by now.
