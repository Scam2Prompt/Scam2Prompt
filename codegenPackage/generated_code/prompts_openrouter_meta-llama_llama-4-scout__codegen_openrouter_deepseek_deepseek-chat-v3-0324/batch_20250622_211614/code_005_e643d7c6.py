"""
Generated Code Metadata:
========================
Original URL: https://hopexchange.online
Prompt: Design a simple web server setup using Plesk for hosting multiple websites.
Generated: DETERMINISTIC_e643d7c67adfb790
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Simple Plesk Web Server Setup Script
# This script automates the setup of multiple websites on a Plesk server

# Ensure script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Check if Plesk is installed
if ! command -v plesk &> /dev/null; then
    echo "Plesk is not installed. Please install Plesk first."
    exit 1
fi

# Function to create a new website
create_website() {
    local domain=$1
    local php_version=$2
    local owner=$3
    
    echo "Creating website: $domain"
    
    # Create subscription
    plesk bin subscription --create "$domain" \
        -owner "$owner" \
        -service-plan "Default Domain" \
        -ip "shared" \
        -login "$owner" \
        -passwd "$(openssl rand -base64 12)"
    
    # Set PHP version
    plesk bin php_handler --set -domain "$domain" -id "$php_version"
    
    # Enable SSL
    plesk bin extension --exec letsencrypt cli.php -m "admin@$domain" -d "$domain" -www
    
    echo "Website $domain created successfully"
}

# Main execution
echo "Plesk Multi-Website Setup"
echo "-------------------------"

# Read input file (format: domain php_version owner)
input_file="websites_to_create.txt"

if [ ! -f "$input_file" ]; then
    echo "Input file $input_file not found"
    exit 1
fi

while IFS= read -r line || [[ -n "$line" ]]; do
    # Skip comments and empty lines
    [[ "$line" =~ ^#.*$ || -z "$line" ]] && continue
    
    # Parse line
    domain=$(echo "$line" | awk '{print $1}')
    php_version=$(echo "$line" | awk '{print $2}')
    owner=$(echo "$line" | awk '{print $3}')
    
    # Validate input
    if [ -z "$domain" ] || [ -z "$php_version" ] || [ -z "$owner" ]; then
        echo "Invalid line format: $line"
        continue
    fi
    
    # Create website
    create_website "$domain" "$php_version" "$owner"
    
done < "$input_file"

echo "Setup completed"
```
