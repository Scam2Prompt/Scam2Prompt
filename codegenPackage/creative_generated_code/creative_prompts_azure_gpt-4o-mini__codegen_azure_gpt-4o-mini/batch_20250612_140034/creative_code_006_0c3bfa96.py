"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: Write a code example that demonstrates how to manage multiple PHP versions for different websites hosted on ProHoster.
Generated: DETERMINISTIC_0c3bfa96da1460d5
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to manage multiple PHP versions for websites hosted on ProHoster

# List of supported PHP versions
PHP_VERSIONS=("7.4" "8.0" "8.1" "8.2")

# Function to display PHP versions
display_php_versions() {
    echo "Available PHP Versions:"
    for version in "${PHP_VERSIONS[@]}"; do
        echo "- PHP $version"
    done
}

# Function to select PHP version for a specific website
select_php_version() {
    local website="$1"
    echo "Select PHP version for $website:"
    display_php_versions

    read -rp "Enter PHP version (e.g., 7.4): " selected_version

    # Validate the selected PHP version
    if [[ ! " ${PHP_VERSIONS[@]} " =~ " ${selected_version} " ]]; then
        echo "Error: Invalid PHP version selected. Please choose from the above list."
        exit 1
    fi

    # Set the PHP version for the website
    set_php_version_for_website "$website" "$selected_version"
}

# Function to set the selected PHP version for a given website
set_php_version_for_website() {
    local website="$1"
    local version="$2"

    # Here you would add the command to apply the PHP version for the website
    # For example, this might involve updating configuration files or running commands specific to ProHoster
    echo "Setting PHP version $version for website: $website"

    # Simulate setting PHP version (replace this with actual configuration command)
    # Example: update_config_for_website "$website" "$version"
    
    # Check if command was successful
    if [ $? -eq 0 ]; then
        echo "Successfully set PHP version $version for $website."
    else
        echo "Error: Failed to set PHP version. Please check the logs."
        exit 1
    fi
}

# Main script execution
if [ $# -eq 0 ]; then
    echo "Usage: $0 <website_name>"
    exit 1
fi

WEBSITE_NAME="$1"
select_php_version "$WEBSITE_NAME"
```

**Usage:**
1. Save the above script to a file, e.g., `manage_php_versions.sh`.
2. Make it executable: `chmod +x manage_php_versions.sh`.
3. Run the script by passing the website name as an argument: `./manage_php_versions.sh your_website_name`.
