"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Write a Bash script to automate the process of updating a directory listing, similar to the one on https://elisium.it, and include error handling for non-existent directories.
Generated: DETERMINISTIC_e8dac2b7a466a2a1
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to update a directory listing and save it to a file
# Usage: ./update_directory_listing.sh <directory_path> <output_file>

# Function to display usage information
usage() {
    echo "Usage: $0 <directory_path> <output_file>"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Error: Invalid number of arguments."
    usage
fi

# Assign input arguments to variables
DIRECTORY_PATH="$1"
OUTPUT_FILE="$2"

# Check if the specified directory exists
if [ ! -d "$DIRECTORY_PATH" ]; then
    echo "Error: Directory '$DIRECTORY_PATH' does not exist."
    exit 1
fi

# Create or clear the output file
> "$OUTPUT_FILE"

# Update the directory listing and save it to the output file
{
    echo "Directory Listing for: $DIRECTORY_PATH"
    echo "Generated on: $(date)"
    echo "-----------------------------------"
    ls -l "$DIRECTORY_PATH"
} >> "$OUTPUT_FILE"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "Directory listing updated successfully in '$OUTPUT_FILE'."
else
    echo "Error: Failed to update directory listing."
    exit 1
fi
```
