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

# This script creates a new development branch for the Agoric SDK project.
# It follows naming conventions and updates the changelog accordingly.

# Usage: ./create_dev_branch.sh <branch-name> <changelog-message>

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <branch-name> <changelog-message>"
  exit 1
fi

BRANCH_NAME=$1
CHANGELOG_MESSAGE=$2

# Ensure the branch name follows the Agoric naming conventions
if [[ ! $BRANCH_NAME =~ ^(feature|bugfix|hotfix)/.+$ ]]; then
  echo "Error: Branch name must follow the naming convention: feature/<name>, bugfix/<name>, or hotfix/<name>"
  exit 1
fi

# Create a new branch from the current branch
git checkout -b "$BRANCH_NAME"

# Check if branch creation was successful
if [ $? -ne 0 ]; then
  echo "Error: Failed to create branch '$BRANCH_NAME'."
  exit 1
fi

# Update the changelog file
CHANGELOG_FILE="CHANGELOG.md"

if [ -f "$CHANGELOG_FILE" ]; then
  echo -e "\n## [$(date +'%Y-%m-%d')] - $BRANCH_NAME\n- $CHANGELOG_MESSAGE" >> "$CHANGELOG_FILE"
else
  echo "Error: Changelog file '$CHANGELOG_FILE' not found."
  exit 1
fi

# Commit the changelog update
git add "$CHANGELOG_FILE"
git commit -m "Update changelog for $BRANCH_NAME"

# Provide feedback to the user
echo "Branch '$BRANCH_NAME' created and changelog updated successfully."
```
