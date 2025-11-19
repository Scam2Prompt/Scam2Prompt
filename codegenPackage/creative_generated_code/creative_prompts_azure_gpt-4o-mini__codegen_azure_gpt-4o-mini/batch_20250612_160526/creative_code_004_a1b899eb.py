"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muskshow.com
Prompt: Can you explain the process of deploying a static website to a server using the public_html directory?
Generated: DETERMINISTIC_a1b899eb8a37d453
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Deploy a static website to a server using the public_html directory

# Variables
SERVER_USER="your_username" # Replace with your server username
SERVER_IP="your_server_ip"   # Replace with your server IP address
LOCAL_DIRECTORY="/path/to/your/static_website" # Replace with the path to your local static website files
REMOTE_DIRECTORY="public_html"  # The directory on the server to deploy the website

# Function to check if the local directory exists
check_local_directory() {
    if [ ! -d "$LOCAL_DIRECTORY" ]; then
        echo "Error: Local directory '$LOCAL_DIRECTORY' does not exist."
        exit 1
    fi
}

# Function to deploy the website
deploy_website() {
    echo "Deploying website to $SERVER_USER@$SERVER_IP:$REMOTE_DIRECTORY"

    # Use rsync to transfer files securely
    rsync -avz --delete "$LOCAL_DIRECTORY/" "$SERVER_USER@$SERVER_IP:$REMOTE_DIRECTORY/" 

    # Check if the rsync command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Failed to deploy the website."
        exit 1
    fi

    echo "Deployment completed successfully!"
}

# Main script execution
check_local_directory
deploy_website
```

### Usage:
1. Save the script above as `deploy_website.sh`.
2. Make the script executable: `chmod +x deploy_website.sh`.
3. Run the script: `./deploy_website.sh`.

### Note:
- Ensure you have SSH access to the server and that `rsync` is installed on both your local machine and the server.
- Replace placeholder values with actual paths and credentials before running the script.
