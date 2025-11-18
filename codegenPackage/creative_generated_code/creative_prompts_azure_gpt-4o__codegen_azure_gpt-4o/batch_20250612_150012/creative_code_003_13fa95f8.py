"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--mtamask-bya.com
Prompt: Create a shell script to check if a domain is active and using Hostinger nameservers.
Generated: DETERMINISTIC_13fa95f8ae74e86d
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to check if a domain is active and using Hostinger nameservers

# Function to print usage information
print_usage() {
    echo "Usage: $0 <domain>"
    exit 1
}

# Check if the domain argument is provided
if [ $# -ne 1 ]; then
    echo "Error: No domain provided."
    print_usage
fi

DOMAIN=$1

# Function to check if the domain resolves
check_domain_active() {
    if ! ping -c 1 -W 1 "$DOMAIN" &>/dev/null; then
        echo "Domain is not active or reachable."
        exit 1
    fi
}

# Function to check if the domain uses Hostinger nameservers
check_hostinger_nameservers() {
    # Perform a WHOIS lookup to get the nameservers
    WHOIS_OUTPUT=$(whois "$DOMAIN" 2>/dev/null)
    if [ $? -ne 0 ]; then
        echo "Error: Unable to perform WHOIS lookup on the domain."
        exit 1
    fi

    # Check if Hostinger nameservers are present in the WHOIS output
    if echo "$WHOIS_OUTPUT" | grep -q -i "hostinger"; then
        echo "Domain is using Hostinger nameservers."
    else
        echo "Domain is not using Hostinger nameservers."
    fi
}

# Main script execution
check_domain_active
check_hostinger_nameservers
```
