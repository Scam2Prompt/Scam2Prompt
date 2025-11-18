"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Write a script to configure a LiteSpeed Web Server to serve a custom directory listing similar to the one at 8lements.xyz.
Generated: DETERMINISTIC_e3cd5b7879af0060
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure LiteSpeed Web Server for custom directory listing

# Define variables for configuration
LITESPEED_DIR="/usr/local/lsws"  # Path to LiteSpeed installation
VIRTUAL_HOST_CONF="$LITESPEED_DIR/conf/vhosts.conf"  # Path to virtual host configuration
DOC_ROOT="/var/www/html"  # Document root for the website
CUSTOM_LISTING_PATH="$DOC_ROOT/custom_listing"  # Custom directory for listing
SERVICE_NAME="lsws"  # Name of LiteSpeed service

# Function to check if a command was successful
check_command() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed."
        exit 1
    fi
}

# Create custom listing directory if it doesn't exist
if [ ! -d "$CUSTOM_LISTING_PATH" ]; then
    mkdir -p "$CUSTOM_LISTING_PATH"
    check_command "Creating custom listing directory"
    echo "Custom listing directory created at $CUSTOM_LISTING_PATH"
else
    echo "Custom listing directory already exists at $CUSTOM_LISTING_PATH"
fi

# Configure LiteSpeed to serve the custom directory listing
{
    echo "<VirtualHost *:80>"
    echo "    ServerName example.com"  # Replace with your domain
    echo "    DocumentRoot $DOC_ROOT"
    echo "    <Directory $CUSTOM_LISTING_PATH>"
    echo "        Options +Indexes"
    echo "        AllowOverride None"
    echo "        Require all granted"
    echo "    </Directory>"
    echo "    ErrorLog /var/log/lsws/error.log"
    echo "    CustomLog /var/log/lsws/access.log common"
    echo "</VirtualHost>"
} >> "$VIRTUAL_HOST_CONF"
check_command "Appending virtual host configuration"

# Restart LiteSpeed to apply changes
service $SERVICE_NAME restart
check_command "Restarting LiteSpeed service"

echo "LiteSpeed configured to serve custom directory listing at $CUSTOM_LISTING_PATH"
```

Make sure to replace `example.com` with your actual domain before running this script. This script should be executed with root privileges to ensure it can create directories and modify configurations.
