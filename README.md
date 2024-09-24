# Digital_Sign
# Raspberry Pi Digital Sign

This project allows you to create a digital sign using a Raspberry Pi. The sign can display different statuses such as "Out of Office", "Open", "Lunch", or "In a Meeting". The display is controlled via a simple script and can be accessed remotely using SSH.

## Features
- Display custom status images based on input commands.
- Remotely control the sign via SSH.
- Easy to customize with different images.

## Materials
- Raspberry Pi
- Micro SD card
- Micro SD card adapter
- USB Stick
- HDMI cord
- Canakit Power Cable
- Monitor
- Keyboard 
- Mouse

## How It Works
This project uses a bash script on the Raspberry Pi to display images, and a Python script to control the sign remotely via SSH.

### Script Overview
1. **`Bash Image Selection`**: A bash script that takes an argument (`OUT`, `OPEN`, `LUNCH`, or `MEETING`) and displays a corresponding image using the `nsxiv` image viewer.
2. **`Python Remote Access `**: A Python script that connects to the Raspberry Pi over SSH and runs the bash script to change the displayed image.
