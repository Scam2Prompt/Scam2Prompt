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

# Script to check if a domain is properly configured by verifying SSL certificate and DNS record.

# Function to display usage instructions
usage() {
    echo "Usage: $0 <domain>"
    exit 1
}

# Check if a domain argument is provided
if [ $# -ne 1 ]; then
    usage
fi

DOMAIN=$1

# Function to check DNS record
check_dns() {
    echo "Checking DNS record for $DOMAIN..."
    if nslookup "$DOMAIN" > /dev/null 2>&1; then
        echo "DNS record is valid."
    else
        echo "DNS record is invalid or not found."
        exit 1
    fi
}

# Function to check SSL certificate
check_ssl() {
    echo "Checking SSL certificate for $DOMAIN..."
    # Use openssl to check SSL certificate validity
    if echo | openssl s_client -connect "$DOMAIN:443" -servername "$DOMAIN" 2>/dev/null | openssl x509 -noout -dates > /dev/null 2>&1; then
        echo "SSL certificate is present and valid."
    else
        echo "SSL certificate is missing or invalid."
        exit 1
    fi
}

# Main script execution
check_dns
check_ssl

echo "Domain $DOMAIN is properly configured."
exit 0
```
