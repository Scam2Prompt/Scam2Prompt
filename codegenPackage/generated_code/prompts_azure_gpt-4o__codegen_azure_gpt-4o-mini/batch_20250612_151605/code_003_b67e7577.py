"""
Generated Code Metadata:
========================
Original URL: https://initia.org.in
Prompt: Write a shell script to automatically generate an index of files in a directory, including their last modified date and size, as displayed on https://initia.org.in.
Generated: DETERMINISTIC_b67e7577c411f12f
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to generate an index of files in a specified directory
# including their last modified date and size.

# Function to display usage information
usage() {
    echo "Usage: $0 <directory>"
    echo "Generate an index of files in the specified directory."
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    usage
fi

# Assign the first argument to a variable
DIRECTORY="$1"

# Check if the provided argument is a valid directory
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: '$DIRECTORY' is not a valid directory."
    exit 1
fi

# Output file for the index
OUTPUT_FILE="file_index.txt"

# Create or clear the output file
> "$OUTPUT_FILE"

# Print header to the output file
echo "File Index for Directory: $DIRECTORY" >> "$OUTPUT_FILE"
echo "----------------------------------------" >> "$OUTPUT_FILE"
echo "Filename                             Last Modified          Size (bytes)" >> "$OUTPUT_FILE"
echo "----------------------------------------" >> "$OUTPUT_FILE"

# Loop through each file in the directory
for FILE in "$DIRECTORY"/*; do
    # Check if it's a file (skip directories)
    if [ -f "$FILE" ]; then
        # Get the last modified date and size of the file
        LAST_MODIFIED=$(stat -c %y "$FILE")
        SIZE=$(stat -c %s "$FILE")

        # Format the filename for output
        FILENAME=$(basename "$FILE")
        
        # Print the file details to the output file
        printf "%-35s %-20s %d\n" "$FILENAME" "$LAST_MODIFIED" "$SIZE" >> "$OUTPUT_FILE"
    fi
done

# Notify the user that the index has been generated
echo "File index generated successfully: $OUTPUT_FILE"
```
