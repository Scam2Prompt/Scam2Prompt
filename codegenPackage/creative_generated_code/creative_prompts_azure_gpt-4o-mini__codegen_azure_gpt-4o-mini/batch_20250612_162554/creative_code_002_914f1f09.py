"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.biz
Prompt: How can I configure my server to support both IPv4 and IPv6 for my website?
Generated: DETERMINISTIC_914f1f097c1e0de9
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures a web server to support both IPv4 and IPv6.
# It assumes that you have root privileges.

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Update package index
echo "Updating package index..."
apt-get update -y

# Install necessary packages (nginx as an example)
echo "Installing Nginx web server..."
apt-get install -y nginx

# Enable both IPv4 and IPv6 in the Nginx configuration
NGINX_CONFIG="/etc/nginx/sites-available/default"

if [ -f "$NGINX_CONFIG" ]; then
    echo "Configuring Nginx for IPv4 and IPv6..."

    # Back up existing Nginx configuration
    cp "$NGINX_CONFIG" "$NGINX_CONFIG.bak"

    # Modify the server block to listen on both IPv4 and IPv6
    sed -i 's/listen 80 default_server;/listen 80 default_server;\n    listen [::]:80 default_server;/' "$NGINX_CONFIG"

    # Check Nginx configuration for syntax errors
    nginx -t
    if [ $? -ne 0 ]; then
        echo "Nginx configuration test failed. Restoring backup..."
        mv "$NGINX_CONFIG.bak" "$NGINX_CONFIG"
        exit 1
    fi

    # Restart Nginx to apply changes
    echo "Restarting Nginx..."
    systemctl restart nginx

    echo "Nginx configured to support both IPv4 and IPv6."
else
    echo "Nginx configuration file not found."
    exit 1
fi

# Enable IPv6 in the system settings
if [ "$(sysctl net.ipv6.conf.all.disable_ipv6)" -eq 1 ]; then
    echo "Enabling IPv6 on the system..."
    sysctl -w net.ipv6.conf.all.disable_ipv6=0
    sysctl -w net.ipv6.conf.default.disable_ipv6=0
    echo "IPv6 has been enabled."
else
    echo "IPv6 is already enabled on the system."
fi

# Complete
echo "Server configured to support both IPv4 and IPv6 successfully."
```
To use this script:
1. Save it to a file, for example, `configure_server.sh`.
2. Make the script executable: `chmod +x configure_server.sh`.
3. Run the script with root privileges: `sudo ./configure_server.sh`.
