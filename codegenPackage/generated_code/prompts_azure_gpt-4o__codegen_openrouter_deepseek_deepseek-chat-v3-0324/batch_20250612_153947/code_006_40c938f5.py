"""
Generated Code Metadata:
========================
Original URL: https://claimairtoday.com
Prompt: Create a diagnostic tool in Bash to check if a domain hosted on FASTPANEL has proper DNS records and SSL configuration.
Generated: DETERMINISTIC_40c938f5b28fb1ce
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Domain Diagnostic Tool for FASTPANEL
# Checks DNS records and SSL configuration for a given domain

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Check if required commands are available
check_dependencies() {
    local dependencies=("dig" "curl" "openssl" "nc" "whois")
    local missing=()

    for cmd in "${dependencies[@]}"; do
        if ! command -v "$cmd" &> /dev/null; then
            missing+=("$cmd")
        fi
    done

    if [ ${#missing[@]} -gt 0 ]; then
        echo -e "${RED}Error: Missing required commands: ${missing[*]}${NC}"
        exit 1
    fi
}

# Check DNS records
check_dns() {
    local domain=$1
    local ipv4_records=()
    local ipv6_records=()
    local mx_records=()
    local txt_records=()
    local ns_records=()
    local has_error=false

    echo -e "\n${YELLOW}Checking DNS records for ${domain}...${NC}"

    # Get A records
    ipv4_records=($(dig +short A "$domain"))
    if [ ${#ipv4_records[@]} -eq 0 ]; then
        echo -e "${RED}✗ No IPv4 (A) records found${NC}"
        has_error=true
    else
        echo -e "${GREEN}✓ IPv4 (A) records:${NC}"
        for record in "${ipv4_records[@]}"; do
            echo "  $record"
        done
    fi

    # Get AAAA records
    ipv6_records=($(dig +short AAAA "$domain"))
    if [ ${#ipv6_records[@]} -eq 0 ]; then
        echo -e "${YELLOW}⚠ No IPv6 (AAAA) records found${NC}"
    else
        echo -e "${GREEN}✓ IPv6 (AAAA) records:${NC}"
        for record in "${ipv6_records[@]}"; do
            echo "  $record"
        done
    fi

    # Get MX records
    mx_records=($(dig +short MX "$domain" | sort -n))
    if [ ${#mx_records[@]} -eq 0 ]; then
        echo -e "${RED}✗ No MX records found${NC}"
        has_error=true
    else
        echo -e "${GREEN}✓ MX records:${NC}"
        for record in "${mx_records[@]}"; do
            echo "  $record"
        done
    fi

    # Get TXT records
    txt_records=($(dig +short TXT "$domain"))
    if [ ${#txt_records[@]} -eq 0 ]; then
        echo -e "${YELLOW}⚠ No TXT records found${NC}"
    else
        echo -e "${GREEN}✓ TXT records:${NC}"
        for record in "${txt_records[@]}"; do
            echo "  $record"
        done
    fi

    # Get NS records
    ns_records=($(dig +short NS "$domain"))
    if [ ${#ns_records[@]} -eq 0 ]; then
        echo -e "${RED}✗ No NS records found${NC}"
        has_error=true
    else
        echo -e "${GREEN}✓ NS records:${NC}"
        for record in "${ns_records[@]}"; do
            echo "  $record"
        done
    fi

    return $has_error
}

# Check SSL certificate
check_ssl() {
    local domain=$1
    local has_error=false

    echo -e "\n${YELLOW}Checking SSL certificate for ${domain}...${NC}"

    # Check if port 443 is open
    if ! nc -z -w 2 "$domain" 443 &> /dev/null; then
        echo -e "${RED}✗ Port 443 is not open${NC}"
        return 1
    fi

    # Get certificate details
    local cert_info
    cert_info=$(openssl s_client -connect "$domain:443" -servername "$domain" < /dev/null 2>/dev/null | openssl x509 -noout -dates 2>/dev/null)

    if [ -z "$cert_info" ]; then
        echo -e "${RED}✗ No SSL certificate found${NC}"
        has_error=true
    else
        echo -e "${GREEN}✓ SSL certificate found${NC}"
        echo "$cert_info"

        # Check expiration
        local expiry_date
        expiry_date=$(echo "$cert_info" | grep 'notAfter' | cut -d= -f2)
        local expiry_epoch=$(date -d "$expiry_date" +%s)
        local now_epoch=$(date +%s)
        local days_left=$(( (expiry_epoch - now_epoch) / 86400 ))

        if [ "$days_left" -lt 0 ]; then
            echo -e "${RED}✗ Certificate expired ${days_left#-} days ago${NC}"
            has_error=true
        elif [ "$days_left" -lt 7 ]; then
            echo -e "${RED}✗ Certificate expires in $days_left days${NC}"
            has_error=true
        elif [ "$days_left" -lt 30 ]; then
            echo -e "${YELLOW}⚠ Certificate expires in $days_left days${NC}"
        else
            echo -e "${GREEN}✓ Certificate valid for $days_left days${NC}"
        fi
    fi

    return $has_error
}

# Main function
main() {
    check_dependencies

    if [ $# -ne 1 ]; then
        echo -e "${RED}Usage: $0 <domain>${NC}"
        exit 1
    fi

    local domain=$1
    local overall_status=0

    check_dns "$domain" || overall_status=1
    check_ssl "$domain" || overall_status=1

    echo -e "\n${YELLOW}Diagnostic summary for ${domain}:${NC}"
    if [ $overall_status -eq 0 ]; then
        echo -e "${GREEN}✓ All checks passed${NC}"
    else
        echo -e "${RED}✗ Some issues were found${NC}"
    fi

    exit $overall_status
}

main "$@"
```
