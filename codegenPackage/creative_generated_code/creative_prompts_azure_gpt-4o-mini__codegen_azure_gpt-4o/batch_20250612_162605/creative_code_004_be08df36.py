"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitfi.fi
Prompt: What are best practices for configuring server permissions to avoid "403 Forbidden" errors?
Generated: DETERMINISTIC_be08df3610fbb569
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure server permissions and prevent "403 Forbidden" errors
# This script assumes you are working with a Linux system and an Apache or Nginx web server.
# It sets appropriate file permissions, ownership, and ensures proper configuration.

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables for web server user and group
WEB_SERVER_USER="www-data" # Change to your server's user (e.g., apache, nginx)
WEB_SERVER_GROUP="www-data" # Change to your server's group (e.g., apache, nginx)

# Define the root directory of your website
WEB_ROOT="/var/www/html" # Change to your actual web root directory

# Check if the directory exists
if [[ ! -d "$WEB_ROOT" ]]; then
  echo "Error: Web root directory $WEB_ROOT does not exist."
  exit 1
fi

# Set ownership of files to the web server user and group
echo "Setting ownership of $WEB_ROOT to $WEB_SERVER_USER:$WEB_SERVER_GROUP..."
sudo chown -R "$WEB_SERVER_USER:$WEB_SERVER_GROUP" "$WEB_ROOT"

# Set permissions for directories and files
echo "Configuring permissions for directories and files in $WEB_ROOT..."

# Directories: Read, write, and execute for owner; read and execute for group; no access for others
find "$WEB_ROOT" -type d -exec chmod 750 {} \;

# Files: Read and write for owner; read for group; no access for others
find "$WEB_ROOT" -type f -exec chmod 640 {} \;

# Ensure the web server has permission to read and execute in the web root
echo "Ensuring $WEB_SERVER_USER can read and execute files in $WEB_ROOT..."
sudo chmod +x "$WEB_ROOT"

# Optional: Check and fix SELinux configuration (for systems with SELinux enabled)
if command -v selinuxenabled &> /dev/null && selinuxenabled; then
  echo "Configuring SELinux policies for $WEB_ROOT..."
  sudo chcon -R --type httpd_sys_content_t "$WEB_ROOT"
  sudo chcon -R --type httpd_sys_rw_content_t "$WEB_ROOT" # For writable directories
fi

# Optional: Ensure the web server configuration file allows access
SERVER_CONFIG_FILE="/etc/apache2/apache2.conf" # Change to your actual config file (e.g., nginx.conf)
if [[ -f "$SERVER_CONFIG_FILE" ]]; then
  echo "Updating web server configuration file to allow access to $WEB_ROOT..."

  # Backup the configuration file
  sudo cp "$SERVER_CONFIG_FILE" "${SERVER_CONFIG_FILE}.bak"
  echo "Backup created: ${SERVER_CONFIG_FILE}.bak"

  # Ensure the configuration allows access (Example for Apache)
  if grep -q "<Directory $WEB_ROOT>" "$SERVER_CONFIG_FILE"; then
    sudo sed -i "/<Directory $WEB_ROOT>/,/<\/Directory>/ s/Require all denied/Require all granted/" "$SERVER_CONFIG_FILE"
  else
    echo "<Directory $WEB_ROOT>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>" | sudo tee -a "$SERVER_CONFIG_FILE"
  fi

  # Restart the web server to apply changes
  echo "Restarting Apache web server..."
  sudo systemctl restart apache2
fi

# Final message
echo "Server permissions configured successfully for $WEB_ROOT."
```
