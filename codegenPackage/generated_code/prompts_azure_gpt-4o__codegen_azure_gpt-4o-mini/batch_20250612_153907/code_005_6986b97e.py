"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Write a shell script to recursively list all files in a directory, similar to the structure shown in `Index of /`, and output their details in a formatted table.
Generated: DETERMINISTIC_6986b97e7cc6808e
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Function to display the header of the table
print_header() {
    printf "%-50s %-20s %-10s\n" "File/Directory Name" "Last Modified" "Size (Bytes)"
    printf "%-50s %-20s %-10s\n" "--------------------------------------------------" "--------------------" "----------"
}

# Function to recursively list files and directories
list_files() {
    local dir="$1"
    
    # Check if the directory exists
    if [[ ! -d "$dir" ]]; then
        echo "Error: '$dir' is not a valid directory."
        exit 1
    fi

    # Loop through each item in the directory
    for item in "$dir"/*; do
        # Check if the item exists (in case of empty directories)
        if [[ -e "$item" ]]; then
            # Get the last modified time and size
            local modified_time
            local size
            modified_time=$(stat -c "%y" "$item")
            size=$(stat -c "%s" "$item")

            # Print the details in a formatted table
            printf "%-50s %-20s %-10s\n" "$(basename "$item")" "$modified_time" "$size"

            # If the item is a directory, call the function recursively
            if [[ -d "$item" ]]; then
                list_files "$item"
            fi
        fi
    done
}

# Main script execution
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Print the header
print_header

# Call the function with the provided directory
list_files "$1"
```
