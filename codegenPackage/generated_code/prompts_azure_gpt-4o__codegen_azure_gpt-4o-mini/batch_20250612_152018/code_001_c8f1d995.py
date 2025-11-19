"""
Generated Code Metadata:
========================
Original URL: https://refconegypt.net
Prompt: Create a Bash script to recursively display the contents of a directory, including file sizes and last modified dates, as seen in the directory listing on https://refconegypt.net.
Generated: DETERMINISTIC_c8f1d995faab265f
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to recursively display the contents of a directory
# including file sizes and last modified dates.

# Function to display directory contents
display_directory_contents() {
    local dir="$1"

    # Check if the provided argument is a directory
    if [[ ! -d "$dir" ]]; then
        echo "Error: '$dir' is not a valid directory."
        return 1
    fi

    # Loop through each item in the directory
    for item in "$dir"/*; do
        # Check if the item exists (handles empty directories)
        if [[ -e "$item" ]]; then
            # Get the file size and last modified date
            local size
            local modified_date
            size=$(stat -c%s "$item")
            modified_date=$(stat -c%y "$item")

            # Display the item details
            echo "Name: $(basename "$item")"
            echo "Size: $size bytes"
            echo "Last Modified: $modified_date"
            echo ""

            # If the item is a directory, call the function recursively
            if [[ -d "$item" ]]; then
                display_directory_contents "$item"
            fi
        fi
    done
}

# Main script execution
# Check if a directory is provided as an argument
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Call the function with the provided directory
display_directory_contents "$1"
```

### Usage
To run the script, save it to a file (e.g., `list_directory.sh`), give it execute permissions with `chmod +x list_directory.sh`, and execute it by passing a directory path as an argument:

```bash
./list_directory.sh /path/to/directory
```
