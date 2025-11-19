"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Explain how to set up a free SSL certificate on iFastNet hosting and provide a code example for the configuration.
Generated: DETERMINISTIC_3686d165c7664ce1
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script automates the process of setting up a free SSL certificate on iFastNet hosting using Certbot.

# Define variables
DOMAIN="yourdomain.com"  # Replace with your actual domain
EMAIL="youremail@example.com"  # Replace with your email for notifications
WEBROOT="/path/to/your/webroot"  # Replace with the path to your website's root directory

# Update package list and install Certbot
echo "Updating package list..."
apt-get update

echo "Installing Certbot..."
apt-get install -y certbot

# Obtain a free SSL certificate
echo "Obtaining SSL certificate for $DOMAIN..."
certbot certonly --webroot -w $WEBROOT -d $DOMAIN --email $EMAIL --agree-tos --non-interactive

# Check if the certificate was successfully obtained
if [[ $? -ne 0 ]]; then
    echo "Error: Failed to obtain SSL certificate."
    exit 1
else
    echo "SSL certificate obtained successfully."
fi

# Set up automatic renewal of the SSL certificate
echo "Setting up automatic renewal for the SSL certificate..."
echo "0 0 * * * certbot renew --quiet" | crontab -

# Check if the cron job was added successfully
if [[ $? -ne 0 ]]; then
    echo "Error: Failed to set up automatic renewal."
    exit 1
else
    echo "Automatic renewal set up successfully."
fi

# Display the location of the obtained certificates
echo "SSL certificates are stored at:"
echo "/etc/letsencrypt/live/$DOMAIN/fullchain.pem"
echo "/etc/letsencrypt/live/$DOMAIN/privkey.pem"

# End of script
``` 

**Note:** Before running this script, ensure that you replace the placeholders with your actual domain, email, and webroot path. Additionally, this script should be executed on a server where you have root access, and the necessary dependencies are installed.
