"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icomain.top
Prompt: What are the steps to delete or overwrite the automatically generated index.html page in a web project?
Generated: DETERMINISTIC_0789a7b5c0de57f5
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to delete or overwrite the automatically generated index.html page in a web project

# Usage: ./manage_index.sh [delete|overwrite] [new_content_file]

# Function to display usage information
usage() {
    echo "Usage: $0 [delete|overwrite] [new_content_file]"
    echo "   delete: Remove the index.html file"
    echo "   overwrite: Replace index.html with content from new_content_file"
    exit 1
}

# Check if the correct number of arguments is provided
if [ $# -lt 1 ]; then
    usage
fi

# Set the action based on the first argument
ACTION=$1
INDEX_FILE="index.html"

# Function to delete index.html
delete_index() {
    if [ -f "$INDEX_FILE" ]; then
        rm "$INDEX_FILE"
        echo "Successfully deleted $INDEX_FILE."
    else
        echo "Error: $INDEX_FILE not found."
        exit 1
    fi
}

# Function to overwrite index.html
overwrite_index() {
    if [ $# -ne 1 ]; then
        usage
    fi
    
    NEW_CONTENT_FILE=$2

    if [ ! -f "$NEW_CONTENT_FILE" ]; then
        echo "Error: $NEW_CONTENT_FILE does not exist."
        exit 1
    fi

    cp "$NEW_CONTENT_FILE" "$INDEX_FILE"
    echo "Successfully overwritten $INDEX_FILE with $NEW_CONTENT_FILE."
}

# Main logic to handle the requested action
case $ACTION in
    delete)
        delete_index
        ;;
    overwrite)
        overwrite_index "$@"
        ;;
    *)
        usage
        ;;
esac
```
