"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ip-net.org
Prompt: What steps should I take to configure server permissions to avoid 403 Forbidden errors?
Generated: DETERMINISTIC_9d090deea606db59
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures server permissions to avoid 403 Forbidden errors
# for an Apache web server. Adjust the paths and user/group settings as needed.

# Variables
WEB_ROOT="/var/www/html"  # Path to the web root directory
APACHE_USER="www-data"    # Apache user, adjust based on your server setup
APACHE_GROUP="www-data"   # Apache group, adjust based on your server setup

# Function to set directory permissions
set_directory_permissions() {
    echo "Setting directory permissions for $WEB_ROOT..."

    # Grant read and execute permissions to the user and group
    # and no permissions to others for all directories
    find "$WEB_ROOT" -type d -exec chmod 750 {} \;

    # Grant read and write permissions to the user
    # and read permissions to the group for all files
    find "$WEB_ROOT" -type f -exec chmod 640 {} \;

    # Change ownership of the web root to the Apache user and group
    chown -R "$APACHE_USER":"$APACHE_GROUP" "$WEB_ROOT"

    echo "Directory permissions set successfully."
}

# Function to check if the script is run with root privileges
check_root_privileges() {
    if [[ "$EUID" -ne 0 ]]; then
        echo "Error: Please run this script as root or with sudo."
        exit 1
    fi
}

# Function to restart Apache service
restart_apache() {
    echo "Restarting Apache service..."
    systemctl restart apache2

    if [[ $? -ne 0 ]]; then
        echo "Error: Failed to restart Apache service."
        exit 1
    fi

    echo "Apache service restarted successfully."
}

# Main script execution
check_root_privileges
set_directory_permissions
restart_apache

echo "Server permissions configured successfully to avoid 403 Forbidden errors."
```
