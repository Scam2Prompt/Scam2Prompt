"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: How do I configure my server to support both IPv4 and IPv6 in FASTPANEL?
Generated: DETERMINISTIC_b19650bab803acb3
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure server for both IPv4 and IPv6 support in FASTPANEL

# Ensure the script is run with root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Update package repository
echo "Updating package repository..."
apt-get update || { echo "Failed to update package repository"; exit 1; }

# Install necessary packages for IPv6 support if not already installed
echo "Installing necessary packages..."
apt-get install -y net-tools || { echo "Failed to install net-tools"; exit 1; }
apt-get install -y iputils-ping || { echo "Failed to install iputils-ping"; exit 1; }

# Check if IPv6 is enabled in the kernel
if ! sysctl net.ipv6.conf.all.disable_ipv6 | grep -q "0"; then
    echo "Enabling IPv6 support..."
    echo "net.ipv6.conf.all.disable_ipv6 = 0" >> /etc/sysctl.conf
    echo "net.ipv6.conf.default.disable_ipv6 = 0" >> /etc/sysctl.conf
    sysctl -p || { echo "Failed to apply sysctl changes"; exit 1; }
else
    echo "IPv6 is already enabled."
fi

# Configure FASTPANEL to listen on both IPv4 and IPv6
# Modify the configuration file as necessary
FASTPANEL_CONF="/etc/nginx/sites-available/your_fastpanel_config.conf"

if [ -f "$FASTPANEL_CONF" ]; then
    echo "Configuring FASTPANEL to support both IPv4 and IPv6..."
    sed -i 's/listen 80;/listen 80; listen [::]:80;/' "$FASTPANEL_CONF" || { echo "Failed to modify FASTPANEL config"; exit 1; }
    sed -i 's/listen 443 ssl;/listen 443 ssl; listen [::]:443 ssl;/' "$FASTPANEL_CONF" || { echo "Failed to modify FASTPANEL config"; exit 1; }
else
    echo "FASTPANEL configuration file not found: $FASTPANEL_CONF"
    exit 1
fi

# Restart the web server to apply changes
echo "Restarting FASTPANEL service..."
systemctl restart nginx || { echo "Failed to restart FASTPANEL service"; exit 1; }

echo "Server successfully configured to support both IPv4 and IPv6 in FASTPANEL."
exit 0
```
