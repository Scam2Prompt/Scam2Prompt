"""
Generated Code Metadata:
========================
Original URL: https://saniva.com.sg
Prompt: How can I troubleshoot and resolve common issues with directory indexing and file serving on a LiteSpeed Web Server, specifically for a site like saniva.com.sg?
Generated: DETERMINISTIC_039ba1afb90fb221
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to troubleshoot and resolve common issues with directory indexing and file serving on a LiteSpeed Web Server

# Function to check if LiteSpeed is running
check_litespeed_status() {
    echo "Checking LiteSpeed Web Server status..."
    if systemctl is-active --quiet lsws; then
        echo "LiteSpeed is running."
    else
        echo "LiteSpeed is not running. Attempting to start..."
        systemctl start lsws
        if systemctl is-active --quiet lsws; then
            echo "LiteSpeed started successfully."
        else
            echo "Failed to start LiteSpeed. Please check the logs."
            exit 1
        fi
    fi
}

# Function to check directory indexing settings
check_directory_indexing() {
    echo "Checking directory indexing settings..."
    local config_file="/usr/local/lsws/conf/httpd_config.conf"
    
    if grep -q "IndexOptions" "$config_file"; then
        echo "Directory indexing is enabled."
    else
        echo "Directory indexing is disabled. Enabling it..."
        echo "IndexOptions +Indexes" >> "$config_file"
        echo "Directory indexing has been enabled."
        # Reload LiteSpeed to apply changes
        systemctl reload lsws
    fi
}

# Function to check file permissions
check_file_permissions() {
    echo "Checking file permissions for the web root..."
    local web_root="/var/www/html/saniva.com.sg"
    
    if [ -d "$web_root" ]; then
        echo "Web root directory found."
        # Check permissions
        if [ "$(stat -c '%a' "$web_root")" -ne 755 ]; then
            echo "Correcting permissions for the web root directory..."
            chmod 755 "$web_root"
            echo "Permissions corrected to 755."
        else
            echo "Permissions are correctly set to 755."
        fi
    else
        echo "Web root directory not found. Please check the path."
        exit 1
    fi
}

# Function to check LiteSpeed error logs
check_error_logs() {
    echo "Checking LiteSpeed error logs for issues..."
    local log_file="/usr/local/lsws/logs/error.log"
    
    if [ -f "$log_file" ]; then
        echo "Last 10 lines of the error log:"
        tail -n 10 "$log_file"
    else
        echo "Error log file not found. Please check the installation."
        exit 1
    fi
}

# Main script execution
main() {
    check_litespeed_status
    check_directory_indexing
    check_file_permissions
    check_error_logs
}

# Execute the main function
main
```
