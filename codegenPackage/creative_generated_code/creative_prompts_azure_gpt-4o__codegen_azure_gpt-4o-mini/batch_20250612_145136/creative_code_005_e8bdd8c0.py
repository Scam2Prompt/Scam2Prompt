"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Develop a Linux shell script to perform weekly remote backups for websites hosted on a server, as described in the hosting features of the Megh iTech website.
Generated: DETERMINISTIC_e8bdd8c0459c0b30
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script for performing weekly remote backups of websites.

# Define constants
BACKUP_DIR="/path/to/backup/dir"   # Local backup directory
REMOTE_SERVER="user@remote.server"  # Remote server user and address
REMOTE_DIR="/path/to/remote/backup" # Remote directory for backups
DATE=$(date +"%Y-%m-%d")            # Current date for backup filename
LOG_FILE="/var/log/weekly_backup.log" # Log file for backup processes
WEBSITE_DIRS=("/var/www/html/site1" "/var/www/html/site2") # List of website directories to backup

# Function to log messages
log_message() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" >> "$LOG_FILE"
}

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Loop through each website directory
for DIR in "${WEBSITE_DIRS[@]}"; do
    # Check if directory exists
    if [ -d "$DIR" ]; then
        # Define backup filename
        BACKUP_FILENAME="$(basename "$DIR")-$DATE.tar.gz"

        # Create a compressed archive of the website directory
        tar -czf "$BACKUP_DIR/$BACKUP_FILENAME" -C "$(dirname "$DIR")" "$(basename "$DIR")" 2>> "$LOG_FILE"
        
        # Check if the tar command was successful
        if [ $? -eq 0 ]; then
            log_message "Backup of $DIR completed successfully as $BACKUP_FILENAME."
        else
            log_message "Error: Backup of $DIR failed."
            continue
        fi

        # Transfer the backup to the remote server
        scp "$BACKUP_DIR/$BACKUP_FILENAME" "$REMOTE_SERVER:$REMOTE_DIR" 2>> "$LOG_FILE"
        
        # Check if the scp command was successful
        if [ $? -eq 0 ]; then
            log_message "Successfully transferred $BACKUP_FILENAME to $REMOTE_SERVER."
            # Optionally, remove the local backup after successful transfer
            rm "$BACKUP_DIR/$BACKUP_FILENAME"
        else
            log_message "Error: Failed to transfer $BACKUP_FILENAME to $REMOTE_SERVER."
        fi
    else
        log_message "Warning: Directory $DIR does not exist. Skipping backup."
    fi
done

# End of script
```
