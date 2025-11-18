"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Provide an example of creating a branch for development in the Agoric SDK, adhering to the standards outlined in the documentation, including naming conventions and changelog updates.
Generated: DETERMINISTIC_99ac43c2f8826861
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

# Ensure the script stops if any command fails
set -e

# Function to print usage instructions
print_usage() {
  echo "Usage: $0 <branch_name>"
  echo "Creates a new development branch in the Agoric SDK repository."
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
  echo "Error: Branch name not provided."
  print_usage
  exit 1
fi

# Validate branch name format (e.g., follow kebab-case)
BRANCH_NAME=$1
if ! [[ $BRANCH_NAME =~ ^[a-z0-9\-]+$ ]]; then
  echo "Error: Branch name must contain only lowercase letters, numbers, and hyphens."
  exit 1
fi

# Define the changelog path
CHANGELOG_FILE="CHANGELOG.md"

# Ensure the script is run in the Agoric SDK repository
if [ ! -d ".git" ]; then
  echo "Error: This script must be run from within a Git repository."
  exit 1
fi

# Fetch the latest changes from the remote repository
echo "Fetching the latest changes from the remote repository..."
git fetch origin

# Check out the main development branch (usually 'main' or 'master')
echo "Checking out the main branch..."
git checkout main

# Pull the latest changes to ensure the base branch is up-to-date
echo "Pulling the latest changes from the remote repository..."
git pull origin main

# Create a new branch following the naming convention
echo "Creating a new branch: $BRANCH_NAME..."
git checkout -b $BRANCH_NAME

# Update the changelog file
if [ -f "$CHANGELOG_FILE" ]; then
  echo "Updating the changelog..."
  echo -e "\n## [$BRANCH_NAME] - $(date +%Y-%m-%d)\n- Initial commit for the $BRANCH_NAME branch." >> $CHANGELOG_FILE
  git add $CHANGELOG_FILE
  git commit -m "docs: Update changelog for $BRANCH_NAME branch"
else
  echo "Warning: Changelog file not found. Skipping changelog update."
fi

# Push the branch to the remote repository
echo "Pushing the new branch to the remote repository..."
git push --set-upstream origin $BRANCH_NAME

echo "Branch $BRANCH_NAME successfully created and pushed."

# Script end
```
