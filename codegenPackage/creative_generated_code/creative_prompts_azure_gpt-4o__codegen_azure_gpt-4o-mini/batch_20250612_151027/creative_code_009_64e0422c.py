"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.cfd
Prompt: Write a script to replace the default HTTP Test Page with a custom HTML file on a CentOS-WebPanel-powered server.
Generated: DETERMINISTIC_64e0422c943e3493
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to replace the default HTTP Test Page with a custom HTML file on a CentOS-WebPanel-powered server

# Define the paths
DEFAULT_HTTP_PAGE="/usr/local/cwpsrv/var/services/localhost/public_html/index.html"
CUSTOM_HTML_FILE="/path/to/your/custom.html"

# Function to check if a file exists
check_file_exists() {
    if [[ ! -f "$1" ]]; then
        echo "Error: File $1 does not exist."
        exit 1
    fi
}

# Function to back up the default HTTP page
backup_default_page() {
    if [[ -f "$DEFAULT_HTTP_PAGE" ]]; then
        cp "$DEFAULT_HTTP_PAGE" "${DEFAULT_HTTP_PAGE}.bak"
        echo "Backup of the default HTTP page created at ${DEFAULT_HTTP_PAGE}.bak"
    else
        echo "Warning: Default HTTP page not found. No backup created."
    fi
}

# Function to replace the default HTTP page
replace_http_page() {
    cp "$CUSTOM_HTML_FILE" "$DEFAULT_HTTP_PAGE"
    if [[ $? -eq 0 ]]; then
        echo "Successfully replaced the default HTTP page with $CUSTOM_HTML_FILE"
    else
        echo "Error: Failed to replace the default HTTP page."
        exit 1
    fi
}

# Main script execution
check_file_exists "$CUSTOM_HTML_FILE"
backup_default_page
replace_http_page

echo "Operation completed successfully."
exit 0
```

**Note:** Replace `/path/to/your/custom.html` with the actual path to your custom HTML file before running the script. Make sure to run this script with proper permissions (e.g., as a user with write access to the web server files).
