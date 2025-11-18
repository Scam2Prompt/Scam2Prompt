"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agromec.cl
Prompt: Write a script to automate backups for websites hosted on a Linux-based hosting service in Chile.
Generated: DETERMINISTIC_e1e71ea70c66d12e
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# backup_website.sh
# A script to automate backups for websites hosted on a Linux-based hosting service.
# This script creates a compressed tarball of the specified website directory and saves it to a backup directory.

# Configuration
SOURCE_DIR="/var/www/html"               # Directory containing the website files
BACKUP_DIR="/backup/website_backups"      # Directory where backups will be stored
TIMESTAMP=$(date +"%Y%m%d%H%M")           # Timestamp for the backup file name
BACKUP_FILE="website_backup_$TIMESTAMP.tar.gz"  # Backup file name

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Function to perform the backup
function perform_backup {
    # Check if source directory exists
    if [ ! -d "$SOURCE_DIR" ]; then
        echo "Error: Source directory $SOURCE_DIR does not exist."
        exit 1
    fi

    # Create a compressed tarball of the website files
    tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$SOURCE_DIR" .

    # Check if the tar command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Backup process failed."
        exit 1
    fi

    echo "Backup completed successfully: $BACKUP_DIR/$BACKUP_FILE"
}

# Function to clean up old backups
function cleanup_old_backups {
    # Find backups older than 7 days and delete them
    find "$BACKUP_DIR" -type f -name "website_backup_*.tar.gz" -mtime +7 -exec rm {} \;
    echo "Old backups cleaned up."
}

# Execute backup and cleanup functions
perform_backup
cleanup_old_backups
```
