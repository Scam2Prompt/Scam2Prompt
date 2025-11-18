"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslatrust.net
Prompt: Provide a step-by-step guide to configure a CentOS-WebPanel server to replace the default HTTP test page with custom content in the `/home/USERNAME/public_html` directory.
Generated: DETERMINISTIC_e2b2a57a66572755
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# ================================
# Script to configure CentOS-WebPanel server
# Replace the default HTTP test page with custom content
# in the /home/USERNAME/public_html directory.
# ================================

# Ensure the script is executed as root
if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root" >&2
  exit 1
fi

# Set variables
USERNAME="your_username" # Replace with the actual username.
CUSTOM_CONTENT="index.html" # Replace with the filename of your custom content file.
CUSTOM_CONTENT_PATH="/path/to/$CUSTOM_CONTENT" # Replace with the full path to your custom content file.
PUBLIC_HTML_DIR="/home/$USERNAME/public_html"

# Step 1: Check if the username exists on the system
if ! id -u "$USERNAME" >/dev/null 2>&1; then
  echo "Error: Username '$USERNAME' does not exist on the system" >&2
  exit 1
fi

# Step 2: Verify that the public_html directory exists
if [[ ! -d "$PUBLIC_HTML_DIR" ]]; then
  echo "Error: Directory $PUBLIC_HTML_DIR does not exist" >&2
  exit 1
fi

# Step 3: Verify that the custom content file exists
if [[ ! -f "$CUSTOM_CONTENT_PATH" ]]; then
  echo "Error: File $CUSTOM_CONTENT_PATH does not exist" >&2
  exit 1
fi

# Step 4: Backup the existing index.html (if it exists)
if [[ -f "$PUBLIC_HTML_DIR/index.html" ]]; then
  echo "Backing up existing index.html to index.html.bak"
  cp "$PUBLIC_HTML_DIR/index.html" "$PUBLIC_HTML_DIR/index.html.bak"
fi

# Step 5: Copy the custom content to the public_html directory
echo "Deploying custom content to $PUBLIC_HTML_DIR"
cp "$CUSTOM_CONTENT_PATH" "$PUBLIC_HTML_DIR/index.html"

# Step 6: Set correct permissions for the public_html directory
echo "Setting correct permissions for $PUBLIC_HTML_DIR"
chown -R "$USERNAME:$USERNAME" "$PUBLIC_HTML_DIR"
chmod 755 "$PUBLIC_HTML_DIR"
chmod 644 "$PUBLIC_HTML_DIR/index.html"

# Step 7: Restart the web server to apply changes
echo "Restarting the web server..."
systemctl restart httpd

# Step 8: Confirm success
echo "Custom content has been successfully deployed to $PUBLIC_HTML_DIR"

# Exit the script
exit 0
```
