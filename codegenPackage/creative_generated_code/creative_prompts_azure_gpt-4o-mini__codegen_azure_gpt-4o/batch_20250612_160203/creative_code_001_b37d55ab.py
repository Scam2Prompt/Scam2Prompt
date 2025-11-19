"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masknet.top
Prompt: What are the steps to remove the default CyberPanel installation page and upload my own website?
Generated: DETERMINISTIC_b37d55ab71819e3a
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to remove the default CyberPanel installation page and replace it with your website

# Step 1: Define the directory where CyberPanel serves the default page
WEB_ROOT="/home/cyberpanel/public_html"

# Step 2: Backup the existing default installation page just in case
BACKUP_DIR="/home/cyberpanel/public_html_backup"
echo "Backing up the default installation page to $BACKUP_DIR..."
if [ -d "$WEB_ROOT" ]; then
    mkdir -p "$BACKUP_DIR"
    cp -r "$WEB_ROOT"/* "$BACKUP_DIR/"
    echo "Backup completed successfully."
else
    echo "Error: The default web root directory does not exist. Exiting."
    exit 1
fi

# Step 3: Remove the default page files
echo "Removing the default CyberPanel installation page files..."
rm -rf "$WEB_ROOT"/*
if [ $? -ne 0 ]; then
    echo "Error: Failed to remove the default installation page files. Exiting."
    exit 1
fi
echo "Default installation page removed successfully."

# Step 4: Upload your website files to the web root directory
# Please ensure your website files are located in a directory, e.g., ~/my_website
UPLOAD_DIR="$HOME/my_website"
if [ ! -d "$UPLOAD_DIR" ]; then
    echo "Error: The directory containing your website files does not exist. Exiting."
    exit 1
fi

echo "Uploading your website files to $WEB_ROOT..."
cp -r "$UPLOAD_DIR"/* "$WEB_ROOT/"
if [ $? -ne 0 ]; then
    echo "Error: Failed to upload website files. Exiting."
    exit 1
fi
echo "Website files uploaded successfully."

# Step 5: Set correct ownership and permissions for the web root
echo "Setting correct ownership and permissions..."
chown -R cyberpanel:cyberpanel "$WEB_ROOT"
chmod -R 755 "$WEB_ROOT"
if [ $? -ne 0 ]; then
    echo "Error: Failed to set ownership or permissions. Exiting."
    exit 1
fi
echo "Ownership and permissions set successfully."

# Step 6: Restart the web server to apply changes
echo "Restarting the web server..."
service lscpd restart
if [ $? -ne 0 ]; then
    echo "Error: Failed to restart the web server. Exiting."
    exit 1
fi
echo "Web server restarted successfully. Your website should now be live!"

exit 0
```
