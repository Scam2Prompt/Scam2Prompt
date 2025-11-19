"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Develop a Linux shell script to perform weekly remote backups for websites hosted on a server, as described in the hosting features of the Megh iTech website.
Generated: DETERMINISTIC_e8bdd8c0459c0b30
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Remote Backup Script for Websites
# Performs weekly backups of website files and databases
# Author: Megh iTech
# Version: 1.0

# Configuration
BACKUP_DIR="/backups"
LOG_FILE="/var/log/backup.log"
DATE=$(date +%Y%m%d)
RETENTION_DAYS=30
REMOTE_USER="backupuser"
REMOTE_SERVER="backup.example.com"
REMOTE_DIR="/remote/backups"
MYSQL_USER="backup"
MYSQL_PASS="securepassword"
WEBSITE_DIRS=("/var/www/site1" "/var/www/site2")
DATABASES=("db1" "db2")

# Ensure backup directory exists
mkdir -p "$BACKUP_DIR"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Error handling function
error_exit() {
    log "ERROR: $1"
    exit 1
}

# Check if required commands are available
for cmd in mysqldump rsync ssh tar; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        error_exit "Required command '$cmd' not found"
    fi
done

# Create backup directory for current date
CURRENT_BACKUP="$BACKUP_DIR/$DATE"
mkdir -p "$CURRENT_BACKUP" || error_exit "Failed to create backup directory $CURRENT_BACKUP"

log "Starting weekly backup process"

# Backup website files
for site in "${WEBSITE_DIRS[@]}"; do
    SITE_NAME=$(basename "$site")
    BACKUP_FILE="$CURRENT_BACKUP/$SITE_NAME-files.tar.gz"
    
    log "Backing up website files from $site"
    tar -czf "$BACKUP_FILE" "$site" 2>> "$LOG_FILE" || error_exit "Failed to create tar archive for $site"
done

# Backup MySQL databases
for db in "${DATABASES[@]}"; do
    BACKUP_FILE="$CURRENT_BACKUP/$db.sql.gz"
    
    log "Backing up database $db"
    mysqldump -u "$MYSQL_USER" -p"$MYSQL_PASS" "$db" | gzip > "$BACKUP_FILE" 2>> "$LOG_FILE" || error_exit "Failed to backup database $db"
done

# Transfer backups to remote server
log "Transferring backups to remote server"
rsync -avz -e ssh "$CURRENT_BACKUP/" "$REMOTE_USER@$REMOTE_SERVER:$REMOTE_DIR/$DATE/" >> "$LOG_FILE" 2>&1 || error_exit "Failed to transfer backups to remote server"

# Clean up old local backups
log "Cleaning up backups older than $RETENTION_DAYS days"
find "$BACKUP_DIR" -type d -mtime +$RETENTION_DAYS -exec rm -rf {} \; >> "$LOG_FILE" 2>&1

log "Backup completed successfully"
exit 0
```
