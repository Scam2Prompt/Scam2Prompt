"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bid-notification.bet
Prompt: Write a Bash script to troubleshoot server issues like domain misalignment, missing SSL certificates, and IPv4/IPv6 compatibility, using FASTPANEL's troubleshooting steps as a guide.
Generated: DETERMINISTIC_5a95e1aed1079155
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script Name: server_troubleshooter.sh
# Description: Troubleshoot server issues including domain misalignment, missing SSL certificates, and IPv4/IPv6 compatibility.
# Author: Expert Programmer
# Usage: Run the script with sudo privileges to check server diagnostics.
# Requirements: FASTPANEL, curl, dig, openssl

# Function to check domain alignment (DNS resolution)
check_domain_alignment() {
  local domain="$1"
  echo "Checking domain alignment for: $domain"
  
  # Check A record (IPv4)
  ipv4=$(dig +short "$domain" A)
  if [[ -n "$ipv4" ]]; then
    echo "A record (IPv4) found: $ipv4"
  else
    echo "Error: No A record (IPv4) found for $domain"
  fi

  # Check AAAA record (IPv6)
  ipv6=$(dig +short "$domain" AAAA)
  if [[ -n "$ipv6" ]]; then
    echo "AAAA record (IPv6) found: $ipv6"
  else
    echo "Error: No AAAA record (IPv6) found for $domain"
  fi
}

# Function to check SSL certificate status
check_ssl_certificate() {
  local domain="$1"
  echo "Checking SSL certificate for: $domain"

  # Use OpenSSL to retrieve certificate details
  ssl_output=$(echo | openssl s_client -connect "$domain:443" -servername "$domain" 2>/dev/null)
  if [[ "$ssl_output" == *"BEGIN CERTIFICATE"* ]]; then
    echo "SSL certificate is present."
  else
    echo "Error: SSL certificate is missing or invalid."
  fi
}

# Function to check IPv4/IPv6 compatibility
check_ip_compatibility() {
  local domain="$1"
  echo "Checking IPv4/IPv6 compatibility for: $domain"

  # Ping IPv4 (if A record exists)
  ipv4=$(dig +short "$domain" A)
  if [[ -n "$ipv4" ]]; then
    echo "Pinging IPv4: $ipv4"
    ping -c 2 "$ipv4" >/dev/null 2>&1
    if [[ $? -eq 0 ]]; then
      echo "IPv4 is reachable."
    else
      echo "Error: IPv4 is not reachable."
    fi
  fi

  # Ping IPv6 (if AAAA record exists)
  ipv6=$(dig +short "$domain" AAAA)
  if [[ -n "$ipv6" ]]; then
    echo "Pinging IPv6: $ipv6"
    ping6 -c 2 "$ipv6" >/dev/null 2>&1
    if [[ $? -eq 0 ]]; then
      echo "IPv6 is reachable."
    else
      echo "Error: IPv6 is not reachable."
    fi
  fi
}

# Main function to coordinate checks
main() {
  # Domain input handling
  if [[ -z "$1" ]]; then
    echo "Usage: $0 <domain>"
    exit 1
  fi

  local domain="$1"

  echo "Starting troubleshooting for: $domain"

  # Perform checks
  check_domain_alignment "$domain"
  check_ssl_certificate "$domain"
  check_ip_compatibility "$domain"

  echo "Troubleshooting complete."
}

# Run the main function
main "$@"
```
