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
# Checks for the presence of an A record and an SSL certificate

# Function to print usage instructions
print_usage() {
    echo "Usage: $0 <domain>"
    echo "Example: $0 example.com"
}

# Check if a domain argument is provided
if [ "$#" -ne 1 ]; then
    echo "Error: Domain name is required."
    print_usage
    exit 1
fi

DOMAIN=$1

# Function to check for an A record
check_a_record() {
    echo "Checking A record for domain: $DOMAIN..."
    A_RECORD=$(dig +short "$DOMAIN" A)
    if [ -z "$A_RECORD" ]; then
        echo "Error: No A record found for $DOMAIN."
        return 1
    else
        echo "A record found: $A_RECORD"
        return 0
    fi
}

# Function to check for an SSL certificate
check_ssl_certificate() {
    echo "Checking SSL certificate for domain: $DOMAIN..."
    SSL_OUTPUT=$(echo | openssl s_client -connect "$DOMAIN:443" -servername "$DOMAIN" 2>/dev/null)
    if echo "$SSL_OUTPUT" | grep -q "BEGIN CERTIFICATE"; then
        echo "SSL certificate is present for $DOMAIN."
        return 0
    else
        echo "Error: No SSL certificate found for $DOMAIN."
        return 1
    fi
}

# Perform checks
check_a_record
A_RECORD_STATUS=$?

check_ssl_certificate
SSL_STATUS=$?

# Final status
if [ "$A_RECORD_STATUS" -eq 0 ] && [ "$SSL_STATUS" -eq 0 ]; then
    echo "Domain $DOMAIN is properly configured."
    exit 0
else
    echo "Domain $DOMAIN is not properly configured."
    exit 1
fi
```
