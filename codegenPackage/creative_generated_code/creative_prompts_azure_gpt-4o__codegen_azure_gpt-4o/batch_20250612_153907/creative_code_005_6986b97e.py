"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consejodigitalmx.com
Prompt: Write a shell script to recursively list all files in a directory, similar to the structure shown in `Index of /`, and output their details in a formatted table.
Generated: DETERMINISTIC_6986b97e7cc6808e
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to recursively list all files in a directory and output their details in a formatted table.

# Function to check if the correct number of arguments is provided
function usage() {
    echo "Usage: $0 <directory_path>"
    exit 1
}

# Ensure the user provides a directory path as an argument
if [[ $# -ne 1 ]]; then
    usage
fi

# Assign the first argument to a variable
DIR_PATH=$1

# Check if the provided path is a valid directory
if [[ ! -d "$DIR_PATH" ]]; then
    echo "Error: '$DIR_PATH' is not a valid directory."
    exit 1
fi

# Print the header for the table
printf "%-50s %-10s %-20s %-10s\n" "File Path" "Size (KB)" "Last Modified" "Type"
printf "%-50s %-10s %-20s %-10s\n" "----------" "---------" "-------------" "----"

# Function to recursively list files and output their details
function list_files() {
    local directory="$1"

    # Iterate over all files and subdirectories in the current directory
    for file in "$directory"/*; do
        if [[ -f "$file" ]]; then
            # If it's a file, get its details
            local size=$(du -k "$file" | cut -f 1)        # File size in KB
            local modified_date=$(stat -c "%y" "$file" | cut -d '.' -f 1) # Last modified date
            local file_type=$(file -b "$file")           # File type description

            # Print file details in table format
            printf "%-50s %-10s %-20s %-10s\n" "$file" "$size" "$modified_date" "$file_type"
        elif [[ -d "$file" ]]; then
            # If it's a directory, recursively call the function
            list_files "$file"
        fi
    done
}

# Call the recursive function on the provided directory path
list_files "$DIR_PATH"

exit 0
```
