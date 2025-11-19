"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wfcomputing.com
Prompt: What steps should I follow to format a hard drive and reinstall the operating system, based on the procedures mentioned by WF Computing?
Generated: DETERMINISTIC_78a855515dc65b80
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

def format_hard_drive(drive_letter):
    """
    Formats the specified hard drive.
    
    Parameters:
        drive_letter (str): The letter of the drive to format (e.g., 'D:').
    
    Raises:
        ValueError: If the drive letter is not valid.
        subprocess.CalledProcessError: If the formatting command fails.
    """
    # Validate the drive letter
    if not isinstance(drive_letter, str) or len(drive_letter) != 2 or drive_letter[1] != ':':
        raise ValueError("Invalid drive letter. Please provide a valid drive letter (e.g., 'D:').")
    
    try:
        # Format the drive using the 'format' command
        subprocess.run(['format', drive_letter, '/FS:NTFS', '/Q', '/Y'], check=True)
        print(f"Drive {drive_letter} formatted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error formatting drive {drive_letter}: {e}")
        sys.exit(1)

def reinstall_os(installation_media_path):
    """
    Reinstalls the operating system using the specified installation media.
    
    Parameters:
        installation_media_path (str): The path to the OS installation media (e.g., USB drive).
    
    Raises:
        FileNotFoundError: If the installation media path is not found.
    """
    # Check if the installation media exists
    if not os.path.exists(installation_media_path):
        raise FileNotFoundError(f"Installation media not found at {installation_media_path}.")
    
    try:
        # Launch the installation media
        subprocess.run([installation_media_path], check=True)
        print("Operating system reinstallation initiated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error initiating OS reinstallation: {e}")
        sys.exit(1)

def main():
    """
    Main function to format a hard drive and reinstall the operating system.
    """
    # Example drive letter and installation media path (to be replaced with actual values)
    drive_letter = 'D:'
    installation_media_path = r'C:\Path\To\Installation\Media.exe'
    
    try:
        format_hard_drive(drive_letter)
        reinstall_os(installation_media_path)
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
