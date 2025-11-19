"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: How can I implement a free SSL certificate for my website hosted on ProHoster? Provide a step-by-step guide.
Generated: DETERMINISTIC_b39d20ca9001120a
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the process of obtaining and installing a free SSL certificate from Let's Encrypt
# for a website hosted on ProHoster. It requires certbot to be installed on the server.

# Define variables
DOMAIN="yourdomain.com" # Replace with your domain
EMAIL="youremail@example.com" # Replace with your email for Let's Encrypt notifications

# Function to check if certbot is installed
check_certbot_installed() {
    if ! command -v certbot &> /dev/null
    then
        echo "Certbot could not be found. Please install it before running this script."
        exit 1
    fi
}

# Function to obtain SSL certificate
obtain_ssl_certificate() {
    echo "Obtaining SSL certificate for $DOMAIN..."

    # Run certbot to obtain the SSL certificate
    certbot certonly --standalone --preferred-challenges http -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive
    if [ $? -ne 0 ]; then
        echo "Failed to obtain SSL certificate. Please check your domain settings and try again."
        exit 1
    fi

    echo "SSL certificate obtained successfully!"
}

# Function to set up automatic renewal of the SSL certificate
setup_auto_renewal() {
    echo "Setting up automatic renewal for the SSL certificate..."

    # Create a cron job for certificate renewal
    (crontab -l; echo "0 0 * * * /usr/bin/certbot renew --quiet") | crontab -
    if [ $? -ne 0 ]; then
        echo "Failed to set up automatic renewal. Please check your cron job settings."
        exit 1
    fi

    echo "Automatic renewal setup successfully!"
}

# Main script execution
check_certbot_installed
obtain_ssl_certificate
setup_auto_renewal

echo "SSL installation and configuration completed successfully!"
```

**Instructions:**
1. Replace `yourdomain.com` with your actual domain.
2. Replace `youremail@example.com` with your actual email address.
3. Ensure that `certbot` is installed on your server.
4. Save the script as `install_ssl.sh`.
5. Make the script executable: `chmod +x install_ssl.sh`.
6. Run the script: `./install_ssl.sh`.
