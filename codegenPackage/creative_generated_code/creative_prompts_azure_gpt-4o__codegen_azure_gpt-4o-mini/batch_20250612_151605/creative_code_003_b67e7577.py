"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Write a shell script to automatically generate an index of files in a directory, including their last modified date and size, as displayed on https://initia.org.in.
Generated: DETERMINISTIC_b67e7577c411f12f
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script generates an index of files in a specified directory.
# It includes the file name, last modified date, and size in bytes.

# Function to display usage information
usage() {
    echo "Usage: $0 <directory>"
    echo "Generates an index of files in the specified directory."
    exit 1
}

# Check if a directory argument is provided
if [ $# -ne 1 ]; then
    usage
fi

# Assign the first argument to a variable
DIRECTORY="$1"

# Check if the provided argument is a directory
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: $DIRECTORY is not a valid directory."
    exit 1
fi

# Output file for the index
INDEX_FILE="file_index.txt"

# Create or clear the index file
> "$INDEX_FILE"

# Write the header for the index file
echo "File Index for Directory: $DIRECTORY" > "$INDEX_FILE"
echo "--------------------------------" >> "$INDEX_FILE"
echo "Filename                     Last Modified             Size (bytes)" >> "$INDEX_FILE"
echo "--------------------------------" >> "$INDEX_FILE"

# Iterate through the files in the specified directory
for FILE in "$DIRECTORY"/*; do
    # Check if it is a file
    if [ -f "$FILE" ]; then
        # Get the last modified date and size of the file
        LAST_MODIFIED=$(stat -c %y "$FILE")
        FILE_SIZE=$(stat -c %s "$FILE")

        # Format the output and append it to the index file
        printf "%-30s %-25s %s\n" "$(basename "$FILE")" "$LAST_MODIFIED" "$FILE_SIZE" >> "$INDEX_FILE"
    fi
done

# Notify the user that the index has been generated
echo "File index has been generated: $INDEX_FILE"
```
