"""
Generated Code Metadata:
========================
Original URL: https://perurest.com
Prompt: Create a shell script to automate the backup of files listed in a directory served by LiteSpeed Web Server.
Generated: DETERMINISTIC_3e64c651e735d239
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# LiteSpeed Web Server Backup Script
# Automates the backup of files listed in a specified directory served by LiteSpeed

# Configuration variables
BACKUP_DIR="/var/www/html"          # Directory to be backed up
DEST_DIR="/backups/litespeed"       # Destination directory for backups
LOG_FILE="/var/log/litespeed_backup.log"  # Log file path
MAX_BACKUPS=7                       # Maximum number of backups to retain
DATE=$(date +%Y%m%d_%H%M%S)        # Timestamp for backup filename

# Ensure script is run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" | tee -a "$LOG_FILE"
    exit 1
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"
if [ $? -ne 0 ]; then
    echo "Failed to create destination directory: $DEST_DIR" | tee -a "$LOG_FILE"
    exit 1
fi

# Create backup filename
BACKUP_FILE="$DEST_DIR/litespeed_backup_$DATE.tar.gz"

# Log start of backup
echo "[$(date)] Starting backup of $BACKUP_DIR to $BACKUP_FILE" >> "$LOG_FILE"

# Create compressed tar archive
tar -czf "$BACKUP_FILE" -C "$(dirname "$BACKUP_DIR")" "$(basename "$BACKUP_DIR")" 2>> "$LOG_FILE"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "[$(date)] Backup completed successfully: $BACKUP_FILE" >> "$LOG_FILE"
    
    # Rotate backups - keep only MAX_BACKUPS most recent
    cd "$DEST_DIR" || exit 1
    ls -t litespeed_backup_*.tar.gz | tail -n +$((MAX_BACKUPS + 1)) | xargs rm -f 2>> "$LOG_FILE"
    
    echo "[$(date)] Backup rotation completed. Kept last $MAX_BACKUPS backups." >> "$LOG_FILE"
else
    echo "[$(date)] Backup failed. Check $LOG_FILE for details." | tee -a "$LOG_FILE"
    exit 1
fi

exit 0
```
