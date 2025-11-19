"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Write a code example that demonstrates how to manage multiple PHP versions for different websites hosted on ProHoster.
Generated: DETERMINISTIC_0c3bfa96da1460d5
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to manage multiple PHP versions for websites hosted on ProHoster
# This script assumes PHP versions are installed and managed using `update-alternatives`.

# Function to set PHP version for a specific website
set_php_version() {
    local website_root=$1
    local php_version=$2

    # Validate inputs
    if [[ -z "$website_root" || -z "$php_version" ]]; then
        echo "Error: Website root and PHP version must be provided."
        exit 1
    fi

    if [[ ! -d "$website_root" ]]; then
        echo "Error: Website root directory does not exist: $website_root"
        exit 1
    fi

    # Check if the PHP version is installed
    if ! update-alternatives --list php | grep -q "php$php_version"; then
        echo "Error: PHP version $php_version is not installed."
        exit 1
    fi

    # Create or update the .htaccess file to set the PHP version
    local htaccess_file="$website_root/.htaccess"
    echo "Updating .htaccess file for $website_root to use PHP $php_version..."

    cat > "$htaccess_file" <<EOL
# .htaccess file to set PHP version
<IfModule mod_php.c>
    AddHandler application/x-httpd-php$php_version .php
</IfModule>
EOL

    echo "PHP version $php_version has been set for $website_root."
}

# Example usage
# Set PHP version for multiple websites
set_php_version "/var/www/site1" "7.4"
set_php_version "/var/www/site2" "8.0"
set_php_version "/var/www/site3" "8.1"

# Note: Adjust the paths and PHP versions as needed.
# Ensure the script is run with appropriate permissions to modify .htaccess files.
```
