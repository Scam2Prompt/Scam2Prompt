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

# Bash script to replace the default HTTP test page with custom content in the /public_html directory using CentOS-WebPanel

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
PUBLIC_HTML_DIR="/home/$(whoami)/public_html"
BACKUP_FILE="$PUBLIC_HTML_DIR/index.html.bak"
DEFAULT_PAGE="$PUBLIC_HTML_DIR/index.html"
CUSTOM_PAGE_CONTENT="<html>
<head>
    <title>My Custom Page</title>
</head>
<body>
    <h1>Welcome to My Custom Page!</h1>
    <p>This is my custom content replacing the default HTTP test page.</p>
</body>
</html>"

# Check if the /public_html directory exists
if [ ! -d "$PUBLIC_HTML_DIR" ]; then
    echo "Error: Directory $PUBLIC_HTML_DIR does not exist."
    exit 1
fi

# Check if the default page exists, and back it up if present
if [ -f "$DEFAULT_PAGE" ]; then
    echo "Backing up existing default page..."
    cp "$DEFAULT_PAGE" "$BACKUP_FILE"
    echo "Backup created: $BACKUP_FILE"
fi

# Replace the default page with custom content
echo "Writing custom content to $DEFAULT_PAGE..."
echo "$CUSTOM_PAGE_CONTENT" > "$DEFAULT_PAGE"

# Verify that the operation was successful
if [ $? -eq 0 ]; then
    echo "Custom page successfully created at $DEFAULT_PAGE"
else
    echo "Error: Failed to create custom page."
    exit 1
fi

# Set appropriate permissions for the /public_html directory
echo "Setting permissions for $PUBLIC_HTML_DIR..."
chmod -R 755 "$PUBLIC_HTML_DIR"
if [ $? -eq 0 ]; then
    echo "Permissions successfully set for $PUBLIC_HTML_DIR"
else
    echo "Error: Failed to set permissions."
    exit 1
fi

echo "Script completed successfully."
```
