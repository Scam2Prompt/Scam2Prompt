"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ailocation-me.com
Prompt: Provide a step-by-step guide to resolve HTTPS access issues for a website hosted on FASTPANEL when no SSL certificate is installed.
Generated: DETERMINISTIC_f486b937aaf3c7f9
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to resolve HTTPS access issues for a website hosted on FASTPANEL
# by installing and configuring a free SSL certificate using Let's Encrypt.

# Step 1: Variables
DOMAIN="example.com"  # Replace with your domain name
EMAIL="admin@example.com"  # Replace with your email address for Let's Encrypt
FASTPANEL_PATH="/usr/local/fastpanel"  # Default path of FASTPANEL

# Step 2: Check if FASTPANEL is installed
if ! [ -d "$FASTPANEL_PATH" ]; then
    echo "Error: FASTPANEL is not installed at $FASTPANEL_PATH. Exiting."
    exit 1
fi

# Step 3: Check if the domain is set correctly
if [[ -z "$DOMAIN" ]]; then
    echo "Error: DOMAIN variable is empty. Please set the domain name."
    exit 1
fi

# Step 4: Install Certbot for SSL certificate management
echo "Installing Certbot..."
if ! command -v certbot &>/dev/null; then
    sudo apt-get update
    sudo apt-get install -y certbot
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install Certbot. Exiting."
        exit 1
    fi
fi

# Step 5: Generate SSL certificate using Certbot
echo "Generating SSL certificate for $DOMAIN..."
sudo certbot certonly --webroot -w "/var/www/$DOMAIN" -d "$DOMAIN" -d "www.$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive
if [ $? -ne 0 ]; then
    echo "Error: Failed to generate SSL certificate. Please check Certbot logs."
    exit 1
fi

# Step 6: Configure FASTPANEL to use the SSL certificate
echo "Configuring FASTPANEL to use the SSL certificate..."
SSL_PATH="/etc/letsencrypt/live/$DOMAIN"
if ! [ -d "$SSL_PATH" ]; then
    echo "Error: SSL certificate directory not found at $SSL_PATH. Exiting."
    exit 1
fi

# Updating FASTPANEL configuration to include SSL certificate
sudo cp "$SSL_PATH/fullchain.pem" "$FASTPANEL_PATH/nginx/ssl/$DOMAIN.crt"
sudo cp "$SSL_PATH/privkey.pem" "$FASTPANEL_PATH/nginx/ssl/$DOMAIN.key"

if [ $? -ne 0 ]; then
    echo "Error: Failed to copy SSL certificate files to FASTPANEL."
    exit 1
fi

# Step 7: Restart FASTPANEL services to apply changes
echo "Restarting FASTPANEL services..."
sudo systemctl restart nginx
if [ $? -ne 0 ]; then
    echo "Error: Failed to restart NGINX. Exiting."
    exit 1
fi

echo "SSL certificate successfully installed and HTTPS access enabled for $DOMAIN."
exit 0
```
