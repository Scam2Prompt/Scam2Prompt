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

# Backup Script for LiteSpeed Web Server Files
# This script automates the backup of files listed in a specified directory.
# It creates a timestamped archive of the files and stores it in a designated backup directory.

# Configuration
SOURCE_DIR="/path/to/litespeed/files"  # Directory containing files to back up
BACKUP_DIR="/path/to/backup/directory"   # Directory where backups will be stored
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")       # Generate timestamp for backup filename
BACKUP_FILE="backup_$TIMESTAMP.tar.gz"   # Name of the backup file

# Ensure backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
  echo "Backup directory does not exist. Creating it now..."
  mkdir -p "$BACKUP_DIR"
  
  # Check if directory creation was successful
  if [ $? -ne 0 ]; then
    echo "Error: Failed to create backup directory."
    exit 1
  fi
fi

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Source directory does not exist."
  exit 1
fi

# Create the backup
echo "Creating backup of files from $SOURCE_DIR to $BACKUP_DIR/$BACKUP_FILE..."
tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$SOURCE_DIR" .

# Check if the tar command was successful
if [ $? -ne 0 ]; then
  echo "Error: Backup failed."
  exit 1
fi

echo "Backup successful! Backup file is located at $BACKUP_DIR/$BACKUP_FILE"

# Optional: Remove backups older than 7 days
find "$BACKUP_DIR" -type f -name "backup_*.tar.gz" -mtime +7 -exec rm {} \;

# Notify completion
echo "Old backups removed. Backup process completed."
```
