"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Explain how to use Linode's CLI to manage backups and restore data, providing code examples for common commands.
Generated: DETERMINISTIC_8f5557dd47ff13f9
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

# Script to demonstrate using Linode CLI to manage backups and restore data.
# Ensure you have the Linode CLI installed and configured with your API token.
# Run `linode-cli configure` to set up the CLI before using this script.

# Function to list available backups for a Linode instance
list_backups() {
  # Replace <LINODE_ID> with the ID of your Linode instance
  LINODE_ID="<LINODE_ID>"
  
  echo "Listing backups for Linode ID: $LINODE_ID"
  linode-cli linodes backups-view $LINODE_ID --json | jq '.'
}

# Function to enable backups for a Linode instance
enable_backups() {
  # Replace <LINODE_ID> with the ID of your Linode instance
  LINODE_ID="<LINODE_ID>"
  
  echo "Enabling backups for Linode ID: $LINODE_ID"
  linode-cli linodes update $LINODE_ID --backups_enabled true
}

# Function to restore a backup to a Linode instance
restore_backup() {
  # Replace <LINODE_ID> with the ID of your Linode instance
  LINODE_ID="<LINODE_ID>"
  # Replace <BACKUP_ID> with the ID of the backup you want to restore
  BACKUP_ID="<BACKUP_ID>"
  
  echo "Restoring backup ID: $BACKUP_ID to Linode ID: $LINODE_ID"
  linode-cli linodes backups-restore $LINODE_ID --backup_id $BACKUP_ID
}

# Main menu for the script
echo "Linode CLI Backup Management Script"
echo "1. List Backups"
echo "2. Enable Backups"
echo "3. Restore Backup"
echo "4. Exit"
read -p "Choose an option: " OPTION

case $OPTION in
  1)
    list_backups
    ;;
  2)
    enable_backups
    ;;
  3)
    restore_backup
    ;;
  4)
    echo "Exiting script."
    exit 0
    ;;
  *)
    echo "Invalid option. Please try again."
    ;;
esac
```

### Notes:
- Replace `<LINODE_ID>` and `<BACKUP_ID>` with actual values for your Linode instance and backup.
- Ensure `jq` is installed for JSON parsing (`sudo apt install jq` on Debian-based systems).
- This script assumes the Linode CLI is already installed and configured.
