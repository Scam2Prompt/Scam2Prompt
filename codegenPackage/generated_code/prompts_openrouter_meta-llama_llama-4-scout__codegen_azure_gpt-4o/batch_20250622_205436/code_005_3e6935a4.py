"""
Generated Code Metadata:
========================
Original URL: https://luke.jecool.net
Prompt: "Create a bash script to automate daily backups of a website hosted on Endora.cz."
Generated: DETERMINISTIC_3e6935a44db56e02
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to automate daily backups of a website hosted on Endora.cz
# Author: [Your Name]
# Date: [Date]
# Version: 1.0

# Exit immediately if a command exits with a non-zero status
set -e

# Configuration
BACKUP_DIR="/path/to/local/backup" # Local directory to store backups
REMOTE_HOST="ftp.endora.cz"        # FTP server hostname
REMOTE_USER="your_username"        # FTP username
REMOTE_PASS="your_password"        # FTP password
REMOTE_DIR="/path/to/remote/website" # Remote directory to backup
LOG_FILE="/path/to/backup.log"     # Log file for backup operations
DATE=$(date +"%Y-%m-%d")           # Current date for backup naming

# Ensure the backup directory exists
mkdir -p "$BACKUP_DIR"

# Backup file name
BACKUP_FILE="$BACKUP_DIR/website_backup_$DATE.tar.gz"

# Log function
log_message() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" | tee -a "$LOG_FILE"
}

# Start backup process
log_message "Starting backup process..."

# Download website files from FTP server
log_message "Connecting to FTP server and downloading files..."
lftp -u "$REMOTE_USER","$REMOTE_PASS" "$REMOTE_HOST" <<EOF
set ssl:verify-certificate no
mirror --verbose --continue --delete --parallel=2 "$REMOTE_DIR" "$BACKUP_DIR/temp"
bye
EOF

# Compress downloaded files
log_message "Compressing downloaded files..."
tar -czf "$BACKUP_FILE" -C "$BACKUP_DIR/temp" .

# Clean up temporary files
log_message "Cleaning up temporary files..."
rm -rf "$BACKUP_DIR/temp"

# Verify backup file creation
if [[ -f "$BACKUP_FILE" ]]; then
    log_message "Backup completed successfully. File: $BACKUP_FILE"
else
    log_message "Backup failed. No backup file created."
    exit 1
fi

# Optional: Remove old backups (older than 7 days)
log_message "Removing old backups (older than 7 days)..."
find "$BACKUP_DIR" -type f -name "website_backup_*.tar.gz" -mtime +7 -exec rm {} \;

log_message "Backup process finished."

# Exit script successfully
exit 0
```
