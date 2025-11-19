"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5000eth.rf.gd
Prompt: How can I set up a free SSL certificate on my iFastNet hosting account? Provide a step-by-step guide.
Generated: DETERMINISTIC_0f76ce2085234b32
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the process of setting up a free SSL certificate on an iFastNet hosting account using Certbot.

# Define variables
DOMAIN="yourdomain.com"  # Replace with your domain name
EMAIL="youremail@example.com"  # Replace with your email address
WEB_ROOT="/path/to/your/webroot"  # Replace with the path to your website's root directory

# Function to install Certbot
install_certbot() {
    echo "Checking for Certbot installation..."
    if ! command -v certbot &> /dev/null; then
        echo "Certbot not found, installing..."
        sudo apt-get update -y
        sudo apt-get install certbot -y
    else
        echo "Certbot is already installed."
    fi
}

# Function to obtain SSL certificate
obtain_ssl_certificate() {
    echo "Obtaining SSL certificate for $DOMAIN..."
    
    # Run Certbot with the webroot plugin
    sudo certbot certonly --webroot -w "$WEB_ROOT" -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive --quiet
    
    # Check if the certificate was obtained successfully
    if [ $? -eq 0 ]; then
        echo "SSL certificate obtained successfully."
    else
        echo "Failed to obtain SSL certificate. Please check the error above."
        exit 1
    fi
}

# Function to set up automatic renewal
setup_automatic_renewal() {
    echo "Setting up automatic renewal of the SSL certificate..."
    
    # Create a cron job to run the renewal command twice a day
    (crontab -l 2>/dev/null; echo "0 0,12 * * * /usr/bin/certbot renew --quiet") | crontab -
    
    # Check if the cron job was added successfully
    if [ $? -eq 0 ]; then
        echo "Automatic renewal set up successfully."
    else
        echo "Failed to set up automatic renewal."
        exit 1
    fi
}

# Main script execution
echo "Starting SSL certificate setup..."
install_certbot
obtain_ssl_certificate
setup_automatic_renewal

echo "SSL setup complete. Your website is now secured with HTTPS!"
```
