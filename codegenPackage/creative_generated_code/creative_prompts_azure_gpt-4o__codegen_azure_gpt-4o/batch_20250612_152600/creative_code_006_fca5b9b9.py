"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ailocation-me.com
Prompt: Explain how to configure a FASTPANEL server to support both IPv4 and IPv6, and write code to update DNS records accordingly.
Generated: DETERMINISTIC_fca5b9b984149627
Batch ID: 20250612_152600
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://ipv6.icanhazip.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://ipv4.icanhazip.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.dnsprovider.com/v1/dns": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure FASTPANEL server to support both IPv4 and IPv6
# and update DNS records accordingly.

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to check if a command exists
function check_command_exists() {
    command -v "$1" >/dev/null 2>&1 || {
        echo "Error: $1 is not installed. Please install it and run the script again."
        exit 1
    }
}

# Ensure necessary tools are installed
check_command_exists "fastpanel"
check_command_exists "curl"
check_command_exists "jq"

####################
# IPv4 Configuration
####################
# Verify and configure IPv4
echo "Configuring IPv4..."
IPv4_ADDRESS=$(curl -s http://ipv4.icanhazip.com/)
if [[ -z "$IPv4_ADDRESS" ]]; then
    echo "Error: Unable to fetch the IPv4 address."
    exit 1
fi
echo "Detected IPv4 Address: $IPv4_ADDRESS"

# Add IPv4 configuration to FASTPANEL
fastpanel network add --type ipv4 --address "$IPv4_ADDRESS"

####################
# IPv6 Configuration
####################
# Verify and configure IPv6
echo "Configuring IPv6..."
IPv6_ADDRESS=$(curl -s http://ipv6.icanhazip.com/)
if [[ -z "$IPv6_ADDRESS" ]]; then
    echo "Error: Unable to fetch the IPv6 address."
    exit 1
fi
echo "Detected IPv6 Address: $IPv6_ADDRESS"

# Add IPv6 configuration to FASTPANEL
fastpanel network add --type ipv6 --address "$IPv6_ADDRESS"

############################
# Update DNS Records
############################
# Function to update DNS records
function update_dns_records() {
    local domain="$1"
    local ipv4="$2"
    local ipv6="$3"

    echo "Updating DNS records for domain: $domain"

    # Replace with your DNS provider's API endpoint and token
    DNS_API_ENDPOINT="https://api.dnsprovider.com/v1/dns"
    API_TOKEN="your_api_token_here"

    # Update A record (IPv4)
    curl -X POST "$DNS_API_ENDPOINT" \
        -H "Authorization: Bearer $API_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
            "type": "A",
            "name": "'"$domain"'",
            "content": "'"$ipv4"'",
            "ttl": 3600
        }'

    # Update AAAA record (IPv6)
    curl -X POST "$DNS_API_ENDPOINT" \
        -H "Authorization: Bearer $API_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
            "type": "AAAA",
            "name": "'"$domain"'",
            "content": "'"$ipv6"'",
            "ttl": 3600
        }'

    echo "DNS records updated successfully."
}

# Prompt for domain name
read -p "Enter your domain name: " DOMAIN_NAME

# Update DNS records
update_dns_records "$DOMAIN_NAME" "$IPv4_ADDRESS" "$IPv6_ADDRESS"

echo "Configuration completed successfully."
```
