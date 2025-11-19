"""
Generated Code Metadata:
========================
Original URL: https://airdrop-stepngo.asia
Prompt: Write a step-by-step guide to configure a domain in FASTPANEL, ensuring proper SSL certificate installation and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_6ce3ec5bad1094bb
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Step 1: Install necessary packages
# Update package list and install required packages for domain configuration
echo "Updating package list..."
sudo apt-get update -y

echo "Installing necessary packages..."
sudo apt-get install -y nginx certbot python3-certbot-nginx

# Step 2: Configure Nginx for the domain
# Replace 'your_domain.com' with your actual domain name
DOMAIN="your_domain.com"
NGINX_CONF="/etc/nginx/sites-available/$DOMAIN"

# Create Nginx configuration file
echo "Creating Nginx configuration for $DOMAIN..."
cat <<EOL | sudo tee $NGINX_CONF
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN www.$DOMAIN;

    root /var/www/$DOMAIN/html;
    index index.html index.htm;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOL

# Enable the configuration by creating a symbolic link
echo "Enabling Nginx configuration..."
sudo ln -s $NGINX_CONF /etc/nginx/sites-enabled/

# Step 3: Create the document root directory
echo "Creating document root directory..."
sudo mkdir -p /var/www/$DOMAIN/html

# Step 4: Set permissions for the document root
echo "Setting permissions for document root..."
sudo chown -R $USER:$USER /var/www/$DOMAIN/html
sudo chmod -R 755 /var/www/$DOMAIN

# Step 5: Test Nginx configuration
echo "Testing Nginx configuration..."
if sudo nginx -t; then
    echo "Nginx configuration is valid."
else
    echo "Nginx configuration is invalid. Please check the configuration."
    exit 1
fi

# Step 6: Restart Nginx to apply changes
echo "Restarting Nginx..."
sudo systemctl restart nginx

# Step 7: Obtain SSL certificate using Certbot
echo "Obtaining SSL certificate for $DOMAIN..."
if sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN; then
    echo "SSL certificate obtained successfully."
else
    echo "Failed to obtain SSL certificate. Please check your domain settings."
    exit 1
fi

# Step 8: Set up automatic renewal for the SSL certificate
echo "Setting up automatic renewal for SSL certificate..."
echo "0 0 * * * root certbot renew --quiet" | sudo tee -a /etc/crontab

# Step 9: Verify IPv4 and IPv6 compatibility
echo "Verifying IPv4 and IPv6 compatibility..."
if ip -6 addr show | grep -q "inet6"; then
    echo "IPv6 is enabled on this server."
else
    echo "IPv6 is not enabled on this server. Please check your network settings."
fi

# Step 10: Final message
echo "Domain configuration for $DOMAIN is complete. Please visit your domain to verify."
```
