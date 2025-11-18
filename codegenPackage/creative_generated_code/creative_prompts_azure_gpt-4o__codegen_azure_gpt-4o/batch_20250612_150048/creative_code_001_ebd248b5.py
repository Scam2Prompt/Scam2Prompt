"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamak.lagunaproductions.net
Prompt: Generate a Bash script to recursively download all files from an Apache directory index like the one at https://mestamak.lagunaproductions.net using `wget`.
Generated: DETERMINISTIC_ebd248b5a6d4bfe1
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to recursively download all files from an Apache directory index using wget

# Check if a URL is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL of the Apache directory index
URL=$1

# Output directory for downloaded files
OUTPUT_DIR="downloaded_files"

# Create the output directory if it doesn't exist
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
fi

# Run wget to recursively download all files
wget_options=(
    --recursive       # Recursively download files
    --no-parent       # Do not ascend to parent directories
    --no-clobber      # Avoid overwriting existing files
    --reject "index.html*" # Skip downloading index.html files
    --directory-prefix="$OUTPUT_DIR" # Save files to the specified output directory
)

# Execute wget with error handling
if ! wget "${wget_options[@]}" "$URL"; then
    echo "Error: Failed to download files from $URL"
    exit 2
fi

# Inform the user of successful completion
echo "Download complete. Files are saved in '$OUTPUT_DIR'."
```
