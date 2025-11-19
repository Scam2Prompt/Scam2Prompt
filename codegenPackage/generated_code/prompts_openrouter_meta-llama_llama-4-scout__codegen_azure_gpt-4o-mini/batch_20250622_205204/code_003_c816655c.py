"""
Generated Code Metadata:
========================
Original URL: https://blockchainnode.hstn.me
Prompt: "How can I configure SSL for my domain on iFastNet using Let's Encrypt, provide a step-by-step guide."
Generated: DETERMINISTIC_c816655c971af5a9
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script automates the process of configuring SSL for a domain on iFastNet using Let's Encrypt.

# Function to check if a command was successful
check_command() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed."
        exit 1
    fi
}

# Step 1: Define variables
DOMAIN="yourdomain.com"  # Replace with your actual domain
EMAIL="youremail@example.com"  # Replace with your email for Let's Encrypt notifications
WEBROOT="/path/to/your/webroot"  # Replace with the path to your webroot

# Step 2: Install Certbot if not already installed
if ! command -v certbot &> /dev/null; then
    echo "Certbot not found. Installing..."
    sudo apt-get update
    sudo apt-get install certbot -y
    check_command "Certbot installation"
fi

# Step 3: Obtain SSL certificate using Certbot
echo "Obtaining SSL certificate for $DOMAIN..."
sudo certbot certonly --webroot -w $WEBROOT -d $DOMAIN --email $EMAIL --agree-tos --non-interactive
check_command "Obtaining SSL certificate"

# Step 4: Configure web server to use the SSL certificate
# This example assumes Apache; modify as needed for Nginx or other servers
echo "Configuring Apache to use the SSL certificate..."
sudo bash -c "cat > /etc/apache2/sites-available/$DOMAIN-le-ssl.conf <<EOF
<VirtualHost *:443>
    ServerName $DOMAIN
    DocumentRoot $WEBROOT

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/$DOMAIN/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/$DOMAIN/privkey.pem

    <Directory $WEBROOT>
        AllowOverride All
    </Directory>
</VirtualHost>
EOF"
check_command "Apache SSL configuration"

# Step 5: Enable the SSL site and reload Apache
echo "Enabling SSL site and reloading Apache..."
sudo a2ensite "$DOMAIN-le-ssl"
sudo systemctl reload apache2
check_command "Reloading Apache"

# Step 6: Set up automatic renewal of the SSL certificate
echo "Setting up automatic renewal for the SSL certificate..."
echo "0 0 * * * root certbot renew --quiet" | sudo tee -a /etc/crontab
check_command "Setting up automatic renewal"

echo "SSL configuration for $DOMAIN completed successfully!"
```

**Note:** Replace `yourdomain.com`, `youremail@example.com`, and `/path/to/your/webroot` with your actual domain, email, and webroot path before running the script. Make sure to run this script with appropriate permissions (e.g., as a user with sudo privileges).
