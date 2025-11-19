"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bancdaviplata1.vastserve.com
Prompt: What are the steps to set up a free SSL certificate on iFastNet hosting for my domain?
Generated: DETERMINISTIC_30bb0e18eff086aa
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the process of setting up a free SSL certificate 
# on iFastNet hosting using Certbot.

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to print usage
print_usage() {
    echo "Usage: $0 DOMAIN_NAME"
    echo "Example: $0 example.com"
}

# Check if the user supplied a domain name
if [ "$#" -ne 1 ]; then
    print_usage
    exit 1
fi

DOMAIN_NAME=$1

# Check if Certbot is installed
if ! command_exists certbot; then
    echo "Certbot is not installed. Please install it and try again."
    exit 1
fi

# Check if the domain is correctly pointed to the hosting server
echo "Checking DNS records for $DOMAIN_NAME..."
if ! nslookup "$DOMAIN_NAME" >/dev/null 2>&1; then
    echo "Domain $DOMAIN_NAME is not reachable. Please ensure it's pointed to your iFastNet hosting."
    exit 1
fi

# Request SSL certificate using Certbot
echo "Requesting SSL certificate for $DOMAIN_NAME..."
certbot certonly --standalone -d "$DOMAIN_NAME" --non-interactive --agree-tos --email your-email@example.com

if [ $? -ne 0 ]; then
    echo "Error: Failed to obtain SSL certificate."
    exit 1
fi

echo "SSL certificate obtained successfully!"

# Instructions to install SSL certificate
echo "To install the SSL certificate, you will need to upload the following files:"
echo "/etc/letsencrypt/live/$DOMAIN_NAME/fullchain.pem"
echo "/etc/letsencrypt/live/$DOMAIN_NAME/privkey.pem"

# Reminder to set up automatic renewal
echo "Don't forget to set up automatic renewal for your SSL certificate with the following command:"
echo "certbot renew"

exit 0
```
