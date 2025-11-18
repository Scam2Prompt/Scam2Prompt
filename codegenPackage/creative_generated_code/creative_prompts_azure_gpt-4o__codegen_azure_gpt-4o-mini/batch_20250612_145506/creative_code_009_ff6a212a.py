"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chillguy.lol
Prompt: Generate code to automate the setup of SSL certificates for multiple domains on a FASTPANEL server.
Generated: DETERMINISTIC_ff6a212abaf3eedd
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the setup of SSL certificates for multiple domains on a FASTPANEL server
# Usage: ./setup_ssl.sh domain1.com domain2.com ...

# Exit on any error
set -e

# Function to install Certbot if not already installed
install_certbot() {
    if ! command -v certbot &>/dev/null; then
        echo "Certbot not found. Installing..."
        apt update
        apt install -y certbot
    else
        echo "Certbot is already installed."
    fi
}

# Function to obtain SSL certificate for a given domain
obtain_ssl_certificate() {
    local domain="$1"

    # Check if the domain is valid
    if [[ -z "$domain" ]]; then
        echo "Error: No domain provided."
        return 1
    fi

    echo "Obtaining SSL certificate for: $domain"

    # Attempt to obtain an SSL certificate using Certbot
    if certbot certonly --non-interactive --agree-tos --email your-email@example.com --webroot -w /var/www/$domain -d "$domain"; then
        echo "SSL certificate obtained successfully for $domain."
    else
        echo "Error obtaining SSL certificate for $domain."
        return 1
    fi
}

# Main script logic
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 domain1.com domain2.com ..."
    exit 1
fi

install_certbot

for domain in "$@"; do
    obtain_ssl_certificate "$domain"
done

echo "All specified SSL certificates have been processed."
```

**Instructions:**
1. Save the above script as `setup_ssl.sh`.
2. Make the script executable: `chmod +x setup_ssl.sh`.
3. Run the script with the domains as arguments: `./setup_ssl.sh domain1.com domain2.com`. 
4. Replace `your-email@example.com` with your contact email for certificate notifications.
