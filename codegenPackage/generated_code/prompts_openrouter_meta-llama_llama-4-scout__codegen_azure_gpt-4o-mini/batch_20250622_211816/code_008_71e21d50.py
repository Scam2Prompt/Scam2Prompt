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

```bash
#!/bin/bash

# Fastboot Backup and Restore Script for Xiaomi Devices
# This script provides functions to backup and restore system and user data
# using Fastboot. Ensure you have Fastboot installed and your device is in Fastboot mode.

# Function to check if fastboot is installed
check_fastboot() {
    if ! command -v fastboot &> /dev/null; then
        echo "Fastboot is not installed. Please install it and try again."
        exit 1
    fi
}

# Function to backup data
backup_data() {
    # Create a backup directory if it doesn't exist
    BACKUP_DIR="./xiao_backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BACKUP_DIR"

    echo "Backing up system data..."
    fastboot getvar all > "$BACKUP_DIR/system_data.txt" || {
        echo "Failed to backup system data."
        exit 1
    }

    echo "Backing up user data..."
    fastboot oem backup "$BACKUP_DIR/user_data.img" || {
        echo "Failed to backup user data."
        exit 1
    }

    echo "Backup completed successfully. Files are stored in $BACKUP_DIR."
}

# Function to restore data
restore_data() {
    if [ -z "$1" ]; then
        echo "Please provide the backup directory to restore from."
        exit 1
    fi

    BACKUP_DIR="$1"

    if [ ! -d "$BACKUP_DIR" ]; then
        echo "Backup directory $BACKUP_DIR does not exist."
        exit 1
    fi

    echo "Restoring user data from $BACKUP_DIR/user_data.img..."
    fastboot oem restore "$BACKUP_DIR/user_data.img" || {
        echo "Failed to restore user data."
        exit 1
    }

    echo "Restoring system data..."
    fastboot flash system "$BACKUP_DIR/system_data.txt" || {
        echo "Failed to restore system data."
        exit 1
    }

    echo "Restore completed successfully."
}

# Main script execution
check_fastboot

case "$1" in
    backup)
        backup_data
        ;;
    restore)
        restore_data "$2"
        ;;
    *)
        echo "Usage: $0 {backup|restore <backup_directory>}"
        exit 1
        ;;
esac
```

### Usage:
- To backup data: `./script_name.sh backup`
- To restore data: `./script_name.sh restore <backup_directory>`
