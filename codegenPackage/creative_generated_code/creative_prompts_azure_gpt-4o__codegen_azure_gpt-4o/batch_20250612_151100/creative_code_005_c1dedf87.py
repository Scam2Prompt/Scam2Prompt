"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Provide an example of using `yarn workspaces info` to analyze dependencies between subprojects in the Agoric SDK and resolve mismatched workspace dependencies.
Generated: DETERMINISTIC_c1dedf87bb3f7541
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script analyzes dependencies between subprojects in an Agoric SDK monorepo
# and resolves mismatched workspace dependencies using `yarn workspaces info`.

set -e

# Ensure the script is being run from the root directory of the monorepo.
if [ ! -f "package.json" ]; then
  echo "Error: This script must be run from the root directory of a Yarn monorepo."
  exit 1
fi

# Step 1: Output workspace dependency information
echo "Fetching workspace dependency information..."
workspacesInfo=$(yarn workspaces info --json)

if [ $? -ne 0 ]; then
  echo "Error: Failed to fetch workspace information with 'yarn workspaces info'."
  exit 1
fi

echo "Workspace dependency information successfully retrieved."

# Step 2: Parse and analyze dependencies using jq (ensure jq is installed)
if ! command -v jq &> /dev/null; then
  echo "Error: 'jq' is required to parse JSON output. Please install jq and rerun the script."
  exit 1
fi

# Extract workspace names and dependencies from the JSON output
echo "Analyzing workspace dependencies..."
workspaceData=$(echo "$workspacesInfo" | jq -r '.data')

if [ -z "$workspaceData" ]; then
  echo "Error: Failed to parse workspace data."
  exit 1
fi

# Step 3: Detect mismatched dependencies
echo "Checking for mismatched workspace dependencies..."
mismatchedDeps=()

# Loop through each workspace and analyze dependencies
echo "$workspaceData" | jq -c 'to_entries[]' | while read -r workspace; do
  workspaceName=$(echo "$workspace" | jq -r '.key')
  workspaceDeps=$(echo "$workspace" | jq -r '.value.workspaceDependencies[]')

  for dep in $workspaceDeps; do
    depVersion=$(jq -r ".data[\"${dep}\"]?.value.version" <<< "$workspacesInfo")
    expectedVersion=$(jq -r ".data[\"${workspaceName}\"]?.value.dependencies[\"${dep}\"]" <<< "$workspace")

    if [ "$depVersion" != "$expectedVersion" ]; then
      mismatchedDeps+=("$workspaceName -> $dep ($expectedVersion expected, $depVersion found)")
    fi
  done
done

# Step 4: Output results
if [ ${#mismatchedDeps[@]} -eq 0 ]; then
  echo "No mismatched workspace dependencies detected."
  exit 0
else
  echo "Mismatched dependencies found:"
  for mismatch in "${mismatchedDeps[@]}"; do
    echo "  - $mismatch"
  fi
fi

# Suggest resolution steps
echo "To resolve mismatched dependencies, ensure all workspace dependencies are set properly in package.json files."
echo "Run 'yarn install' after making corrections to update the lockfile and ensure consistency."

exit 0
```
