"""
Generated Code Metadata:
========================
Original URL: https://agromec.cl
Prompt: Create a simple website deployment script for a PHP application on a Linux server.
Generated: DETERMINISTIC_83aea765f22552c2
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Website Deployment Script for PHP Application
# Author: [Your Name]
# Date: [Date]
# Description: This script automates the deployment of a PHP application on a Linux server.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage instructions
usage() {
    echo "Usage: $0 <source_directory> <destination_directory>"
    echo "Example: $0 /path/to/source /var/www/html"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    usage
fi

# Variables
SOURCE_DIR=$1
DEST_DIR=$2
BACKUP_DIR="${DEST_DIR}_backup_$(date +%Y%m%d%H%M%S)"

# Ensure the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Ensure the destination directory exists
if [ ! -d "$DEST_DIR" ]; then
    echo "Error: Destination directory '$DEST_DIR' does not exist."
    exit 1
fi

# Backup the existing website files
echo "Creating backup of existing website files..."
mkdir -p "$BACKUP_DIR"
cp -r "$DEST_DIR/"* "$BACKUP_DIR/"
echo "Backup created at '$BACKUP_DIR'."

# Deploy the new website files
echo "Deploying new website files..."
rsync -av --delete "$SOURCE_DIR/" "$DEST_DIR/"
echo "Deployment completed successfully."

# Set proper permissions for the destination directory
echo "Setting permissions for '$DEST_DIR'..."
chown -R www-data:www-data "$DEST_DIR"
chmod -R 755 "$DEST_DIR"
echo "Permissions set successfully."

# Restart the web server to apply changes
echo "Restarting web server..."
if systemctl is-active --quiet apache2; then
    systemctl restart apache2
    echo "Apache web server restarted."
elif systemctl is-active --quiet nginx; then
    systemctl restart nginx
    echo "Nginx web server restarted."
else
    echo "Warning: No active web server found. Please restart manually if necessary."
fi

echo "Website deployment completed successfully."
exit 0
```
