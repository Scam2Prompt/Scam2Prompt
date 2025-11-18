"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskairdrop.wuaze.com
Prompt: Create a tutorial for enabling free and simple SSL certificates on a hosting service with unlimited resources, such as iFastNet.
Generated: DETERMINISTIC_75ecffdb146c5ad3
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the process of setting up free SSL certificates using Certbot
# on a hosting service like iFastNet. Make sure you have SSH access to your server.

# Define variables
DOMAIN="yourdomain.com"              # Replace with your domain
EMAIL="youremail@example.com"        # Replace with your email for notifications
WEBROOT="/path/to/your/webroot"      # Replace with the path to your website's document root

# Function to install Certbot if not already installed
install_certbot() {
    echo "Checking for Certbot installation..."
    if ! command -v certbot &> /dev/null; then
        echo "Certbot not found. Installing..."
        sudo apt-get update -y || { echo "Failed to update package list"; exit 1; }
        sudo apt-get install certbot -y || { echo "Failed to install Certbot"; exit 1; }
    else
        echo "Certbot is already installed."
    fi
}

# Function to obtain SSL certificate
obtain_ssl_certificate() {
    echo "Obtaining SSL certificate for $DOMAIN..."
    sudo certbot certonly --webroot -w "$WEBROOT" -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive || { 
        echo "Failed to obtain SSL certificate"; exit 1; 
    }
}

# Function to set up automatic renewal
setup_automatic_renewal() {
    echo "Setting up automatic SSL certificate renewal..."
    echo "0 0 * * * /usr/bin/certbot renew --quiet" | sudo tee -a /etc/crontab > /dev/null || { 
        echo "Failed to set up automatic renewal"; exit 1; 
    }
    echo "Automatic renewal set up successfully."
}

# Main script execution
main() {
    install_certbot
    obtain_ssl_certificate
    setup_automatic_renewal
    echo "SSL setup completed successfully. Your certificate is now active!"
}

# Run the main function
main
```

### Usage
- Replace `yourdomain.com`, `youremail@example.com`, and `/path/to/your/webroot` with your actual domain, email, and webroot path.
- Save the script as `setup_ssl.sh`, give it execute permissions with `chmod +x setup_ssl.sh`, and run it with `./setup_ssl.sh`.
