"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaranetwork.cloud
Prompt: Create a bash script to back up website files and databases before migrating to Hostinger.
Generated: DETERMINISTIC_4628ffcd5ea8831c
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Backup Script for Website Files and Databases
# Author: [Your Name]
# Date: [Date]
# Description: This script backs up website files and databases before migrating to Hostinger.

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
WEB_ROOT="/var/www/html"            # Path to website files
BACKUP_DIR="$HOME/website_backup"   # Directory to store backups
DB_USER="your_db_user"              # Database username
DB_PASSWORD="your_db_password"      # Database password
DB_NAMES=("db1" "db2")              # List of databases to back up

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Timestamp for backup files
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Function to log messages
log_message() {
    echo "[INFO] $1"
}

# Backup website files
log_message "Starting backup of website files..."
tar -czf "$BACKUP_DIR/website_files_$TIMESTAMP.tar.gz" -C "$WEB_ROOT" .
log_message "Website files backed up successfully to $BACKUP_DIR/website_files_$TIMESTAMP.tar.gz"

# Backup databases
log_message "Starting backup of databases..."
for DB_NAME in "${DB_NAMES[@]}"; do
    BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_$TIMESTAMP.sql"
    if mysqldump -u"$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" > "$BACKUP_FILE"; then
        log_message "Database '$DB_NAME' backed up successfully to $BACKUP_FILE"
    else
        log_message "Error backing up database '$DB_NAME'. Aborting."
        exit 1
    fi
done

# Verify backups
log_message "Verifying backups..."
if [[ -f "$BACKUP_DIR/website_files_$TIMESTAMP.tar.gz" ]]; then
    log_message "Website files backup verified."
else
    log_message "Website files backup not found. Aborting."
    exit 1
fi

for DB_NAME in "${DB_NAMES[@]}"; do
    BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_$TIMESTAMP.sql"
    if [[ -f "$BACKUP_FILE" ]]; then
        log_message "Database '$DB_NAME' backup verified."
    else
        log_message "Database '$DB_NAME' backup not found. Aborting."
        exit 1
    fi
done

log_message "All backups completed successfully."

# Instructions for next step
log_message "You can now proceed to migrate your data to Hostinger."

exit 0
```
