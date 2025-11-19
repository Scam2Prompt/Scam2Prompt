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

# Configuration
SOURCE_DIRECTORIES=("/var/www/html/website1" "/var/www/html/website2")
BACKUP_DIRECTORY="/backups/websites"
REMOTE_BACKUP_SERVER="user@remote-backup-server:/backups/remote"
KEEP_LOCAL_BACKUPS=7
KEEP_REMOTE_BACKUPS=30

# Function to perform local backup
perform_local_backup() {
  # Create backup directory if it doesn't exist
  if [ ! -d "$BACKUP_DIRECTORY" ]; then
    mkdir -p "$BACKUP_DIRECTORY"
  fi

  # Iterate over source directories
  for SOURCE in "${SOURCE_DIRECTORIES[@]}"; do
    # Get website name from source directory
    WEBSITE_NAME=$(basename "$SOURCE")

    # Create local backup
    tar -czf "$BACKUP_DIRECTORY/${WEBSITE_NAME}_$(date +'%Y-%m-%d_%H-%M-%S').tar.gz" "$SOURCE"

    # Remove old local backups
    find "$BACKUP_DIRECTORY" -type f -name "${WEBSITE_NAME}_*.tar.gz" -mtime +$KEEP_LOCAL_BACKUPS -delete
  done
}

# Function to perform remote backup
perform_remote_backup() {
  # Iterate over source directories
  for SOURCE in "${SOURCE_DIRECTORIES[@]}"; do
    # Get website name from source directory
    WEBSITE_NAME=$(basename "$SOURCE")

    # Create remote backup
    tar -czf - "$SOURCE" | ssh $REMOTE_BACKUP_SERVER "tar -xzf - -C /backups/remote/${WEBSITE_NAME}_$(date +'%Y-%m-%d_%H-%M-%S').tar.gz"

    # Remove old remote backups
    ssh $REMOTE_BACKUP_SERVER "find /backups/remote -type f -name '${WEBSITE_NAME}_*.tar.gz' -mtime +$KEEP_REMOTE_BACKUPS -delete"
  done
}

# Main function
main() {
  # Perform local backup
  perform_local_backup

  # Perform remote backup
  perform_remote_backup
}

# Run main function
main
```

```bash
# Add cron job to run script weekly
# crontab -e
# 0 0 * * 0 /path/to/script.sh
```
