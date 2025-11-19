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

# Function to print file details in a formatted table
print_file_details() {
  local directory=$1
  local indent=$2

  # Check if directory exists
  if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    return 1
  fi

  # Get list of files and directories
  local files_and_dirs=($(ls -a "$directory"))

  # Print directory header
  printf "%s%s\n" "$indent" "$(basename "$directory")/"

  # Print file details
  printf "%s%s%10s %10s %s\n" "$indent" "Name" "Size" "Date" "Time"
  for file_or_dir in "${files_and_dirs[@]}"; do
    # Skip current and parent directories
    if [ "$file_or_dir" = "." ] || [ "$file_or_dir" = ".." ]; then
      continue
    fi

    local full_path="$directory/$file_or_dir"
    local file_type=$(stat -c "%F" "$full_path")

    if [ "$file_type" = "directory" ]; then
      # Recursively list files in subdirectory
      print_file_details "$full_path" "${indent}  "
    else
      local file_size=$(stat -c "%s" "$full_path")
      local file_date=$(date +"%Y-%m-%d" -r "$full_path")
      local file_time=$(date +"%H:%M" -r "$full_path")

      printf "%s  %s%10d %10s %s\n" "$indent" "$file_or_dir" "$file_size" "$file_date" "$file_time"
    fi
  done
}

# Main function
main() {
  if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    return 1
  fi

  local directory=$1
  print_file_details "$directory" ""
}

# Call main function
main "$1"
```

```bash
# Usage example:
# Save this script to a file (e.g., list_files.sh), make it executable with `chmod +x list_files.sh`, and run it with `./list_files.sh /path/to/directory`
```
