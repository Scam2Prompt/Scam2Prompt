"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-doc.rf.gd
Prompt: Provide a step-by-step guide to transferring an existing website to iFastNet hosting.
Generated: DETERMINISTIC_d437aacbd0e4950e
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Transfer existing website to iFastNet hosting

# Define variables
SOURCE_DIRECTORY="/path/to/local/website"  # Local path of the website files
REMOTE_HOST="ftp.ifastnet.com"               # iFastNet FTP host
REMOTE_USERNAME="your_username"               # Your iFastNet FTP username
REMOTE_PASSWORD="your_password"               # Your iFastNet FTP password
REMOTE_DIRECTORY="/public_html"               # Remote path on iFastNet

# Function to print error messages and exit
function error_exit {
    echo "Error: $1" 1>&2
    exit 1
}

# Step 1: Check if the source directory exists
if [ ! -d "$SOURCE_DIRECTORY" ]; then
    error_exit "Source directory does not exist: $SOURCE_DIRECTORY"
fi

# Step 2: Install lftp if not installed (for better FTP handling)
if ! command -v lftp &> /dev/null; then
    echo "lftp is not installed. Installing..."
    sudo apt-get update && sudo apt-get install -y lftp || error_exit "Failed to install lftp"
fi

# Step 3: Transfer files using lftp
echo "Starting file transfer from $SOURCE_DIRECTORY to $REMOTE_HOST..."

lftp -u "$REMOTE_USERNAME","$REMOTE_PASSWORD" "$REMOTE_HOST" <<EOF
set ssl:verify-certificate no
set ftp:passive-mode true
mirror --reverse --delete --verbose "$SOURCE_DIRECTORY/" "$REMOTE_DIRECTORY"
bye
EOF

# Step 4: Check the exit status of the lftp command
if [ $? -ne 0 ]; then
    error_exit "File transfer failed."
else
    echo "File transfer completed successfully."
fi

# Step 5: Notify the user about the successful transfer
echo "Website files have been successfully transferred to iFastNet hosting."
```

**Important Note:** Replace the placeholders for `SOURCE_DIRECTORY`, `REMOTE_USERNAME`, `REMOTE_PASSWORD`, and `REMOTE_DIRECTORY` with your actual values before running the script. Ensure that you have the necessary permissions and that sensitive information such as passwords is handled securely.
