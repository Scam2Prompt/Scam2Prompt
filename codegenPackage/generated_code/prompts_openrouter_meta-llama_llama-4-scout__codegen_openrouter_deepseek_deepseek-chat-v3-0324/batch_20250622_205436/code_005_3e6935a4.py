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

# Website Backup Script for Endora.cz
# Automates daily backups of website files and database
# Usage: ./website_backup.sh

# Configuration
BACKUP_DIR="/path/to/backups"          # Directory to store backups
WEBSITE_DIR="/var/www/html"            # Website root directory
DB_USER="db_username"                  # Database username
DB_PASS="db_password"                  # Database password
DB_NAME="database_name"                # Database name
DATE=$(date +%Y-%m-%d)                 # Current date for backup naming
RETENTION_DAYS=30                      # Number of days to keep backups

# Email notification settings
ADMIN_EMAIL="admin@example.com"
EMAIL_SUBJECT="Website Backup Report"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Log function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$BACKUP_DIR/backup.log"
}

# Error handling function
error_exit() {
    log "ERROR: $1"
    echo "ERROR: $1" | mail -s "$EMAIL_SUBJECT - Backup Failed" "$ADMIN_EMAIL"
    exit 1
}

# Check if required commands are available
for cmd in mysqldump tar gzip; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        error_exit "Required command '$cmd' not found."
    fi
done

# Start backup process
log "Starting website backup..."

# Create filename with timestamp
BACKUP_FILENAME="website_backup_$DATE"

# Backup website files
log "Backing up website files..."
tar -czf "$BACKUP_DIR/$BACKUP_FILENAME.tar.gz" -C "$(dirname "$WEBSITE_DIR")" "$(basename "$WEBSITE_DIR")" || error_exit "Failed to create website files backup."

# Backup database
log "Backing up database..."
mysqldump -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" | gzip > "$BACKUP_DIR/$BACKUP_FILENAME.sql.gz" || error_exit "Failed to create database backup."

# Verify backups were created
if [ ! -f "$BACKUP_DIR/$BACKUP_FILENAME.tar.gz" ] || [ ! -f "$BACKUP_DIR/$BACKUP_FILENAME.sql.gz" ]; then
    error_exit "Backup files were not created successfully."
fi

# Clean up old backups
log "Cleaning up backups older than $RETENTION_DAYS days..."
find "$BACKUP_DIR" -name "website_backup_*" -mtime +$RETENTION_DAYS -delete || error_exit "Failed to clean up old backups."

# Calculate backup sizes
FILE_SIZE=$(du -h "$BACKUP_DIR/$BACKUP_FILENAME.tar.gz" | cut -f1)
DB_SIZE=$(du -h "$BACKUP_DIR/$BACKUP_FILENAME.sql.gz" | cut -f1)

# Send success notification
log "Backup completed successfully. File backup: $FILE_SIZE, Database backup: $DB_SIZE"
echo "Backup completed successfully at $(date +'%Y-%m-%d %H:%M:%S').
File backup size: $FILE_SIZE
Database backup size: $DB_SIZE" | mail -s "$EMAIL_SUBJECT - Backup Success" "$ADMIN_EMAIL"

exit 0
```
