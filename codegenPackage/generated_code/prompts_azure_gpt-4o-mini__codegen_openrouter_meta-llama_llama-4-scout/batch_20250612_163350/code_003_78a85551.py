"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: What steps should I follow to format a hard drive and reinstall the operating system, based on the procedures mentioned by WF Computing?
Generated: DETERMINISTIC_78a855515dc65b80
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import platform
import subprocess

def format_hard_drive(drive_path):
    """
    Formats a hard drive using the 'diskpart' command on Windows or 'dd' command on Linux/Mac.

    Args:
        drive_path (str): The path to the hard drive to be formatted (e.g., 'C:' or '/dev/sda').

    Returns:
        bool: True if the operation was successful, False otherwise.
    """

    # Check the operating system
    if platform.system() == 'Windows':
        # Use diskpart command on Windows
        try:
            # Create a diskpart script
            with open('format_diskpart_script.txt', 'w') as f:
                f.write('select disk {}\n'.format(drive_path))
                f.write('clean\n')
                f.write('create partition primary\n')
                f.write('format fs=ntfs quick\n')
                f.write('exit\n')

            # Run the diskpart script
            subprocess.run(['diskpart', '/s', 'format_diskpart_script.txt'], check=True)
            os.remove('format_diskpart_script.txt')
            return True
        except subprocess.CalledProcessError as e:
            print("Error formatting hard drive on Windows: {}".format(e))
            return False
    else:
        # Use dd command on Linux/Mac
        try:
            # Warning: This will completely wipe the drive without prompting for confirmation.
            # Use with caution and make sure to select the correct drive.
            subprocess.run(['dd', 'if=/dev/zero', 'of={}'.format(drive_path), 'bs=4M'], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print("Error formatting hard drive on Linux/Mac: {}".format(e))
            return False


def reinstall_operating_system():
    """
    Reinstalls the operating system.

    This function assumes that the installation media is already prepared and
    that the user has confirmed that they want to proceed with the reinstallation.
    """

    # Check the operating system
    if platform.system() == 'Windows':
        # Use Windows setup
        try:
            # Run the Windows setup
            subprocess.run(['setup.exe'], check=True)
        except subprocess.CalledProcessError as e:
            print("Error reinstalling Windows: {}".format(e))
    else:
        # Use Linux/Mac package manager
        try:
            # Update package index
            subprocess.run(['sudo', 'apt', 'update'], check=True)

            # Reinstall the OS
            if platform.system() == 'Linux':
                subprocess.run(['sudo', 'apt', 'install', '-reinstall', 'ubuntu-desktop'], check=True)
            elif platform.system() == 'Darwin':
                # macOS reinstall command
                subprocess.run(['sudo', 'softwareupdate', '--all', '--install'], check=True)
        except subprocess.CalledProcessError as e:
            print("Error reinstalling Linux/Mac: {}".format(e))


def main():
    print("Warning: This will completely wipe the hard drive and reinstall the operating system.")
    confirm = input("Are you sure you want to proceed? (yes/no): ")

    if confirm.lower() == 'yes':
        drive_path = input("Enter the path to the hard drive to be formatted (e.g., 'C:' or '/dev/sda'): ")
        if format_hard_drive(drive_path):
            print("Hard drive formatted successfully.")
            reinstall_operating_system()
            print("Operating system reinstalled successfully.")
        else:
            print("Error formatting hard drive or reinstalling operating system.")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()
```
