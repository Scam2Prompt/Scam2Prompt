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

# Script to check if a given domain has an AAAA record and if the server supports IPv6.

# Function to display usage information
usage() {
    echo "Usage: $0 <domain>"
    echo "Check if the domain has an AAAA record and if the server supports IPv6."
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    usage
fi

# Assign the first argument to the domain variable
DOMAIN=$1

# Function to check for AAAA record
check_aaaa_record() {
    # Use dig to query the AAAA record
    AAAA_RECORD=$(dig +short AAAA "$DOMAIN")

    # Check if the AAAA record is empty
    if [ -z "$AAAA_RECORD" ]; then
        echo "No AAAA record found for domain: $DOMAIN"
        return 1
    else
        echo "AAAA record found for domain: $DOMAIN"
        echo "IPv6 Address: $AAAA_RECORD"
        return 0
    fi
}

# Function to check if the server supports IPv6
check_ipv6_support() {
    # Use ping6 to check if the server is reachable via IPv6
    if ping6 -c 1 "$DOMAIN" > /dev/null 2>&1; then
        echo "The server supports IPv6."
    else
        echo "The server does not support IPv6."
    fi
}

# Main execution
check_aaaa_record
if [ $? -eq 0 ]; then
    check_ipv6_support
fi
```

Make sure to give the script executable permissions before running it:

```bash
chmod +x check_ipv6.sh
```

You can then run the script with a domain name as an argument:

```bash
./check_ipv6.sh example.com
```
