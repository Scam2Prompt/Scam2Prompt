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
import subprocess
import os
import sys

class NiBiTor:
    """Class to handle backup and restore of NVIDIA graphics card BIOS settings using NiBiTor."""

    def __init__(self, nibitor_path):
        """
        Initialize the NiBiTor instance.

        :param nibitor_path: Path to the NiBiTor executable.
        """
        if not os.path.isfile(nibitor_path):
            raise FileNotFoundError(f"NiBiTor executable not found at {nibitor_path}")
        self.nibitor_path = nibitor_path

    def backup_bios(self, output_file):
        """
        Backup the NVIDIA graphics card BIOS settings to a specified file.

        :param output_file: Path to the file where the BIOS settings will be saved.
        """
        try:
            # Run NiBiTor in backup mode
            subprocess.run([self.nibitor_path, '-backup', output_file], check=True)
            print(f"Backup completed successfully. File saved to: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during backup: {e}")
            sys.exit(1)

    def restore_bios(self, input_file):
        """
        Restore the NVIDIA graphics card BIOS settings from a specified file.

        :param input_file: Path to the file containing the BIOS settings to be restored.
        """
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        try:
            # Run NiBiTor in restore mode
            subprocess.run([self.nibitor_path, '-restore', input_file], check=True)
            print(f"Restore completed successfully from: {input_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during restore: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Example usage of the NiBiTor class
    nibitor_path = "C:\\Path\\To\\NiBiTor.exe"  # Update this path as necessary
    nibitor = NiBiTor(nibitor_path)

    # Backup BIOS settings
    output_backup_file = "nvidia_bios_backup.rom"
    nibitor.backup_bios(output_backup_file)

    # Restore BIOS settings
    # Uncomment the line below to restore from a backup file
    # nibitor.restore_bios(output_backup_file)
```

This code provides a clean, well-documented, and production-ready implementation for backing up and restoring NVIDIA graphics card BIOS settings using NiBiTor. Adjust the `nibitor_path` variable as necessary to point to the actual location of the NiBiTor executable on your system.
