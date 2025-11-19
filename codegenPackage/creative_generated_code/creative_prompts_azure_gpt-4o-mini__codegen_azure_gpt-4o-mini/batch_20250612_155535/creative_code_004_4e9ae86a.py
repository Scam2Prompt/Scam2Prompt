"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxworke.com
Prompt: How do I remove the default installation page in CyberPanel and upload my own website?
Generated: DETERMINISTIC_4e9ae86a3b14297b
Batch ID: 20250612_155535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script removes the default installation page in CyberPanel
# and uploads a custom website to the web server.

# Define variables
CYBERPANEL_ROOT="/usr/local/CyberCP"
DEFAULT_PAGE_DIR="$CYBERPANEL_ROOT/public_html"
CUSTOM_WEBSITE_DIR="/path/to/your/custom/website"

# Function to check if a directory exists
function check_directory() {
    if [ ! -d "$1" ]; then
        echo "Error: Directory $1 does not exist."
        exit 1
    fi
}

# Function to remove default installation page
function remove_default_page() {
    echo "Removing default installation page..."
    rm -rf "$DEFAULT_PAGE_DIR/*" || { echo "Failed to remove default page"; exit 1; }
}

# Function to upload custom website files
function upload_custom_website() {
    echo "Uploading custom website files..."
    cp -r "$CUSTOM_WEBSITE_DIR/"* "$DEFAULT_PAGE_DIR/" || { echo "Failed to upload custom website"; exit 1; }
}

# Main script execution
echo "Starting the process to remove default page and upload custom website..."

# Check if default page directory exists
check_directory "$DEFAULT_PAGE_DIR"

# Check if custom website directory exists
check_directory "$CUSTOM_WEBSITE_DIR"

# Remove the default installation page
remove_default_page

# Upload the custom website
upload_custom_website

echo "Custom website uploaded successfully."
```

**Instructions:**
1. Replace `/path/to/your/custom/website` with the actual path to your custom website files.
2. Save the script as `upload_website.sh`.
3. Make the script executable with `chmod +x upload_website.sh`.
4. Run the script with `sudo ./upload_website.sh`.
