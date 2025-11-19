"""
Generated Code Metadata:
========================
Original URL: https://jobgridl.top
Prompt: Generate a bash script to uninstall aaPanel and clean up associated files from a server.
Generated: DETERMINISTIC_b6982b458ed62695
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Uninstall aaPanel and clean up associated files

# Check if script is run as root
if [ $(id -u) -ne 0 ]; then
  echo "This script must be run as root"
  exit 1
fi

# Stop aaPanel service
echo "Stopping aaPanel service..."
systemctl stop aapanel

# Uninstall aaPanel
echo "Uninstalling aaPanel..."
/etc/init.d/aapanel stop
rm -rf /etc/aapanel
rm -rf /var/www/aapanel
rm -rf /usr/local/aapanel

# Remove aaPanel repository
echo "Removing aaPanel repository..."
rm -rf /etc/yum.repos.d/aapanel.repo
rm -rf /etc/apt/sources.list.d/aapanel.list

# Clean up associated files
echo "Cleaning up associated files..."
rm -rf /var/log/aapanel
rm -rf /var/lib/aapanel

# Remove aaPanel user and group
echo "Removing aaPanel user and group..."
userdel -f aapanel
groupdel aapanel

# Clean up systemd services
echo "Cleaning up systemd services..."
systemctl disable aapanel
rm -rf /etc/systemd/system/aapanel.service

# Update package list
echo "Updating package list..."
if [ -x "$(command -v apt)" ]; then
  apt update
elif [ -x "$(command -v yum)" ]; then
  yum update -y
fi

echo "aaPanel uninstallation and cleanup complete."
```
