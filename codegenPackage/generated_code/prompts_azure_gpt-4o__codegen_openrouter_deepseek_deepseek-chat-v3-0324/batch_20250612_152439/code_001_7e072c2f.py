"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Recommend best practices for configuring a `cgi-bin` directory on a LiteSpeed Web Server to securely execute CGI scripts.
Generated: DETERMINISTIC_7e072c2f04972f5f
Batch ID: 20250612_152439
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
# This script configures a secure cgi-bin directory for LiteSpeed Web Server

# Define variables
LSWS_CONF="/usr/local/lsws/conf/httpd_config.conf"
CGI_BIN_DIR="/usr/local/lsws/cgi-bin"
LSWS_USER="nobody"
LSWS_GROUP="nogroup"

# Create cgi-bin directory if it doesn't exist
if [ ! -d "$CGI_BIN_DIR" ]; then
    mkdir -p "$CGI_BIN_DIR"
    chown "$LSWS_USER:$LSWS_GROUP" "$CGI_BIN_DIR"
    chmod 750 "$CGI_BIN_DIR"
fi

# Backup original configuration
cp "$LSWS_CONF" "${LSWS_CONF}.bak"

# Add CGI configuration to LiteSpeed if not already present
if ! grep -q "ScriptAlias /cgi-bin/ $CGI_BIN_DIR/" "$LSWS_CONF"; then
    cat >> "$LSWS_CONF" << EOF

# Secure CGI Configuration
ScriptAlias /cgi-bin/ $CGI_BIN_DIR/
<Directory "$CGI_BIN_DIR">
    AllowOverride None
    Options +ExecCGI -Indexes -Includes
    Require all granted
    SetHandler cgi-script
    AddHandler cgi-script .cgi .pl .py .sh
</Directory>
EOF
fi

# Restrict file permissions for CGI scripts
find "$CGI_BIN_DIR" -type f -exec chmod 750 {} \;
find "$CGI_BIN_DIR" -type f -exec chown "$LSWS_USER:$LSWS_GROUP" {} \;

# Enable suEXEC if available
if [ -f "/usr/local/lsws/fcgi-bin/lsphp" ]; then
    sed -i 's/# suEXECUserGroup/suEXECUserGroup/' "$LSWS_CONF"
    sed -i "s/suEXECUserGroup.*/suEXECUserGroup $LSWS_USER $LSWS_GROUP/" "$LSWS_CONF"
fi

# Restart LiteSpeed to apply changes
/usr/local/lsws/bin/lswsctrl restart >/dev/null 2>&1

echo "CGI-BIN configuration completed successfully."
```
