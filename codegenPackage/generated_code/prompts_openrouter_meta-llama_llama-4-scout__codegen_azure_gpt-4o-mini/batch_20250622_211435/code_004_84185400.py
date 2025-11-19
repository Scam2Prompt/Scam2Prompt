"""
Generated Code Metadata:
========================
Original URL: https://abset.org
Prompt: What are some best practices for managing and securing a Debian-based server with Apache, considering the version numbers provided on the abset.org webpage?
Generated: DETERMINISTIC_8418540069e5660f
Batch ID: 20250622_211435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to manage and secure a Debian-based server with Apache

# Update package list and upgrade installed packages
echo "Updating package list and upgrading installed packages..."
sudo apt update && sudo apt upgrade -y

# Install Apache if not already installed
if ! command -v apache2 &> /dev/null; then
    echo "Apache not found. Installing Apache..."
    sudo apt install apache2 -y
else
    echo "Apache is already installed."
fi

# Enable UFW (Uncomplicated Firewall) if not already enabled
if ! sudo ufw status | grep -q "Status: active"; then
    echo "Enabling UFW..."
    sudo ufw enable
else
    echo "UFW is already enabled."
fi

# Allow HTTP and HTTPS traffic through the firewall
echo "Allowing HTTP and HTTPS traffic through UFW..."
sudo ufw allow 'Apache Full'

# Secure Apache by disabling directory listing
echo "Securing Apache by disabling directory listing..."
sudo sed -i 's/Options Indexes FollowSymLinks/Options FollowSymLinks/' /etc/apache2/apache2.conf

# Disable unnecessary modules
echo "Disabling unnecessary Apache modules..."
sudo a2dismod autoindex
sudo a2dismod status

# Enable security headers
echo "Enabling security headers..."
cat <<EOL | sudo tee /etc/apache2/conf-available/security-headers.conf
<IfModule mod_headers.c>
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-XSS-Protection "1; mode=block"
    Header always set X-Frame-Options "DENY"
    Header always set Content-Security-Policy "default-src 'self'"
</IfModule>
EOL
sudo a2enconf security-headers

# Restart Apache to apply changes
echo "Restarting Apache to apply changes..."
sudo systemctl restart apache2

# Set up automatic security updates
echo "Setting up automatic security updates..."
sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure --priority=low unattended-upgrades

# Check Apache status
echo "Checking Apache status..."
sudo systemctl status apache2

# Final message
echo "Server management and security setup completed successfully."
```

**Note:** This script should be run with root privileges or using `sudo`. Always test scripts in a safe environment before deploying them to production.
