"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeta-swap.org
Prompt: Write a script to back up and restore website data using Plesk's hosting automation tools.
Generated: DETERMINISTIC_b0d54e2789656b82
Batch ID: 20250612_152000
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
import datetime
import argparse

def backup_website(domain_name, backup_dir):
    """
    Create a backup of website data for a specific domain using Plesk.

    Args:
        domain_name (str): The domain name of the website to be backed up.
        backup_dir (str): Directory where the backup file will be stored.

    Returns:
        str: Path to the created backup file.
    """
    try:
        # Ensure backup directory exists
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Generate backup file name with timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f"{domain_name}_backup_{timestamp}.tar")

        # Run Plesk backup command
        plesk_backup_command = [
            'plesk', 'bin', 'domain', 'backup',
            domain_name,
            '-destination', backup_file
        ]
        
        result = subprocess.run(plesk_backup_command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("Website backup completed successfully.")
        return backup_file

    except subprocess.CalledProcessError as e:
        print(f"Error while creating backup: {e.stderr.decode()}")
        raise

    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        raise


def restore_website(domain_name, backup_file):
    """
    Restore website data for a specific domain using Plesk.

    Args:
        domain_name (str): The domain name of the website to be restored.
        backup_file (str): Path to the backup file to be restored.

    Returns:
        None
    """
    try:
        if not os.path.exists(backup_file):
            raise FileNotFoundError(f"Backup file '{backup_file}' does not exist.")

        # Run Plesk restore command
        plesk_restore_command = [
            'plesk', 'bin', 'domain', 'restore',
            domain_name,
            '-source', backup_file
        ]
        
        result = subprocess.run(plesk_restore_command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("Website restoration completed successfully.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error while restoring backup: {e.stderr.decode()}")
        raise

    except FileNotFoundError as e:
        print(f"File Error: {str(e)}")
        raise

    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        raise


def main():
    """
    Main function to parse command line arguments and perform backup or restore actions.
    """
    parser = argparse.ArgumentParser(description="Backup and restore website data using Plesk.")

    subparsers = parser.add_subparsers(dest="action", required=True, help="Action to perform")

    # Backup command
    backup_parser = subparsers.add_parser("backup", help="Backup a website")
    backup_parser.add_argument("domain_name", help="Domain name of the website to be backed up")
    backup_parser.add_argument("backup_dir", help="Directory to store the backup file")

    # Restore command
    restore_parser = subparsers.add_parser("restore", help="Restore a website")
    restore_parser.add_argument("domain_name", help="Domain name of the website to be restored")
    restore_parser.add_argument("backup_file", help="Path to the backup file to be restored")

    args = parser.parse_args()

    if args.action == "backup":
        backup_file = backup_website(args.domain_name, args.backup_dir)
        print(f"Backup created: {backup_file}")
    elif args.action == "restore":
        restore_website(args.domain_name, args.backup_file)


if __name__ == "__main__":
    main()
```
