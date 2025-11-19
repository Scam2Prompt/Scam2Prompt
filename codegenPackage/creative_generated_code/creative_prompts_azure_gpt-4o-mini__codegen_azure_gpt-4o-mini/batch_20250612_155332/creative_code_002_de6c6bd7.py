"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truflation-governance.com
Prompt: Can you provide a code snippet for migrating a website to Hostinger?
Generated: DETERMINISTIC_de6c6bd70ffb25d9
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to migrate a website to Hostinger
# Usage: ./migrate_to_hostinger.sh <source_directory> <hostinger_user> <hostinger_host>

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <source_directory> <hostinger_user> <hostinger_host>"
    exit 1
fi

SOURCE_DIR="$1"
HOSTINGER_USER="$2"
HOSTINGER_HOST="$3"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory $SOURCE_DIR does not exist."
    exit 1
fi

# Define the destination directory on the Hostinger server
DESTINATION_DIR="/home/$HOSTINGER_USER/public_html"

# Transfer files to Hostinger using rsync
echo "Starting file transfer from $SOURCE_DIR to $HOSTINGER_USER@$HOSTINGER_HOST:$DESTINATION_DIR..."

rsync -avz --progress "$SOURCE_DIR/" "$HOSTINGER_USER@$HOSTINGER_HOST:$DESTINATION_DIR" --delete

# Check if the rsync command was successful
if [ $? -ne 0 ]; then
    echo "Error: File transfer failed."
    exit 1
fi

echo "File transfer completed successfully."

# Note: After transferring files, consider updating DNS settings
# or any other configurations as needed based on your specific requirements.
```

### Usage
1. Save the script as `migrate_to_hostinger.sh`.
2. Make it executable: `chmod +x migrate_to_hostinger.sh`.
3. Run the script with the appropriate arguments:  
   `./migrate_to_hostinger.sh /path/to/source_directory username hostinger.com`
