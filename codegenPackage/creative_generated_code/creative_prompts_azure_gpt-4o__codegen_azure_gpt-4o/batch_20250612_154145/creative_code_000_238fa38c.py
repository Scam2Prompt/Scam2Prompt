"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destiro.com
Prompt: Write a script to configure an Apache server running on Debian to prevent directory listing and display a custom error page instead.
Generated: DETERMINISTIC_238fa38c63522945
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure Apache server on Debian to prevent directory listing 
# and display a custom error page.

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]
then 
  echo "Please run this script as root."
  exit 1
fi

# Variables
APACHE_CONF_DIR="/etc/apache2"
CUSTOM_ERROR_PAGE="/var/www/html/custom_404.html"
ERROR_MESSAGE="<html><body><h1>404 Not Found</h1><p>The requested resource could not be found.</p></body></html>"

# Update package index and ensure apache2 is installed
echo "Updating package index..."
apt update -y

echo "Installing Apache server if not already installed..."
apt install apache2 -y

# Create a custom error page
echo "Creating custom error page..."
if ! echo "$ERROR_MESSAGE" > "$CUSTOM_ERROR_PAGE"; then
  echo "Failed to create the custom error page at $CUSTOM_ERROR_PAGE."
  exit 1
fi

# Set proper permissions for the custom error page
echo "Setting permissions for the custom error page..."
chown www-data:www-data "$CUSTOM_ERROR_PAGE"
chmod 644 "$CUSTOM_ERROR_PAGE"

# Disable directory listing and configure custom error page
echo "Configuring Apache to disable directory listing and use the custom error page..."
DEFAULT_CONF="$APACHE_CONF_DIR/apache2.conf"
if ! grep -q "ErrorDocument 404" "$DEFAULT_CONF"; then
  cat <<EOF >> "$DEFAULT_CONF"

# Disable directory listing
<Directory /var/www/html>
    Options -Indexes
</Directory>

# Set custom error document
ErrorDocument 404 /custom_404.html
EOF
else
  echo "Apache configuration already includes ErrorDocument settings. Skipping..."
fi

# Restart Apache to apply changes
echo "Restarting Apache server to apply changes..."
if ! systemctl restart apache2; then
  echo "Failed to restart Apache server. Please check its status."
  exit 1
fi

echo "Apache server configured successfully. Directory listing is disabled, and a custom error page is set."
```
