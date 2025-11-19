"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Develop a script to scan and list all screen savers installed on a Windows system, ensuring compatibility with the formats provided on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_e90ef8305fda2fb2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import ctypes

def get_screen_savers():
    """
    Retrieves a list of installed screen savers on a Windows system.

    Returns:
        list: A list of paths to the screen saver files.
    """
    # Define the possible screen saver file extensions
    extensions = ['.scr']

    # Define the possible screen saver locations
    locations = [
        r'C:\Windows\System32',  # Default system32 location
        r'C:\Windows\SysWOW64',  # Default syswow64 location for 64-bit systems
    ]

    # Initialize an empty list to store the screen saver paths
    screen_savers = []

    # Iterate over each location
    for location in locations:
        # Check if the location exists
        if os.path.exists(location):
            # Iterate over each file in the location
            for filename in os.listdir(location):
                # Check if the file has a screen saver extension
                if os.path.splitext(filename)[1].lower() in extensions:
                    # Append the full path to the screen saver file to the list
                    screen_savers.append(os.path.join(location, filename))

    return screen_savers

def validate_screen_saver(file_path):
    """
    Validates a screen saver file by checking its file signature.

    Args:
        file_path (str): The path to the screen saver file.

    Returns:
        bool: True if the file is a valid screen saver, False otherwise.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return False

        # Check the file signature
        with open(file_path, 'rb') as file:
            # The first 2 bytes of a screen saver file should be 'SCR'
            signature = file.read(2).decode('utf-8')
            return signature == 'SCR'
    except Exception as e:
        print(f"Error validating screen saver: {e}")
        return False

def main():
    # Get the list of screen savers
    screen_savers = get_screen_savers()

    # Validate and print the screen savers
    for screen_saver in screen_savers:
        if validate_screen_saver(screen_saver):
            print(screen_saver)

if __name__ == "__main__":
    # Check if the script is running with admin privileges
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Please run the script with admin privileges.")
    else:
        main()
```
