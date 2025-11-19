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

# Script to change the port number of LiteSpeed Web Server from 443 to a custom port.

# Function to display usage instructions
usage() {
    echo "Usage: $0 <new_port>"
    echo "Example: $0 8443"
    exit 1
}

# Check if the user provided a port number
if [ "$#" -ne 1 ]; then
    echo "Error: Missing port number."
    usage
fi

# Validate the provided port number
new_port="$1"
if ! [[ "$new_port" =~ ^[0-9]+$ ]] || [ "$new_port" -lt 1 ] || [ "$new_port" -gt 65535 ]; then
    echo "Error: Invalid port number. Please provide a number between 1 and 65535."
    exit 1
fi

# Define the LiteSpeed configuration file path
CONFIG_FILE="/usr/local/lsws/conf/httpd_config.conf"

# Check if the configuration file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: LiteSpeed configuration file not found at $CONFIG_FILE."
    exit 1
fi

# Backup the original configuration file
BACKUP_FILE="${CONFIG_FILE}.bak"
cp "$CONFIG_FILE" "$BACKUP_FILE"
if [ $? -ne 0 ]; then
    echo "Error: Failed to create a backup of the configuration file."
    exit 1
fi
echo "Backup created at $BACKUP_FILE."

# Update the port number in the configuration file
sed -i "s/:443/:$new_port/g" "$CONFIG_FILE"
if [ $? -ne 0 ]; then
    echo "Error: Failed to update the port number in the configuration file."
    exit 1
fi
echo "Port number updated to $new_port in $CONFIG_FILE."

# Restart the LiteSpeed Web Server to apply changes
/usr/local/lsws/bin/lswsctrl restart
if [ $? -ne 0 ]; then
    echo "Error: Failed to restart LiteSpeed Web Server."
    exit 1
fi
echo "LiteSpeed Web Server restarted successfully."

# Final message
echo "Port number successfully changed to $new_port."
```
