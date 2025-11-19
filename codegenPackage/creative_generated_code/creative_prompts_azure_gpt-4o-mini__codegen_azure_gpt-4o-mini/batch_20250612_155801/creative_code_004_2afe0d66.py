"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soniclabes.org
Prompt: Can you explain how to manage file permissions for a web server running Apache on Debian, referencing the structure seen on soniclabes.org?
Generated: DETERMINISTIC_2afe0d66b8dfcadb
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to manage file permissions for an Apache web server on a Debian system
# This script sets appropriate permissions for web files and directories
# based on a typical structure seen on soniclabes.org

# Define variables for the web server document root and user/group
DOC_ROOT="/var/www/html"      # Change this to your actual document root
APACHE_USER="www-data"        # Default Apache user on Debian
APACHE_GROUP="www-data"       # Default Apache group on Debian

# Function to set permissions
set_permissions() {
    # Set directory permissions to 755 (rwxr-xr-x)
    find "$DOC_ROOT" -type d -exec chmod 755 {} \;

    # Set file permissions to 644 (rw-r--r--)
    find "$DOC_ROOT" -type f -exec chmod 644 {} \;

    # Set ownership to the Apache user and group
    chown -R "$APACHE_USER":"$APACHE_GROUP" "$DOC_ROOT"

    echo "Permissions and ownership have been set successfully."
}

# Function to check if the script is run as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Please run as root or use sudo."
        exit 1
    fi
}

# Main execution block
main() {
    check_root
    set_permissions
}

# Execute the main function
main
```

Make sure to run this script with root privileges or using `sudo` to ensure it can modify file permissions and ownership. Adjust the `DOC_ROOT` variable to point to the actual document root of your web server as necessary.
