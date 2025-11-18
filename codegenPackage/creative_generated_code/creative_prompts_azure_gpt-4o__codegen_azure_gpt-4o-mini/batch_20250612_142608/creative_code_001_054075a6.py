"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Generate a script to publish markdown-based documentation online using GitBook, ensuring compatibility with the features highlighted in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_054075a638cdcff4
Batch ID: 20250612_142608
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/yourusername/my-docs.git": {
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

# Script to publish markdown-based documentation online using GitBook
# This script assumes that you have GitBook CLI installed and configured

# Set variables
GITBOOK_DIR="my-docs"          # Directory for GitBook documentation
GITBOOK_REPO="https://github.com/yourusername/my-docs.git" # Replace with your repo URL
BRANCH="gh-pages"               # Branch for GitHub Pages
BUILD_DIR="${GITBOOK_DIR}/_book" # Directory for the built documentation

# Function to display error messages
function error_exit {
    echo "$1" 1>&2
    exit 1
}

# Step 1: Clone the repository
if [ -d "$GITBOOK_DIR" ]; then
    echo "Directory ${GITBOOK_DIR} already exists. Pulling latest changes."
    cd "$GITBOOK_DIR" || error_exit "Failed to change directory."
    git pull origin "$BRANCH" || error_exit "Failed to pull latest changes."
else
    echo "Cloning the repository..."
    git clone "$GITBOOK_REPO" "$GITBOOK_DIR" || error_exit "Failed to clone repository."
    cd "$GITBOOK_DIR" || error_exit "Failed to change directory."
fi

# Step 2: Install GitBook dependencies
echo "Installing GitBook dependencies..."
gitbook install || error_exit "Failed to install GitBook dependencies."

# Step 3: Build the documentation
echo "Building the documentation..."
gitbook build . "$BUILD_DIR" || error_exit "Failed to build documentation."

# Step 4: Deploy to GitHub Pages
echo "Deploying to GitHub Pages..."
cd "$BUILD_DIR" || error_exit "Failed to change directory to build directory."

# Initialize a new Git repository in the build directory
git init
git config user.name "Your Name"  # Replace with your name
git config user.email "you@example.com"  # Replace with your email

# Add remote repository
git remote add origin "$GITBOOK_REPO" || error_exit "Failed to add remote repository."

# Checkout to the gh-pages branch
git checkout -B "$BRANCH" || error_exit "Failed to checkout to the branch."

# Add and commit changes
git add . || error_exit "Failed to add files."
git commit -m "Update documentation $(date +'%Y-%m-%d %H:%M:%S')" || error_exit "Failed to commit changes."

# Push changes to GitHub
git push -f origin "$BRANCH" || error_exit "Failed to push changes to GitHub."

# Step 5: Cleanup
echo "Cleaning up..."
cd .. || error_exit "Failed to change directory."
rm -rf "$GITBOOK_DIR" # Remove the local repository

echo "Documentation published successfully to GitHub Pages."
```

**Usage:**
1. Replace `yourusername`, `Your Name`, and `you@example.com` with your actual GitHub username, name, and email.
2. Make the script executable: `chmod +x publish_docs.sh`.
3. Run the script: `./publish_docs.sh`.
