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

# Domain SSL and DNS validation script
# Usage: ./domain_check.sh <domain>

set -o errexit
set -o nounset
set -o pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Check if domain argument is provided
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: No domain specified.${NC}"
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN=$1

# Function to check SSL certificate
check_ssl() {
    local domain=$1
    echo -e "${YELLOW}Checking SSL certificate for $domain...${NC}"
    
    if openssl s_client -connect "$domain:443" -servername "$domain" </dev/null 2>/dev/null | openssl x509 -noout -dates >/dev/null 2>&1; then
        echo -e "${GREEN}SSL certificate is valid and properly configured.${NC}"
        
        # Get certificate expiration date
        local expiry_date=$(openssl s_client -connect "$domain:443" -servername "$domain" </dev/null 2>/dev/null | openssl x509 -noout -enddate | cut -d= -f2)
        echo -e "Certificate expires on: $expiry_date"
        return 0
    else
        echo -e "${RED}SSL certificate is not valid or not configured.${NC}"
        return 1
    fi
}

# Function to check DNS resolution
check_dns() {
    local domain=$1
    echo -e "${YELLOW}Checking DNS resolution for $domain...${NC}"
    
    # Check IPv4 resolution
    if dig +short A "$domain" @8.8.8.8 | grep -q '^[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}$'; then
        echo -e "${GREEN}IPv4 resolution successful.${NC}"
        dig +short A "$domain" @8.8.8.8 | while read -r ip; do
            echo "Resolved to: $ip"
        done
    else
        echo -e "${RED}IPv4 resolution failed.${NC}"
    fi
    
    # Check IPv6 resolution
    if dig +short AAAA "$domain" @8.8.8.8 | grep -q ':'; then
        echo -e "${GREEN}IPv6 resolution successful.${NC}"
        dig +short AAAA "$domain" @8.8.8.8 | while read -r ip; do
            echo "Resolved to: $ip"
        done
    else
        echo -e "${YELLOW}IPv6 resolution failed or not configured.${NC}"
    fi
}

# Main execution
echo -e "\n${YELLOW}Starting domain validation for: $DOMAIN${NC}\n"

check_ssl "$DOMAIN"
echo ""
check_dns "$DOMAIN"

echo -e "\n${YELLOW}Domain validation completed.${NC}"
```
