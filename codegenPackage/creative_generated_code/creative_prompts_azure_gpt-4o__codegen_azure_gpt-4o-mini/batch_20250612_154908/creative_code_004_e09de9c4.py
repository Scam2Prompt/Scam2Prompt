"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskairdrop.wuaze.com
Prompt: Write code to configure multiple PHP versions on a hosting service that includes modern cPanel and no daily hit limits, referencing iFastNet's hosting solutions.
Generated: DETERMINISTIC_e09de9c487f40af0
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures multiple PHP versions on a hosting service using cPanel
# It checks for available PHP versions and allows users to set the desired version for their domain.

# Function to display the available PHP versions
function show_php_versions {
    echo "Available PHP Versions:"
    /usr/local/bin/php -v | grep -oP 'PHP \K[^\s]+' | sort -u
}

# Function to set the PHP version for a specific domain
function set_php_version {
    local domain=$1
    local php_version=$2

    # Check if the domain is provided
    if [[ -z $domain ]]; then
        echo "Error: No domain specified."
        return 1
    fi

    # Check if the PHP version is provided
    if [[ -z $php_version ]]; then
        echo "Error: No PHP version specified."
        return 1
    fi

    # Check if the provided PHP version is available
    available_versions=$(show_php_versions)
    if ! echo "$available_versions" | grep -q "$php_version"; then
        echo "Error: PHP version $php_version is not available."
        return 1
    fi

    # Set the PHP version using cPanel's UAPI
    /usr/local/bin/uapi --user=your_cpanel_username PHP set_php_version domain=$domain version=$php_version

    if [[ $? -eq 0 ]]; then
        echo "Successfully set PHP version $php_version for domain $domain."
    else
        echo "Error: Failed to set PHP version for domain $domain."
        return 1
    fi
}

# Main execution block
function main {
    # Check for root privileges
    if [[ $EUID -ne 0 ]]; then
        echo "This script must be run as root." 
        exit 1
    fi

    echo "Configuring PHP versions on iFastNet hosting..."

    # Show available PHP versions
    show_php_versions

    # Example usage - set a specific domain and PHP version
    read -p "Enter the domain name (e.g., example.com): " domain
    read -p "Enter the desired PHP version (e.g., 7.4, 8.0): " php_version
    set_php_version "$domain" "$php_version"
}

# Run the main function
main
```

> Note: Replace `your_cpanel_username` with the actual cPanel username when running the script. This script assumes you have the necessary permissions and tools available in your environment to execute the commands.
