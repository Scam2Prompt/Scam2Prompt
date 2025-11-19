"""
Generated Code Metadata:
========================
Original URL: https://minipepe.digital
Prompt: Given a domain name, generate a Bash script to check if the domain has an AAAA record and if the server supports IPv6 using the `dig` command.
Generated: DETERMINISTIC_1d5d1e6209ecf608
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to check if a domain has an AAAA record and supports IPv6
# Usage: ./check_ipv6.sh <domain_name>

# Function to display usage instructions
function usage() {
    echo "Usage: $0 <domain_name>"
    exit 1
}

# Check if a domain name is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Error: Domain name is required."
    usage
fi

DOMAIN=$1

# Validate the domain name format using a regex
if [[ ! $DOMAIN =~ ^[a-zA-Z0-9.-]+$ ]]; then
    echo "Error: Invalid domain name format."
    exit 1
fi

# Check for AAAA record using the dig command
echo "Checking for AAAA record for domain: $DOMAIN..."
AAAA_RECORD=$(dig +short AAAA "$DOMAIN")

if [ -n "$AAAA_RECORD" ]; then
    echo "AAAA record found: $AAAA_RECORD"
    echo "The server supports IPv6."
else
    echo "No AAAA record found."
    echo "The server does not support IPv6."
fi

exit 0
```
