"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://datmaui.liveblog365.com
Prompt: Write a code snippet to configure a free SSL certificate for a domain hosted on iFastNet.
Generated: DETERMINISTIC_91ad73f87f9865aa
Batch ID: 20250612_161044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures a free SSL certificate for a domain hosted on iFastNet
# It uses Certbot to obtain a Let's Encrypt SSL certificate

# Variables
DOMAIN="yourdomain.com"               # Replace with your domain name
EMAIL="youremail@example.com"          # Replace with your email for certificate registration
WEBROOT="/path/to/your/webroot"        # Replace with the path to your webroot directory

# Function to install Certbot if not already installed
install_certbot() {
    echo "Checking for Certbot installation..."
    if ! command -v certbot &> /dev/null; then
        echo "Certbot not found. Installing..."
        sudo apt-get update
        sudo apt-get install -y certbot
    else
        echo "Certbot is already installed."
    fi
}

# Function to obtain the SSL certificate
obtain_ssl_certificate() {
    echo "Obtaining SSL certificate for $DOMAIN..."
    sudo certbot certonly --webroot -w "$WEBROOT" -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive
}

# Function to check the certificate installation
check_certificate() {
    if [ -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]; then
        echo "SSL certificate successfully obtained for $DOMAIN."
    else
        echo "Failed to obtain SSL certificate for $DOMAIN."
    fi
}

# Function to renew the SSL certificate
renew_ssl_certificate() {
    echo "Setting up automatic renewal for the SSL certificate..."
    echo "0 0 * * * root certbot renew --quiet" | sudo tee -a /etc/crontab
}

# Main function to execute the script
main() {
    install_certbot
    obtain_ssl_certificate
    check_certificate
    renew_ssl_certificate
    
    echo "SSL certificate configuration completed."
}

# Run the main function
main
``` 

**Note:** Before executing this script, make sure to replace the placeholder values for `DOMAIN`, `EMAIL`, and `WEBROOT` with your actual domain name, email address, and the path to your webroot directory. Additionally, ensure you have the necessary permissions and that your server meets the requirements for running Certbot.
