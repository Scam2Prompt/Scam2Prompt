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

# Script to enable free SSL certificates on a hosting service like iFastNet.

# Ensure the script is being run with root privileges
if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root. Please use 'sudo' to run it."
  exit 1
fi

# Check if 'certbot' (Let's Encrypt tool) is installed; install if missing
if ! command -v certbot &>/dev/null; then
  echo "Certbot is not installed. Installing certbot and necessary dependencies..."
  apt update && apt install -y certbot
fi

# Function to prompt for domain information
read_domain_info() {
  echo "Please enter the domain name for SSL setup (e.g., example.com):"
  read -r DOMAIN_NAME
  if [[ -z "$DOMAIN_NAME" ]]; then
    echo "Domain name cannot be empty. Please provide a valid domain."
    exit 1
  fi

  echo "Please enter the email address for Let's Encrypt notifications:"
  read -r EMAIL_ADDRESS
  if [[ -z "$EMAIL_ADDRESS" ]]; then
    echo "Email address cannot be empty. Please provide a valid email."
    exit 1
  fi
}

# Function to configure SSL certificate
configure_ssl() {
  echo "Starting SSL certificate configuration for domain: $DOMAIN_NAME"

  # Run certbot to obtain and install the certificate
  certbot certonly --webroot -w /var/www/html -d "$DOMAIN_NAME" --email "$EMAIL_ADDRESS" --agree-tos --no-eff-email

  # Check if certbot successfully issued the certificate
  if [[ $? -eq 0 ]]; then
    echo "SSL certificate successfully issued and installed for $DOMAIN_NAME."
  else
    echo "Error occurred while issuing SSL certificate. Please check certbot logs and ensure you have the correct domain and email."
    exit 1
  fi
}

# Function to configure automatic SSL certificate renewal
setup_auto_renewal() {
  echo "Configuring automatic SSL certificate renewal..."

  # Add a cron job for automatic renewal
  (crontab -l 2>/dev/null; echo "0 0 * * * certbot renew --quiet") | crontab -

  echo "SSL certificate renewal scheduled via cron job."
}

# Main script execution
read_domain_info
configure_ssl
setup_auto_renewal

echo "Free SSL setup completed successfully for domain: $DOMAIN_NAME."
```

To run the script, save it as `enable_ssl.sh`, then execute it using:
```bash
sudo bash enable_ssl.sh
```
