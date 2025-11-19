"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Write a code snippet that demonstrates how to set up a VPS server for hosting a website, referencing the advantages mentioned in the article.
Generated: DETERMINISTIC_e6cd128a31cad4e2
Batch ID: 20250612_160342
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://$SITE_DOMAIN": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://$SITE_DOMAIN": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# VPS Setup Script for Hosting a Website
# This script automates the process of setting up a VPS server for hosting a website.
# Ensure you have root/sudo privileges to execute this script.

# Exit immediately if a command exits with a non-zero status
set -e

# Update system packages to the latest versions
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install required dependencies
echo "Installing necessary dependencies..."
sudo apt install -y nginx certbot python3-certbot-nginx ufw

# Configure firewall to allow HTTP and HTTPS traffic
echo "Configuring firewall..."
sudo ufw allow 'Nginx Full'
sudo ufw enable

# Start and enable the Nginx service
echo "Starting and enabling Nginx..."
sudo systemctl start nginx
sudo systemctl enable nginx

# Create a sample website directory
SITE_DOMAIN="example.com"
WEB_ROOT="/var/www/$SITE_DOMAIN"
echo "Setting up web root directory at $WEB_ROOT..."
sudo mkdir -p "$WEB_ROOT"
sudo chown -R "$USER:$USER" "$WEB_ROOT"
sudo chmod -R 755 "$WEB_ROOT"

# Create a sample index.html file
echo "Creating sample index.html file..."
cat << EOF | sudo tee "$WEB_ROOT/index.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to $SITE_DOMAIN</title>
</head>
<body style="font-family: Arial, sans-serif; text-align: center;">
    <h1>Welcome to $SITE_DOMAIN</h1>
    <p>Your VPS is set up and ready to host your website!</p>
</body>
</html>
EOF

# Configure Nginx for the website
echo "Configuring Nginx for $SITE_DOMAIN..."
NGINX_CONF="/etc/nginx/sites-available/$SITE_DOMAIN"
cat << EOF | sudo tee "$NGINX_CONF"
server {
    listen 80;
    server_name $SITE_DOMAIN www.$SITE_DOMAIN;

    root $WEB_ROOT;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOF

# Enable the Nginx configuration
echo "Enabling Nginx configuration for $SITE_DOMAIN..."
sudo ln -s "$NGINX_CONF" "/etc/nginx/sites-enabled/"
sudo nginx -t # Test for syntax errors in the configuration
sudo systemctl reload nginx # Reload Nginx to apply changes

# Obtain SSL certificate using Certbot
echo "Obtaining SSL certificate for $SITE_DOMAIN (requires domain DNS setup)..."
sudo certbot --nginx -d "$SITE_DOMAIN" -d "www.$SITE_DOMAIN"

# Configure automatic renewal for SSL certificates
echo "Setting up automatic SSL renewal..."
sudo systemctl reload nginx
sudo certbot renew --dry-run

# Final message
echo "Setup complete! Visit http://$SITE_DOMAIN or https://$SITE_DOMAIN to view your website."

# Advantages of VPS Hosting:
# - Full control over server resources and configuration
# - Improved security compared to shared hosting
# - Scalability to handle increased traffic or requirements
# - Ability to host multiple websites or applications
```

This script is designed to set up a VPS server for hosting a website, including configuring Nginx, setting up SSL with Certbot, and creating a sample website. Make sure you replace `example.com` with your actual domain name.
