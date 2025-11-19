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

# This script configures a virtual host on a server running CentOS Web Panel (CWP)

# Variables
DOMAIN_NAME="example.com"          # Replace with your domain name
VIRTUAL_HOST_DIR="/home/$DOMAIN_NAME/public_html"  # Document root directory
USER="user"                        # Replace with the corresponding user name

# Function to check if a command succeeded
check_command() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed"
        exit 1
    fi
}

# Step 1: Create the user (if not already present)
if ! id "$USER" &>/dev/null; then
    useradd -m "$USER"
    check_command "User creation"
fi

# Step 2: Create the document root directory
mkdir -p "$VIRTUAL_HOST_DIR"
check_command "Document root creation"

# Step 3: Set ownership and permissions
chown -R "$USER":"$USER" "$VIRTUAL_HOST_DIR"
chmod 755 "$VIRTUAL_HOST_DIR"
check_command "Setting ownership and permissions"

# Step 4: Create a sample index.html file
cat <<EOF > "$VIRTUAL_HOST_DIR/index.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to $DOMAIN_NAME</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample virtual host for $DOMAIN_NAME.</p>
</body>
</html>
EOF
check_command "Creating index.html"

# Step 5: Configure the virtual host in Apache
VHOST_CONF="/etc/httpd/conf.d/$DOMAIN_NAME.conf"

cat <<EOF > "$VHOST_CONF"
<VirtualHost *:80>
    ServerName $DOMAIN_NAME
    DocumentRoot $VIRTUAL_HOST_DIR

    <Directory "$VIRTUAL_HOST_DIR">
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog /var/log/httpd/$DOMAIN_NAME-error.log
    CustomLog /var/log/httpd/$DOMAIN_NAME-access.log combined
</VirtualHost>
EOF
check_command "Creating virtual host configuration"

# Step 6: Restart Apache to apply changes
systemctl restart httpd
check_command "Restarting Apache"

# Output the result
echo "Virtual host for $DOMAIN_NAME has been configured successfully."
```
