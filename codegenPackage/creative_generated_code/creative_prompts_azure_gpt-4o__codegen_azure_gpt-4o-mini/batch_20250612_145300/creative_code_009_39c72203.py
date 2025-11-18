"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: Create a tutorial for setting up secure SSL certificates for a site hosted on aaPanel.
Generated: DETERMINISTIC_39c72203bcdde359
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the process of setting up secure SSL certificates for a site hosted on aaPanel.
# Ensure to run this script with appropriate permissions (e.g., as root or using sudo).

# Variables
DOMAIN="yourdomain.com"  # Replace with your domain
EMAIL="youremail@example.com"  # Replace with your email address for Let's Encrypt notifications
AA_PANEL_PATH="/www/server/panel"  # Path to the aaPanel installation

# Function to install Certbot
install_certbot() {
    echo "Installing Certbot..."
    apt update && apt install -y certbot python3-certbot-nginx || { echo "Failed to install Certbot"; exit 1; }
}

# Function to obtain SSL certificate
obtain_ssl_certificate() {
    echo "Obtaining SSL certificate for $DOMAIN..."
    certbot certonly --nginx -d $DOMAIN --email $EMAIL --agree-tos --non-interactive || { echo "Failed to obtain SSL certificate"; exit 1; }
}

# Function to configure Nginx
configure_nginx() {
    echo "Configuring Nginx for SSL..."
    NGINX_CONF_FILE="/etc/nginx/sites-available/$DOMAIN"
    if [ -f "$NGINX_CONF_FILE" ]; then
        # Backup existing config
        cp "$NGINX_CONF_FILE" "$NGINX_CONF_FILE.bak"
        
        # Update the Nginx configuration
        sed -i "s/listen 80;/listen 80;\n    listen 443 ssl;\n    ssl_certificate \/etc\/letsencrypt\/live\/$DOMAIN\/fullchain.pem;\n    ssl_certificate_key \/etc\/letsencrypt\/live\/$DOMAIN\/privkey.pem;/g" "$NGINX_CONF_FILE" || { echo "Failed to update Nginx configuration"; exit 1; }
        
        # Test Nginx configuration
        nginx -t || { echo "Nginx configuration test failed"; exit 1; }
        
        # Reload Nginx to apply changes
        systemctl reload nginx || { echo "Failed to reload Nginx"; exit 1; }
    else
        echo "Nginx configuration file not found: $NGINX_CONF_FILE"
        exit 1
    fi
}

# Function to set up automatic renewal
setup_renewal() {
    echo "Setting up automatic renewal for SSL certificates..."
    echo "0 0 * * * root certbot renew --post-hook 'systemctl reload nginx'" > /etc/cron.d/certbot || { echo "Failed to set up renewal cron job"; exit 1; }
}

# Main script execution
echo "Starting SSL setup for $DOMAIN..."

# Install Certbot if not already installed
if ! command -v certbot &> /dev/null; then
    install_certbot
else
    echo "Certbot is already installed."
fi

# Obtain SSL certificate
obtain_ssl_certificate

# Configure Nginx
configure_nginx

# Set up automatic renewal
setup_renewal

echo "SSL setup completed successfully for $DOMAIN."
```
