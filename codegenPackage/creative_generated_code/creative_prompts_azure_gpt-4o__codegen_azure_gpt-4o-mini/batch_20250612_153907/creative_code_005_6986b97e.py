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

# Define a function to recursively list files in a directory
# and format them in a table-like structure
list_files() {
    local dir="$1"
    
    # Check if the provided argument is a directory
    if [[ ! -d "$dir" ]]; then
        echo "Error: '$dir' is not a valid directory." >&2
        return 1
    fi

    # Print the header of the table
    printf "%-50s %-10s %-20s\n" "Filename" "Size (KB)" "Last Modified"
    printf "%-50s %-10s %-20s\n" "----------------------------------" "----------" "--------------------"

    # Use find to recursively locate files and format their details
    while IFS= read -r -d '' file; do
        # Get the size of the file in KB
        size_kb=$(du -k "$file" | cut -f1)
        # Get the last modified date of the file
        last_modified=$(date -r "$file" +"%Y-%m-%d %H:%M:%S")
        
        # Print the file details in a formatted manner
        printf "%-50s %-10s %-20s\n" "$(basename "$file")" "$size_kb" "$last_modified"
    done < <(find "$dir" -type f -print0)
}

# Check if the script is executed with the required arguments
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <directory-path>"
    exit 1
fi

# Call the function with the provided directory path
list_files "$1"
```
