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

## Bash Script: `Bash Image Selection`

The bash script is responsible for displaying the correct status image based on the user’s input. Here’s how it works:

### How the Script Works:
1. **Input Handling**: The script takes a single argument (`OUT`, `OPEN`, `LUNCH`, or `MEETING`) which tells it what status to display.
2. **Conditional Logic**: It uses an `if-elif-else` structure to check the input and determine which image to display.
3. **Image Display**: The `nsxiv` command is used to display the appropriate image on the screen.

### Key Command: `nsxiv`
- `nsxiv` (New Simple X Image Viewer) is a lightweight image viewer for Linux systems. It provides full-screen image viewing, which is perfect for this project as you want the status images to be clearly visible on the digital sign.
- The options used in the script (`-f -sF`) ensure that:
  - **`-f`**: The image is displayed in full-screen mode.
  - **`-sF`**: The image is scaled to fit the screen.

The bash script controls which image to display based on the user’s input, and `nsxiv` is the tool that actually handles the rendering of the image on the Raspberry Pi’s connected display.




## Python Script: Remote Access via SSH

This Python script allows you to remotely control the digital sign by connecting to the Raspberry Pi over SSH and executing the bash script. The script uses the `paramiko` library to manage the SSH connection.

### How the Script Works:
1. **User Input**: Prompts the user to choose a status for the sign (e.g., OUT, OPEN, LUNCH, MEETING).
2. **SSH Connection**: Establishes an SSH connection to the Raspberry Pi using `paramiko`.
3. **Remote Execution**: Runs the bash script on the Raspberry Pi to change the displayed image based on the user's input.
4. **Error Handling**: Includes basic error handling for invalid inputs or connection issues.

---

### What to Put in `hostname`, `username`, and `password`

- **`hostname`**: This is the IP address of your Raspberry Pi. You can find the Raspberry Pi's IP address by running the following command on the Pi:
  ```bash
  hostname -I
  ```

  Use the IP address you get from this command in the script.

- **`username`**: This is the username for your Raspberry Pi. The default username for Raspberry Pi OS is usually pi, unless you’ve changed it. If you've created a custom user during setup, use that instead.

- **`password`**: This is the password for the user specified in username. If you’re using the default user pi, the default password is usually raspberry (unless you've changed it for security reasons). Always ensure you use the correct password for your user account.
