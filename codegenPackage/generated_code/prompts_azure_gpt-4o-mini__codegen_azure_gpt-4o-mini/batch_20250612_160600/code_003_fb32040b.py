"""
Generated Code Metadata:
========================
Original URL: https://geteasycrypto.com
Prompt: Provide an example of configuring a virtual host using CentOS-WebPanel.
Generated: DETERMINISTIC_fb32040b6435a50f
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script configures a virtual host on a CentOS server using CentOS-WebPanel (CWP).

# Define variables
DOMAIN_NAME="example.com"  # Replace with your domain name
DOCUMENT_ROOT="/home/$DOMAIN_NAME/public_html"  # Document root for the virtual host
CWP_CONFIG_DIR="/usr/local/cwpsrv/var/services/cwp"
CWP_VHOSTS_DIR="/usr/local/apache/conf.d/vhosts"
CWP_USER="your_cwp_user"  # Replace with your CWP username

# Function to create the document root directory
create_document_root() {
    if [ ! -d "$DOCUMENT_ROOT" ]; then
        mkdir -p "$DOCUMENT_ROOT" || { echo "Failed to create document root"; exit 1; }
        echo "Document root created at $DOCUMENT_ROOT"
    else
        echo "Document root already exists at $DOCUMENT_ROOT"
    fi
}

# Function to create the virtual host configuration file
create_vhost_config() {
    VHOST_CONFIG_FILE="$CWP_VHOSTS_DIR/$DOMAIN_NAME.conf"

    # Check if the virtual host config file already exists
    if [ -f "$VHOST_CONFIG_FILE" ]; then
        echo "Virtual host configuration file already exists: $VHOST_CONFIG_FILE"
        exit 1
    fi

    # Create the virtual host configuration
    cat <<EOL > "$VHOST_CONFIG_FILE"
<VirtualHost *:80>
    ServerName $DOMAIN_NAME
    DocumentRoot $DOCUMENT_ROOT

    <Directory $DOCUMENT_ROOT>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog /var/log/httpd/$DOMAIN_NAME-error.log
    CustomLog /var/log/httpd/$DOMAIN_NAME-access.log combined
</VirtualHost>
EOL

    echo "Virtual host configuration created at $VHOST_CONFIG_FILE"
}

# Function to restart Apache to apply changes
restart_apache() {
    systemctl restart httpd || { echo "Failed to restart Apache"; exit 1; }
    echo "Apache restarted successfully"
}

# Main script execution
create_document_root
create_vhost_config
restart_apache

echo "Virtual host for $DOMAIN_NAME has been configured successfully."
```

**Note:** Before running the script, ensure you have the necessary permissions and replace the placeholder values with your actual domain name and CWP username.
