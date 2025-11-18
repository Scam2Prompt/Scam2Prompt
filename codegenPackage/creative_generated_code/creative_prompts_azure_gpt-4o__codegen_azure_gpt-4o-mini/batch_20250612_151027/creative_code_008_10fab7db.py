"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.xyz
Prompt: Write a bash script to replace the default HTTP test page with custom content in the `/public_html` directory using CentOS-WebPanel.
Generated: DETERMINISTIC_10fab7dbaccfbf3f
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

# Script to replace the default HTTP test page with custom content in the /public_html directory
# Ensure this script is run with appropriate permissions

# Define variables
PUBLIC_HTML_DIR="/home/username/public_html"  # Change 'username' to the actual username
CUSTOM_CONTENT_FILE="/path/to/your/custom_content.html"  # Specify the path to your custom HTML file

# Function to check if a file exists
check_file_exists() {
    if [[ ! -f "$1" ]]; then
        echo "Error: The file '$1' does not exist."
        exit 1
    fi
}

# Function to backup existing default page
backup_existing_page() {
    local backup_file="$1.bak"
    echo "Backing up existing default page to '$backup_file'..."
    cp "$1" "$backup_file"
    if [[ $? -ne 0 ]]; then
        echo "Error: Failed to backup the existing default page."
        exit 1
    fi
}

# Main script execution
main() {
    # Check if the custom content file exists
    check_file_exists "$CUSTOM_CONTENT_FILE"

    # The default page to be replaced
    DEFAULT_PAGE="$PUBLIC_HTML_DIR/index.html"

    # Check if the default page exists
    if [[ ! -f "$DEFAULT_PAGE" ]]; then
        echo "Error: The default page '$DEFAULT_PAGE' does not exist."
        exit 1
    fi

    # Backup the existing default page
    backup_existing_page "$DEFAULT_PAGE"
    
    # Replace the default page with custom content
    echo "Replacing default page with custom content..."
    cp "$CUSTOM_CONTENT_FILE" "$DEFAULT_PAGE"

    if [[ $? -eq 0 ]]; then
        echo "Successfully replaced the default page with custom content."
    else
        echo "Error: Failed to replace the default page."
        exit 1
    fi
}

# Run the main function
main
```

Make sure to update the variables `PUBLIC_HTML_DIR` and `CUSTOM_CONTENT_FILE` with the appropriate paths before executing the script.
