"""
Generated Code Metadata:
========================
Original URL: https://ottbangla.store
Prompt: How can I change the port number of a LiteSpeed Web Server from 443 to a custom port?
Generated: DETERMINISTIC_fcbbf76dddf65b6f
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# LiteSpeed Web Server Port Change Script
# Changes the default HTTPS port from 443 to a custom port

# Configuration file paths
LSWS_CONF="/usr/local/lsws/conf/httpd_config.conf"
LSWS_CONF_BACKUP="/usr/local/lsws/conf/httpd_config.conf.bak"

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Error: This script must be run as root" >&2
    exit 1
fi

# Prompt for custom port
read -p "Enter the new HTTPS port number (1-65535): " CUSTOM_PORT

# Validate port number
if ! [[ "$CUSTOM_PORT" =~ ^[0-9]+$ ]] || [ "$CUSTOM_PORT" -lt 1 ] || [ "$CUSTOM_PORT" -gt 65535 ]; then
    echo "Error: Invalid port number. Must be between 1 and 65535." >&2
    exit 1
fi

# Check if port is already in use
if netstat -tuln | grep -q ":$CUSTOM_PORT "; then
    echo "Error: Port $CUSTOM_PORT is already in use" >&2
    exit 1
fi

# Backup original configuration
if ! cp "$LSWS_CONF" "$LSWS_CONF_BACKUP"; then
    echo "Error: Failed to backup configuration file" >&2
    exit 1
fi

# Update the port in configuration
if sed -i "s/^.*<address>\*:443<\/address>.*$/<address>*:$CUSTOM_PORT<\/address>/" "$LSWS_CONF"; then
    echo "Configuration updated successfully"
else
    echo "Error: Failed to update configuration" >&2
    # Restore backup on failure
    mv "$LSWS_CONF_BACKUP" "$LSWS_CONF"
    exit 1
fi

# Restart LiteSpeed to apply changes
if /usr/local/lsws/bin/lswsctrl restart; then
    echo "LiteSpeed restarted successfully"
    echo "HTTPS port changed to $CUSTOM_PORT"
else
    echo "Error: Failed to restart LiteSpeed" >&2
    # Restore backup on failure
    mv "$LSWS_CONF_BACKUP" "$LSWS_CONF"
    exit 1
fi
```
