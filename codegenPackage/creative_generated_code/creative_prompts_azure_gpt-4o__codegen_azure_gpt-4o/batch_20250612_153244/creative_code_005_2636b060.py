"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxworke.com
Prompt: Write a bash script to remove the default CyberPanel installation page and upload a custom website to the server.
Generated: DETERMINISTIC_2636b060b5bd3393
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# CyberPanel Website Replacement Script
# This script removes the default CyberPanel installation page
# and uploads a custom website to the server.

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
WEBROOT="/home/cyberpanel/public_html"  # Default web root for CyberPanel
CUSTOM_WEBSITE_ARCHIVE="custom_website.zip"  # Path to the custom website archive
TEMP_DIR="/tmp/custom_website"  # Temporary directory for extraction

# Functions
function error_exit {
    echo "Error: $1" >&2
    exit 1
}

# Check if script is run as root
if [[ $EUID -ne 0 ]]; then
    error_exit "This script must be run as root"
fi

# Confirm removal of the default CyberPanel page
read -p "Are you sure you want to replace the default CyberPanel installation page? (yes/no): " CONFIRM
if [[ "$CONFIRM" != "yes" ]]; then
    echo "Operation canceled."
    exit 0
fi

# Verify custom website archive exists
if [[ ! -f "$CUSTOM_WEBSITE_ARCHIVE" ]]; then
    error_exit "Custom website archive ($CUSTOM_WEBSITE_ARCHIVE) does not exist"
fi

# Remove default CyberPanel installation page
echo "Removing default CyberPanel installation page..."
rm -rf "$WEBROOT/*" || error_exit "Failed to remove default installation page"

# Create temporary directory for extraction
echo "Creating temporary directory for the custom website..."
mkdir -p "$TEMP_DIR" || error_exit "Failed to create temporary directory"

# Extract custom website archive to the temporary directory
echo "Extracting custom website archive..."
unzip -q "$CUSTOM_WEBSITE_ARCHIVE" -d "$TEMP_DIR" || error_exit "Failed to extract custom website archive"

# Move extracted files to the web root
echo "Uploading custom website to the server..."
mv "$TEMP_DIR"/* "$WEBROOT" || error_exit "Failed to move custom website files to web root"

# Clean up temporary directory
echo "Cleaning up..."
rm -rf "$TEMP_DIR"

# Set appropriate permissions
echo "Setting permissions for web root..."
chown -R cyberpanel:cyberpanel "$WEBROOT" || error_exit "Failed to set permissions for web root"
chmod -R 755 "$WEBROOT" || error_exit "Failed to set file permissions"

# Restart web server to apply changes
echo "Restarting web server..."
systemctl restart lscpd || error_exit "Failed to restart web server"

# Success message
echo "Custom website has been successfully uploaded and the default page has been removed."
```
