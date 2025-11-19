"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webautomigrate.hstn.me
Prompt: Write a sample configuration for enabling SSL on a website hosted with iFastNet, including the steps for obtaining a free SSL certificate.
Generated: DETERMINISTIC_fd378c067212bbbc
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash
# Script to configure SSL for a website hosted with iFastNet

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# Variables
DOMAIN="example.com" # Replace with your domain name
EMAIL="your-email@example.com" # Replace with your email address

# Step 1: Install Certbot
echo "Installing Certbot..."
apt update
apt install -y certbot python3-certbot-apache

# Step 2: Obtain a free SSL certificate from Let's Encrypt
echo "Obtaining SSL certificate for $DOMAIN..."
certbot --apache -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive

# Step 3: Verify installation
echo "Verifying SSL installation..."
if certbot certificates | grep "$DOMAIN"; then
  echo "SSL certificate successfully installed for $DOMAIN"
else
  echo "Failed to install SSL certificate. Please check the logs."
  exit 1
fi

# Step 4: Automate SSL certificate renewal
echo "Automating SSL certificate renewal..."
# Add a cron job for automatic renewal
CRON_JOB="0 0 * * * certbot renew --quiet"
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "SSL configuration for $DOMAIN is complete."
```
