"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://425876928756287.icu
Prompt: Write a Bash script to list all domains on a FASTPANEL server and check their HTTPS configuration status.
Generated: DETERMINISTIC_f66635832c0eb531
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to list all domains on a FASTPANEL server and check their HTTPS configuration status.
# Written with best practices, proper error handling, and clean code.

# Function to check HTTPS status of a domain
check_https_status() {
    local domain=$1
    # Send a request to the domain using curl and check the HTTP status code
    response=$(curl -s -o /dev/null -w "%{http_code}" https://"$domain")
    
    if [[ "$response" -eq 200 ]]; then
        echo "HTTPS is configured and working for $domain"
    else
        echo "WARNING: HTTPS is not properly configured for $domain (HTTP code: $response)"
    fi
}

# Validate if the necessary tools are installed
if ! command -v curl &> /dev/null; then
    echo "Error: 'curl' is required but not installed. Please install curl and re-run the script."
    exit 1
fi

# Fetch the list of domains from FASTPANEL
domains=$(fastpanel-cli site list | awk '{print $1}' | sed 1d)

# Ensure there are domains returned
if [[ -z "$domains" ]]; then
    echo "Error: No domains found on the FASTPANEL server."
    exit 1
fi

echo "Checking HTTPS status for domains on the FASTPANEL server..."
echo "--------------------------------------------"

# Iterate over each domain and check its HTTPS status
while read -r domain; do
    check_https_status "$domain"
done <<< "$domains"

echo "--------------------------------------------"
echo "HTTPS status check complete."
exit 0
```
