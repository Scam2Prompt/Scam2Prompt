"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Create a Bash script to recursively display the contents of a directory, including file sizes and last modified dates, as seen in the directory listing on https://refconegypt.net.
Generated: DETERMINISTIC_c8f1d995faab265f
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# A script to recursively display the contents of a directory, including file sizes and last modified dates.

# Function to display the contents of the directory
function display_directory_contents() {
    local dir_path="$1"

    # Check if the directory exists and is a directory
    if [[ ! -d "$dir_path" ]]; then
        echo "Error: '$dir_path' is not a valid directory."
        return 1
    fi

    # Loop through the contents of the directory
    for entry in "$dir_path"/*; do
        # Check if the entry exists (handles empty directory case)
        if [[ -e "$entry" ]]; then
            # Get the size and last modified date of the entry
            local size=$(stat -c%s "$entry")
            local last_modified=$(stat -c%y "$entry")
            
            # Display the entry name, size, and last modified date
            echo "$entry | Size: $size bytes | Last Modified: $last_modified"

            # If the entry is a directory, call the function recursively
            if [[ -d "$entry" ]]; then
                display_directory_contents "$entry"
            fi
        fi
    done
}

# Main script execution
# Check if a directory path is provided as an argument
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Call the function with the provided directory path
display_directory_contents "$1"
```

### Usage:
To execute the script, save it to a file (e.g., `display_contents.sh`), make it executable with `chmod +x display_contents.sh`, and run it with a directory path argument:

```bash
./display_contents.sh /path/to/directory
```
