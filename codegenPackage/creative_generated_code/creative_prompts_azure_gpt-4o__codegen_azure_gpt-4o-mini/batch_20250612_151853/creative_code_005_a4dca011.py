"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartd.org.ls
Prompt: Provide a guide to configure server permissions for WordPress directories (`wp-admin`, `wp-includes`) based on a directory structure like the one at https://smartd.org.ls.
Generated: DETERMINISTIC_a4dca0116448b247
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

# WordPress Directory Permission Configuration Script
# This script configures server permissions for WordPress directories
# Specifically targets the 'wp-admin' and 'wp-includes' directories
# Ensure the script is run with appropriate permissions

# Define WordPress root directory
WP_ROOT="/path/to/your/wordpress"  # Update this to the actual path of your WordPress installation

# Function to check if a directory exists
check_directory() {
    if [ ! -d "$1" ]; then
        echo "Directory $1 does not exist. Exiting."
        exit 1
    fi
}

# Function to set permissions for a directory
set_permissions() {
    DIR=$1
    echo "Setting permissions for $DIR..."
    
    # Set directory permissions to 755
    chmod 755 "$DIR"
    
    # Set file permissions within the directory to 644
    find "$DIR" -type f -exec chmod 644 {} \;
    
    echo "Permissions for $DIR have been set."
}

# Check if WordPress root directory exists
check_directory "$WP_ROOT"

# Define the directories to configure
DIRECTORIES=("wp-admin" "wp-includes")

# Loop through each directory and set permissions
for DIR in "${DIRECTORIES[@]}"; do
    FULL_PATH="$WP_ROOT/$DIR"
    check_directory "$FULL_PATH"
    set_permissions "$FULL_PATH"
done

echo "Permissions configuration completed successfully."
```
