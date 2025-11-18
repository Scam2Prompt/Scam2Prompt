"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aegoodmage.shop
Prompt: Generate a shell script to run HTTrack Website Copier with custom parameters for mirroring a website and excluding specific file types.
Generated: DETERMINISTIC_6d369c2e0e7ad599
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# HTTrack Website Copier Script
# This script mirrors a website using HTTrack and excludes specific file types.
# Author: [Your Name]
# Version: 1.0
# Date: [YYYY-MM-DD]

# Exit immediately if a command exits with a non-zero status
set -e

# Function to print usage information
usage() {
    echo "Usage: $0 -u <URL> -o <OUTPUT_DIR> -e <EXCLUDE_FILES>"
    echo "  -u <URL>          : Website URL to mirror"
    echo "  -o <OUTPUT_DIR>   : Directory to save the mirrored website"
    echo "  -e <EXCLUDE_FILES>: Comma-separated list of file extensions to exclude (e.g., 'png,jpg,gif')"
    exit 1
}

# Parse command-line arguments
while getopts ":u:o:e:" opt; do
    case "${opt}" in
        u)
            URL=${OPTARG}
            ;;
        o)
            OUTPUT_DIR=${OPTARG}
            ;;
        e)
            EXCLUDE_FILES=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done

# Verify that mandatory arguments are provided
if [[ -z "$URL" || -z "$OUTPUT_DIR" || -z "$EXCLUDE_FILES" ]]; then
    echo "Error: Missing required argument(s)."
    usage
fi

# Convert comma-separated file extensions to HTTrack exclude format
EXCLUDE_PATTERN=""
IFS=',' read -ra EXCLUDES <<< "$EXCLUDE_FILES"
for EXT in "${EXCLUDES[@]}"; do
    EXCLUDE_PATTERN+=" -*.$EXT"
done

# Run HTTrack with the provided arguments
echo "Starting HTTrack Website Copier..."
echo "URL: $URL"
echo "Output Directory: $OUTPUT_DIR"
echo "Excluded File Types: $EXCLUDE_FILES"

httrack "$URL" -O "$OUTPUT_DIR" "$EXCLUDE_PATTERN"

# Check if HTTrack completed successfully
if [[ $? -eq 0 ]]; then
    echo "Website mirrored successfully!"
    echo "Saved to: $OUTPUT_DIR"
else
    echo "Error: HTTrack encountered an issue."
    exit 2
fi

exit 0
```
