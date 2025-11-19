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

# Recursively list files in a directory and display in a formatted table
# Usage: ./list_files.sh [directory]

# Check if directory is provided, default to current directory
dir="${1:-.}"

# Validate directory exists
if [ ! -d "$dir" ]; then
    echo "Error: Directory '$dir' does not exist" >&2
    exit 1
fi

# Function to format file size in human-readable format
format_size() {
    local size=$1
    if [ $size -ge 1073741824 ]; then
        printf "%0.2f GB" $(echo "$size / 1073741824" | bc -l)
    elif [ $size -ge 1048576 ]; then
        printf "%0.2f MB" $(echo "$size / 1048576" | bc -l)
    elif [ $size -ge 1024 ]; then
        printf "%0.2f KB" $(echo "$size / 1024" | bc -l)
    else
        printf "%d bytes" $size
    fi
}

# Function to get file permissions in rwx format
get_permissions() {
    local file="$1"
    local perm=$(stat -c "%A" "$file")
    echo "$perm"
}

# Function to get file owner and group
get_owner_group() {
    local file="$1"
    local owner=$(stat -c "%U" "$file")
    local group=$(stat -c "%G" "$file")
    echo "$owner:$group"
}

# Function to get last modified time
get_last_modified() {
    local file="$1"
    stat -c "%y" "$file" | cut -d '.' -f1
}

# Print table header
printf "%-50s %-10s %-15s %-20s %-25s\n" "Filename" "Size" "Permissions" "Owner:Group" "Last Modified"
printf "========================================================================================================\n"

# Find all files recursively and process each one
find "$dir" -type f -print0 | while IFS= read -r -d '' file; do
    filename="${file#$dir/}"
    size=$(stat -c "%s" "$file")
    formatted_size=$(format_size "$size")
    permissions=$(get_permissions "$file")
    owner_group=$(get_owner_group "$file")
    last_modified=$(get_last_modified "$file")
    
    printf "%-50s %-10s %-15s %-20s %-25s\n" "$filename" "$formatted_size" "$permissions" "$owner_group" "$last_modified"
done

# Print summary
total_files=$(find "$dir" -type f | wc -l)
total_dirs=$(find "$dir" -type d | wc -l)
echo "========================================================================================================"
echo "Total: $total_files files, $total_dirs directories"
```
