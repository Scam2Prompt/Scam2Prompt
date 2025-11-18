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

# Bash script to list all files in the "cgi-bin" directory 
# and check their execution permissions.

# Set the directory to check
CGI_BIN_DIR="./cgi-bin"

# Check if the directory exists
if [[ ! -d "$CGI_BIN_DIR" ]]; then
  echo "Directory '$CGI_BIN_DIR' does not exist."
  exit 1
fi

# Iterate over all files in the directory
echo "Checking files in '$CGI_BIN_DIR':"
for file in "$CGI_BIN_DIR"/*; do
  # Skip if it's not a regular file
  if [[ ! -f "$file" ]]; then
    continue
  fi
  
  # Check for execution permission
  if [[ -x "$file" ]]; then
    echo "$(basename "$file") - Executable"
  else
    echo "$(basename "$file") - Not executable"
  fi
done

exit 0
```
