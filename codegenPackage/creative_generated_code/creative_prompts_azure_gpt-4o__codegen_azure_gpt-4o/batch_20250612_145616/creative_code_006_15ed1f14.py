"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-clink.org
Prompt: Generate a Bash script to automate the backup of Nginx Proxy Manager configuration files.
Generated: DETERMINISTIC_15ed1f14186e93fc
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the backup of Nginx Proxy Manager configuration files
# Author: [Your Name]
# Date: [YYYY-MM-DD]
# Version: 1.0

# Exit on error
set -euo pipefail

# Variables
BACKUP_DIR="/var/backups/nginx-proxy-manager"
CONFIG_DIR="/data/nginx-proxy-manager"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="npm_backup_$TIMESTAMP.tar.gz"
LOG_FILE="/var/log/nginx-proxy-manager-backup.log"

# Ensure backup directory exists
if [[ ! -d "$BACKUP_DIR" ]]; then
    mkdir -p "$BACKUP_DIR"
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] Created backup directory: $BACKUP_DIR" >> "$LOG_FILE"
fi

# Check if configuration directory exists
if [[ ! -d "$CONFIG_DIR" ]]; then
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] ERROR: Configuration directory $CONFIG_DIR does not exist." | tee -a "$LOG_FILE"
    exit 1
fi

# Perform the backup
echo "[$(date +"%Y-%m-%d %H:%M:%S")] Starting backup of $CONFIG_DIR to $BACKUP_DIR/$BACKUP_FILE" >> "$LOG_FILE"
tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$CONFIG_DIR" .

# Verify if the backup was successful
if [[ $? -eq 0 ]]; then
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] Backup completed successfully: $BACKUP_DIR/$BACKUP_FILE" >> "$LOG_FILE"
else
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] ERROR: Backup failed." | tee -a "$LOG_FILE"
    exit 1
fi

# Clean up old backups (older than 30 days)
find "$BACKUP_DIR" -type f -name "npm_backup_*.tar.gz" -mtime +30 -exec rm -f {} \;
echo "[$(date +"%Y-%m-%d %H:%M:%S")] Old backups cleaned up (files older than 30 days)." >> "$LOG_FILE"

# Completion message
echo "[$(date +"%Y-%m-%d %H:%M:%S")] Backup operation completed." >> "$LOG_FILE"
exit 0
```
