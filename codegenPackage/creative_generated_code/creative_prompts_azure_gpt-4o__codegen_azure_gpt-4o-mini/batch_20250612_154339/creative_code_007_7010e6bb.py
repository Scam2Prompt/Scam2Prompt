"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.online
Prompt: Explain how Plesk's hosting panel can be used to manage both DNS and mail services, and provide an example script for each.
Generated: DETERMINISTIC_7010e6bbbdb501de
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Example script to manage DNS records using Plesk's CLI

# Function to add a DNS record
add_dns_record() {
    local domain=$1
    local type=$2
    local host=$3
    local value=$4
    local ttl=$5

    # Check if necessary parameters are provided
    if [ -z "$domain" ] || [ -z "$type" ] || [ -z "$host" ] || [ -z "$value" ]; then
        echo "Usage: $0 <domain> <record_type> <host> <value> [ttl]"
        exit 1
    fi

    # Set default TTL if not provided
    ttl=${ttl:-3600}

    # Add the DNS record using Plesk's CLI
    /usr/local/psa/bin/dns --add "$domain" --type "$type" --host "$host" --value "$value" --ttl "$ttl"

    # Check if the command succeeded
    if [ $? -eq 0 ]; then
        echo "DNS record added successfully."
    else
        echo "Failed to add DNS record."
        exit 1
    fi
}

# Example usage
# add_dns_record "example.com" "A" "www" "192.0.2.1" 3600


# Example script to manage mail services using Plesk's CLI

# Function to create a mail account
create_mail_account() {
    local domain=$1
    local email=$2
    local password=$3

    # Check if necessary parameters are provided
    if [ -z "$domain" ] || [ -z "$email" ] || [ -z "$password" ]; then
        echo "Usage: $0 <domain> <email> <password>"
        exit 1
    fi

    # Create the mail account using Plesk's CLI
    /usr/local/psa/bin/mail --add "$email@$domain" -passwd "$password" -domain "$domain"

    # Check if the command succeeded
    if [ $? -eq 0 ]; then
        echo "Mail account created successfully."
    else
        echo "Failed to create mail account."
        exit 1
    fi
}

# Example usage
# create_mail_account "example.com" "user" "securepassword123"
```
