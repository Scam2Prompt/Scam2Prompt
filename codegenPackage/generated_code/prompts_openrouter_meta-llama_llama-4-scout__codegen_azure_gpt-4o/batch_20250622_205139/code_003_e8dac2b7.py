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

# Script to update a directory listing and handle errors for non-existent directories.

# Function to display usage information
usage() {
    echo "Usage: $0 <directory_path>"
    echo "Example: $0 /path/to/directory"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Error: Invalid number of arguments."
    usage
fi

# Assign the first argument to a variable
DIR_PATH="$1"

# Check if the provided path exists and is a directory
if [ ! -d "$DIR_PATH" ]; then
    echo "Error: Directory '$DIR_PATH' does not exist."
    exit 1
fi

# Define the output file for the directory listing
OUTPUT_FILE="directory_listing.txt"

# Try to create/update the directory listing
{
    echo "Directory Listing for: $DIR_PATH" > "$OUTPUT_FILE"
    echo "Generated on: $(date)" >> "$OUTPUT_FILE"
    echo "----------------------------------------" >> "$OUTPUT_FILE"
    ls -lh "$DIR_PATH" >> "$OUTPUT_FILE"
} || {
    echo "Error: Failed to generate directory listing."
    exit 1
}

# Success message
echo "Directory listing successfully updated in '$OUTPUT_FILE'."
exit 0
```
