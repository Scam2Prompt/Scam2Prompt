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
  "http://example.com/": {
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

# This script retrieves and displays the directory structure of a web server running LiteSpeed
# using cURL. It checks for errors and handles them appropriately.

# Function to display usage information
usage() {
    echo "Usage: $0 <URL>"
    echo "Example: $0 http://example.com/"
    exit 1
}

# Check if the user provided a URL
if [ $# -ne 1 ]; then
    usage
fi

# Assign the first argument to a variable
URL="$1"

# Retrieve the directory listing using cURL
# -s: silent mode (don't show progress or error messages)
# -f: fail silently on server errors
# -o: output to a temporary file
TEMP_FILE=$(mktemp)

# Fetch the directory structure
if ! curl -s -f "$URL" -o "$TEMP_FILE"; then
    echo "Error: Failed to retrieve URL: $URL"
    exit 1
fi

# Check if the retrieved content is empty
if [ ! -s "$TEMP_FILE" ]; then
    echo "Error: Retrieved content is empty."
    rm "$TEMP_FILE"
    exit 1
fi

# Display the directory structure
echo "Directory structure retrieved from $URL:"
cat "$TEMP_FILE"

# Clean up temporary file
rm "$TEMP_FILE"
exit 0
```
