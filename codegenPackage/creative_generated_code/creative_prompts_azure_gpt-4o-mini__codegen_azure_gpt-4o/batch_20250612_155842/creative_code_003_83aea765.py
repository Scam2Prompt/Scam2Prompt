"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agromec.cl
Prompt: Create a simple website deployment script for a PHP application on a Linux server.
Generated: DETERMINISTIC_83aea765f22552c2
Batch ID: 20250612_155842
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/example/$APP_NAME.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Website Deployment Script for PHP Application on a Linux Server
# Author: [Your Name]
# Date: [Date]
# Version: 1.0

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
APP_NAME="my_php_app"                 # Name of the application
DEPLOY_DIR="/var/www/$APP_NAME"       # Deployment directory
BACKUP_DIR="/var/backups/$APP_NAME"   # Backup directory
SOURCE_CODE_DIR="/tmp/$APP_NAME"      # Temporary location for new source code
WEB_SERVER="apache2"                  # Web server (can also be nginx)
PHP_VERSION="php8.1"                  # PHP version to check

# Function to check if a command exists
check_command() {
    command -v "$1" >/dev/null 2>&1 || {
        echo "Error: $1 is not installed or not in PATH." >&2
        exit 1
    }
}

# Check dependencies
check_command git
check_command rsync
check_command $WEB_SERVER
check_command $PHP_VERSION

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root." >&2
    exit 1
fi

# Step 1: Backup current application (if exists)
if [ -d "$DEPLOY_DIR" ]; then
    echo "Creating backup of current application..."
    mkdir -p "$BACKUP_DIR"
    TIMESTAMP=$(date +"%Y%m%d%H%M%S")
    BACKUP_FILE="$BACKUP_DIR/$APP_NAME-backup-$TIMESTAMP.tar.gz"
    tar -czf "$BACKUP_FILE" -C "$DEPLOY_DIR" .
    echo "Backup created at $BACKUP_FILE"
else
    echo "No existing application found. Skipping backup step."
fi

# Step 2: Clean up old deployment directory
echo "Cleaning up old deployment files..."
rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"

# Step 3: Download or copy new source code
echo "Downloading new source code..."
# Example: Fetch code from a Git repository (replace with your repository URL)
git clone https://github.com/example/$APP_NAME.git "$SOURCE_CODE_DIR"

# Step 4: Deploy new source code to the deployment directory
echo "Deploying new source code..."
rsync -av --delete "$SOURCE_CODE_DIR/" "$DEPLOY_DIR/"
rm -rf "$SOURCE_CODE_DIR"

# Step 5: Set appropriate permissions
echo "Setting appropriate permissions..."
chown -R www-data:www-data "$DEPLOY_DIR"
chmod -R 755 "$DEPLOY_DIR"

# Step 6: Restart web server
echo "Restarting web server..."
systemctl restart "$WEB_SERVER"

# Step 7: Verify deployment
echo "Verifying deployment..."
if systemctl is-active --quiet "$WEB_SERVER"; then
    echo "Web server is running."
else
    echo "Error: Web server failed to start." >&2
    exit 1
fi

# End of script
echo "Deployment completed successfully!"
```
