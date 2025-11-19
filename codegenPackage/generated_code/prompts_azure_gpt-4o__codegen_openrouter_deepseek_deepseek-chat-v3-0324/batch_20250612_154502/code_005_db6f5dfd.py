"""
Generated Code Metadata:
========================
Original URL: https://glveaways-metamasks-lo.html-5.me
Prompt: Generate a script to automate the setup of multiple PHP versions on a hosting platform with cPanel, similar to iFastNet hosting.
Generated: DETERMINISTIC_db6f5dfdbbaff105
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to automate the setup of multiple PHP versions on a cPanel hosting platform
# Ensure this script is run with root privileges

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Please use sudo or switch to root user."
    exit 1
fi

# Define PHP versions to install
PHP_VERSIONS=("7.4" "8.0" "8.1" "8.2")

# Function to install a specific PHP version
install_php_version() {
    local version=$1
    echo "Installing PHP ${version}..."
    
    # Check if the version is already installed
    if /usr/local/cpanel/bin/rebuild_phpconf --current | grep -q "php-${version}"; then
        echo "PHP ${version} is already installed. Skipping..."
        return 0
    fi
    
    # Install PHP version using EasyApache4
    /usr/local/cpanel/bin/whmapi1 install_php_version version=$version
    
    # Check if installation was successful
    if [ $? -ne 0 ]; then
        echo "Failed to install PHP ${version}."
        return 1
    fi
    
    echo "Successfully installed PHP ${version}."
    return 0
}

# Function to set default PHP version
set_default_php_version() {
    local version=$1
    echo "Setting PHP ${version} as default..."
    
    /usr/local/cpanel/bin/whmapi1 php_set_default_version version=$version
    
    if [ $? -ne 0 ]; then
        echo "Failed to set PHP ${version} as default."
        return 1
    fi
    
    echo "Successfully set PHP ${version} as default."
    return 0
}

# Function to enable PHP version for a user
enable_php_for_user() {
    local version=$1
    local username=$2
    
    echo "Enabling PHP ${version} for user ${username}..."
    
    /usr/local/cpanel/bin/whmapi1 php_set_user_version user=$username version=$version
    
    if [ $? -ne 0 ]; then
        echo "Failed to enable PHP ${version} for user ${username}."
        return 1
    fi
    
    echo "Successfully enabled PHP ${version} for user ${username}."
    return 0
}

# Main execution
main() {
    # Update EasyApache4 first
    echo "Updating EasyApache4..."
    /usr/local/cpanel/bin/whmapi1 update_ea4
    
    # Install all specified PHP versions
    for version in "${PHP_VERSIONS[@]}"; do
        install_php_version "$version"
    done
    
    # Set the latest PHP version as default
    latest_version=${PHP_VERSIONS[-1]}
    set_default_php_version "$latest_version"
    
    # Optional: Enable specific PHP version for all users
    # Uncomment and modify as needed
    # for user in $(ls -A /var/cpanel/users/); do
    #     enable_php_for_user "7.4" "$user"
    # done
    
    echo "PHP setup completed successfully."
}

# Execute main function
main
```
