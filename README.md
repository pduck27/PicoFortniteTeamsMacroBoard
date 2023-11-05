# Pico Fortnite and Teams Macro Board

This project is about a typical macro keyboard based on Raspberry Pi Pico connected via USB to my PC. It emulates keyboard strokes and can be used for two scenarios. 
First I use it to glitch some XP points in Fortnite by emulating several movements, so I dont need to be present at PC. 
Second it is used for Home Office and work with Microsoft Teams. I can mute microphone and camera with it.
A couple of buttons and a display make it easier to control. The _red button_ resets the board, the other three buttons are for navigation in the menu.

Main menu when connecting the board or reset:
![mainmenu](/githubresource/MainMenu.jpg)

Fortnite menu with two modes _walk in circles_ and _run forward_:
![mainmenu](/githubresource/FortniteMenu.jpg)

Teams menu with two modes _(Un)mute microphone_ and _(Un)mute camera_:
![mainmenu](/githubresource/TeamsMenu.jpg)

The three buttons are assigned to the shown tiles on the menu and switch the modes. The Teams modes are momentary (Mute / Unmute) and the Fortnite modes are permanent. 
![mainmenu](/githubresource/FortniteRunning.jpg)

The Fortnite modes can be canceled with the _return button (here green)_ but it could be that some of the send keystrokes will be executed still anyway ⚠️. If you are totally lost then push the _reset button (here red)_.

# Requirements
You need the following by now:
 - A [https://www.raspberrypi.com/products/raspberry-pi-pico/](Raspberry Pi Pico) connected via USB
 - A seperate Display. I used a [https://www.az-delivery.de/products/1-3zoll-i2c-oled-display](1,3" OLED I2C 128 x 64 Pixel Display with a SSH 1106 controller). ⚠️ If you use another display you must adjust the display settings in the code.
 - A couple of momentary switches.
 - For development I used [https://thonny.org/](Thonny GUI) and [https://circuitpython.org/board/raspberry_pi_pico/](Circuit Python) because it supports the Keyboard HID better. You must add the [https://docs.circuitpython.org/projects/display_text/en/latest/index.html](following libraries from Adafruit) then manually:
   - _adafruit_display_text_
   - _adafruit_displayio_
   - _adafruit_hid_
   - For adjusting the spritesheets / icons I recommend this [https://gist.github.com/todbot/99ee476b600e19da7793a94155ff3805](Emoji Flipper project from todbot). I helps to understand and find the right tool.
 
