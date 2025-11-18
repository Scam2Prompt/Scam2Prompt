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

# Function to check if a domain is active
check_domain_active() {
    local domain=$1
    # Use 'dig' to check if the domain has an A record
    if dig +short "$domain" | grep -q '^[0-9]'; then
        return 0  # Domain is active
    else
        return 1  # Domain is not active
    fi
}

# Function to check if the domain is using Hostinger nameservers
check_hostinger_nameservers() {
    local domain=$1
    # Get the nameservers for the domain
    local nameservers
    nameservers=$(dig +short ns "$domain")

    # Check if any of the nameservers match Hostinger's known nameservers
    local hostinger_ns=("ns1.dns-parking.com" "ns2.dns-parking.com")
    for ns in "${hostinger_ns[@]}"; do
        if echo "$nameservers" | grep -q "$ns"; then
            return 0  # Using Hostinger nameservers
        fi
    done

    return 1  # Not using Hostinger nameservers
}

# Main script execution
if [ $# -ne 1 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN=$1

# Check if the domain is active
if check_domain_active "$DOMAIN"; then
    echo "The domain '$DOMAIN' is active."
    # Check if the domain is using Hostinger nameservers
    if check_hostinger_nameservers "$DOMAIN"; then
        echo "The domain '$DOMAIN' is using Hostinger nameservers."
    else
        echo "The domain '$DOMAIN' is not using Hostinger nameservers."
    fi
else
    echo "The domain '$DOMAIN' is not active."
    exit 2
fi

exit 0
```
