"""
Generated Code Metadata:
========================
Original URL: https://thuthuatxiaomi.com
Prompt: "Explain how to use Fastboot for backing up and restoring Xiaomi device data, including system and user data."
Generated: DETERMINISTIC_71e21d5015a0b99d
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to use Fastboot commands to back up and restore Xiaomi device data.
It uses Python's `subprocess` module to execute Fastboot commands. Ensure Fastboot is installed
and properly configured on your system before running this script.

Note: This script assumes the device is already in Fastboot mode. To enter Fastboot mode, power off
the device and press Volume Down + Power button simultaneously.
"""

import subprocess
import os

def execute_fastboot_command(command):
    """
    Executes a Fastboot command and returns the output.
    :param command: List of Fastboot command arguments.
    :return: Tuple containing (output, error).
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except FileNotFoundError:
        raise Exception("Fastboot executable not found. Ensure Fastboot is installed and added to PATH.")
    except Exception as e:
        raise Exception(f"An error occurred while executing Fastboot command: {e}")

def backup_partition(partition_name, output_file):
    """
    Backs up a specific partition from the Xiaomi device.
    :param partition_name: Name of the partition to back up (e.g., 'system', 'userdata').
    :param output_file: Path to the output file where the backup will be saved.
    """
    print(f"Backing up partition '{partition_name}' to '{output_file}'...")
    command = ["fastboot", "flash", partition_name, output_file]
    output, error = execute_fastboot_command(command)
    if error:
        print(f"Error during backup: {error}")
    else:
        print(f"Backup completed successfully. Output: {output}")

def restore_partition(partition_name, input_file):
    """
    Restores a specific partition to the Xiaomi device.
    :param partition_name: Name of the partition to restore (e.g., 'system', 'userdata').
    :param input_file: Path to the input file containing the backup data.
    """
    print(f"Restoring partition '{partition_name}' from '{input_file}'...")
    command = ["fastboot", "flash", partition_name, input_file]
    output, error = execute_fastboot_command(command)
    if error:
        print(f"Error during restore: {error}")
    else:
        print(f"Restore completed successfully. Output: {output}")

def main():
    """
    Main function to demonstrate backup and restore functionality.
    """
    # Define partitions and file paths
    partitions_to_backup = ["system", "userdata"]
    backup_directory = "./backups"

    # Ensure backup directory exists
    os.makedirs(backup_directory, exist_ok=True)

    # Backup partitions
    for partition in partitions_to_backup:
        backup_file = os.path.join(backup_directory, f"{partition}.img")
        backup_partition(partition, backup_file)

    # Restore partitions (example usage)
    for partition in partitions_to_backup:
        backup_file = os.path.join(backup_directory, f"{partition}.img")
        restore_partition(partition, backup_file)

if __name__ == "__main__":
    main()
```

**Note:** This script is for demonstration purposes only. Ensure you have proper permissions and understand the risks of using Fastboot commands, as incorrect usage can lead to data loss or device bricking. Always test on a non-critical device before using in production.
