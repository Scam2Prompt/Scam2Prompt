"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syr-whistler.com
Prompt: Generate a Bash script to list all files in a "cgi-bin" directory and check their execution permissions.
Generated: DETERMINISTIC_4de45e9978eba4ad
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script lists all files in the "cgi-bin" directory and checks their execution permissions.

# Set the cgi-bin directory path
CGI_BIN_DIR="./cgi-bin"

# Check if the cgi-bin directory exists
if [ ! -d "$CGI_BIN_DIR" ]; then
    echo "Error: Directory '$CGI_BIN_DIR' does not exist."
    exit 1
fi

# List files in the cgi-bin directory
echo "Listing files in '$CGI_BIN_DIR' and checking execution permissions:"
echo "---------------------------------------------------------------"

# Loop through each file in the cgi-bin directory
for file in "$CGI_BIN_DIR"/*; do
    # Check if it's a file
    if [ -f "$file" ]; then
        # Check if the file has execution permissions
        if [ -x "$file" ]; then
            echo "$(basename "$file"): Executable"
        else
            echo "$(basename "$file"): Not executable"
        fi
    fi
done

echo "---------------------------------------------------------------"
echo "Check completed."
```
