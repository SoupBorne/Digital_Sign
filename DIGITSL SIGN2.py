#module neccessary to SSH into a linux sysem wihth python
import paramiko

# User choice
choice = input("Hello, I am your virtual sign and I need you to pick an option to display. There are 4 options to choose from: OUT, OPEN, LUNCH, and MEETING: ")

#Decision structure being used to identify/verify input and User choice
if choice == "OUT":
    print("This is a valid input")
elif choice == "OPEN":
    print("This is a valid input")
elif choice == "LUNCH":
    print("This is a valid input")
elif choice == "MEETING":
    print("This is a valid input")
else:
    print("This is an invalid input")
    exit()  # Exit the script if the input is invalid

# SSH connection details
hostname = #'Your IP goes here'
port = 22
username = #'Your Username goes here'
password = #'Your Password goes here'
display = 'export DISPLAY=:0'
script_path = #'Direct path to your sign script'
command = f'{display} && {script_path} {choice}'

# Create an SSH client instance
ssh = paramiko.SSHClient()

# Automatically add the server's host key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect(hostname, port, username, password)
    
    # Execute the command on the remote server
    stdin, stdout, stderr = ssh.exec_command(command)
    
    # Read and print the output
    print(stdout.read().decode())
    print(stderr.read().decode())
    
except Exception as e:
    print(f"An error has occurred: {e}")
    
finally:
    # Close the connection
    ssh.close()
print("System Close")