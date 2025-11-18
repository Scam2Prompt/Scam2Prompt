"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: Create a tutorial for setting up secure SSL certificates for a site hosted on aaPanel.
Generated: DETERMINISTIC_39c72203bcdde359
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to set up secure SSL certificates using Let's Encrypt on aaPanel-hosted websites.

# Ensure the script is executed as root to have the necessary permissions.
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root."
  exit 1
fi

# Function to install Certbot (Let's Encrypt client) if it's not already installed.
install_certbot() {
  echo "Checking if Certbot is installed..."
  if ! command -v certbot &> /dev/null; then
    echo "Certbot not found. Installing..."
    # Update package list
    apt-get update -y
    # Install Certbot and required dependencies
    apt-get install certbot -y
    echo "Certbot installed successfully."
  else
    echo "Certbot is already installed."
  fi
}

# Function to set up SSL certificates for the specified domain.
setup_ssl_certificate() {
  local domain=$1
  echo "Setting up SSL certificate for domain: $domain"
  
  # Run Certbot to generate and install the SSL certificate
  certbot certonly --webroot -w /www/wwwroot/"$domain" -d "$domain" --email admin@"$domain" --agree-tos --non-interactive
  
  # Check if the SSL files were successfully generated
  if [ -f "/etc/letsencrypt/live/$domain/fullchain.pem" ] && [ -f "/etc/letsencrypt/live/$domain/privkey.pem" ]; then
    echo "SSL certificate generated successfully!"
  else
    echo "Failed to generate SSL certificate for domain: $domain"
    exit 1
  fi
}

# Function to reload the web server to apply the SSL configuration.
reload_web_server() {
  echo "Reloading web server to apply SSL settings..."
  # Check for common web servers and reload accordingly
  if systemctl is-active --quiet nginx; then
    systemctl reload nginx
    echo "Web server (Nginx) reloaded successfully."
  elif systemctl is-active --quiet apache2; then
    systemctl reload apache2
    echo "Web server (Apache) reloaded successfully."
  else
    echo "No supported web server found. Please reload your server manually."
  fi
}

# Main script execution
echo "Starting SSL certificate setup..."

# Example usage for domain setup
DOMAIN="example.com"

# Install Certbot if necessary
install_certbot

# Set up SSL certificate for the domain
setup_ssl_certificate "$DOMAIN"

# Reload the web server to apply changes
reload_web_server

echo "SSL certificate setup complete for domain: $DOMAIN"
```

Make sure to replace `example.com` with the actual domain name you want to secure. This script assumes the web root directory for the domain is `/www/wwwroot/<domain>` and `aaPanel` manages the hosting environment.
