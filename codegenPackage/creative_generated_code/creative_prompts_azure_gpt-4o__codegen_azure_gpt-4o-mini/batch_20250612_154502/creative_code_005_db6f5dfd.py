"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glveaways-metamasks-lo.html-5.me
Prompt: Generate a script to automate the setup of multiple PHP versions on a hosting platform with cPanel, similar to iFastNet hosting.
Generated: DETERMINISTIC_db6f5dfdbbaff105
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the setup of multiple PHP versions on a cPanel hosting platform.

# Exit immediately if a command exits with a non-zero status
set -e

# Define an array of PHP versions to install
PHP_VERSIONS=("7.4" "8.0" "8.1" "8.2")

# Function to install PHP versions
install_php_version() {
    local version=$1
    echo "Starting installation of PHP version $version..."

    # Check if the PHP version is already installed
    if [ -d "/opt/cpanel/ea-php$version" ]; then
        echo "PHP version $version is already installed. Skipping..."
        return
    fi

    # Install the specified PHP version
    /scripts/phpextensionmgr install -y ea-php$version

    echo "PHP version $version installed successfully."
}

# Function to configure PHP versions
configure_php_version() {
    local version=$1
    echo "Configuring PHP version $version..."

    # Set PHP version for the account (replace with the actual account's username)
    local username="username_here"
    /usr/local/bin/php -d /opt/cpanel/ea-php$version -m

    echo "PHP version $version configured successfully for user $username."
}

# Main script execution
echo "Beginning PHP version installation and configuration..."

# Loop through each PHP version and install/configure it
for version in "${PHP_VERSIONS[@]}"; do
    install_php_version "$version"
    configure_php_version "$version"
done

echo "All specified PHP versions have been successfully installed and configured."
exit 0
```
