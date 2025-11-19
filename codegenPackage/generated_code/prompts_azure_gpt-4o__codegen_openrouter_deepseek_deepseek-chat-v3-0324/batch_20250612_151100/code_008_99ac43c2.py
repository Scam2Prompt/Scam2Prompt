"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Provide an example of creating a branch for development in the Agoric SDK, adhering to the standards outlined in the documentation, including naming conventions and changelog updates.
Generated: DETERMINISTIC_99ac43c2f8826861
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

# Ensure we are in the Agoric SDK repository root
if [ ! -f "package.json" ] || [ ! -f "lerna.json" ]; then
  echo "Error: Must be run from the Agoric SDK root directory"
  exit 1
fi

# Get current branch name
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Verify we're not already on a feature branch
if [[ "$CURRENT_BRANCH" != "master" && "$CURRENT_BRANCH" != "main" ]]; then
  echo "Error: Must create feature branch from master/main"
  exit 1
fi

# Pull latest changes
git pull origin "$CURRENT_BRANCH"

# Prompt for feature name
read -p "Enter feature name (lowercase-with-dashes): " FEATURE_NAME

# Validate feature name format
if ! [[ "$FEATURE_NAME" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "Error: Feature name must be lowercase-with-dashes format"
  exit 1
fi

# Create branch with standard naming convention
BRANCH_NAME="feat-${FEATURE_NAME}"
git checkout -b "$BRANCH_NAME"

# Update CHANGELOG.md with new section
CHANGELOG_ENTRY="## Unreleased\n\n### Features\n- ${FEATURE_NAME}: Initial implementation\n"
echo -e "$CHANGELOG_ENTRY\n$(cat CHANGELOG.md)" > CHANGELOG.md

# Commit changelog update
git add CHANGELOG.md
git commit -m "docs(changelog): Add entry for ${FEATURE_NAME} feature"

echo "Created branch ${BRANCH_NAME} and updated CHANGELOG.md"
```
