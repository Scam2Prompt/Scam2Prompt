"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Generate a Bash script to set up a "cgi-bin" directory on an Apache server and configure permissions for CGI execution.
Generated: DETERMINISTIC_73e127d7d4cd6401
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script sets up a "cgi-bin" directory for an Apache server and configures permissions for CGI execution.
# Author: [Your Name]
# Date: [Date]

# Exit immediately if a command exits with a non-zero status
set -e

# Function to print error messages and exit
error_exit() {
    echo "Error: $1" >&2
    exit 1
}

# Define the Apache CGI directory path
CGI_BIN_DIR="/var/www/cgi-bin"

# Verify that the script is run as root
if [[ $EUID -ne 0 ]]; then
    error_exit "This script must be run as root. Please use sudo or log in as root."
fi

# Step 1: Create the "cgi-bin" directory if it doesn't exist
if [[ ! -d "$CGI_BIN_DIR" ]]; then
    echo "Creating CGI directory at $CGI_BIN_DIR..."
    mkdir -p "$CGI_BIN_DIR" || error_exit "Failed to create directory $CGI_BIN_DIR."
else
    echo "Directory $CGI_BIN_DIR already exists. Skipping creation."
fi

# Step 2: Set the appropriate permissions
echo "Setting permissions for $CGI_BIN_DIR..."
chmod 755 "$CGI_BIN_DIR" || error_exit "Failed to set permissions for $CGI_BIN_DIR."
chown www-data:www-data "$CGI_BIN_DIR" || error_exit "Failed to set ownership for $CGI_BIN_DIR."

# Step 3: Enable CGI module in Apache if not already enabled
if ! a2enmod cgi >/dev/null 2>&1; then
    echo "Enabling CGI module in Apache..."
    a2enmod cgi || error_exit "Failed to enable CGI module in Apache."
fi

# Step 4: Configure Apache to allow execution of CGI scripts in "cgi-bin"
APACHE_CONF_FILE="/etc/apache2/conf-available/serve-cgi-bin.conf"
if [[ -e "$APACHE_CONF_FILE" ]]; then
    echo "Configuring Apache for CGI execution..."
    # Enable the default CGI config file if not already enabled
    a2enconf serve-cgi-bin || error_exit "Failed to enable CGI configuration in Apache."
else
    error_exit "Apache configuration file $APACHE_CONF_FILE not found."
fi

# Step 5: Restart Apache to apply changes
echo "Restarting Apache server..."
systemctl restart apache2 || error_exit "Failed to restart Apache server."

# Final message
echo "CGI-bin setup completed successfully."
```
