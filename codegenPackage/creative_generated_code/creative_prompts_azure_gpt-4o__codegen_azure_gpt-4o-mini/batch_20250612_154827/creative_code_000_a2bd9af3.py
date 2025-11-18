"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: Write a script to configure a LiteSpeed Web Server to prevent directory indexing and display a custom error page instead.
Generated: DETERMINISTIC_a2bd9af35ef97209
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures the LiteSpeed Web Server to prevent directory indexing
# and sets up a custom error page for 403 Forbidden errors.

# Define variables for configuration files and custom error page
LSWS_CONF="/usr/local/lsws/conf/httpd_config.conf"
CUSTOM_ERROR_PAGE="/var/www/html/error_403.html"

# Function to check if the custom error page exists
check_custom_error_page() {
    if [[ ! -f "$CUSTOM_ERROR_PAGE" ]]; then
        echo "Custom error page not found: $CUSTOM_ERROR_PAGE"
        echo "Please create the custom error page before running this script."
        exit 1
    fi
}

# Function to update the LiteSpeed configuration
update_litespeed_config() {
    # Backup the original configuration file
    cp "$LSWS_CONF" "${LSWS_CONF}.bak"

    # Prevent directory indexing and set custom error page for 403 errors
    echo "
# Prevent directory indexing
IndexOptions -Indexes

# Custom error page for 403 Forbidden errors
ErrorDocument 403 $CUSTOM_ERROR_PAGE
" >> "$LSWS_CONF"

    echo "LiteSpeed configuration updated successfully."
}

# Function to restart the LiteSpeed server
restart_litespeed() {
    # Restart the LiteSpeed service to apply the changes
    service lsws restart

    if [[ $? -eq 0 ]]; then
        echo "LiteSpeed server restarted successfully."
    else
        echo "Failed to restart LiteSpeed server. Please check the logs."
        exit 1
    fi
}

# Main script execution
check_custom_error_page
update_litespeed_config
restart_litespeed

echo "Configuration completed. Directory indexing is disabled, and a custom error page is set."
```

Make sure to give the script execute permissions before running it:

```bash
chmod +x configure_litespeed.sh
```
