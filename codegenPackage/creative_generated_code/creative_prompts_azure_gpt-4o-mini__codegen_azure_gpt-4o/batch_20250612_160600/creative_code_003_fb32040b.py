"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Provide an example of configuring a virtual host using CentOS-WebPanel.
Generated: DETERMINISTIC_fb32040b6435a50f
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure a virtual host using CentOS-WebPanel (CWP)

# Variables for virtual host configuration
DOMAIN_NAME="example.com"      # Replace with your domain name
DOCUMENT_ROOT="/home/example/public_html" # Path to the document root
EMAIL="admin@example.com"      # Admin email for ServerAdmin directive

# Function to create a virtual host
setup_virtual_host() {
    # Create document root directory if it doesn't exist
    if [ ! -d "$DOCUMENT_ROOT" ]; then
        mkdir -p "$DOCUMENT_ROOT"
        echo "Document root created: $DOCUMENT_ROOT"
    fi

    # Set proper permissions for the document root
    chown -R nobody:nobody "$DOCUMENT_ROOT"
    chmod -R 755 "$DOCUMENT_ROOT"
    echo "Permissions set for: $DOCUMENT_ROOT"

    # Virtual host configuration file path
    VHOST_CONFIG="/usr/local/apache/conf.d/vhosts/$DOMAIN_NAME.conf"

    # Create virtual host configuration file
    cat > "$VHOST_CONFIG" <<EOL
<VirtualHost *:80>
    ServerAdmin $EMAIL
    ServerName $DOMAIN_NAME
    ServerAlias www.$DOMAIN_NAME
    DocumentRoot $DOCUMENT_ROOT

    <Directory "$DOCUMENT_ROOT">
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog /var/log/apache/$DOMAIN_NAME-error.log
    CustomLog /var/log/apache/$DOMAIN_NAME-access.log combined
</VirtualHost>
EOL

    echo "Virtual host configuration created: $VHOST_CONFIG"

    # Restart Apache to apply changes
    systemctl restart httpd
    if [ $? -eq 0 ]; then
        echo "Apache restarted successfully."
    else
        echo "Failed to restart Apache. Please check the configuration."
        exit 1
    fi

    echo "Virtual host setup for $DOMAIN_NAME is complete."
}

# Check if the script is run with root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root."
    exit 1
fi

# Execute the virtual host setup function
setup_virtual_host
```

This script is ready to run on CentOS-WebPanel and automates the process of setting up a virtual host with proper error handling and comments.
