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
import os
import subprocess
import sys

class NiBiTor:
    """
    A class to handle the backup and restoration of NVIDIA graphics card BIOS settings using NiBiTor.
    """

    def __init__(self, nibitor_path):
        """
        Initializes the NiBiTor class with the path to the NiBiTor executable.

        :param nibitor_path: Path to the NiBiTor executable.
        """
        self.nibitor_path = nibitor_path

    def backup_bios(self, output_file):
        """
        Backs up the NVIDIA graphics card BIOS settings to a specified file.

        :param output_file: The file where the BIOS settings will be saved.
        :raises RuntimeError: If the backup process fails.
        """
        try:
            # Command to execute NiBiTor for BIOS backup
            command = [self.nibitor_path, '-backup', output_file]
            subprocess.run(command, check=True)
            print(f"Backup successful! BIOS settings saved to {output_file}.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to backup BIOS: {e}")

    def restore_bios(self, input_file):
        """
        Restores the NVIDIA graphics card BIOS settings from a specified file.

        :param input_file: The file from which the BIOS settings will be restored.
        :raises RuntimeError: If the restore process fails.
        """
        try:
            # Command to execute NiBiTor for BIOS restoration
            command = [self.nibitor_path, '-restore', input_file]
            subprocess.run(command, check=True)
            print(f"Restore successful! BIOS settings restored from {input_file}.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to restore BIOS: {e}")

def main():
    """
    Main function to execute the backup or restore process based on user input.
    """
    if len(sys.argv) < 4:
        print("Usage: python nibitor_script.py <nibitor_path> <backup|restore> <file_path>")
        sys.exit(1)

    nibitor_path = sys.argv[1]
    action = sys.argv[2].lower()
    file_path = sys.argv[3]

    nibitor = NiBiTor(nibitor_path)

    try:
        if action == 'backup':
            nibitor.backup_bios(file_path)
        elif action == 'restore':
            nibitor.restore_bios(file_path)
        else:
            print("Invalid action. Use 'backup' or 'restore'.")
            sys.exit(1)
    except RuntimeError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
