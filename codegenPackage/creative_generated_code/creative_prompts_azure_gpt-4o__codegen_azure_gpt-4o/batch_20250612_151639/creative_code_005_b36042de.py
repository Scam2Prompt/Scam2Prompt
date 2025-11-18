"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syneoshealthls.com
Prompt: Write a shell script to automate the process of creating subscriptions for domains in Plesk, following the procedure mentioned on Media Temple's server page.
Generated: DETERMINISTIC_b36042de2e0181c1
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the creation of subscriptions for domains in Plesk
# This script requires the Plesk CLI (`plesk bin`) and proper permissions

# Exit immediately if a command exits with a non-zero status
set -e

# Check if user has provided domain name and subscription details
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <domain_name> <username> <password>"
    exit 1
fi

# Variables
DOMAIN_NAME="$1"
USERNAME="$2"
PASSWORD="$3"

# Function to create a subscription in Plesk
create_subscription() {
    local domain=$1
    local user=$2
    local pass=$3
    
    echo "Creating subscription for domain: $domain..."

    # Create the subscription
    plesk bin subscription --create "$domain" \
        -owner admin \
        -service-plan "Default" \
        -login "$user" \
        -passwd "$pass"

    if [ $? -eq 0 ]; then
        echo "Subscription created successfully for: $domain"
    else
        echo "Failed to create subscription for: $domain"
        exit 1
    fi
}

# Execute the function
create_subscription "$DOMAIN_NAME" "$USERNAME" "$PASSWORD"

# End of script
```
