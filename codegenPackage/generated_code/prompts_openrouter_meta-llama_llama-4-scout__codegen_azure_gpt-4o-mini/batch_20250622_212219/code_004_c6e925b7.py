"""
Generated Code Metadata:
========================
Original URL: https://muradsolana.net
Prompt: Generate a bash script to test if a domain is properly configured on a server by checking for the presence of an SSL certificate and a valid DNS record.
Generated: DETERMINISTIC_c6e925b74977536f
Batch ID: 20250622_212219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script checks if a domain is properly configured on a server
# by verifying the presence of an SSL certificate and a valid DNS record.

# Function to check for SSL certificate
check_ssl() {
    local domain=$1
    # Use openssl to check for SSL certificate
    echo "Checking SSL certificate for $domain..."
    if echo | openssl s_client -connect "$domain:443" -servername "$domain" 2>/dev/null | grep -q 'BEGIN CERTIFICATE'; then
        echo "SSL certificate is present for $domain."
    else
        echo "No SSL certificate found for $domain."
        return 1
    fi
}

# Function to check for valid DNS record
check_dns() {
    local domain=$1
    # Use dig to check for DNS records
    echo "Checking DNS records for $domain..."
    if dig +short "$domain" | grep -q '.'; then
        echo "Valid DNS record found for $domain."
    else
        echo "No valid DNS record found for $domain."
        return 1
    fi
}

# Main script execution
if [ $# -ne 1 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN=$1

# Check for SSL certificate and DNS record
check_ssl "$DOMAIN"
SSL_STATUS=$?

check_dns "$DOMAIN"
DNS_STATUS=$?

# Final status
if [ $SSL_STATUS -eq 0 ] && [ $DNS_STATUS -eq 0 ]; then
    echo "Domain $DOMAIN is properly configured with SSL and DNS."
else
    echo "Domain $DOMAIN is not properly configured."
    exit 1
fi

exit 0
```
