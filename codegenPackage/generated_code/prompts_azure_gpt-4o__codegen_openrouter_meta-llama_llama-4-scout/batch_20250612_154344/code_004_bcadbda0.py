"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Create a Python program to automate data backup and recovery processes, ensuring minimal downtime, as described in IMTS's managed IT services.
Generated: DETERMINISTIC_bcadbda029ee7550
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import datetime
import logging
import argparse

# Set up logging configuration
logging.basicConfig(filename='backup_recovery.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_backup(source_dir, backup_dir):
    """
    Creates a backup of the source directory.

    Args:
        source_dir (str): The directory to be backed up.
        backup_dir (str): The directory where the backup will be stored.

    Returns:
        str: The path to the backup directory.
    """
    try:
        # Check if source and backup directories exist
        if not os.path.exists(source_dir):
            logging.error(f"Source directory '{source_dir}' does not exist.")
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            logging.info(f"Backup directory '{backup_dir}' created.")

        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        os.makedirs(backup_path)
        logging.info(f"Backup directory '{backup_path}' created.")

        # Copy files from source to backup directory
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isfile(item_path):
                shutil.copy2(item_path, backup_path)
                logging.info(f"File '{item}' backed up.")
            elif os.path.isdir(item_path):
                shutil.copytree(item_path, os.path.join(backup_path, item))
                logging.info(f"Directory '{item}' backed up.")

        return backup_path

    except Exception as e:
        logging.error(f"Error creating backup: {str(e)}")
        raise

def recover_backup(backup_dir, recovery_dir):
    """
    Recovers data from a backup directory.

    Args:
        backup_dir (str): The directory containing the backup.
        recovery_dir (str): The directory where the data will be recovered.

    Returns:
        str: The path to the recovery directory.
    """
    try:
        # Check if backup and recovery directories exist
        if not os.path.exists(backup_dir):
            logging.error(f"Backup directory '{backup_dir}' does not exist.")
            raise FileNotFoundError(f"Backup directory '{backup_dir}' does not exist.")
        if not os.path.exists(recovery_dir):
            os.makedirs(recovery_dir)
            logging.info(f"Recovery directory '{recovery_dir}' created.")

        # Iterate through backups and prompt user to select one
        backups = [os.path.join(backup_dir, item) for item in os.listdir(backup_dir) if os.path.isdir(os.path.join(backup_dir, item))]
        if not backups:
            logging.error(f"No backups found in '{backup_dir}'.")
            raise FileNotFoundError(f"No backups found in '{backup_dir}'.")

        print("Available backups:")
        for i, backup in enumerate(backups):
            print(f"{i+1}. {os.path.basename(backup)}")

        choice = input("Enter the number of the backup to recover: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(backups):
                raise ValueError
        except ValueError:
            logging.error("Invalid backup choice.")
            raise

        selected_backup = backups[choice - 1]
        logging.info(f"Recovering from backup '{selected_backup}'.")

        # Copy files from backup to recovery directory
        for item in os.listdir(selected_backup):
            item_path = os.path.join(selected_backup, item)
            if os.path.isfile(item_path):
                shutil.copy2(item_path, recovery_dir)
                logging.info(f"File '{item}' recovered.")
            elif os.path.isdir(item_path):
                shutil.copytree(item_path, os.path.join(recovery_dir, item))
                logging.info(f"Directory '{item}' recovered.")

        return recovery_dir

    except Exception as e:
        logging.error(f"Error recovering backup: {str(e)}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup and recovery script")
    subparsers = parser.add_subparsers(dest="command")

    backup_parser = subparsers.add_parser("backup", help="Create a backup")
    backup_parser.add_argument("-s", "--source", required=True, help="Source directory")
    backup_parser.add_argument("-b", "--backup", required=True, help="Backup directory")

    recover_parser = subparsers.add_parser("recover", help="Recover from a backup")
    recover_parser.add_argument("-b", "--backup", required=True, help="Backup directory")
    recover_parser.add_argument("-r", "--recovery", required=True, help="Recovery directory")

    args = parser.parse_args()

    if args.command == "backup":
        create_backup(args.source, args.backup)
    elif args.command == "recover":
        recover_backup(args.backup, args.recovery)
    else:
        parser.print_help()
```
