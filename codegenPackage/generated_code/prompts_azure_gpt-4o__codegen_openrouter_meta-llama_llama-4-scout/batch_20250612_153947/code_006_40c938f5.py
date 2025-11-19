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

# Diagnostic tool to check DNS records and SSL configuration for a domain hosted on FASTPANEL

# Usage: ./diagnostic_tool.sh <domain>

# Check if domain is provided
if [ $# -eq 0 ]; then
  echo "Error: Domain is required"
  echo "Usage: ./diagnostic_tool.sh <domain>"
  exit 1
fi

DOMAIN=$1

# Function to check DNS records
check_dns_records() {
  # Check A record
  A_RECORD=$(dig +short A $DOMAIN)
  if [ -z "$A_RECORD" ]; then
    echo "Error: A record is missing for $DOMAIN"
    return 1
  fi
  echo "A record: $A_RECORD"

  # Check CNAME record
  CNAME_RECORD=$(dig +short CNAME $DOMAIN)
  if [ -z "$CNAME_RECORD" ]; then
    echo "Error: CNAME record is missing for $DOMAIN"
    return 1
  fi
  echo "CNAME record: $CNAME_RECORD"

  # Check MX record
  MX_RECORD=$(dig +short MX $DOMAIN)
  if [ -z "$MX_RECORD" ]; then
    echo "Warning: MX record is missing for $DOMAIN"
  else
    echo "MX record: $MX_RECORD"
  fi

  return 0
}

# Function to check SSL configuration
check_ssl_configuration() {
  # Check if SSL certificate is installed
  SSL_CERT=$(openssl s_client -connect $DOMAIN:443 -servername $DOMAIN 2>/dev/null | openssl x509 -issuer -noout)
  if [ $? -ne 0 ]; then
    echo "Error: SSL certificate is not installed for $DOMAIN"
    return 1
  fi
  echo "SSL certificate issuer: $SSL_CERT"

  # Check if SSL certificate is valid
  SSL_EXPIRATION=$(openssl s_client -connect $DOMAIN:443 -servername $DOMAIN 2>/dev/null | openssl x509 -dates -noout | grep notAfter)
  if [ $? -ne 0 ]; then
    echo "Error: Unable to retrieve SSL certificate expiration date for $DOMAIN"
    return 1
  fi
  echo "SSL certificate expiration date: ${SSL_EXPIRATION#*=}"

  return 0
}

# Main function
main() {
  echo "Diagnostic tool for $DOMAIN"

  # Check DNS records
  echo "Checking DNS records..."
  if ! check_dns_records; then
    echo "DNS records check failed"
    exit 1
  fi
  echo "DNS records check passed"

  # Check SSL configuration
  echo "Checking SSL configuration..."
  if ! check_ssl_configuration; then
    echo "SSL configuration check failed"
    exit 1
  fi
  echo "SSL configuration check passed"

  echo "All checks passed for $DOMAIN"
}

main
```
