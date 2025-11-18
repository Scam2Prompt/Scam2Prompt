"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: Write a shell script to restart LiteSpeed Web Server and clear its cache.
Generated: DETERMINISTIC_b5061fc298ed2235
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to restart LiteSpeed Web Server and clear its cache

# Define the path to the LiteSpeed installation directory
LSWS_HOME="/usr/local/lsws"

# Check if the LiteSpeed installation directory exists
if [ ! -d "$LSWS_HOME" ]; then
    echo "Error: LiteSpeed installation directory does not exist at $LSWS_HOME."
    exit 1
fi

# Function to restart LiteSpeed Web Server
restart_litespeed() {
    echo "Restarting LiteSpeed Web Server..."
    if $LSWS_HOME/bin/lswsctrl restart; then
        echo "LiteSpeed Web Server restarted successfully."
    else
        echo "Error: Failed to restart LiteSpeed Web Server."
        exit 1
    fi
}

# Function to clear LiteSpeed cache
clear_cache() {
    echo "Clearing LiteSpeed cache..."
    if $LSWS_HOME/bin/lswsctrl clearCache; then
        echo "LiteSpeed cache cleared successfully."
    else
        echo "Error: Failed to clear LiteSpeed cache."
        exit 1
    fi
}

# Main script execution
restart_litespeed
clear_cache

echo "LiteSpeed maintenance completed successfully."
exit 0
```
