"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadsters.info
Prompt: What are best practices for configuring server permissions to avoid "403 Forbidden" errors?
Generated: DETERMINISTIC_be08df3610fbb569
Batch ID: 20250612_160413
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
# It sets appropriate file permissions, adjusts ownership, and configures SELinux if applicable.

# Define variables
WEB_ROOT="/var/www/html"  # Path to the web server's document root
WEB_USER="www-data"       # Web server user (change to `apache` for CentOS/RHEL)
GROUP="www-data"          # Group associated with the web server user

# Check if the script is executed with root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Error: Please run this script as root." >&2
  exit 1
fi

# Step 1: Set ownership of the web root directory
echo "Setting ownership of $WEB_ROOT..."
chown -R $WEB_USER:$GROUP $WEB_ROOT
if [ $? -ne 0 ]; then
  echo "Error: Failed to set ownership of $WEB_ROOT." >&2
  exit 1
fi

# Step 2: Assign proper file and directory permissions
echo "Setting file and directory permissions..."

# Directories: Read, write, and execute for the owner; execute for others
find $WEB_ROOT -type d -exec chmod 755 {} \;

# Files: Read and write for the owner; read-only for others
find $WEB_ROOT -type f -exec chmod 644 {} \;

if [ $? -ne 0 ]; then
  echo "Error: Failed to set permissions for files and directories in $WEB_ROOT." >&2
  exit 1
fi

# Step 3: Check and configure SELinux (if enabled)
if command -v getenforce &> /dev/null && [ "$(getenforce)" != "Disabled" ]; then
  echo "Configuring SELinux permissions..."
  
  # Allow the web server to access files in the web root directory
  semanage fcontext -a -t httpd_sys_content_t "${WEB_ROOT}(/.*)?"
  restorecon -Rv $WEB_ROOT
  
  if [ $? -ne 0 ]; then
    echo "Error: Failed to configure SELinux permissions." >&2
    exit 1
  fi
fi

# Step 4: Restart the web server to apply changes
echo "Restarting web server..."
if command -v systemctl &> /dev/null; then
  systemctl restart apache2 || systemctl restart nginx
else
  service apache2 restart || service nginx restart
fi

if [ $? -ne 0 ]; then
  echo "Error: Failed to restart the web server." >&2
  exit 1
fi

# Final message
echo "Server permissions configured successfully. Check your website for proper functionality."
exit 0
```
