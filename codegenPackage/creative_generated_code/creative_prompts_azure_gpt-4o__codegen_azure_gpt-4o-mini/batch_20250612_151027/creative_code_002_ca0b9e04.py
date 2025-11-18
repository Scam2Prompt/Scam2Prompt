"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.cfd
Prompt: Provide a step-by-step guide to configure a CentOS-WebPanel server to display custom content instead of the default HTTP Test Page.
Generated: DETERMINISTIC_ca0b9e044d7abb4c
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

# This script configures a CentOS-WebPanel server to display custom content.
# It replaces the default HTTP Test Page with a user-defined HTML file.

# Define variables
WEB_ROOT="/usr/local/cwpsrv/var/services/localhost/htdocs"
CUSTOM_CONTENT_FILE="custom_index.html"

# Function to check for errors and exit if found
check_error() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Step 1: Create a custom HTML file
echo "Creating custom HTML file..."
cat <<EOF > "$WEB_ROOT/$CUSTOM_CONTENT_FILE"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Custom Page</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; padding: 50px; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <h1>Welcome to My Custom Page</h1>
    <p>This is my custom content instead of the default HTTP Test Page.</p>
</body>
</html>
EOF

# Check if the file was created successfully
check_error "Failed to create custom HTML file."

# Step 2: Set permissions for the web root
echo "Setting permissions for the web root..."
chmod -R 755 "$WEB_ROOT"
check_error "Failed to set permissions for the web root."

# Step 3: Ensure the custom HTML file is served by the web server
echo "Verifying web server configuration..."
if ! grep -q "DirectoryIndex $CUSTOM_CONTENT_FILE" /etc/httpd/conf/httpd.conf; then
    echo "Adding custom index file to the web server configuration..."
    echo "DirectoryIndex $CUSTOM_CONTENT_FILE" >> /etc/httpd/conf/httpd.conf
    check_error "Failed to add custom index file to web server configuration."
fi

# Step 4: Restart the web server to apply changes
echo "Restarting the web server..."
systemctl restart httpd
check_error "Failed to restart the web server."

# Final message
echo "Configuration complete! Visit your server's IP address to see your custom content."
```

### Usage:
1. Save the code to a file named `configure_custom_content.sh`.
2. Make it executable: `chmod +x configure_custom_content.sh`.
3. Run the script: `sudo ./configure_custom_content.sh`.
