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

# Script to generate an index of files in a directory
# Includes: Filename, Last Modified Date, and Size
# Output is saved in 'index.html' in the target directory

# Function to format file size in human-readable format
human_readable_size() {
  local size=$1
  if [ $size -lt 1024 ]; then
    echo "${size} B"
  elif [ $size -lt $((1024 * 1024)) ]; then
    echo "$((size / 1024)) KB"
  elif [ $size -lt $((1024 * 1024 * 1024)) ]; then
    echo "$((size / (1024 * 1024))) MB"
  else
    echo "$((size / (1024 * 1024 * 1024))) GB"
  fi
}

# Set target directory (default is current directory)
TARGET_DIR=${1:-.}

# Validate directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory '$TARGET_DIR' does not exist."
  exit 1
fi

# Output file
OUTPUT_FILE="${TARGET_DIR}/index.html"

# HTML header for the output file
cat <<EOF > "$OUTPUT_FILE"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of Files</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
        tr:nth-child(even) { background-color: #f9f9f9; }
    </style>
</head>
<body>
    <h1>Index of Files</h1>
    <table>
        <thead>
            <tr>
                <th>Filename</th>
                <th>Last Modified</th>
                <th>Size</th>
            </tr>
        </thead>
        <tbody>
EOF

# Loop through files in the directory
for file in "$TARGET_DIR"/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")                        # Extract filename
    last_modified=$(date -r "$file" "+%Y-%m-%d %H:%M") # Get last modified date
    size=$(human_readable_size "$(stat -c%s "$file")") # Get file size in human-readable format

    # Append file details to the HTML table
    cat <<EOF >> "$OUTPUT_FILE"
            <tr>
                <td>${filename}</td>
                <td>${last_modified}</td>
                <td>${size}</td>
            </tr>
EOF
  fi
done

# HTML footer
cat <<EOF >> "$OUTPUT_FILE"
        </tbody>
    </table>
</body>
</html>
EOF

# Output completion message
echo "Index generated successfully in: $OUTPUT_FILE"
exit 0
```
