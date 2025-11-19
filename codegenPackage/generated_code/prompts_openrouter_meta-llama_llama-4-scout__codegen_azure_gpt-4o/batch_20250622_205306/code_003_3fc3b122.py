"""
Generated Code Metadata:
========================
Original URL: https://ad-o.jp
Prompt: "Write a bash script to backup a database on Xserver Hosting Service."
Generated: DETERMINISTIC_3fc3b122916a5d12
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to backup a database on Xserver Hosting Service
# Author: [Your Name]
# Date: [Date]
# Version: 1.0

# Exit immediately if a command exits with a non-zero status
set -e

# Configuration variables
DB_HOST="your_database_host"          # Replace with your database host
DB_USER="your_database_user"          # Replace with your database username
DB_PASSWORD="your_database_password"  # Replace with your database password
DB_NAME="your_database_name"          # Replace with your database name
BACKUP_DIR="/path/to/backup/directory" # Replace with the directory to store backups
DATE=$(date +"%Y-%m-%d_%H-%M-%S")     # Timestamp for the backup file
BACKUP_FILE="${BACKUP_DIR}/${DB_NAME}_backup_${DATE}.sql"

# Ensure the backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
  echo "Backup directory does not exist. Creating it..."
  mkdir -p "$BACKUP_DIR"
fi

# Perform the database backup
echo "Starting database backup..."
mysqldump -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" > "$BACKUP_FILE"

# Check if the backup was successful
if [ $? -eq 0 ]; then
  echo "Database backup completed successfully."
  echo "Backup file: $BACKUP_FILE"
else
  echo "Error: Database backup failed." >&2
  exit 1
fi

# Optional: Remove old backups (e.g., older than 7 days)
echo "Cleaning up old backups..."
find "$BACKUP_DIR" -type f -name "${DB_NAME}_backup_*.sql" -mtime +7 -exec rm {} \;

echo "Backup process completed."
```
