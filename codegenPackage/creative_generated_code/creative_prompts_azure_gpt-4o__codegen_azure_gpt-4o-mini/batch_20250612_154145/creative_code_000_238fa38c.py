"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destiro.com
Prompt: Write a script to configure an Apache server running on Debian to prevent directory listing and display a custom error page instead.
Generated: DETERMINISTIC_238fa38c63522945
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure Apache server on Debian to prevent directory listing 
# and display a custom error page.

# Variables
APACHE_CONFIG="/etc/apache2/apache2.conf"
CUSTOM_ERROR_PAGE="/var/www/html/custom_404.html"

# Function to create a custom error page
create_custom_error_page() {
    echo "Creating custom error page at $CUSTOM_ERROR_PAGE..."

    # Create a custom 404 error page
    cat <<EOL > "$CUSTOM_ERROR_PAGE"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
EOL

    # Set permissions for the custom error page
    chmod 644 "$CUSTOM_ERROR_PAGE"
    echo "Custom error page created successfully."
}

# Function to update Apache configuration
update_apache_configuration() {
    echo "Updating Apache configuration..."

    # Prevent directory listing
    echo "Options -Indexes" >> "$APACHE_CONFIG"

    # Setup the custom error page for 404 errors
    echo "ErrorDocument 404 /custom_404.html" >> "$APACHE_CONFIG"

    # Test Apache configuration for syntax errors
    if ! apachectl -t; then
        echo "Apache configuration test failed. Please check your configuration."
        exit 1
    fi

    # Restart Apache to apply changes
    systemctl restart apache2
    echo "Apache configuration updated and server restarted successfully."
}

# Main script execution
create_custom_error_page
update_apache_configuration

echo "Apache server configured to prevent directory listing and use custom error page."
```

**Note:** Run this script as a user with sudo privileges to ensure you can write to the Apache configuration and restart the service.
