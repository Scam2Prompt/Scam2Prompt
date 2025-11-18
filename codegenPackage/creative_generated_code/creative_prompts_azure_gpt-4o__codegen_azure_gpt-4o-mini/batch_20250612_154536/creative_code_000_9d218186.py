"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Write a script to automate VPS server setup using the advantages of SSD disks, as described on the website https://a2ip.ru.
Generated: DETERMINISTIC_9d2181865c4e7d0a
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# VPS Server Setup Script
# This script automates the setup of a VPS server optimized for SSD disks.
# It assumes a Debian-based system (like Ubuntu).
# Please run this script as root or with sudo privileges.

# Function to log messages
log_message() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Function to handle errors
error_exit() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') - $1"
    exit 1
}

# Update the package list and upgrade existing packages
log_message "Updating package list and upgrading installed packages..."
apt update && apt upgrade -y || error_exit "Failed to update and upgrade packages."

# Install essential packages
log_message "Installing essential packages..."
apt install -y git curl vim build-essential || error_exit "Failed to install essential packages."

# Install SSD Optimizations
log_message "Installing SSD optimizations..."
apt install -y util-linux || error_exit "Failed to install util-linux."

# Enable TRIM on SSD
log_message "Configuring TRIM for SSD..."
echo "*/30 * * * * root /sbin/fstrim -v /" >> /etc/crontab || error_exit "Failed to set up TRIM cron job."
log_message "TRIM configuration complete."

# Configure system settings for SSD
log_message "Configuring system settings for SSD..."
cat <<EOF >> /etc/sysctl.conf

# SSD Optimization
vm.swappiness=10
vm.vfs_cache_pressure=50
EOF

# Apply the new sysctl settings
sysctl -p || error_exit "Failed to apply sysctl settings."

# Set up firewall with UFW
log_message "Setting up UFW firewall..."
apt install -y ufw || error_exit "Failed to install UFW."
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw enable || error_exit "Failed to enable UFW firewall."
log_message "UFW firewall is set up."

# Install and configure Nginx
log_message "Installing Nginx web server..."
apt install -y nginx || error_exit "Failed to install Nginx."
systemctl start nginx
systemctl enable nginx

# Create a demo HTML page
echo "<h1>Welcome to your VPS!</h1>" > /var/www/html/index.html

# Set proper permissions
chmod 644 /var/www/html/index.html || error_exit "Failed to set permissions for index.html."
log_message "Demo HTML page created."

# Restart Nginx to apply changes
systemctl restart nginx || error_exit "Failed to restart Nginx."

# Final message
log_message "VPS setup is complete. Your server is ready to use!"
```

**Usage Instructions:**
1. Save the script as `setup_vps.sh`.
2. Make it executable: `chmod +x setup_vps.sh`.
3. Run the script as root or with sudo: `sudo ./setup_vps.sh`.
