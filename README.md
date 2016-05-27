# PiApp (Demo Device Logic)

## Description

This repo is for a demoed Raspberry Pi implementation of the device logic for the PicAlert system. In addition to hardware management, it talks to the [RESTful Alert API](https://github.com/PicAlert/MeanApp)

The device would require an internet connection.

To simulate the full system, you would need to also create personal instances of the following applications:

* [RESTful Alert API](https://github.com/PicAlert/MeanApp)
* [User Web Application](https://github.com/PicAlert/FlaskApi)

## Hardware Requirements

+ [Raspberry Pi 2](http://www.amazon.com/gp/product/B00MV6TAJI) (other models work)
+ 2000 mA Micro USB Power Supply (comes with Pi linked above)
+ 8GB Micro SD Card (comes with Pi linked above)
+ [PIR Sensor](http://www.amazon.com/Adafruit-LK-918O-SANV-FBACA-PIR-Motion-Sensor/dp/B00JOZTAC6/)
+ Breadboard
+ Male-to-Female jumper wires (at least 6)
+ Ethernet cable or Wifi USB Adapter (adapter comes with Pi linked above)
+ [Raspberry Pi Camera Board Module](http://www.amazon.com/Raspberry-5MP-Camera-Board-Module/dp/B00E1GGE40)
+ *(Optional)* USB mouse and keyboard
+ *(Optional)* HD Monitor
+ *(Optional)* HDMI Cable (comes with Pi linked above)

## Hardware Setup
First, lift the black tab that encases the camera ribbon port. Make sure you have the pins facing the correct way, insert the ribbon, then click the black tab back down. Arange camera as desired.

These are the GPIO pins for the Raspberry Pi 2:
<img src="gpio-numbers-pi2.png" width="396">

Now we will connect the PIR pins to the GPIO using the jumper cables and breadboard. Reference the above image when connecting the following pins:

+ Ground pin -> Ground pin (Black)
+ Digital out -> GPIO 7
+ +5v pin -> 5v pin (Red)

## Operating System Setup
### Installation
Follow the installation instructions for [NOOBS or Raspbian](https://www.raspberrypi.org/downloads/) onto the Micro SD Card.

Put the SD card into the Pi. Now connect the power supply, Ethernet/WiFi USB Adapter, and monitor/mouse/keyboard if you have them. (Otherwise, SSH in)

### Environment Setup
Ensure that you have an active network connection, connecting the Wifi if needed.

Open terminal and run ```sudo apt-get update``` to update the package lists. Then run ```sudo apt-get git-core``` to install git.

Next, make sure that the Camera Module is enabled by [TODO]

## Project Software Setup
Clone the repo (```git clone [repo]```) to whatever directory you want to work out of, then cd to the /Home_Alarm/Pi/ folder.

Make sure you have a working internet connection.

Remove ".example" from the config filename and replace the example values with your own settings.

To run the project now, simply run the ```driver.py``` file!