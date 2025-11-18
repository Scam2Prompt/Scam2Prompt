"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Generate a Bash script to retrieve and display the directory structure from a web server running LiteSpeed, using cURL or wget.
Generated: DETERMINISTIC_c22ed86a4a585257
Batch ID: 20250612_151525
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to retrieve and display the directory structure from a LiteSpeed web server
# using cURL or wget.

# Exit immediately if any command exits with a non-zero status
set -e

# Function to display usage information
usage() {
    echo "Usage: $0 <URL>"
    echo "Example: $0 http://example.com"
    exit 1
}

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    usage
fi

# URL of the LiteSpeed web server to query
URL="$1"

# Validate that the URL starts with http:// or https://
if [[ ! "$URL" =~ ^https?:// ]]; then
    echo "Error: Invalid URL format. URL must start with http:// or https://"
    exit 1
fi

# Temporary file to store the HTML content
TEMP_FILE=$(mktemp)

# Clean up the temporary file on script exit
trap "rm -f $TEMP_FILE" EXIT

# Use cURL or wget to retrieve the directory listing from the server
if command -v curl &> /dev/null; then
    # Using cURL
    curl -s "$URL" -o "$TEMP_FILE"
elif command -v wget &> /dev/null; then
    # Using wget
    wget -q "$URL" -O "$TEMP_FILE"
else
    echo "Error: Neither cURL nor wget is installed on this system."
    exit 1
fi

# Extract and display the directory structure
echo "Directory structure retrieved from $URL:"
grep -oP '(?<=href=")[^"]+' "$TEMP_FILE" | grep -vE '^https?://' | sort -u

# End of script
```
