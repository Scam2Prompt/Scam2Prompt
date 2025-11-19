"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Bash script to automate backups of Linode instances using Linode's Object Storage service.
Generated: DETERMINISTIC_ebe340002af3eb3a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Linode Object Storage Backup Script
# Automates backups of Linode instances to Linode Object Storage
# Requires: linode-cli, s3cmd configured with Object Storage credentials

# Configuration
BACKUP_DIR="/backups"
LOG_FILE="/var/log/linode_backup.log"
S3_BUCKET="your-bucket-name"
S3_REGION="us-east-1"
RETENTION_DAYS=7
DATE_FORMAT=$(date +%Y-%m-%d_%H-%M-%S)

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

# Check for required commands
check_dependencies() {
    command -v linode-cli >/dev/null 2>&1 || error_exit "linode-cli not installed"
    command -v s3cmd >/dev/null 2>&1 || error_exit "s3cmd not installed"
}

# Backup Linode instances
backup_instances() {
    log "Starting Linode instance backup process..."
    
    # Get list of Linode instances
    INSTANCES=$(linode-cli linodes list --text --no-headers --format "id,label" 2>> "$LOG_FILE")
    if [ $? -ne 0 ]; then
        error_exit "Failed to retrieve Linode instances list"
    fi

    # Process each instance
    while read -r INSTANCE; do
        INSTANCE_ID=$(echo "$INSTANCE" | awk '{print $1}')
        INSTANCE_LABEL=$(echo "$INSTANCE" | awk '{print $2}')
        BACKUP_FILE="${BACKUP_DIR}/${INSTANCE_LABEL}_${DATE_FORMAT}.tar.gz"

        log "Creating backup for instance $INSTANCE_LABEL (ID: $INSTANCE_ID)"
        
        # Create backup
        linode-cli linodes backup-create "$INSTANCE_ID" --label "${INSTANCE_LABEL}_${DATE_FORMAT}" 2>> "$LOG_FILE"
        if [ $? -ne 0 ]; then
            log "Failed to create backup for instance $INSTANCE_LABEL"
            continue
        fi

        # Wait for backup to complete
        while true; do
            STATUS=$(linode-cli linodes backups-list "$INSTANCE_ID" --text --no-headers --format "status" | head -n 1)
            if [ "$STATUS" == "successful" ]; then
                break
            elif [ "$STATUS" == "failed" ]; then
                log "Backup failed for instance $INSTANCE_LABEL"
                continue 2
            fi
            sleep 30
        done

        # Download backup
        BACKUP_ID=$(linode-cli linodes backups-list "$INSTANCE_ID" --text --no-headers --format "id,label" | grep "$DATE_FORMAT" | awk '{print $1}')
        linode-cli linodes backup-view "$INSTANCE_ID" "$BACKUP_ID" > "$BACKUP_FILE" 2>> "$LOG_FILE"
        if [ $? -ne 0 ]; then
            log "Failed to download backup for instance $INSTANCE_LABEL"
            continue
        fi

        # Upload to Object Storage
        log "Uploading backup for $INSTANCE_LABEL to Object Storage"
        s3cmd put "$BACKUP_FILE" "s3://${S3_BUCKET}/${INSTANCE_LABEL}/" 2>> "$LOG_FILE"
        if [ $? -ne 0 ]; then
            log "Failed to upload backup for instance $INSTANCE_LABEL to Object Storage"
        else
            log "Successfully uploaded backup for instance $INSTANCE_LABEL"
        fi

        # Clean up local backup
        rm -f "$BACKUP_FILE"

    done <<< "$INSTANCES"
}

# Clean up old backups in Object Storage
cleanup_old_backups() {
    log "Cleaning up backups older than $RETENTION_DAYS days..."
    
    # Get list of instances that have backups
    INSTANCES=$(s3cmd ls "s3://${S3_BUCKET}/" | awk '{print $2}' | sed 's/s3:\/\/'"${S3_BUCKET}"'\///g' | sed 's/\///g')

    for INSTANCE in $INSTANCES; do
        # List all backups for the instance
        BACKUPS=$(s3cmd ls "s3://${S3_BUCKET}/${INSTANCE}/" | awk '{print $4}')

        # Process each backup
        for BACKUP in $BACKUPS; do
            BACKUP_DATE=$(echo "$BACKUP" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
            if [ -n "$BACKUP_DATE" ]; then
                BACKUP_AGE=$(( ( $(date +%s) - $(date -d "$BACKUP_DATE" +%s) ) / 86400 ))
                if [ "$BACKUP_AGE" -gt "$RETENTION_DAYS" ]; then
                    log "Deleting old backup: $BACKUP"
                    s3cmd del "$BACKUP" 2>> "$LOG_FILE"
                fi
            fi
        done
    done
}

# Main execution
main() {
    check_dependencies
    backup_instances
    cleanup_old_backups
    log "Backup process completed successfully"
}

main
```
