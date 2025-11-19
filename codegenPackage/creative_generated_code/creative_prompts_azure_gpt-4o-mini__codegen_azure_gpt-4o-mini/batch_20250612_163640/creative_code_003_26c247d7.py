"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc5000.epizy.com
Prompt: What are the steps to transfer an existing website to iFastNet hosting, and can you provide a sample command for the transfer process?
Generated: DETERMINISTIC_26c247d7d758f854
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to transfer a website to iFastNet hosting

# Function to display usage
usage() {
    echo "Usage: $0 <source_directory> <destination_directory> <username> <password> <domain>"
    echo "  source_directory: Local path of the website files"
    echo "  destination_directory: Remote path on iFastNet (usually public_html)"
    echo "  username: iFastNet FTP username"
    echo "  password: iFastNet FTP password"
    echo "  domain: iFastNet domain or IP address"
    exit 1
}

# Check if the correct number of arguments are provided
if [ "$#" -ne 5 ]; then
    usage
fi

SOURCE_DIR=$1
DEST_DIR=$2
USERNAME=$3
PASSWORD=$4
DOMAIN=$5

# Error handling for source directory
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Transfer files using FTP
ftp -inv $DOMAIN <<EOF
user $USERNAME $PASSWORD
lcd $SOURCE_DIR
cd $DEST_DIR
prompt
mput *
bye
EOF

# Check if the transfer was successful
if [ $? -eq 0 ]; then
    echo "Website transferred successfully to $DOMAIN/$DEST_DIR."
else
    echo "Error: Transfer failed."
    exit 1
fi
```

### To run the script:
```bash
chmod +x transfer_website.sh
./transfer_website.sh /path/to/local/website public_html your_username your_password your_domain
```
