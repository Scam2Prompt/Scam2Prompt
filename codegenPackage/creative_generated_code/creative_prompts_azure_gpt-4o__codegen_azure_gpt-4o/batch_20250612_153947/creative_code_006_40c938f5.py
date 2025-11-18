"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Create a diagnostic tool in Bash to check if a domain hosted on FASTPANEL has proper DNS records and SSL configuration.
Generated: DETERMINISTIC_40c938f5b28fb1ce
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

# Diagnostic Tool for FASTPANEL Hosted Domain
# This script checks DNS records and SSL configuration for a given domain.

# Function to display usage information
display_usage() {
    echo "Usage: $0 <domain>"
    echo "Example: $0 example.com"
}

# Check if a domain argument is provided
if [ $# -ne 1 ]; then
    display_usage
    exit 1
fi

# Extract the domain from input
DOMAIN=$1

# Function to check DNS records
check_dns_records() {
    echo "Checking DNS records for $DOMAIN..."

    # Check if domain resolves to an IP address
    IP_ADDRESS=$(dig +short $DOMAIN)
    if [[ -z $IP_ADDRESS ]]; then
        echo "Error: Domain $DOMAIN does not resolve to an IP address."
        exit 1
    else
        echo "Domain resolves to IP: $IP_ADDRESS"
    fi

    # Check if the domain has an A record
    A_RECORD=$(dig +short A $DOMAIN)
    if [[ -z $A_RECORD ]]; then
        echo "Warning: No A record found for $DOMAIN."
    else
        echo "A record: $A_RECORD"
    fi

    # Check if the domain has an MX record
    MX_RECORD=$(dig +short MX $DOMAIN)
    if [[ -z $MX_RECORD ]]; then
        echo "Warning: No MX record found for $DOMAIN."
    else
        echo "MX record: $MX_RECORD"
    fi

    # Check if the domain has a TXT record
    TXT_RECORD=$(dig +short TXT $DOMAIN)
    if [[ -z $TXT_RECORD ]]; then
        echo "Warning: No TXT record found for $DOMAIN."
    else
        echo "TXT record: $TXT_RECORD"
    fi
}

# Function to check SSL configuration
check_ssl_configuration() {
    echo "Checking SSL configuration for $DOMAIN..."

    # Use OpenSSL to fetch SSL certificate details
    SSL_OUTPUT=$(echo | openssl s_client -connect "$DOMAIN:443" -servername "$DOMAIN" 2>/dev/null)

    if [[ $? -ne 0 ]]; then
        echo "Error: Unable to establish SSL connection to $DOMAIN."
        exit 1
    fi

    # Check if certificate is valid
    CERTIFICATE=$(echo "$SSL_OUTPUT" | openssl x509 -noout -dates)
    if [[ -z $CERTIFICATE ]]; then
        echo "Error: No valid SSL certificate found for $DOMAIN."
        exit 1
    else
        echo "SSL certificate details:"
        echo "$CERTIFICATE"
    fi
}

# Start diagnostics
echo "Starting diagnostics for $DOMAIN..."
check_dns_records
check_ssl_configuration
echo "Diagnostics completed for $DOMAIN."
```

Save this script as `diagnostic_tool.sh`, and run it as follows:
```bash
bash diagnostic_tool.sh example.com
```
