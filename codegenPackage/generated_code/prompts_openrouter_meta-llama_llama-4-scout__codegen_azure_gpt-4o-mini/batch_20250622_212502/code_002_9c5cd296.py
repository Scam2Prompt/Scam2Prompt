"""
Generated Code Metadata:
========================
Original URL: https://ethegas.in
Prompt: Generate a bash script to verify if a domain is properly configured on a server by checking for the presence of an A record and an SSL certificate.
Generated: DETERMINISTIC_9c5cd29617f3a37f
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to verify if a domain is properly configured on a server
# by checking for the presence of an A record and an SSL certificate.

# Function to check for A record
check_a_record() {
    local domain=$1
    # Use dig to check for A record
    if dig +short "$domain" A > /dev/null; then
        echo "A record for $domain exists."
        return 0
    else
        echo "No A record found for $domain."
        return 1
    fi
}

# Function to check for SSL certificate
check_ssl_certificate() {
    local domain=$1
    # Use openssl to check for SSL certificate
    if echo | openssl s_client -connect "$domain:443" -servername "$domain" 2>/dev/null | grep -q 'BEGIN CERTIFICATE'; then
        echo "SSL certificate for $domain is present."
        return 0
    else
        echo "No SSL certificate found for $domain."
        return 1
    fi
}

# Main script execution
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN=$1

# Check for A record
if ! check_a_record "$DOMAIN"; then
    echo "Domain verification failed: A record missing."
    exit 1
fi

# Check for SSL certificate
if ! check_ssl_certificate "$DOMAIN"; then
    echo "Domain verification failed: SSL certificate missing."
    exit 1
fi

echo "Domain $DOMAIN is properly configured."
exit 0
```
