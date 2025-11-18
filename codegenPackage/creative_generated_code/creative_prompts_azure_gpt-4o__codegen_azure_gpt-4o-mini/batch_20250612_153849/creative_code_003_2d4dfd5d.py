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

# Script to enable HTTPS on LiteSpeed Web Server using Let's Encrypt

# Function to install Certbot if not already installed
install_certbot() {
    echo "Installing Certbot..."
    sudo apt-get update
    sudo apt-get install -y certbot
}

# Function to obtain and install Let's Encrypt SSL certificate
obtain_ssl_certificate() {
    local domain="$1"
    
    echo "Obtaining SSL certificate for $domain..."
    
    # Using Certbot to obtain the SSL certificate
    if ! sudo certbot certonly --standalone -d "$domain"; then
        echo "Error obtaining SSL certificate for $domain"
        exit 1
    fi
}

# Function to configure LiteSpeed to use the SSL certificate
configure_litespeed() {
    local domain="$1"
    
    echo "Configuring LiteSpeed to use the SSL certificate..."
    
    # Define paths to the SSL certificate and key files
    local ssl_cert_path="/etc/letsencrypt/live/$domain/fullchain.pem"
    local ssl_key_path="/etc/letsencrypt/live/$domain/privkey.pem"
    
    # Check if the certificate files exist
    if [[ ! -f "$ssl_cert_path" || ! -f "$ssl_key_path" ]]; then
        echo "SSL certificate or key not found."
        exit 1
    fi
    
    # Configure LiteSpeed to use the new SSL certificate
    sudo /usr/local/lsws/bin/lswsctrl restart
    
    echo "LiteSpeed has been configured to use the SSL certificate."
}

# Main script execution
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN="$1"

# Check if Certbot is installed; install if not
if ! command -v certbot &> /dev/null; then
    install_certbot
fi

# Obtain SSL certificate
obtain_ssl_certificate "$DOMAIN"

# Configure LiteSpeed Web Server with the new SSL certificate
configure_litespeed "$DOMAIN"

echo "HTTPS has been successfully enabled for $DOMAIN."
```

### Instructions:
1. Save the script as `enable_https.sh`.
2. Make it executable: `chmod +x enable_https.sh`.
3. Run the script with your domain as an argument: `./enable_https.sh yourdomain.com`.
