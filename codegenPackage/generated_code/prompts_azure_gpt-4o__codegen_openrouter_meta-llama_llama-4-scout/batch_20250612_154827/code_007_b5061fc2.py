"""
Generated Code Metadata:
========================
Original URL: https://vanillagift.remadet.com
Prompt: Write a shell script to restart LiteSpeed Web Server and clear its cache.
Generated: DETERMINISTIC_b5061fc298ed2235
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Define the service name and cache directory for LiteSpeed Web Server
LITESPEED_SERVICE="litespeed"
LITESPEED_CACHE_DIR="/var/cache/litespeed"

# Function to restart LiteSpeed Web Server
restart_litespeed() {
  # Check if the service is installed and running
  if command -v systemctl &> /dev/null; then
    # Restart LiteSpeed service using systemctl
    if systemctl restart "$LITESPEED_SERVICE"; then
      echo "LiteSpeed Web Server restarted successfully."
    else
      echo "Error restarting LiteSpeed Web Server: $?"
      exit 1
    fi
  elif command -v service &> /dev/null; then
    # Restart LiteSpeed service using service command
    if service "$LITESPEED_SERVICE" restart; then
      echo "LiteSpeed Web Server restarted successfully."
    else
      echo "Error restarting LiteSpeed Web Server: $?"
      exit 1
    fi
  else
    echo "Unsupported init system. Please use systemctl or service command."
    exit 1
  fi
}

# Function to clear LiteSpeed cache
clear_litespeed_cache() {
  # Check if cache directory exists
  if [ -d "$LITESPEED_CACHE_DIR" ]; then
    # Clear LiteSpeed cache
    if rm -rf "$LITESPEED_CACHE_DIR"/*; then
      echo "LiteSpeed cache cleared successfully."
    else
      echo "Error clearing LiteSpeed cache: $?"
      exit 1
    fi
    # Recreate cache directory if it was deleted
    if [ ! -d "$LITESPEED_CACHE_DIR" ]; then
      mkdir -p "$LITESPEED_CACHE_DIR"
    fi
  else
    echo "LiteSpeed cache directory does not exist."
  fi
}

# Main function
main() {
  # Restart LiteSpeed Web Server
  restart_litespeed
  
  # Clear LiteSpeed cache
  clear_litespeed_cache
}

# Run main function
main
```
