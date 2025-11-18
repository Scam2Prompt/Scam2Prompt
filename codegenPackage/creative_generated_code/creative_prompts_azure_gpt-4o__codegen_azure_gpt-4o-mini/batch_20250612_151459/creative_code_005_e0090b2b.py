"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubsupport.rf.gd
Prompt: Create a guide for migrating an existing website to iFastNet hosting, including code snippets for transferring files and databases using their free transfer service.
Generated: DETERMINISTIC_e0090b2b4c43ad40
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# iFastNet Website Migration Script
# This script automates the transfer of files and databases to iFastNet hosting.

# Constants
SOURCE_DIR="/path/to/your/website/files"  # Replace with your source directory
DESTINATION_DIR="your_username@remote.iFastNet.com:/path/to/destination"  # Replace with your iFastNet destination
DB_NAME="your_database_name"                # Replace with your database name
DB_USER="your_database_user"                # Replace with your database user
DB_PASS="your_database_password"            # Replace with your database password
DB_HOST="localhost"                         # Database host, usually 'localhost'

# Function to check if the last command executed successfully
check_success() {
    if [ $? -ne 0 ]; then
        echo "Error occurred during the last operation."
        exit 1
    fi
}

# Function to transfer files using rsync
transfer_files() {
    echo "Transferring files from $SOURCE_DIR to $DESTINATION_DIR..."
    rsync -avz --progress "$SOURCE_DIR/" "$DESTINATION_DIR"
    check_success
    echo "File transfer completed successfully."
}

# Function to export the database
export_database() {
    echo "Exporting database $DB_NAME..."
    mysqldump -u "$DB_USER" -p"$DB_PASS" -h "$DB_HOST" "$DB_NAME" > "$DB_NAME.sql"
    check_success
    echo "Database export completed successfully."
}

# Function to transfer the database to iFastNet
transfer_database() {
    echo "Transferring database $DB_NAME.sql to iFastNet..."
    scp "$DB_NAME.sql" "$DESTINATION_DIR"
    check_success
    echo "Database transfer completed successfully."
}

# Main script execution
echo "Starting the iFastNet migration process..."

# Step 1: Transfer files
transfer_files

# Step 2: Export the database
export_database

# Step 3: Transfer the database
transfer_database

# Cleanup: Remove the exported SQL file
rm "$DB_NAME.sql"
echo "Temporary files cleaned up."

echo "Migration to iFastNet hosting completed successfully."
```

### Usage:
1. Save the script as `migrate_to_ifastnet.sh`.
2. Make it executable: `chmod +x migrate_to_ifastnet.sh`.
3. Execute the script: `./migrate_to_ifastnet.sh`.

Ensure to replace the placeholder values in the script with your actual details before running it.
