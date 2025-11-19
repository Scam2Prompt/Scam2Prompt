"""
Generated Code Metadata:
========================
Original URL: https://link-reward.com
Prompt: Provide a Bash script to back up and restore Nginx Proxy Manager configurations, including host settings and SSL certificates.
Generated: DETERMINISTIC_2bdc77dfd40d3f47
Batch ID: 20250612_151610
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
# This script allows you to back up and restore Nginx Proxy Manager configurations,
# including host settings and SSL certificates.

# Define variables
NPM_CONFIG_DIR="/path/to/nginx-proxy-manager/config"  # Change this to your Nginx Proxy Manager config directory
BACKUP_DIR="/path/to/backup"                           # Change this to your desired backup directory
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/npm_backup_$TIMESTAMP.tar.gz"

# Function to display usage
usage() {
    echo "Usage: $0 {backup|restore}"
    exit 1
}

# Function to back up Nginx Proxy Manager configurations
backup() {
    echo "Starting backup of Nginx Proxy Manager configurations..."
    
    # Check if the config directory exists
    if [ ! -d "$NPM_CONFIG_DIR" ]; then
        echo "Error: Nginx Proxy Manager config directory does not exist: $NPM_CONFIG_DIR"
        exit 1
    fi

    # Create backup directory if it doesn't exist
    mkdir -p "$BACKUP_DIR"

    # Create a tarball of the configuration directory
    tar -czf "$BACKUP_FILE" -C "$NPM_CONFIG_DIR" .
    
    if [ $? -eq 0 ]; then
        echo "Backup successful: $BACKUP_FILE"
    else
        echo "Error: Backup failed."
        exit 1
    fi
}

# Function to restore Nginx Proxy Manager configurations
restore() {
    echo "Starting restoration of Nginx Proxy Manager configurations..."
    
    # Check if the backup file exists
    if [ ! -f "$BACKUP_FILE" ]; then
        echo "Error: Backup file does not exist: $BACKUP_FILE"
        exit 1
    fi

    # Restore the configuration from the backup file
    tar -xzf "$BACKUP_FILE" -C "$NPM_CONFIG_DIR"
    
    if [ $? -eq 0 ]; then
        echo "Restoration successful."
    else
        echo "Error: Restoration failed."
        exit 1
    fi
}

# Main script logic
if [ $# -ne 1 ]; then
    usage
fi

case "$1" in
    backup)
        backup
        ;;
    restore)
        restore
        ;;
    *)
        usage
        ;;
esac
```

**Note:** Make sure to replace `/path/to/nginx-proxy-manager/config` and `/path/to/backup` with the actual paths on your system.
