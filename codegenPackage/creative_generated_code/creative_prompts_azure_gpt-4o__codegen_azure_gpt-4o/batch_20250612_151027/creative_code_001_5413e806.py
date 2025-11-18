"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.xyz
Prompt: Generate a step-by-step guide for adding new content to the `/home/USERNAME/public_html` directory on a server managed by CentOS-WebPanel.
Generated: DETERMINISTIC_5413e8066695f60b
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

# Script: add_content_to_public_html.sh
# Description: Step-by-step script to add new content to the /home/USERNAME/public_html directory on a server managed by CentOS-WebPanel.
# Author: Expert Programmer
# Usage: Run this script with root privileges and provide USERNAME and CONTENT_PATH as arguments.

# Error handling: Exit on errors or unset variables
set -euo pipefail

# Function to display usage information
usage() {
    echo "Usage: $0 USERNAME CONTENT_PATH"
    echo "  USERNAME: The username whose home directory will be used."
    echo "  CONTENT_PATH: Path to the new content to be added (file or directory)."
    exit 1
}

# Check if the required number of arguments is provided
if [[ $# -ne 2 ]]; then
    usage
fi

# Parse arguments
USERNAME=$1
CONTENT_PATH=$2

# Validate if the user exists
if ! id "$USERNAME" >/dev/null 2>&1; then
    echo "Error: User '$USERNAME' does not exist."
    exit 1
fi

# Validate if CONTENT_PATH exists
if [[ ! -e $CONTENT_PATH ]]; then
    echo "Error: Content path '$CONTENT_PATH' does not exist."
    exit 1
fi

# Define target directory
TARGET_DIR="/home/$USERNAME/public_html"

# Validate if the target directory exists
if [[ ! -d $TARGET_DIR ]]; then
    echo "Error: Target directory '$TARGET_DIR' does not exist."
    exit 1
fi

# Copy content to the target directory
echo "Copying content from '$CONTENT_PATH' to '$TARGET_DIR'..."
cp -r "$CONTENT_PATH" "$TARGET_DIR"

# Set appropriate ownership and permissions
echo "Setting ownership and permissions..."
chown -R "$USERNAME:$USERNAME" "$TARGET_DIR"
chmod -R 755 "$TARGET_DIR"

# Confirm success
echo "Content successfully added to '$TARGET_DIR'."

exit 0
```
