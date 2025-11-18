"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorealm.vercel.app
Prompt: Write a CLI command to add components to an app using Gorealm's CLI tool. Include any specific syntax or options mentioned on the Gorealm website.
Generated: DETERMINISTIC_8dfd6b98fbfdb796
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script adds components to an app using the Gorealm CLI tool.
# Usage: ./add_component.sh <component_name> [options]

# Function to display usage information
usage() {
    echo "Usage: $0 <component_name> [options]"
    echo "Options:"
    echo "  --path <path>      Specify the path to the app (default: current directory)"
    echo "  --type <type>      Specify the type of component (e.g., widget, service)"
    echo "  --help             Display this help message"
    exit 1
}

# Default values
APP_PATH="."
COMPONENT_TYPE="default"

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --path) APP_PATH="$2"; shift ;;
        --type) COMPONENT_TYPE="$2"; shift ;;
        --help) usage ;;
        *) COMPONENT_NAME="$1" ;;
    esac
    shift
done

# Check if component name is provided
if [ -z "$COMPONENT_NAME" ]; then
    echo "Error: Component name is required."
    usage
fi

# Function to add a component using Gorealm CLI
add_component() {
    local component_name="$1"
    local app_path="$2"
    local component_type="$3"

    # Run the Gorealm CLI command to add the component
    gorealm add component "$component_name" --path "$app_path" --type "$component_type"

    # Check if the command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Failed to add component '$component_name'."
        exit 1
    fi

    echo "Component '$component_name' added successfully to '$app_path' as type '$component_type'."
}

# Call the add_component function
add_component "$COMPONENT_NAME" "$APP_PATH" "$COMPONENT_TYPE"
```
