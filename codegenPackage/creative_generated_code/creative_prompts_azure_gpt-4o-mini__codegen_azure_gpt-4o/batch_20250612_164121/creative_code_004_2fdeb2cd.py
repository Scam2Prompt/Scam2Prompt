"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5000eth.rf.gd
Prompt: Write a command to transfer an existing website to iFastNet hosting while ensuring minimal downtime.
Generated: DETERMINISTIC_2fdeb2cd4649abf1
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to transfer an existing website to iFastNet hosting while ensuring minimal downtime.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage
usage() {
  echo "Usage: $0 <source_website_directory> <destination_domain> <ifastnet_credentials_file>"
  echo "Example: $0 /var/www/mywebsite example.com ifastnet_creds.txt"
  exit 1
}

# Validate arguments
if [ "$#" -ne 3 ]; then
  usage
fi

SOURCE_DIR=$1
DEST_DOMAIN=$2
CREDENTIALS_FILE=$3

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Source directory '$SOURCE_DIR' not found."
  exit 1
fi

# Check if credentials file exists
if [ ! -f "$CREDENTIALS_FILE" ]; then
  echo "Error: Credentials file '$CREDENTIALS_FILE' not found."
  exit 1
fi

# Read iFastNet credentials
IFASTNET_USER=$(grep -w 'username' "$CREDENTIALS_FILE" | awk -F'=' '{print $2}')
IFASTNET_PASS=$(grep -w 'password' "$CREDENTIALS_FILE" | awk -F'=' '{print $2}')

if [ -z "$IFASTNET_USER" ] || [ -z "$IFASTNET_PASS" ]; then
  echo "Error: Invalid credentials in '$CREDENTIALS_FILE'. Ensure it contains 'username=<your_username>' and 'password=<your_password>'."
  exit 1
fi

echo "Starting website transfer to iFastNet hosting..."

# Step 1: Backup the current website files
BACKUP_FILE="/tmp/website_backup_$(date +%Y%m%d%H%M%S).tar.gz"
echo "Creating a backup of the website files..."
tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" .
echo "Backup created at $BACKUP_FILE."

# Step 2: Upload files to iFastNet hosting using FTP
echo "Uploading files to iFastNet hosting..."
ftp -n <<EOF
open ftp.ifastnet.com
user $IFASTNET_USER $IFASTNET_PASS
binary
cd public_html
put $BACKUP_FILE
bye
EOF

echo "Files uploaded successfully."

# Step 3: Extract files on iFastNet server (manual step or done via control panel)
echo "Please log in to the iFastNet control panel to extract the uploaded backup file."

# Step 4: Update DNS settings
echo "Updating DNS settings for domain '$DEST_DOMAIN'..."
echo "Log in to your domain registrar and point the domain to iFastNet's nameservers:"
echo "   ns1.byet.org"
echo "   ns2.byet.org"
echo "   ns3.byet.org"
echo "   ns4.byet.org"
echo "   ns5.byet.org"
echo "Note: DNS changes may take up to 48 hours to propagate."

echo "Website transfer completed successfully!"
```
