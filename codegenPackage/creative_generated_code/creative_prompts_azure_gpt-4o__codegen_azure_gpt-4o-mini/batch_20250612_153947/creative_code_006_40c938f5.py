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

# Diagnostic Tool for Checking DNS Records and SSL Configuration for a Domain on FASTPANEL

# Function to check if a domain has proper A and CNAME records
check_dns_records() {
    local domain=$1

    echo "Checking DNS records for domain: $domain"

    # Check A record
    if dig +short A "$domain" > /dev/null; then
        echo "A record is properly configured."
    else
        echo "ERROR: A record not found for $domain."
    fi

    # Check CNAME record
    if dig +short CNAME "$domain" > /dev/null; then
        echo "CNAME record is properly configured."
    else
        echo "ERROR: CNAME record not found for $domain."
    fi
}

# Function to check SSL certificate configuration
check_ssl_configuration() {
    local domain=$1

    echo "Checking SSL configuration for domain: $domain"

    # Use OpenSSL to check SSL certificate
    if echo | openssl s_client -connect "$domain:443" -servername "$domain" 2>/dev/null | grep -q 'Certificate chain'; then
        echo "SSL certificate is properly configured."
    else
        echo "ERROR: SSL certificate not found or improperly configured for $domain."
    fi
}

# Main execution
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN=$1

# Validate domain format
if ! [[ $DOMAIN =~ ^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "ERROR: Invalid domain format."
    exit 1
fi

# Check DNS records and SSL configuration
check_dns_records "$DOMAIN"
check_ssl_configuration "$DOMAIN"

echo "Diagnostic check completed for $DOMAIN."
```
