"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismai.live
Prompt: Write a code snippet to enable HTTPS on a LiteSpeed Web Server using Let's Encrypt.
Generated: DETERMINISTIC_2d4dfd5d265fb103
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to enable HTTPS on a LiteSpeed Web Server using Let's Encrypt

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
DOMAIN="yourdomain.com" # Replace with your domain
EMAIL="your-email@example.com" # Replace with your email address

# Ensure LiteSpeed is installed and the certbot tool is available
if ! command -v certbot &> /dev/null; then
    echo "Certbot is not installed. Please install it first."
    exit 1
fi

if ! command -v lswsctrl &> /dev/null; then
    echo "LiteSpeed Web Server is not installed. Please install it first."
    exit 1
fi

# Stop LiteSpeed Web Server to avoid conflicts during certificate issuance
echo "Stopping LiteSpeed Web Server..."
lswsctrl stop

# Request Let's Encrypt SSL certificate
echo "Requesting Let's Encrypt SSL certificate..."
certbot certonly --standalone -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive

# Define certificate paths
CERT_PATH="/etc/letsencrypt/live/$DOMAIN/fullchain.pem"
KEY_PATH="/etc/letsencrypt/live/$DOMAIN/privkey.pem"

# Check if the certificates were generated successfully
if [[ ! -f "$CERT_PATH" || ! -f "$KEY_PATH" ]]; then
    echo "Failed to generate SSL certificates. Please check your setup."
    exit 1
fi

# Configure LiteSpeed Web Server to use the generated certificates
echo "Configuring LiteSpeed Web Server to use HTTPS..."
LITESPEED_CONF="/usr/local/lsws/conf/httpd_config.conf"

if [[ ! -f "$LITESPEED_CONF" ]]; then
    echo "LiteSpeed configuration file not found. Please check your installation."
    exit 1
fi

# Add SSL settings into the LiteSpeed configuration
cat << EOF >> "$LITESPEED_CONF"
listener Default {
    address *:443
    secure 1
    certFile $CERT_PATH
    keyFile $KEY_PATH
}
EOF

# Restart LiteSpeed Web Server to apply the changes
echo "Restarting LiteSpeed Web Server..."
lswsctrl start

echo "HTTPS has been successfully enabled on LiteSpeed Web Server for domain $DOMAIN."
exit 0
```
