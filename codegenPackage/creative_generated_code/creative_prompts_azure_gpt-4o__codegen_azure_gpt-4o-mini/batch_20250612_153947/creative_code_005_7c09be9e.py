"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Provide code examples for setting up an SSL certificate on a FASTPANEL-managed server to ensure HTTPS access works correctly.
Generated: DETERMINISTIC_7c09be9e97267eed
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script sets up an SSL certificate on a FASTPANEL-managed server.
# It assumes you have the necessary permissions and that the server is already set up.

# Function to install Certbot for obtaining SSL certificates
install_certbot() {
    echo "Installing Certbot..."
    # Update package lists
    sudo apt update
    # Install Certbot and the Nginx plugin
    sudo apt install -y certbot python3-certbot-nginx || {
        echo "Error installing Certbot. Please check your package manager."
        exit 1
    }
}

# Function to obtain an SSL certificate
obtain_ssl_certificate() {
    local domain=$1
    echo "Obtaining SSL certificate for $domain..."

    # Use Certbot to obtain the SSL certificate
    sudo certbot --nginx -d "$domain" --agree-tos --email your-email@example.com --non-interactive || {
        echo "Error obtaining SSL certificate for $domain."
        exit 1
    }
}

# Function to set up automatic renewal of the SSL certificate
setup_renewal() {
    echo "Setting up automatic renewal for SSL certificate..."
    # Add a cron job to renew the certificate
    (sudo crontab -l 2>/dev/null; echo "0 3 * * * /usr/bin/certbot renew --quiet") | sudo crontab - || {
        echo "Error setting up automatic renewal. Please check your cron configuration."
        exit 1
    }
}

# Main script execution
main() {
    # Check if the domain is passed as an argument
    if [ "$#" -ne 1 ]; then
        echo "Usage: $0 <your-domain.com>"
        exit 1
    fi

    local domain=$1

    # Install Certbot if it is not already installed
    if ! command -v certbot &> /dev/null; then
        install_certbot
    fi

    # Obtain SSL certificate for the provided domain
    obtain_ssl_certificate "$domain"

    # Setup automatic renewal for the SSL certificate
    setup_renewal

    echo "SSL certificate setup complete for $domain!"
}

# Execute the main function with all script arguments
main "$@"
```
