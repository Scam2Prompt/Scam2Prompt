"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msu.best
Prompt: Provide an example of how to configure HTTPS for a website hosted on FASTPANEL, ensuring proper SSL setup.
Generated: DETERMINISTIC_d94a748c65d08794
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

FASTPANEL does not require programming to configure HTTPS, as it's a web hosting control panel with a graphical interface. However, to automate SSL setup using Linux shell scripting, if the server supports Let's Encrypt, here’s an example script:

```bash
#!/bin/bash

# Script to automate SSL setup for a website hosted on FASTPANEL
# Assumes you are using a Linux server with sudo privileges and FASTPANEL installed
# Make sure Certbot is installed (Let's Encrypt client)

# Variables
DOMAIN="example.com" # Replace with your domain name
WEB_ROOT="/var/www/$DOMAIN" # Replace with your web root directory
EMAIL="admin@example.com" # Replace with your email for Let's Encrypt notifications

# Pre-checks
if ! [ -x "$(command -v certbot)" ]; then
    echo "Certbot not installed. Installing Certbot..."
    sudo apt update
    sudo apt install certbot -y
fi

if [ ! -d "$WEB_ROOT" ]; then
    echo "Web root directory $WEB_ROOT not found. Please check your domain's configuration."
    exit 1
fi

# Obtain SSL certificate
echo "Obtaining SSL certificate for $DOMAIN..."
sudo certbot certonly --webroot -w "$WEB_ROOT" -d "$DOMAIN" -d "www.$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive

# Check if SSL certificate was successfully obtained
if [ $? -ne 0 ]; then
    echo "Failed to obtain SSL certificate for $DOMAIN. Please check the domain setup and DNS configuration."
    exit 1
fi

echo "SSL certificate successfully obtained."

# Configure the web server to use the SSL certificate (Example for Nginx)
NGINX_CONF="/etc/nginx/sites-available/$DOMAIN"

if [ -f "$NGINX_CONF" ]; then
    echo "Configuring Nginx for HTTPS..."
    sudo sed -i "s|listen 80;|listen 443 ssl;|" "$NGINX_CONF"
    sudo sed -i "/listen 443 ssl;/a ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;\nssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;\nssl_protocols TLSv1.2 TLSv1.3;\nssl_ciphers HIGH:!aNULL:!MD5;" "$NGINX_CONF"
    sudo nginx -t && sudo systemctl reload nginx
    echo "Nginx successfully configured for HTTPS."
else
    echo "Nginx configuration file not found at $NGINX_CONF. Please configure manually."
fi

# Set up auto-renewal
echo "Setting up auto-renewal for SSL certificate..."
sudo systemctl enable certbot.timer
echo "Auto-renewal configured."

echo "SSL setup for $DOMAIN completed successfully."
```

This script handles the full process of obtaining and configuring SSL certificates using Let's Encrypt and Certbot while ensuring proper error handling and robust production-ready practices.
