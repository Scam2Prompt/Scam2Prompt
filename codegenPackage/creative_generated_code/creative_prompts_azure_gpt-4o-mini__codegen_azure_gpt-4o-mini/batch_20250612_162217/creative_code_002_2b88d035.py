"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-gas.network
Prompt: Describe how to configure a server to support both IPv4 and IPv6 for a domain.
Generated: DETERMINISTIC_2b88d035d7a344c8
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures a server to support both IPv4 and IPv6 for a domain.

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Variables
DOMAIN="example.com"    # Replace with your domain
IPv4_ADDRESS="192.0.2.1" # Replace with your IPv4 address
IPv6_ADDRESS="2001:db8::1" # Replace with your IPv6 address

# Install necessary packages (Nginx as an example)
apt-get update
apt-get install -y nginx

# Create a configuration file for the domain
NGINX_CONF="/etc/nginx/sites-available/$DOMAIN"

# Check if the configuration already exists
if [[ -f "$NGINX_CONF" ]]; then
    echo "Configuration file already exists. Exiting."
    exit 1
fi

# Create the new Nginx configuration for the domain
cat <<EOL > "$NGINX_CONF"
server {
    listen 80;                  # Listen on IPv4
    listen [::]:80;             # Listen on IPv6
    server_name $DOMAIN;        # Domain name

    location / {
        root /var/www/$DOMAIN;  # Document root
        index index.html index.htm; # Default index files
    }
}

# Redirect HTTP to HTTPS (optional)
server {
    listen 443 ssl;             # Listen on IPv4 for HTTPS
    listen [::]:443 ssl;        # Listen on IPv6 for HTTPS
    server_name $DOMAIN;

    ssl_certificate /etc/ssl/certs/$DOMAIN.crt;  # Path to SSL certificate
    ssl_certificate_key /etc/ssl/private/$DOMAIN.key;  # Path to SSL key

    location / {
        root /var/www/$DOMAIN;
        index index.html index.htm;
    }
}

EOL

# Enable the site
ln -s "$NGINX_CONF" /etc/nginx/sites-enabled/

# Test the Nginx configuration for syntax errors
nginx -t
if [[ $? -ne 0 ]]; then
    echo "Nginx configuration test failed. Exiting."
    exit 1
fi

# Restart Nginx to apply changes
systemctl restart nginx

# Print success message
echo "Nginx has been configured to support both IPv4 and IPv6 for the domain $DOMAIN."
```
