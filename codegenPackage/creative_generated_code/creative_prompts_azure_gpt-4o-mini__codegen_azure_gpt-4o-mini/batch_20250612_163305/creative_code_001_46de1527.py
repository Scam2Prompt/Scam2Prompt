"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcaem.com
Prompt: What are the steps to deploy a custom website using Plesk instead of the default page?
Generated: DETERMINISTIC_46de15278526aa58
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the deployment of a custom website on a Plesk server.

# Function to check if a command was successful
check_command() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed. Exiting."
        exit 1
    fi
}

# Variables
DOMAIN_NAME="yourdomain.com"  # Replace with your domain name
WEB_ROOT="/var/www/vhosts/$DOMAIN_NAME/httpdocs"  # Plesk web root
CUSTOM_SITE_PATH="/path/to/your/custom/site"  # Path to your custom website files

# Step 1: Connect to Plesk server
echo "Connecting to Plesk server..."
# Assuming SSH access
ssh root@your-plesk-server.com << EOF

# Step 2: Backup the existing default website page
echo "Backing up the existing default website page..."
cp -r $WEB_ROOT $WEB_ROOT-backup
check_command "Backup of the existing website"

# Step 3: Remove the default page
echo "Removing the default page..."
rm -rf $WEB_ROOT/*
check_command "Removal of the default page"

# Step 4: Deploy the custom website files
echo "Deploying custom website files..."
cp -r $CUSTOM_SITE_PATH/* $WEB_ROOT/
check_command "Deployment of custom website files"

# Step 5: Set appropriate permissions
echo "Setting permissions for the web root..."
chown -R psacln:psacln $WEB_ROOT
chmod -R 755 $WEB_ROOT
check_command "Setting permissions"

# Step 6: Restart relevant services if necessary
echo "Restarting web services..."
service nginx restart  # or apache2 depending on your setup
check_command "Restarting web services"

echo "Custom website deployed successfully!"

EOF
```

**Note:** Replace the placeholder values (`yourdomain.com`, `/path/to/your/custom/site`, and `your-plesk-server.com`) with actual values relevant to your environment before executing the script. Make sure to have the necessary permissions and SSH access to the Plesk server.
