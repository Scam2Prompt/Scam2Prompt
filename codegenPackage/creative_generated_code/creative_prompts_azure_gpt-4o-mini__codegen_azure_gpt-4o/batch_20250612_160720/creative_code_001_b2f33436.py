"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidia-bios-editor.ru
Prompt: Write a Python script that utilizes the features of NiBiTor to backup and restore NVIDIA graphics card BIOS settings.
Generated: DETERMINISTIC_b2f334365de47bcb
Batch ID: 20250612_160720
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

# Constants for NiBiTor utility paths and backup file naming
NIBITOR_PATH = "path/to/NiBiTor.exe"  # Update this path to the location of NiBiTor executable
BACKUP_FOLDER = "nvidia_bios_backups"
BACKUP_FILENAME = "nvidia_bios_backup.rom"
RESTORE_FILENAME = "restore_bios.rom"

def check_nibitor_existence():
    """
    Verifies that the NiBiTor utility exists at the specified path.
    """
    if not os.path.isfile(NIBITOR_PATH):
        raise FileNotFoundError(f"NiBiTor executable not found at path: {NIBITOR_PATH}")

def create_backup_folder():
    """
    Creates a folder for storing backups if it doesn't already exist.
    """
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

def backup_bios():
    """
    Uses NiBiTor to backup NVIDIA BIOS settings to a file.
    """
    try:
        create_backup_folder()
        backup_path = os.path.join(BACKUP_FOLDER, BACKUP_FILENAME)

        # Command to backup the BIOS
        command = [NIBITOR_PATH, "/backup", backup_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to backup BIOS. Error: {result.stderr.decode('utf-8')}")

        print(f"BIOS backup completed successfully. Backup stored at: {backup_path}")
    except Exception as e:
        print(f"An error occurred during BIOS backup: {e}")

def restore_bios():
    """
    Uses NiBiTor to restore NVIDIA BIOS settings from a backup file.
    """
    try:
        restore_path = os.path.join(BACKUP_FOLDER, RESTORE_FILENAME)

        if not os.path.isfile(restore_path):
            raise FileNotFoundError(f"Restore file not found at path: {restore_path}")

        # Command to restore the BIOS
        command = [NIBITOR_PATH, "/restore", restore_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to restore BIOS. Error: {result.stderr.decode('utf-8')}")

        print("BIOS restore completed successfully.")
    except Exception as e:
        print(f"An error occurred during BIOS restore: {e}")

def main():
    """
    Main function to interact with the user and perform backup or restore operations.
    """
    try:
        check_nibitor_existence()
        print("NiBiTor utility found!")

        print("Select an operation:")
        print("1: Backup BIOS")
        print("2: Restore BIOS")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            backup_bios()
        elif choice == "2":
            restore_bios()
        else:
            print("Invalid choice. Exiting.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
