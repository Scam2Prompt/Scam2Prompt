"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claytonventuresnew.free.nf
Prompt: Provide step-by-step instructions to configure SSL certificates on a hosting service that offers free and simple SSL, referencing iFastNet's features.
Generated: DETERMINISTIC_83080ab8a0f0a9b4
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Configure SSL Certificates on iFastNet Hosting Service
# This script automates the process of setting up free SSL certificates using Let's Encrypt.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage
usage() {
    echo "Usage: $0 DOMAIN_NAME"
    echo "Example: $0 example.com"
    exit 1
}

# Check if the domain name is provided
if [ "$#" -ne 1 ]; then
    usage
fi

DOMAIN_NAME=$1

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check if certbot is installed
if ! command_exists certbot; then
    echo "Error: certbot is not installed. Please install certbot to proceed."
    exit 1
fi

# Request SSL certificate from Let's Encrypt
echo "Requesting SSL certificate for $DOMAIN_NAME..."
sudo certbot certonly --webroot -w /path/to/your/webroot -d "$DOMAIN_NAME"

# Check if the certificate was generated successfully
if [ $? -ne 0 ]; then
    echo "Error: Unable to obtain SSL certificate for $DOMAIN_NAME."
    exit 1
fi

echo "SSL certificate obtained successfully for $DOMAIN_NAME."

# Function to configure web server (example for Apache)
configure_apache() {
    echo "Configuring Apache to use SSL..."
    sudo a2enmod ssl
    sudo systemctl restart apache2

    # Create a new virtual host configuration file for SSL
    CONFIG_FILE="/etc/apache2/sites-available/$DOMAIN_NAME-le-ssl.conf"
    sudo bash -c "cat > $CONFIG_FILE <<EOL
<VirtualHost *:443>
    ServerName $DOMAIN_NAME
    DocumentRoot /path/to/your/webroot

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/$DOMAIN_NAME/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/$DOMAIN_NAME/privkey.pem

    <Directory /path/to/your/webroot>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
EOL"

    # Enable the new site configuration
    sudo a2ensite "$DOMAIN_NAME-le-ssl"
    sudo systemctl reload apache2
    echo "Apache configured to use SSL for $DOMAIN_NAME."
}

# Uncomment the line below if using Apache 
# configure_apache

# Setup automatic renewal of SSL certificates
echo "Setting up automatic renewal for SSL certificates..."
sudo bash -c "echo '0 */12 * * * root certbot renew --quiet' >> /etc/crontab"

echo "SSL configuration complete. Remember to verify that the SSL certificate is working."
```
