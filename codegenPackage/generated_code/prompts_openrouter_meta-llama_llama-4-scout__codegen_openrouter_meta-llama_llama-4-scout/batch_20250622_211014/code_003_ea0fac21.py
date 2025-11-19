"""
Generated Code Metadata:
========================
Original URL: https://eth-gas.in
Prompt: Given a list of domain names, generate a Bash script to check which ones have their A record pointed to a server and suggest fixes for common issues.
Generated: DETERMINISTIC_ea0fac21dc11d96e
Batch ID: 20250622_211014
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Function to check A record for a domain
check_a_record() {
  local domain=$1
  local a_record=$(dig +short $domain A)

  if [ $? -eq 0 ] && [ -n "$a_record" ]; then
    echo "$domain has A record: $a_record"
  else
    echo "$domain does not have A record or DNS lookup failed"
  fi
}

# Function to suggest fixes for common issues
suggest_fixes() {
  local domain=$1
  local issue=$2

  case $issue in
    "no_a_record")
      echo "1. Check if the domain has a valid A record configured in DNS settings."
      echo "2. Ensure the DNS server is authoritative for the domain."
      ;;
    "dns_lookup_failed")
      echo "1. Check if the DNS server is reachable."
      echo "2. Ensure there are no firewall rules blocking DNS lookups."
      ;;
  esac
}

# Main function to check domains and suggest fixes
check_domains() {
  local domains=("$@")

  for domain in "${domains[@]}"; do
    a_record=$(dig +short $domain A)

    if [ $? -eq 0 ] && [ -n "$a_record" ]; then
      echo "$domain has A record: $a_record"
    else
      echo "$domain does not have A record or DNS lookup failed"

      if [ -z "$a_record" ]; then
        suggest_fixes $domain "no_a_record"
      else
        suggest_fixes $domain "dns_lookup_failed"
      fi
    fi
    echo
  done
}

# Example usage
domains=("example.com" "nonexistentdomain.com" "invalidrecord.com")

check_domains "${domains[@]}"
```
