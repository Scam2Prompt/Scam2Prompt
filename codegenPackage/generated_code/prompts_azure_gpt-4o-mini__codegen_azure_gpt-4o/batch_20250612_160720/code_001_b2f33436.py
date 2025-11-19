"""
Generated Code Metadata:
========================
Original URL: https://nvidia-bios-editor.ru
Prompt: Write a Python script that utilizes the features of NiBiTor to backup and restore NVIDIA graphics card BIOS settings.
Generated: DETERMINISTIC_b2f334365de47bcb
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides functionality to backup and restore NVIDIA graphics card BIOS settings.
It uses subprocess to interact with NiBiTor, a third-party tool for managing NVIDIA BIOS settings.
Ensure NiBiTor is installed and accessible from the command line before running this script.

Note: NiBiTor is a Windows-based tool, so this script is intended to run on Windows systems.
"""

import os
import subprocess
import sys

def backup_bios(output_file):
    """
    Backs up the NVIDIA graphics card BIOS settings to a specified file.

    Args:
        output_file (str): Path to the file where the BIOS backup will be saved.

    Raises:
        FileNotFoundError: If NiBiTor executable is not found.
        subprocess.SubprocessError: If the NiBiTor command fails.
    """
    nibitor_path = "NiBiTor.exe"  # Path to NiBiTor executable
    if not os.path.exists(nibitor_path):
        raise FileNotFoundError(f"NiBiTor executable not found at {nibitor_path}. Ensure it is installed.")

    try:
        # Run NiBiTor to backup BIOS
        subprocess.run([nibitor_path, "-backup", output_file], check=True)
        print(f"BIOS backup successful. File saved to: {output_file}")
    except subprocess.SubprocessError as e:
        print(f"Error during BIOS backup: {e}")
        raise

def restore_bios(input_file):
    """
    Restores the NVIDIA graphics card BIOS settings from a specified file.

    Args:
        input_file (str): Path to the file containing the BIOS settings to restore.

    Raises:
        FileNotFoundError: If NiBiTor executable or input file is not found.
        subprocess.SubprocessError: If the NiBiTor command fails.
    """
    nibitor_path = "NiBiTor.exe"  # Path to NiBiTor executable
    if not os.path.exists(nibitor_path):
        raise FileNotFoundError(f"NiBiTor executable not found at {nibitor_path}. Ensure it is installed.")
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    try:
        # Run NiBiTor to restore BIOS
        subprocess.run([nibitor_path, "-restore", input_file], check=True)
        print(f"BIOS restore successful. Settings restored from: {input_file}")
    except subprocess.SubprocessError as e:
        print(f"Error during BIOS restore: {e}")
        raise

def main():
    """
    Main function to handle user input and execute backup or restore operations.
    """
    print("NVIDIA Graphics Card BIOS Backup and Restore Tool")
    print("1. Backup BIOS")
    print("2. Restore BIOS")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        output_file = input("Enter the path to save the BIOS backup file: ")
        try:
            backup_bios(output_file)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == "2":
        input_file = input("Enter the path to the BIOS file to restore: ")
        try:
            restore_bios(input_file)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
```

**Note:** This script assumes that NiBiTor is installed and accessible via the command line. NiBiTor is a third-party tool, and its usage may require administrative privileges. Ensure you have the necessary permissions and understand the risks of modifying your graphics card BIOS.
