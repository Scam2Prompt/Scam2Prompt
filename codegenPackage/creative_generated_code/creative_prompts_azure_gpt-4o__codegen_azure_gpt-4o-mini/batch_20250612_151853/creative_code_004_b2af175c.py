"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartd.org.ls
Prompt: Write a Bash script to automate the cleanup of unused files in a WordPress directory listing, such as the one displayed at https://smartd.org.ls.
Generated: DETERMINISTIC_b2af175c293c67d2
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# WordPress Cleanup Script
# This script automates the cleanup of unused files in a specified WordPress directory.
# It identifies files that have not been accessed in the past 30 days and prompts the user for deletion.

# Configuration
WP_DIR="/path/to/your/wordpress/directory"  # Change this to your WordPress directory
DAYS_THRESHOLD=30  # Number of days to consider a file as unused

# Check if the specified directory exists
if [[ ! -d "$WP_DIR" ]]; then
    echo "Error: Directory $WP_DIR does not exist."
    exit 1
fi

# Find and list unused files
echo "Searching for files not accessed in the last $DAYS_THRESHOLD days in $WP_DIR..."
unused_files=$(find "$WP_DIR" -type f -atime +$DAYS_THRESHOLD)

# Check if there are any unused files
if [[ -z "$unused_files" ]]; then
    echo "No unused files found in $WP_DIR."
    exit 0
fi

# Display the list of unused files
echo "The following unused files were found:"
echo "$unused_files"

# Prompt user for confirmation before deletion
read -p "Do you want to delete these files? (y/n): " confirm

if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
    # Delete the unused files
    echo "Deleting unused files..."
    echo "$unused_files" | xargs rm -f

    # Check if the deletion was successful
    if [[ $? -eq 0 ]]; then
        echo "Unused files deleted successfully."
    else
        echo "Error occurred during deletion."
        exit 1
    fi
else
    echo "Deletion of unused files canceled."
    exit 0
fi
```

**Note:** Be sure to replace `/path/to/your/wordpress/directory` with the actual path to your WordPress installation before running the script. Always test scripts in a safe environment before deploying them in production.
