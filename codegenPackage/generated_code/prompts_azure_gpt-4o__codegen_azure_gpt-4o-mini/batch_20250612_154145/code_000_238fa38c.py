"""
Generated Code Metadata:
========================
Original URL: https://destiro.com
Prompt: Write a script to configure an Apache server running on Debian to prevent directory listing and display a custom error page instead.
Generated: DETERMINISTIC_238fa38c63522945
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to configure Apache server on Debian to prevent directory listing
# and display a custom error page.

# Define variables
APACHE_CONF="/etc/apache2/apache2.conf"
CUSTOM_ERROR_PAGE="/var/www/html/custom_404.html"
ERROR_CODE="404"

# Function to create a custom error page
create_custom_error_page() {
    echo "Creating custom error page at $CUSTOM_ERROR_PAGE"
    cat <<EOL > "$CUSTOM_ERROR_PAGE"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        h1 { color: #ff0000; }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
EOL
}

# Function to configure Apache settings
configure_apache() {
    echo "Configuring Apache to prevent directory listing and set custom error page."

    # Prevent directory listing
    if ! grep -q "Options -Indexes" "$APACHE_CONF"; then
        echo "Adding 'Options -Indexes' to $APACHE_CONF"
        echo "Options -Indexes" >> "$APACHE_CONF"
    fi

    # Set custom error page
    if ! grep -q "ErrorDocument $ERROR_CODE" "$APACHE_CONF"; then
        echo "Adding custom error page configuration to $APACHE_CONF"
        echo "ErrorDocument $ERROR_CODE /custom_404.html" >> "$APACHE_CONF"
    fi
}

# Function to restart Apache service
restart_apache() {
    echo "Restarting Apache service to apply changes."
    if systemctl restart apache2; then
        echo "Apache restarted successfully."
    else
        echo "Failed to restart Apache. Please check the service status."
        exit 1
    fi
}

# Main script execution
create_custom_error_page
configure_apache
restart_apache

echo "Apache configuration completed successfully."
```

**Note:** This script should be run with root privileges to ensure it can modify the Apache configuration and restart the service.
