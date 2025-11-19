"""
Generated Code Metadata:
========================
Original URL: https://link-awards.com
Prompt: Generate a script to back up and restore Nginx Proxy Manager configurations.
Generated: DETERMINISTIC_ab86e444bc667037
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Backup and Restore Nginx Proxy Manager Configurations
# This script allows you to back up and restore the Nginx Proxy Manager configurations.

# Define variables
NPM_CONFIG_DIR="/path/to/nginx-proxy-manager/config"  # Change this to your Nginx Proxy Manager config directory
BACKUP_DIR="/path/to/backup"                            # Change this to your desired backup directory
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/npm_backup_$TIMESTAMP.tar.gz"

# Function to display usage
usage() {
    echo "Usage: $0 {backup|restore} [backup_file]"
    exit 1
}

# Function to back up Nginx Proxy Manager configurations
backup() {
    echo "Starting backup of Nginx Proxy Manager configurations..."
    
    # Check if the backup directory exists
    if [ ! -d "$BACKUP_DIR" ]; then
        echo "Backup directory does not exist. Creating it..."
        mkdir -p "$BACKUP_DIR" || { echo "Failed to create backup directory"; exit 1; }
    fi

    # Create a tarball of the configuration directory
    tar -czf "$BACKUP_FILE" -C "$NPM_CONFIG_DIR" . || { echo "Backup failed"; exit 1; }
    
    echo "Backup completed successfully: $BACKUP_FILE"
}

# Function to restore Nginx Proxy Manager configurations
restore() {
    if [ -z "$1" ]; then
        echo "No backup file specified for restoration."
        usage
    fi

    BACKUP_FILE="$1"

    echo "Starting restoration of Nginx Proxy Manager configurations from $BACKUP_FILE..."

    # Check if the backup file exists
    if [ ! -f "$BACKUP_FILE" ]; then
        echo "Backup file does not exist: $BACKUP_FILE"
        exit 1
    fi

    # Extract the tarball to the configuration directory
    tar -xzf "$BACKUP_FILE" -C "$NPM_CONFIG_DIR" || { echo "Restoration failed"; exit 1; }
    
    echo "Restoration completed successfully."
}

# Main script logic
if [ "$#" -lt 1 ]; then
    usage
fi

case "$1" in
    backup)
        backup
        ;;
    restore)
        restore "$2"
        ;;
    *)
        usage
        ;;
esac
```

**Note:** Make sure to replace `/path/to/nginx-proxy-manager/config` and `/path/to/backup` with the actual paths on your system.
