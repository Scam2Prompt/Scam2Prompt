"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idn-hosting.com
Prompt: Explain how to migrate a website to IDN Hosting's cloud platform without downtime, including code examples for backup and restore.
Generated: DETERMINISTIC_608f206192f03fed
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Define variables for source and destination
SOURCE_DIR="/path/to/your/website"  # Change this to your website's directory
BACKUP_DIR="/path/to/backup"         # Change this to your backup directory
DESTINATION="user@idn-hosting.com:/path/to/destination"  # Change to your IDN Hosting destination

# Function to create a backup of the website
create_backup() {
    echo "Creating backup of the website..."
    # Create a timestamped backup directory
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    BACKUP_TARGET="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"
    
    # Create a compressed archive of the website files
    tar -czf "$BACKUP_TARGET" -C "$SOURCE_DIR" .
    
    if [ $? -eq 0 ]; then
        echo "Backup created successfully at: $BACKUP_TARGET"
    else
        echo "Error: Failed to create backup." >&2
        exit 1
    fi
}

# Function to migrate files to IDN Hosting
migrate_to_idn() {
    echo "Starting migration to IDN Hosting..."
    
    # Use rsync to transfer files with progress and compression
    rsync -avz --delete "$SOURCE_DIR/" "$DESTINATION"

    if [ $? -eq 0 ]; then
        echo "Migration to IDN Hosting completed successfully."
    else
        echo "Error: Migration failed." >&2
        exit 1
    fi
}

# Function to restore backup if needed
restore_backup() {
    echo "Restoring backup from: $1"
    
    # Check if the backup file exists
    if [ -f "$1" ]; then
        # Extract the backup
        tar -xzf "$1" -C "$SOURCE_DIR"
        
        if [ $? -eq 0 ]; then
            echo "Backup restored successfully from: $1"
        else
            echo "Error: Failed to restore backup." >&2
            exit 1
        fi
    else
        echo "Error: Backup file does not exist." >&2
        exit 1
    fi
}

# Main script execution
create_backup      # Step 1: Create a backup
migrate_to_idn     # Step 2: Migrate to IDN Hosting

# Uncomment the following line to restore backup if needed
# restore_backup "/path/to/backup/backup_TIMESTAMP.tar.gz"  # Replace with actual backup file path
```

### Notes:
- Replace placeholder paths and destination information with actual values before running the script.
- Ensure that you have SSH access to the IDN Hosting server for the migration step.
- The restore function is included but commented out; it can be activated by uncommenting and providing an existing backup file path.
