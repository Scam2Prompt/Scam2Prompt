"""
Generated Code Metadata:
========================
Original URL: https://minatos3.com
Prompt: Generate a bash script to test if a domain is properly configured by checking for the presence of an SSL certificate and attempting to resolve the domain using both IPv4 and IPv6.
Generated: DETERMINISTIC_f013a1e70454df6e
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to test if a domain is properly configured by:
# 1. Checking for the presence of an SSL certificate
# 2. Resolving the domain using both IPv4 and IPv6

# Function to print usage instructions
print_usage() {
    echo "Usage: $0 <domain>"
    echo "Example: $0 example.com"
}

# Check if a domain argument is provided
if [ "$#" -ne 1 ]; then
    echo "Error: Missing domain argument."
    print_usage
    exit 1
fi

DOMAIN=$1

# Function to check SSL certificate
check_ssl_certificate() {
    echo "Checking SSL certificate for $DOMAIN..."
    # Use openssl to check SSL certificate
    timeout 10 openssl s_client -connect "$DOMAIN:443" -servername "$DOMAIN" < /dev/null 2>/dev/null | grep -q "BEGIN CERTIFICATE"
    if [ $? -eq 0 ]; then
        echo "SSL certificate is present."
    else
        echo "SSL certificate is NOT present or could not be verified."
    fi
}

# Function to resolve domain using IPv4
resolve_ipv4() {
    echo "Resolving $DOMAIN using IPv4..."
    IPV4=$(dig +short A "$DOMAIN")
    if [ -n "$IPV4" ]; then
        echo "IPv4 address found: $IPV4"
    else
        echo "No IPv4 address found for $DOMAIN."
    fi
}

# Function to resolve domain using IPv6
resolve_ipv6() {
    echo "Resolving $DOMAIN using IPv6..."
    IPV6=$(dig +short AAAA "$DOMAIN")
    if [ -n "$IPV6" ]; then
        echo "IPv6 address found: $IPV6"
    else
        echo "No IPv6 address found for $DOMAIN."
    fi
}

# Main script execution
echo "Testing domain configuration for: $DOMAIN"
check_ssl_certificate
resolve_ipv4
resolve_ipv6

echo "Domain configuration test completed."
```
