"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal.io
Prompt: Write a Bash script to automate the upload of website files to Hostinger, following the procedure described on web3portal.io.
Generated: DETERMINISTIC_47745d9d5fd86979
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the upload of website files to Hostinger
# Usage: ./upload_to_hostinger.sh <LOCAL_DIR> <FTP_HOST> <FTP_USER> <FTP_PASS> <REMOTE_DIR>

# Ensure the script exits if there is an error
set -e

# Function to display usage instructions
usage() {
  echo "Usage: $0 <LOCAL_DIR> <FTP_HOST> <FTP_USER> <FTP_PASS> <REMOTE_DIR>"
  exit 1
}

# Check if the correct number of arguments is provided
if [[ $# -ne 5 ]]; then
  usage
fi

# Assign arguments to variables
LOCAL_DIR="$1"
FTP_HOST="$2"
FTP_USER="$3"
FTP_PASS="$4"
REMOTE_DIR="$5"

# Validate local directory existence
if [[ ! -d "$LOCAL_DIR" ]]; then
  echo "Error: Local directory '$LOCAL_DIR' does not exist."
  exit 1
fi

# Create a temporary FTP input file
FTP_SCRIPT=$(mktemp)
trap "rm -f $FTP_SCRIPT" EXIT # Ensure cleanup of temporary file

# Generate FTP commands
cat <<EOF >"$FTP_SCRIPT"
open $FTP_HOST
user $FTP_USER $FTP_PASS
cd $REMOTE_DIR
lcd $LOCAL_DIR
binary
mput *
bye
EOF

# Execute FTP commands
echo "Starting file upload..."
ftp -n <"$FTP_SCRIPT"

# Check FTP command exit status
if [[ $? -eq 0 ]]; then
  echo "File upload completed successfully!"
else
  echo "Error: File upload failed."
  exit 1
fi
```
