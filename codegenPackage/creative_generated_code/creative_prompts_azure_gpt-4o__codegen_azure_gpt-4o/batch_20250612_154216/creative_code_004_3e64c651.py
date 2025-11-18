"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Create a shell script to automate the backup of files listed in a directory served by LiteSpeed Web Server.
Generated: DETERMINISTIC_3e64c651e735d239
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the backup of files served by LiteSpeed Web Server

# Exit immediately if a command exits with a non-zero status
set -e

# Function to print an error message and exit
handle_error() {
  echo "Error: $1"
  exit 1
}

# Configuration
SOURCE_DIR="/usr/local/lsws/ExampleSite"  # Path to LiteSpeed web server directory
BACKUP_DIR="/var/backups/litespeed"       # Directory to store backups
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")   # Generate timestamp for backup
LOG_FILE="/var/log/litespeed_backup.log" # Log file path

# Ensure the source directory exists
if [[ ! -d "$SOURCE_DIR" ]]; then
  handle_error "Source directory $SOURCE_DIR does not exist."
fi

# Create the backup directory if it doesn't exist
if [[ ! -d "$BACKUP_DIR" ]]; then
  mkdir -p "$BACKUP_DIR" || handle_error "Failed to create backup directory $BACKUP_DIR."
fi

# Create a tarball of the files
BACKUP_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"
tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" . || handle_error "Failed to create backup archive."

# Verify the backup file was created successfully
if [[ ! -f "$BACKUP_FILE" ]]; then
  handle_error "Backup file $BACKUP_FILE was not created."
fi

# Log the backup operation
echo "${TIMESTAMP} - Backup created: ${BACKUP_FILE}" >> "$LOG_FILE" || handle_error "Failed to write to log file."

# Print a success message
echo "Backup completed successfully: ${BACKUP_FILE}"
```
