"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corn-staging.com
Prompt: Explain how to set up a project for direct upload on Cloudflare Pages with specific commands.
Generated: DETERMINISTIC_9b26c3cfc202c4fb
Batch ID: 20250612_135517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to set up a project for direct upload on Cloudflare Pages

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage of the script
usage() {
    echo "Usage: $0 <project-directory> <branch-name>"
    echo "  project-directory: The directory of your project."
    echo "  branch-name: The branch to deploy to Cloudflare Pages."
    exit 1
}

# Validate input parameters
if [ "$#" -ne 2 ]; then
    usage
fi

PROJECT_DIR=$1
BRANCH_NAME=$2

# Step 1: Navigate to the project directory
cd "$PROJECT_DIR" || { echo "Directory not found: $PROJECT_DIR"; exit 1; }

# Step 2: Initialize a new Git repository if it doesn't exist
if [ ! -d ".git" ]; then
    echo "Initializing a new Git repository..."
    git init
    git add .
    git commit -m "Initial commit"
fi

# Step 3: Add the remote repository for Cloudflare Pages
# Update the following URL with your Cloudflare Git repository URL
CLOUDFLARE_REPO_URL="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
git remote add cloudflare "$CLOUDFLARE_REPO_URL"

# Step 4: Create a new branch for deployment
git checkout -b "$BRANCH_NAME"

# Step 5: Push changes to Cloudflare Pages
echo "Pushing changes to Cloudflare Pages on branch '$BRANCH_NAME'..."
git push cloudflare "$BRANCH_NAME"

# Step 6: Confirmation message
echo "Successfully deployed to Cloudflare Pages on branch '$BRANCH_NAME'."
```

### Usage:
1. Save the script as `deploy.sh`.
2. Make it executable: `chmod +x deploy.sh`.
3. Run the script: `./deploy.sh /path/to/your/project branch-name`.
