"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaranetwork.cloud
Prompt: Create a bash script to back up website files and databases before migrating to Hostinger.
Generated: DETERMINISTIC_4628ffcd5ea8831c
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Define backup directory and date format
BACKUP_DIR="/path/to/your/backup/directory"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
WEB_DIR="/path/to/your/website/directory"
DB_NAME="your_database_name"
DB_USER="your_database_user"
DB_PASS="your_database_password"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Function to back up website files
backup_files() {
    echo "Starting backup of website files..."
    tar -czf "$BACKUP_DIR/website_backup_$DATE.tar.gz" -C "$WEB_DIR" .
    if [ $? -eq 0 ]; then
        echo "Website files backed up successfully!"
    else
        echo "Error while backing up website files!" >&2
        exit 1
    fi
}

# Function to back up database
backup_database() {
    echo "Starting backup of database..."
    mysqldump -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$BACKUP_DIR/db_backup_$DB_NAME_$DATE.sql"
    if [ $? -eq 0 ]; then
        echo "Database backed up successfully!"
    else
        echo "Error while backing up database!" >&2
        exit 1
    fi
}

# Function to compress backups
compress_backups() {
    echo "Compressing backups..."
    zip -r "$BACKUP_DIR/backups_$DATE.zip" "$BACKUP_DIR/website_backup_$DATE.tar.gz" "$BACKUP_DIR/db_backup_$DB_NAME_$DATE.sql"
    if [ $? -eq 0 ]; then
        echo "Backups compressed successfully!"
    else
        echo "Error while compressing backups!" >&2
        exit 1
    fi
}

# Main script execution
backup_files
backup_database
compress_backups

echo "Backup completed successfully! All files are stored in $BACKUP_DIR."
```

Make sure to replace the placeholder paths and database credentials with your actual values before running the script.
