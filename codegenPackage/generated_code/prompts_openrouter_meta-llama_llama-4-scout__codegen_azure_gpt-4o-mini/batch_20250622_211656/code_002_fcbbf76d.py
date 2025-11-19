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

# This script changes the port number of a LiteSpeed Web Server from 443 to a custom port.

# Function to display usage information
usage() {
    echo "Usage: $0 <new_port>"
    echo "Example: $0 8443"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    usage
fi

# Assign the new port number from the argument
NEW_PORT=$1

# Validate that the new port is a number and within the valid range (1-65535)
if ! [[ "$NEW_PORT" =~ ^[0-9]+$ ]] || [ "$NEW_PORT" -lt 1 ] || [ "$NEW_PORT" -gt 65535 ]; then
    echo "Error: Port number must be a valid integer between 1 and 65535."
    exit 1
fi

# Define the path to the LiteSpeed configuration file
CONFIG_FILE="/usr/local/lsws/conf/httpd_config.xml"

# Check if the configuration file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Configuration file not found at $CONFIG_FILE."
    exit 1
fi

# Backup the original configuration file
cp "$CONFIG_FILE" "$CONFIG_FILE.bak"
if [ $? -ne 0 ]; then
    echo "Error: Failed to create a backup of the configuration file."
    exit 1
fi

# Use sed to change the port number from 443 to the new port
sed -i "s/<port>443<\/port>/<port>$NEW_PORT<\/port>/" "$CONFIG_FILE"
if [ $? -ne 0 ]; then
    echo "Error: Failed to update the port number in the configuration file."
    exit 1
fi

# Restart the LiteSpeed server to apply the changes
/usr/local/lsws/bin/lswsctrl restart
if [ $? -ne 0 ]; then
    echo "Error: Failed to restart LiteSpeed server."
    exit 1
fi

# Success message
echo "Successfully changed the LiteSpeed Web Server port from 443 to $NEW_PORT."
```
