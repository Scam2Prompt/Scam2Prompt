"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Create a script in Bash to download and organize photos from a specific aviation event covered by Spotters Brasil, using wget and imagemagick.
Generated: DETERMINISTIC_90a2242bf51fb8be
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to download and organize photos from Spotters Brasil aviation events
# Usage: ./spotters_downloader.sh <event_url> <output_directory>

# Check if required arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Error: Invalid number of arguments."
    echo "Usage: $0 <event_url> <output_directory>"
    exit 1
fi

EVENT_URL="$1"
OUTPUT_DIR="$2"

# Check if wget and imagemagick are installed
if ! command -v wget &> /dev/null; then
    echo "Error: wget is not installed. Please install it first."
    exit 1
fi

if ! command -v convert &> /dev/null; then
    echo "Error: ImageMagick is not installed. Please install it first."
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR" || {
    echo "Error: Failed to create output directory."
    exit 1
}

# Temporary directory for downloads
TEMP_DIR=$(mktemp -d) || {
    echo "Error: Failed to create temporary directory."
    exit 1
}

# Function to clean up temporary files
cleanup() {
    rm -rf "$TEMP_DIR"
    echo "Cleaned up temporary files."
}

trap cleanup EXIT

# Download images from the event page
echo "Downloading images from $EVENT_URL..."
wget --recursive --level=1 --no-parent --no-directories --accept "*.jpg,*.jpeg,*.png" --directory-prefix="$TEMP_DIR" "$EVENT_URL" || {
    echo "Error: Failed to download images."
    exit 1
}

# Process downloaded images
echo "Processing downloaded images..."
for img in "$TEMP_DIR"/*; do
    if [ -f "$img" ]; then
        # Get image metadata
        img_date=$(identify -format "%[EXIF:DateTimeOriginal]" "$img" 2>/dev/null)
        
        if [ -z "$img_date" ]; then
            img_date=$(date -r "$img" "+%Y-%m-%d")
        else
            img_date=$(echo "$img_date" | cut -d' ' -f1 | tr ':' '-')
        fi
        
        # Create date directory if it doesn't exist
        date_dir="$OUTPUT_DIR/$img_date"
        mkdir -p "$date_dir" || {
            echo "Warning: Failed to create directory $date_dir. Skipping..."
            continue
        }
        
        # Resize and optimize image
        filename=$(basename "$img")
        output_path="$date_dir/${filename%.*}_optimized.jpg"
        
        convert "$img" -resize 1920x1080\> -quality 85 -strip "$output_path" || {
            echo "Warning: Failed to process image $img. Skipping..."
            continue
        }
    fi
done

echo "Download and processing complete. Images saved to $OUTPUT_DIR"
```
