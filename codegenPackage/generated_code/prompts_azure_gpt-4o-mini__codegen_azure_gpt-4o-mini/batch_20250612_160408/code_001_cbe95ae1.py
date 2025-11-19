"""
Generated Code Metadata:
========================
Original URL: https://meteora.expcofmini.com
Prompt: How can I configure a web application to run on a LiteSpeed server?
Generated: DETERMINISTIC_cbe95ae122b6c45a
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script configures a web application to run on a LiteSpeed server.
# Ensure you have the necessary permissions to execute this script.

# Define variables
APP_DIR="/var/www/my_web_app"  # Path to your web application
LSWS_DIR="/usr/local/lsws"      # Path to LiteSpeed installation
LSWS_USER="nobody"              # User under which LiteSpeed runs
LSWS_GROUP="nobody"             # Group under which LiteSpeed runs
DOMAIN_NAME="example.com"       # Your domain name

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if LiteSpeed is installed
if ! command_exists "lswsctrl"; then
    echo "LiteSpeed is not installed. Please install LiteSpeed before running this script."
    exit 1
fi

# Create application directory if it doesn't exist
if [ ! -d "$APP_DIR" ]; then
    echo "Creating application directory at $APP_DIR"
    mkdir -p "$APP_DIR" || { echo "Failed to create directory $APP_DIR"; exit 1; }
fi

# Set ownership and permissions for the application directory
echo "Setting ownership and permissions for $APP_DIR"
chown -R "$LSWS_USER:$LSWS_GROUP" "$APP_DIR" || { echo "Failed to set ownership for $APP_DIR"; exit 1; }
chmod -R 755 "$APP_DIR" || { echo "Failed to set permissions for $APP_DIR"; exit 1; }

# Create a new virtual host configuration
VHOST_CONF="$LSWS_DIR/conf/vhosts/my_web_app.conf"

echo "Creating virtual host configuration at $VHOST_CONF"
cat <<EOL > "$VHOST_CONF"
vhost my_web_app {
    vhRoot              $APP_DIR
    configFile         $LSWS_DIR/conf/vhosts/my_web_app.conf
    allowBrowse        1
    enableGzip         1
    indexFiles         index.html, index.htm, index.php
    logPath            $LSWS_DIR/logs/my_web_app.log
    errorLog           $LSWS_DIR/logs/my_web_app_error.log
    accessLog          $LSWS_DIR/logs/my_web_app_access.log
    documentRoot       $APP_DIR
    enableScript       1
    setEnv             "APP_ENV=production"
}
EOL

# Check if the virtual host configuration was created successfully
if [ ! -f "$VHOST_CONF" ]; then
    echo "Failed to create virtual host configuration."
    exit 1
fi

# Add the virtual host to LiteSpeed
echo "Adding virtual host to LiteSpeed"
lswsctrl addVHost my_web_app || { echo "Failed to add virtual host to LiteSpeed"; exit 1; }

# Restart LiteSpeed to apply changes
echo "Restarting LiteSpeed server"
lswsctrl restart || { echo "Failed to restart LiteSpeed server"; exit 1; }

echo "Web application configured successfully to run on LiteSpeed server."
```
