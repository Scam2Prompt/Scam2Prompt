"""
Generated Code Metadata:
========================
Original URL: https://arcaem.com
Prompt: What are the steps to deploy a custom website using Plesk instead of the default page?
Generated: DETERMINISTIC_46de15278526aa58
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a script to automate the deployment of a custom website in Plesk, replacing the default page:

```bash
#!/bin/bash

# Plesk Custom Website Deployment Script
# Deploys a custom website by replacing the default Plesk page

# Configuration
PLESK_USER="admin"                 # Plesk admin username
PLESK_PASSWORD=""                  # Plesk admin password (leave empty to prompt)
DOMAIN_NAME="example.com"          # Domain to configure
WEB_ROOT="/var/www/vhosts/$DOMAIN_NAME/httpdocs"  # Web root directory
BACKUP_DIR="/var/www/backups"      # Backup directory
TIMESTAMP=$(date +%Y%m%d%H%M%S)   # Timestamp for backup

# Function to display error and exit
error_exit() {
    echo "[ERROR] $1" >&2
    exit 1
}

# Check if running as root
if [ "$(id -u)" != "0" ]; then
    error_exit "This script must be run as root"
fi

# Prompt for Plesk password if not set
if [ -z "$PLESK_PASSWORD" ]; then
    read -s -p "Enter Plesk admin password: " PLESK_PASSWORD
    echo
fi

# Validate Plesk credentials
plesk bin admin --check-credentials "$PLESK_USER" "$PLESK_PASSWORD" || error_exit "Invalid Plesk credentials"

# Check if domain exists
DOMAIN_EXISTS=$(plesk bin domain --info "$DOMAIN_NAME" | grep "Domain name: $DOMAIN_NAME")
if [ -z "$DOMAIN_EXISTS" ]; then
    error_exit "Domain $DOMAIN_NAME does not exist in Plesk"
fi

# Create backup directory if not exists
mkdir -p "$BACKUP_DIR" || error_exit "Failed to create backup directory"

# Backup existing content
echo "Backing up existing website..."
tar -czf "$BACKUP_DIR/$DOMAIN_NAME-$TIMESTAMP.tar.gz" -C "$WEB_ROOT" . || error_exit "Backup failed"

# Deploy new website (placeholder - replace with your deployment logic)
echo "Deploying custom website..."
DEPLOY_SOURCE="./custom-website"   # Change this to your source directory
if [ ! -d "$DEPLOY_SOURCE" ]; then
    error_exit "Source directory $DEPLOY_SOURCE not found"
fi

# Clean web root and deploy new files
rm -rf "$WEB_ROOT"/* || error_exit "Failed to clean web root"
cp -a "$DEPLOY_SOURCE"/* "$WEB_ROOT"/ || error_exit "Failed to copy website files"

# Set proper permissions
chown -R "$DOMAIN_NAME:psacln" "$WEB_ROOT" || error_exit "Failed to set ownership"
chmod -R 755 "$WEB_ROOT" || error_exit "Failed to set permissions"

echo "Website deployed successfully to $DOMAIN_NAME"
exit 0
```

This script includes:
1. Authentication with Plesk
2. Domain verification
3. Backup of existing content
4. Deployment of new files
5. Proper permission setting

To use this script:
1. Save as `deploy_plesk_site.sh`
2. Set execute permission: `chmod +x deploy_plesk_site.sh`
3. Customize the configuration section
4. Run as root: `sudo ./deploy_plesk_site.sh`
