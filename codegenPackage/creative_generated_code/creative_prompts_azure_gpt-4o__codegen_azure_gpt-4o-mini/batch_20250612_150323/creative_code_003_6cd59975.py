"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefyfinace.io
Prompt: Create a bash script to check and verify DNS propagation after migrating a website to Hostinger.
Generated: DETERMINISTIC_6cd59975cd5be4f6
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# DNS Propagation Checker
# This script checks DNS propagation for a given domain after migrating a website to Hostinger.

# Function to display usage information
usage() {
    echo "Usage: $0 <domain> [<nameserver>]"
    echo "  domain       : The domain to check (e.g., example.com)"
    echo "  nameserver   : Optional, specific nameserver to check (e.g., 8.8.8.8)"
    exit 1
}

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "Error: Missing domain argument."
    usage
fi

# Assigning the domain and nameserver variables
DOMAIN=$1
NAMESERVER=${2:-"8.8.8.8"}  # Default to Google's public DNS if no nameserver is provided

# Function to check DNS records
check_dns() {
    local domain="$1"
    local nameserver="$2"
    
    # Perform DNS lookup
    echo "Checking DNS records for $domain using nameserver $nameserver..."
    DNS_OUTPUT=$(dig @${nameserver} ${domain} +short)

    # Check if the dig command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Failed to perform DNS lookup for $domain."
        exit 1
    fi

    # Check if any DNS records were returned
    if [ -z "$DNS_OUTPUT" ]; then
        echo "No DNS records found for $domain using nameserver $nameserver."
    else
        echo "DNS records for $domain:"
        echo "$DNS_OUTPUT"
    fi
}

# Main script execution
echo "Starting DNS propagation check for $DOMAIN..."

# Check DNS records using the specified nameserver
check_dns "$DOMAIN" "$NAMESERVER"

echo "DNS propagation check completed."
exit 0
```
