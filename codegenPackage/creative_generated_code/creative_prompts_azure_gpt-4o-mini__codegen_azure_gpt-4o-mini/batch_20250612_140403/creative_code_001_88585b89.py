"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev-metamask.wuaze.com
Prompt: Write a code snippet demonstrating how to configure multiple versions of PHP on iFastNet hosting for a multi-site setup.
Generated: DETERMINISTIC_88585b897a77e6f8
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure multiple versions of PHP on iFastNet hosting for a multi-site setup.

# Define the PHP versions to be installed
PHP_VERSIONS=("7.4" "8.0" "8.1")

# Define the base directory for the web root
WEB_ROOT="/home/username/public_html"

# Define the configuration file path
CONFIG_FILE="$WEB_ROOT/.user.ini"

# Function to install PHP versions
install_php_version() {
    local version=$1
    echo "Installing PHP version $version..."

    # Command to install PHP version
    # (This is a placeholder; replace with actual installation command for iFastNet)
    if command -v php"$version" &>/dev/null; then
        echo "PHP version $version is already installed."
    else
        # Placeholder for actual installation command
        echo "Command to install PHP $version goes here"
        # Example: apt-get install php$version -y
        if [ $? -ne 0 ]; then
            echo "Error installing PHP $version"
            exit 1
        fi
    fi
}

# Function to configure PHP version for a specific site
configure_php_for_site() {
    local site_path=$1
    local version=$2
    echo "Configuring PHP version $version for site at $site_path..."

    # Create/overwrite the .user.ini file to set the PHP version
    echo "php_version=$version" > "$site_path/.user.ini"

    if [ $? -ne 0 ]; then
        echo "Error writing to .user.ini for $site_path"
        exit 1
    fi

    echo "Successfully configured PHP version $version for site at $site_path"
}

# Loop through each PHP version and install it
for version in "${PHP_VERSIONS[@]}"; do
    install_php_version "$version"
done

# Configure each site with the desired PHP version
# You can define your sites and their respective PHP versions here
declare -A SITES
SITES["site1.com"]="7.4"
SITES["site2.com"]="8.0"
SITES["site3.com"]="8.1"

for site in "${!SITES[@]}"; do
    site_path="$WEB_ROOT/$site"
    php_version="${SITES[$site]}"
    configure_php_for_site "$site_path" "$php_version"
done

echo "PHP configuration for multi-site setup completed successfully."
```
