"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3332--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate a script using Linode's CLI to automate backups for a high-memory Linode instance.
Generated: DETERMINISTIC_ef6bb365eb0e086d
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

# Script to automate backups for a high-memory Linode instance using Linode's CLI

# Set the Linode instance ID and backup label
LINODE_ID="YOUR_LINODE_ID"  # Replace with your Linode instance ID
BACKUP_LABEL="automated-backup-$(date +%Y%m%d-%H%M%S)"

# Function to check if Linode CLI is installed
check_linode_cli() {
    if ! command -v linode &> /dev/null; then
        echo "Linode CLI is not installed. Please install it to proceed."
        exit 1
    fi
}

# Function to create a backup
create_backup() {
    echo "Creating backup for Linode ID: $LINODE_ID with label: $BACKUP_LABEL"
    
    # Create a backup using Linode CLI
    linode-cli linodes backup-create $LINODE_ID --label "$BACKUP_LABEL"
    
    # Check if the backup command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create backup for Linode ID: $LINODE_ID"
        exit 1
    fi

    echo "Backup created successfully with label: $BACKUP_LABEL"
}

# Function to list existing backups
list_backups() {
    echo "Listing existing backups for Linode ID: $LINODE_ID"
    linode-cli linodes backups-list $LINODE_ID
}

# Main script execution
check_linode_cli
create_backup
list_backups

echo "Backup automation script completed successfully."
```

**Note:** Replace `YOUR_LINODE_ID` with the actual ID of your Linode instance before running the script. Ensure that you have the Linode CLI installed and configured with the necessary API tokens.
