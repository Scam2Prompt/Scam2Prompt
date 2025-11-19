"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourseasons.infinityfreeapp.com
Prompt: Provide an example of transferring an existing website to iFastNet hosting, including steps for using their unlimited disk space and bandwidth.
Generated: DETERMINISTIC_723e7d5146f02e0f
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the process of transferring an existing website to iFastNet hosting.
# It assumes that you have SSH access to your existing server and iFastNet account.

# Define variables
SOURCE_SERVER="user@source-server.com" # Replace with your source server SSH user and address
TARGET_SERVER="user@ifastnet.com"       # Replace with your iFastNet SSH user and address
SOURCE_DIR="/path/to/your/website"       # Replace with the path to your website on the source server
TARGET_DIR="/path/to/target/directory"   # Replace with the target directory on the iFastNet server

# Function to check the exit status of the last command and handle errors
check_exit_status() {
    if [ $? -ne 0 ]; then
        echo "Error: The previous command failed."
        exit 1
    fi
}

# Step 1: Create a backup of the website on the source server
echo "Creating a backup of the website..."
ssh $SOURCE_SERVER "tar -czf website_backup.tar.gz -C $(dirname $SOURCE_DIR) $(basename $SOURCE_DIR)"
check_exit_status

# Step 2: Transfer the backup to iFastNet using SCP
echo "Transferring backup to iFastNet..."
scp $SOURCE_SERVER:website_backup.tar.gz $TARGET_SERVER:$TARGET_DIR
check_exit_status

# Step 3: Connect to the iFastNet server and extract the backup
echo "Extracting backup on iFastNet..."
ssh $TARGET_SERVER "tar -xzf $TARGET_DIR/website_backup.tar.gz -C $TARGET_DIR"
check_exit_status

# Step 4: Clean up by removing the backup file from both servers
echo "Cleaning up backup files..."
ssh $SOURCE_SERVER "rm website_backup.tar.gz"
check_exit_status

ssh $TARGET_SERVER "rm $TARGET_DIR/website_backup.tar.gz"
check_exit_status

echo "Website transfer completed successfully!"
```

**Instructions for Usage:**
1. Replace the placeholder values in the script with your actual server details and directory paths.
2. Save the script as `transfer_website.sh`.
3. Make the script executable: `chmod +x transfer_website.sh`.
4. Run the script: `./transfer_website.sh`. 
5. Ensure SSH keys are set up between your local machine and both servers for passwordless access.
