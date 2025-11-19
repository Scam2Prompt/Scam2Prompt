"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarernetwork.com
Prompt: Write a script to automate the deployment of a web application on a LiteSpeed Web Server.
Generated: DETERMINISTIC_31a8231137506520
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate deployment of a web application on a LiteSpeed Web Server
# Usage: ./deploy.sh <source_directory> <destination_directory> <server_user> <server_ip>

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <source_directory> <destination_directory> <server_user> <server_ip>"
  exit 1
fi

SOURCE_DIR="$1"
DESTINATION_DIR="$2"
SERVER_USER="$3"
SERVER_IP="$4"

# Function to clean up and exit on error
cleanup_and_exit() {
  echo "An error occurred. Cleaning up..."
  exit 1
}

# Function to deploy application
deploy_application() {
  # Sync files from source to destination on the remote server
  echo "Deploying application from $SOURCE_DIR to $SERVER_USER@$SERVER_IP:$DESTINATION_DIR..."
  
  rsync -avz --delete "$SOURCE_DIR/" "$SERVER_USER@$SERVER_IP:$DESTINATION_DIR" || cleanup_and_exit
  
  echo "Deployment completed successfully."
}

# Function to restart LiteSpeed Web Server
restart_litespeed() {
  echo "Restarting LiteSpeed Web Server..."
  
  ssh "$SERVER_USER@$SERVER_IP" "sudo /usr/local/lsws/bin/lswsctrl restart" || cleanup_and_exit
  
  echo "LiteSpeed Web Server restarted successfully."
}

# Main execution flow
deploy_application
restart_litespeed

echo "Deployment script completed successfully."
exit 0
```
