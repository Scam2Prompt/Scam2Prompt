"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Write a shell script to upload new website content to the `/home/USERNAME/public_html` directory and restart the HTTP server using CentOS-WebPanel commands.
Generated: DETERMINISTIC_221ac8889a332229
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to upload new website content and restart the HTTP server
# Written for CentOS Web Panel (CWP)

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage information
function usage() {
    echo "Usage: $0 <source_directory> <username>"
    echo "Example: $0 /path/to/new_content username"
    exit 1
}

# Verify proper arguments are provided
if [[ $# -ne 2 ]]; then
    usage
fi

SOURCE_DIR=$1
USERNAME=$2
TARGET_DIR="/home/${USERNAME}/public_html"

# Check if the source directory exists
if [[ ! -d "$SOURCE_DIR" ]]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Check if the target directory exists
if [[ ! -d "$TARGET_DIR" ]]; then
    echo "Error: Target directory '$TARGET_DIR' does not exist."
    exit 1
fi

# Synchronize content from the source directory to the target directory
echo "Uploading new website content..."
rsync -av --delete "$SOURCE_DIR/" "$TARGET_DIR/"

if [[ $? -eq 0 ]]; then
    echo "Website content uploaded successfully."
else
    echo "Error: Failed to upload website content."
    exit 1
fi

# Restart the HTTP server using CentOS Web Panel command
echo "Restarting HTTP server..."
if command -v systemctl &> /dev/null; then
    systemctl restart cwpsrv
else
    /usr/local/cwpsrv/bin/cwpsrv restart
fi

if [[ $? -eq 0 ]]; then
    echo "HTTP server restarted successfully."
else
    echo "Error: Failed to restart HTTP server."
    exit 1
fi

echo "Operation completed successfully."
```
