"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: What is the process to automate backups on Linode using StackScripts?
Generated: DETERMINISTIC_2288727a6d41b3df
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Backup Automation Script for Linode using StackScripts
# This script automates the process of backing up specified directories to a remote storage location.

# Define variables
SOURCE_DIR="/path/to/your/data"     # Directory to backup
BACKUP_DIR="/path/to/backup"         # Local backup directory
REMOTE_USER="your_username"          # Remote server username
REMOTE_HOST="your_remote_host"       # Remote server host
REMOTE_DIR="/path/to/remote/backup"  # Remote backup directory
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")   # Timestamp for backup filename
BACKUP_FILE="backup_$TIMESTAMP.tar.gz" # Backup file name

# Function to create a local backup
create_local_backup() {
    echo "Creating local backup..."
    tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$SOURCE_DIR" .
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create local backup."
        exit 1
    fi
    echo "Local backup created: $BACKUP_DIR/$BACKUP_FILE"
}

# Function to transfer backup to remote server
transfer_backup() {
    echo "Transferring backup to remote server..."
    scp "$BACKUP_DIR/$BACKUP_FILE" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR/"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to transfer backup to remote server."
        exit 1
    fi
    echo "Backup successfully transferred to $REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR/"
}

# Function to clean up local backups older than 7 days
cleanup_local_backups() {
    echo "Cleaning up local backups older than 7 days..."
    find "$BACKUP_DIR" -type f -name 'backup_*.tar.gz' -mtime +7 -exec rm -f {} \;
    if [ $? -ne 0 ]; then
        echo "Error: Failed to clean up local backups."
        exit 1
    fi
    echo "Local backups cleaned up."
}

# Main script execution
echo "Starting backup process..."
create_local_backup
transfer_backup
cleanup_local_backups
echo "Backup process completed successfully."
```

### Usage:
1. Replace the placeholder paths and credentials in the script.
2. Save the script in a `.sh` file, e.g., `backup_script.sh`.
3. Make the script executable: `chmod +x backup_script.sh`.
4. Execute the script: `./backup_script.sh`. 

### Note:
- Ensure you have SSH access to the remote server and necessary permissions on the directories.
- This script is designed to run on a schedule; consider using cron jobs for automation.
