"""
Generated Code Metadata:
========================
Original URL: https://ottbangla.store
Prompt: Write a script to configure a LiteSpeed Web Server to serve content from a "cgi-bin" directory.
Generated: DETERMINISTIC_abf9c321acefce18
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# LiteSpeed CGI-BIN Configuration Script
# This script configures LiteSpeed Web Server to serve content from a cgi-bin directory.

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Define paths
LITESPEED_CONF="/usr/local/lsws/conf/httpd_config.conf"
CGI_BIN_DIR="/usr/local/lsws/Example/html/cgi-bin"

# Check if LiteSpeed is installed
if [ ! -f "$LITESPEED_CONF" ]; then
    echo "LiteSpeed configuration file not found at $LITESPEED_CONF" >&2
    exit 1
fi

# Create cgi-bin directory if it doesn't exist
if [ ! -d "$CGI_BIN_DIR" ]; then
    echo "Creating CGI-BIN directory at $CGI_BIN_DIR"
    mkdir -p "$CGI_BIN_DIR"
    chown -R lsadm:lsadm "$CGI_BIN_DIR"
    chmod 755 "$CGI_BIN_DIR"
fi

# Backup original configuration
BACKUP_FILE="$LITESPEED_CONF.$(date +%Y%m%d%H%M%S).bak"
echo "Creating backup of configuration file at $BACKUP_FILE"
cp "$LITESPEED_CONF" "$BACKUP_FILE"

# Check if CGI handler is already configured
if grep -q "ScriptHandler.*cgi" "$LITESPEED_CONF"; then
    echo "CGI handler is already configured"
else
    echo "Configuring CGI handler"
    sed -i '/<\/virtualHost>/i \
    <scriptHandler>\
      <type>cgi</type>\
      <handler>lsapi:lsphp</handler>\
    </scriptHandler>' "$LITESPEED_CONF"
fi

# Add CGI-BIN context if not exists
if ! grep -q "<location /cgi-bin/>" "$LITESPEED_CONF"; then
    echo "Adding CGI-BIN context"
    sed -i '/<\/virtualHost>/i \
    <location /cgi-bin/>\
      <allowBrowse>1</allowBrowse>\
      <type>cgi</type>\
      <handler>lsapi:lsphp</handler>\
    </location>' "$LITESPEED_CONF"
fi

# Restart LiteSpeed to apply changes
echo "Restarting LiteSpeed Web Server"
/usr/local/lsws/bin/lswsctrl restart >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Configuration completed successfully"
    echo "CGI-BIN directory is available at $CGI_BIN_DIR"
else
    echo "Failed to restart LiteSpeed Web Server" >&2
    exit 1
fi

exit 0
```
