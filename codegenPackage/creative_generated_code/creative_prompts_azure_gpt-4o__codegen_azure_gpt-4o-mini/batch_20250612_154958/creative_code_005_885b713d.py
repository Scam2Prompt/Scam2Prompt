"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseaaward-program.epizy.com
Prompt: Provide a step-by-step tutorial for setting up SSL certificates on a hosting service with free and simple SSL support, referencing iFastNet hosting.
Generated: DETERMINISTIC_885b713d09693be5
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the process of setting up SSL certificates on iFastNet hosting using Let's Encrypt.
# Prerequisites: You must have access to your iFastNet control panel and a registered domain.

# Define variables
DOMAIN="yourdomain.com" # Replace with your domain
EMAIL="youremail@example.com" # Replace with your email for Let's Encrypt notifications
WEBROOT="/path/to/your/webroot" # Replace with the path to your web root directory

# Function to check if Certbot is installed
check_certbot_installed() {
    if ! command -v certbot &> /dev/null; then
        echo "Certbot is not installed. Installing..."
        sudo apt-get update
        sudo apt-get install certbot
    else
        echo "Certbot is already installed."
    fi
}

# Function to obtain SSL certificate
obtain_ssl_certificate() {
    echo "Obtaining SSL certificate for $DOMAIN..."
    sudo certbot certonly --webroot -w "$WEBROOT" -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive
    if [[ $? -ne 0 ]]; then
        echo "Error obtaining SSL certificate. Please check your domain and try again."
        exit 1
    fi
    echo "SSL certificate obtained successfully."
}

# Function to renew SSL certificate
renew_ssl_certificate() {
    echo "Renewing SSL certificate for $DOMAIN..."
    sudo certbot renew
    if [[ $? -ne 0 ]]; then
        echo "Error renewing SSL certificate."
        exit 1
    fi
    echo "SSL certificate renewed successfully."
}

# Main script execution
check_certbot_installed
obtain_ssl_certificate

# Set up a cron job for automatic renewal (runs every day at noon)
(crontab -l; echo "0 12 * * * /usr/bin/certbot renew --quiet") | crontab -

echo "Setup complete. Your SSL certificate is now configured."
```

### Instructions:
1. Save the script as `setup_ssl.sh`.
2. Make the script executable: `chmod +x setup_ssl.sh`.
3. Modify the variables `DOMAIN`, `EMAIL`, and `WEBROOT` with your actual details.
4. Run the script: `./setup_ssl.sh`.

### Note:
- Ensure that you have proper permissions to install software and modify cron jobs on your system. 
- This script uses `certbot`, which may require additional installation steps if you're using a specific hosting service. Adjust the script accordingly based on your hosting environment.
