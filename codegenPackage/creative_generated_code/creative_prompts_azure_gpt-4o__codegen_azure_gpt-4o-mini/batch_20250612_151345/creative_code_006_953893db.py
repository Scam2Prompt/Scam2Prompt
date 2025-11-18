"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth.fanclub.rocks
Prompt: Write a script to automate SSL certificate installation for a hosting service that offers free and simple SSL, as described on iFastNet.
Generated: DETERMINISTIC_953893dbf20c4839
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate SSL certificate installation for iFastNet hosting service

# Define variables
DOMAIN="yourdomain.com"          # Replace with your domain name
EMAIL="youremail@example.com"    # Replace with your email for certificate notifications
CERT_DIR="/etc/letsencrypt/live/$DOMAIN"  # Directory for SSL certificates

# Function to install Certbot
install_certbot() {
    echo "Installing Certbot..."
    sudo apt-get update
    sudo apt-get install -y certbot python3-certbot-nginx  # Or use apache if using Apache
}

# Function to obtain SSL certificate
obtain_certificate() {
    echo "Obtaining SSL certificate for $DOMAIN..."
    sudo certbot --nginx --non-interactive --agree-tos --email "$EMAIL" -d "$DOMAIN"
}

# Function to configure Nginx for SSL
configure_nginx() {
    echo "Configuring Nginx for SSL..."
    
    NGINX_CONF="/etc/nginx/sites-available/$DOMAIN"
    
    # Check if Nginx configuration exists
    if [ ! -f "$NGINX_CONF" ]; then
        echo "Nginx configuration for $DOMAIN not found!"
        exit 1
    fi

    # Update the Nginx configuration to listen on 443
    sudo sed -i 's/listen 80/listen 443 ssl/' "$NGINX_CONF"
    sudo sed -i "/server_name/a ssl_certificate $CERT_DIR/fullchain.pem;" "$NGINX_CONF"
    sudo sed -i "/server_name/a ssl_certificate_key $CERT_DIR/privkey.pem;" "$NGINX_CONF"
    
    echo "Nginx configuration updated. Testing configuration..."
    sudo nginx -t

    # Reload Nginx to apply changes
    echo "Reloading Nginx..."
    sudo systemctl reload nginx
}

# Function to set up automatic renewal
setup_renewal() {
    echo "Setting up automatic renewal for SSL certificates..."
    # Certbot sets up a cron job automatically, but we can add our own if desired
    (crontab -l ; echo "0 0 * * * certbot renew --quiet") | crontab -
}

# Main script execution
main() {
    # Check if the user is root
    if [[ $EUID -ne 0 ]]; then
        echo "This script must be run as root. Please run with sudo."
        exit 1
    fi

    # Install Certbot if not already installed
    if ! command -v certbot &> /dev/null; then
        install_certbot
    fi

    # Obtain SSL certificate
    obtain_certificate

    # Configure Nginx for SSL
    configure_nginx

    # Setup automatic renewal
    setup_renewal

    echo "SSL certificate installation and configuration completed successfully!"
}

# Execute main function
main
```
