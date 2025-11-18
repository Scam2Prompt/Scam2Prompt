"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drop-news-afe2f.web.app
Prompt: Provide an example of using HTTrack Website Copier to download a website with specific filters to exclude certain file types (e.g., .mp4 or .jpg).
Generated: DETERMINISTIC_92d07db491134722
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# HTTrack Website Copier script to download a website while excluding specific file types.
# Usage: ./download_website.sh <URL> <OUTPUT_DIR>

# Check if the correct number of arguments is passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <OUTPUT_DIR>"
    exit 1
fi

# Assigning arguments to variables
URL=$1
OUTPUT_DIR=$2

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# HTTrack command to download the website
# -q: quiet mode (less output)
# -P: set project name
# --exclude: exclude specific file types
httrack "$URL" -O "$OUTPUT_DIR" -q \
    --exclude '*.mp4' \
    --exclude '*.jpg' \
    --exclude '*.jpeg' \
    --exclude '*.gif' \
    --exclude '*.png' \
    --exclude '*.zip' \
    --exclude '*.tar' \
    --exclude '*.gz' \
    --exclude '*.rar' \
    --exclude '*.exe' \
    --exclude '*.pdf'

# Check if the httrack command was successful
if [ $? -eq 0 ]; then
    echo "Website downloaded successfully to $OUTPUT_DIR."
else
    echo "Error downloading the website. Please check the URL and your HTTrack installation."
    exit 1
fi
```

### How to Use:
1. Save the script as `download_website.sh`.
2. Make it executable with `chmod +x download_website.sh`.
3. Run the script using `./download_website.sh <URL> <OUTPUT_DIR>`.
