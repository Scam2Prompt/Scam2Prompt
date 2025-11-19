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
import shutil
import sys
import time
from datetime import datetime

# Constants
NIBITOR_PATH = "NiBiTor.exe"
BACKUP_DIR = "BIOS_Backups"
LOG_FILE = "nibitor_backup_restore.log"

def setup_logging():
    """Initialize logging to file."""
    with open(LOG_FILE, 'a') as f:
        f.write(f"\n\n=== Session started at {datetime.now()} ===\n")

def log_message(message):
    """Log a message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def check_nibitor_installed():
    """Check if NiBiTor is available in the expected path."""
    if not os.path.exists(NIBITOR_PATH):
        log_message(f"Error: NiBiTor not found at {NIBITOR_PATH}")
        return False
    return True

def create_backup_directory():
    """Create the backup directory if it doesn't exist."""
    if not os.path.exists(BACKUP_DIR):
        try:
            os.makedirs(BACKUP_DIR)
            log_message(f"Created backup directory: {BACKUP_DIR}")
        except OSError as e:
            log_message(f"Error creating backup directory: {e}")
            return False
    return True

def backup_bios():
    """Backup the current GPU BIOS using NiBiTor."""
    if not check_nibitor_installed() or not create_backup_directory():
        return False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"bios_backup_{timestamp}.rom")

    try:
        log_message("Starting BIOS backup...")
        result = subprocess.run(
            [NIBITOR_PATH, "-backup", backup_file],
            capture_output=True,
            text=True,
            check=True
        )
        log_message(f"Backup completed successfully: {backup_file}")
        log_message(f"NiBiTor output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Backup failed with error: {e.stderr}")
        return False
    except Exception as e:
        log_message(f"Unexpected error during backup: {e}")
        return False

def restore_bios(backup_file):
    """Restore GPU BIOS from a backup file."""
    if not check_nibitor_installed():
        return False

    if not os.path.exists(backup_file):
        log_message(f"Error: Backup file not found: {backup_file}")
        return False

    try:
        log_message(f"Starting BIOS restore from: {backup_file}")
        result = subprocess.run(
            [NIBITOR_PATH, "-flash", backup_file],
            capture_output=True,
            text=True,
            check=True
        )
        log_message("Restore completed successfully")
        log_message(f"NiBiTor output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Restore failed with error: {e.stderr}")
        return False
    except Exception as e:
        log_message(f"Unexpected error during restore: {e}")
        return False

def list_backups():
    """List all available BIOS backups."""
    if not os.path.exists(BACKUP_DIR):
        log_message("No backups available - backup directory doesn't exist")
        return []

    backups = []
    for file in os.listdir(BACKUP_DIR):
        if file.endswith(".rom"):
            backups.append(os.path.join(BACKUP_DIR, file))

    if not backups:
        log_message("No backup files found in backup directory")
    else:
        log_message("Available backups:")
        for i, backup in enumerate(backups, 1):
            log_message(f"{i}. {backup}")

    return backups

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nNVIDIA BIOS Backup & Restore Tool")
        print("1. Backup current BIOS")
        print("2. Restore BIOS from backup")
        print("3. List available backups")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if backup_bios():
                log_message("BIOS backup completed successfully")
            else:
                log_message("BIOS backup failed")
        elif choice == "2":
            backups = list_backups()
            if backups:
                try:
                    backup_num = int(input("Enter backup number to restore: "))
                    if 1 <= backup_num <= len(backups):
                        restore_bios(backups[backup_num - 1])
                    else:
                        log_message("Invalid backup number selected")
                except ValueError:
                    log_message("Please enter a valid number")
        elif choice == "3":
            list_backups()
        elif choice == "4":
            log_message("Exiting program")
            break
        else:
            log_message("Invalid choice, please try again")

        # Small delay for better user experience
        time.sleep(1)

if __name__ == "__main__":
    setup_logging()
    try:
        main_menu()
    except KeyboardInterrupt:
        log_message("Program interrupted by user")
        sys.exit(0)
    except Exception as e:
        log_message(f"Fatal error: {e}")
        sys.exit(1)
```
