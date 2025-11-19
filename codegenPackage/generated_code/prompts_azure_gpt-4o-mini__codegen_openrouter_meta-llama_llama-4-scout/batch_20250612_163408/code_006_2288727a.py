"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: What is the process to automate backups on Linode using StackScripts?
Generated: DETERMINISTIC_2288727a6d41b3df
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# StackScript to automate backups on Linode
# ======================================================

# Set backup directory and filename
BACKUP_DIR="/backups"
BACKUP_FILENAME="linode-backup-$(date +'%Y-%m-%d-%H-%M-%S')"

# Check if backup directory exists, create if not
if [ ! -d "$BACKUP_DIR" ]; then
  # Create backup directory with permissions
  mkdir -p -m 700 "$BACKUP_DIR"
fi

# Set databases to backup (space-separated list)
DATABASES="mysql postgres"

# Set directories to backup (space-separated list)
DIRECTORIES="/etc /home /root /srv"

# Function to perform database backup
backup_databases() {
  for db in $DATABASES; do
    case $db in
      mysql)
        # Use mysqldump to backup MySQL databases
        mysqldump -u root -p$MYSQL_PASSWORD --all-databases > "$BACKUP_DIR/${BACKUP_FILENAME}-mysql.sql"
        ;;
      postgres)
        # Use pg_dumpall to backup PostgreSQL databases
        pg_dumpall -U postgres -W $POSTGRES_PASSWORD > "$BACKUP_DIR/${BACKUP_FILENAME}-postgres.sql"
        ;;
    esac
  done
}

# Function to perform directory backup
backup_directories() {
  for dir in $DIRECTORIES; do
    # Use tar to backup directories
    tar -czf "$BACKUP_DIR/${BACKUP_FILENAME}-${dir//\//_}.tar.gz" "$dir"
  done
}

# Main backup function
perform_backup() {
  # Create backup filename
  echo "Performing backup to $BACKUP_DIR/$BACKUP_FILENAME..."
  
  # Backup databases
  backup_databases
  
  # Backup directories
  backup_directories
  
  # Compress and remove individual database backups
  tar -czf "$BACKUP_DIR/${BACKUP_FILENAME}.tar.gz" "$BACKUP_DIR/${BACKUP_FILENAME}-"* 
  rm -rf "$BACKUP_DIR/${BACKUP_FILENAME}-"*
  
  echo "Backup complete: $BACKUP_DIR/${BACKUP_FILENAME}.tar.gz"
}

# Error handling
if [ $(id -u) -ne 0 ]; then
  echo "Error: This script must be run as root."
  exit 1
fi

# Check for required environment variables
if [ -z "$MYSQL_PASSWORD" ] || [ -z "$POSTGRES_PASSWORD" ]; then
  echo "Error: MYSQL_PASSWORD and POSTGRES_PASSWORD environment variables are required."
  exit 1
fi

# Perform backup
perform_backup
```
