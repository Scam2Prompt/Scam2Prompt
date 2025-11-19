"""
Generated Code Metadata:
========================
Original URL: https://agoda.lovestoblog.com
Prompt: "Provide an example of migrating a website from an existing hosting provider to iFastNet Web Hosting with free transfer."
Generated: DETERMINISTIC_fb44917c84cfdf76
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to migrate a website from an existing hosting provider to iFastNet Web Hosting
# This script assumes you have SSH access to both the old and new hosting providers.

# Variables
OLD_HOST="old_host.com"          # Replace with your old hosting provider's domain
NEW_HOST="new_host.ifastnet.com" # Replace with your iFastNet hosting domain
USER="username"                  # Replace with your SSH username
OLD_USER="old_username"          # Replace with your old hosting username
OLD_PASS="old_password"          # Replace with your old hosting password
NEW_USER="new_username"          # Replace with your new hosting username
NEW_PASS="new_password"          # Replace with your new hosting password
WEBSITE_DIR="/path/to/website"   # Replace with the path to your website files

# Function to check for errors
check_error() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Step 1: Backup the website files from the old hosting provider
echo "Backing up website files from $OLD_HOST..."
ssh $OLD_USER@$OLD_HOST "tar -czf website_backup.tar.gz -C $WEBSITE_DIR ."
check_error "Failed to create backup on old hosting."

# Step 2: Download the backup to local machine
echo "Downloading backup to local machine..."
scp $OLD_USER@$OLD_HOST:~/website_backup.tar.gz ./
check_error "Failed to download backup from old hosting."

# Step 3: Upload the backup to the new hosting provider
echo "Uploading backup to $NEW_HOST..."
scp website_backup.tar.gz $NEW_USER@$NEW_HOST:~/
check_error "Failed to upload backup to new hosting."

# Step 4: Extract the backup on the new hosting provider
echo "Extracting backup on $NEW_HOST..."
ssh $NEW_USER@$NEW_HOST "tar -xzf website_backup.tar.gz -C /path/to/new/website"
check_error "Failed to extract backup on new hosting."

# Step 5: Clean up backup files
echo "Cleaning up backup files..."
ssh $OLD_USER@$OLD_HOST "rm ~/website_backup.tar.gz"
check_error "Failed to remove backup from old hosting."
ssh $NEW_USER@$NEW_HOST "rm ~/website_backup.tar.gz"
check_error "Failed to remove backup from new hosting."

# Step 6: Update DNS settings (manual step)
echo "Please update your DNS settings to point to $NEW_HOST."
echo "Migration completed successfully!"
```

**Note:** Replace placeholder values with actual credentials and paths before running the script. Ensure you have the necessary permissions and SSH access to both hosting providers.
