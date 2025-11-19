"""
Generated Code Metadata:
========================
Original URL: https://uzapa.com
Prompt: How to troubleshoot and fix a directory listing issue on a LiteSpeed Web Server?
Generated: DETERMINISTIC_75571bae5addf31f
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to troubleshoot and fix directory listing issues on a LiteSpeed Web Server

# Function to check if LiteSpeed is running
check_litespeed_status() {
    if systemctl is-active --quiet lsws; then
        echo "LiteSpeed Web Server is running."
    else
        echo "LiteSpeed Web Server is not running. Attempting to start..."
        systemctl start lsws
        if systemctl is-active --quiet lsws; then
            echo "LiteSpeed Web Server started successfully."
        else
            echo "Failed to start LiteSpeed Web Server. Please check the logs."
            exit 1
        fi
    fi
}

# Function to check directory listing configuration
check_directory_listing() {
    local dir="$1"
    local config_file="/usr/local/lsws/conf/httpd_config.conf"

    # Check if directory listing is enabled in the configuration
    if grep -q "enable_dir_listing" "$config_file"; then
        echo "Directory listing is configured in $config_file."
    else
        echo "Directory listing is not configured. Adding configuration..."
        echo "enable_dir_listing 1" >> "$config_file"
        echo "Directory listing enabled for $dir."
    fi
}

# Function to check file permissions
check_permissions() {
    local dir="$1"
    
    # Check if the directory exists
    if [ ! -d "$dir" ]; then
        echo "Directory $dir does not exist. Please check the path."
        exit 1
    fi

    # Check permissions
    if [ ! -r "$dir" ]; then
        echo "Directory $dir is not readable. Attempting to change permissions..."
        chmod +r "$dir"
        if [ $? -eq 0 ]; then
            echo "Permissions changed successfully for $dir."
        else
            echo "Failed to change permissions for $dir. Please check your user privileges."
            exit 1
        fi
    else
        echo "Directory $dir is readable."
    fi
}

# Main script execution
main() {
    local target_directory="$1"

    # Check if the target directory is provided
    if [ -z "$target_directory" ]; then
        echo "Usage: $0 <target_directory>"
        exit 1
    fi

    # Check LiteSpeed status
    check_litespeed_status

    # Check directory listing configuration
    check_directory_listing "$target_directory"

    # Check directory permissions
    check_permissions "$target_directory"

    echo "Troubleshooting completed for directory: $target_directory"
}

# Execute the main function with the provided arguments
main "$@"
```
