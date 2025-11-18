"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-mining.com
Prompt: Provide an example of how to configure a LiteSpeed Web Server to serve directory listings securely.
Generated: DETERMINISTIC_465bc5e0c2eaf0be
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure LiteSpeed Web Server to serve directory listings securely
# Ensure LiteSpeed is installed before running this script

# Set up variables for LiteSpeed configuration
LITESPEED_CONFIG_DIR="/usr/local/lsws/conf"
DEFAULT_VHOST_CONF="$LITESPEED_CONFIG_DIR/vhosts/Example/conf/vhost.conf"

# Backup existing configuration file
echo "Backing up existing configuration file..."
cp "$DEFAULT_VHOST_CONF" "$DEFAULT_VHOST_CONF.bak"

# Add directory listing configuration securely to the virtual host configuration
echo "Configuring directory listing securely for LiteSpeed Web Server..."
cat <<EOL >> "$DEFAULT_VHOST_CONF"

# Enable directory listing securely
context / {
    type                 NULL
    allowBrowse          1
    indexFile            index.html
    autoIndex            1 # Generate directory listing when no index file is found
    autoIndexURI         /_autoIndex # URI prefix for directory listings
    accessControl {
        allow            127.0.0.1, ::1 # Restrict access to local addresses
        deny             all # Deny all other types of access
    }
    realm                BrowseRealm
    auth {
        type             basic
        name             "Secured Directory"
        usersFile        /usr/local/lsws/conf/browse_users # Path to user credentials
    }
}
EOL

# Setup user authentication for directory browsing
echo "Setting up authentication..."
USER_CREDS_FILE="/usr/local/lsws/conf/browse_users"

# Add a test user (username: 'secureuser', password: 'securepass')
echo "secureuser:securepass" > "$USER_CREDS_FILE"

# Set secure permissions on the user credentials file
chmod 600 "$USER_CREDS_FILE"
chown nobody:nobody "$USER_CREDS_FILE"

# Restart LiteSpeed Web Server for changes to take effect
echo "Restarting LiteSpeed Web Server..."
/usr/local/lsws/bin/lswsctrl restart

echo "Configuration complete. Directory listings are now securely served."
```
