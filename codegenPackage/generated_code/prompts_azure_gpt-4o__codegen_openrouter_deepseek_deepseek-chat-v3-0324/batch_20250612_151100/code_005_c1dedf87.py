"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Provide an example of using `yarn workspaces info` to analyze dependencies between subprojects in the Agoric SDK and resolve mismatched workspace dependencies.
Generated: DETERMINISTIC_c1dedf87bb3f7541
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Check if Yarn is installed
if ! command -v yarn &> /dev/null; then
    echo "Error: Yarn is not installed. Please install Yarn first."
    exit 1
fi

# Navigate to the Agoric SDK root directory
cd agoric-sdk || { echo "Error: agoric-sdk directory not found"; exit 1; }

# Get workspace dependency information
workspace_info=$(yarn workspaces info --json)

# Check if the command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Failed to get workspace info"
    exit 1
fi

# Parse the JSON output to analyze dependencies
echo "Analyzing workspace dependencies..."
echo "----------------------------------"

# Extract and format the workspace info
formatted_info=$(echo "$workspace_info" | jq -r '
    to_entries[] | 
    "Workspace: \(.key)\nLocation: \(.value.location)\nDependencies: \(.value.workspaceDependencies | join(", "))\nMismatched: \(.value.mismatchedDependencies | join(", "))\n"')

echo "$formatted_info"

# Check for mismatched dependencies
mismatched=$(echo "$workspace_info" | jq -r '.. | .mismatchedDependencies? // empty')
if [ -n "$mismatched" ]; then
    echo "----------------------------------"
    echo "Warning: Mismatched dependencies found!"
    echo "Attempting to resolve with 'yarn install'..."
    echo "----------------------------------"
    
    yarn install --check-files
    
    if [ $? -eq 0 ]; then
        echo "Dependencies resolved successfully"
    else
        echo "Error: Failed to resolve dependencies"
        exit 1
    fi
else
    echo "----------------------------------"
    echo "No mismatched dependencies found"
fi
```
