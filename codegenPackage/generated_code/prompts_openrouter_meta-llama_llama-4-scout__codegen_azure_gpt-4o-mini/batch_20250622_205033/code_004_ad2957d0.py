"""
Generated Code Metadata:
========================
Original URL: https://connext.site
Prompt: Create a tutorial on how to migrate a website from one Hostinger hosting plan to another while keeping the domain nameservers intact.
Generated: DETERMINISTIC_ad2957d031a76767
Batch ID: 20250622_205033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to migrate a website from one Hostinger hosting plan to another
# while keeping the domain nameservers intact.

# Function to display usage information
usage() {
    echo "Usage: $0 <source_ftp_user> <source_ftp_password> <source_ftp_host> <destination_ftp_user> <destination_ftp_password> <destination_ftp_host>"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 6 ]; then
    usage
fi

# Assigning input parameters to variables
SOURCE_FTP_USER=$1
SOURCE_FTP_PASSWORD=$2
SOURCE_FTP_HOST=$3
DESTINATION_FTP_USER=$4
DESTINATION_FTP_PASSWORD=$5
DESTINATION_FTP_HOST=$6

# Function to perform FTP transfer
ftp_transfer() {
    local source_host=$1
    local dest_host=$2
    local user=$3
    local password=$4

    # Create a temporary directory for the transfer
    TEMP_DIR=$(mktemp -d)
    if [ ! -d "$TEMP_DIR" ]; then
        echo "Error: Failed to create temporary directory."
        exit 1
    fi

    # Download files from the source FTP server
    echo "Downloading files from $source_host..."
    lftp -u "$SOURCE_FTP_USER","$SOURCE_FTP_PASSWORD" "$SOURCE_FTP_HOST" -e "mirror --verbose --delete --only-newer . $TEMP_DIR; bye"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to download files from $source_host."
        exit 1
    fi

    # Upload files to the destination FTP server
    echo "Uploading files to $dest_host..."
    lftp -u "$DESTINATION_FTP_USER","$DESTINATION_FTP_PASSWORD" "$DESTINATION_FTP_HOST" -e "mirror --verbose --delete $TEMP_DIR .; bye"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to upload files to $dest_host."
        exit 1
    fi

    # Clean up temporary directory
    rm -rf "$TEMP_DIR"
    echo "Migration completed successfully."
}

# Start the migration process
ftp_transfer "$SOURCE_FTP_HOST" "$DESTINATION_FTP_HOST" "$DESTINATION_FTP_USER" "$DESTINATION_FTP_PASSWORD"
```

### Instructions to Run the Script:
1. Save the script to a file, e.g., `migrate_website.sh`.
2. Make the script executable: `chmod +x migrate_website.sh`.
3. Run the script with the required parameters:
   ```bash
   ./migrate_website.sh <source_ftp_user> <source_ftp_password> <source_ftp_host> <destination_ftp_user> <destination_ftp_password> <destination_ftp_host>
   ```
4. Ensure you have `lftp` installed on your system for FTP operations.
