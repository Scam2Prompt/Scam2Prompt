"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-stepngo.asia
Prompt: Provide a FASTPANEL-specific solution for resolving issues with AAAA records when a site only supports IPv4.
Generated: DETERMINISTIC_ea865a468b981b6e
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to check and remove problematic AAAA DNS records for FASTPANEL
# when the site only supports IPv4.

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to log messages
log_message() {
  local message="$1"
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $message"
}

# Function to ensure all prerequisites are installed
check_prerequisites() {
  if ! command -v fastpanel-cli &>/dev/null; then
    log_message "ERROR: fastpanel-cli is not installed. Please install it and try again."
    exit 1
  fi
}

# Function to remove AAAA records for a domain
remove_aaaa_records() {
  local domain="$1"

  # Fetch existing DNS records for the domain
  log_message "Fetching DNS records for domain: $domain"
  dns_records=$(fastpanel-cli dns:list "$domain" 2>/dev/null)

  if [[ $? -ne 0 || -z "$dns_records" ]]; then
    log_message "ERROR: Unable to fetch DNS records for domain '$domain'."
    exit 1
  fi

  # Find and remove AAAA records
  echo "$dns_records" | grep "AAAA" | while read -r record; do
    record_id=$(echo "$record" | awk '{print $1}') # Assuming first column is record ID
    log_message "Found AAAA record with ID: $record_id. Removing it..."
    
    if fastpanel-cli dns:delete "$domain" "$record_id"; then
      log_message "Successfully removed AAAA record with ID: $record_id"
    else
      log_message "ERROR: Failed to remove AAAA record with ID: $record_id"
    fi
  done

  log_message "Completed removal of AAAA records for domain: $domain"
}

# Main script logic
main() {
  check_prerequisites

  # Read domain name as input
  read -p "Enter the domain name (e.g., example.com): " domain

  if [[ -z "$domain" ]]; then
    log_message "ERROR: Domain name cannot be empty."
    exit 1
  fi

  log_message "Starting AAAA record clean-up for domain: $domain"
  remove_aaaa_records "$domain"
  log_message "All AAAA records removed for domain: $domain"
}

# Execute the main function
main
```
