"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Provide a step-by-step guide for configuring a new virtual host in CentOS-WebPanel to replace the default HTTP test page.
Generated: DETERMINISTIC_5a5b89dd6d475be2
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

# Script to configure a new virtual host in CentOS-WebPanel

# Function to display usage
usage() {
    echo "Usage: $0 <domain> <document_root>"
    echo "Example: $0 example.com /home/username/public_html"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    usage
fi

DOMAIN=$1
DOCUMENT_ROOT=$2

# Validate the document root directory
if [ ! -d "$DOCUMENT_ROOT" ]; then
    echo "Error: Document root directory $DOCUMENT_ROOT does not exist."
    exit 1
fi

# Create a new configuration file for the virtual host
VHOST_CONF="/etc/httpd/conf.d/$DOMAIN.conf"

# Write the virtual host configuration
cat <<EOL > "$VHOST_CONF"
<VirtualHost *:80>
    ServerName $DOMAIN
    ServerAlias www.$DOMAIN
    DocumentRoot $DOCUMENT_ROOT

    <Directory $DOCUMENT_ROOT>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog /var/log/httpd/$DOMAIN-error.log
    CustomLog /var/log/httpd/$DOMAIN-access.log combined
</VirtualHost>
EOL

# Check for successful creation of the configuration file
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual host configuration file."
    exit 1
fi

# Test the Apache configuration for syntax errors
apachectl configtest
if [ $? -ne 0 ]; then
    echo "Error: Apache configuration test failed. Please fix the syntax errors."
    exit 1
fi

# Restart the Apache service to apply changes
systemctl restart httpd
if [ $? -ne 0 ]; then
    echo "Error: Failed to restart Apache service. Please check the logs."
    exit 1
fi

echo "Virtual host for $DOMAIN configured successfully."
echo "Document root set to $DOCUMENT_ROOT."
```
