"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Write code to deploy a Docusaurus 2.0 website to GitHub Pages.
Generated: DETERMINISTIC_7834358cac6124ce
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to deploy a Docusaurus 2.0 website to GitHub Pages
# Ensure you have Git and Node.js installed and configured before running this script.
# Also, make sure you have already initialized your Docusaurus site.

set -e  # Exit the script if any command fails

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Verify required tools are installed
if ! command_exists npm; then
  echo "Error: npm is not installed. Please install Node.js and npm."
  exit 1
fi

if ! command_exists git; then
  echo "Error: git is not installed. Please install Git."
  exit 1
fi

# Build the Docusaurus project
echo "Building the Docusaurus project..."
npm run build

# Verify the build output folder exists
BUILD_DIR="build"
if [ ! -d "$BUILD_DIR" ]; then
  echo "Error: Build directory '$BUILD_DIR' does not exist. Make sure the build was successful."
  exit 1
fi

# Ensure the repository is a valid Git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: This is not a valid Git repository. Please initialize a Git repository first."
  exit 1
fi

# Deploy to GitHub Pages
echo "Deploying to GitHub Pages..."
CURRENT_BRANCH=$(git branch --show-current) # Get the current branch name
if [ -z "$CURRENT_BRANCH" ]; then
  echo "Error: Unable to determine the current Git branch."
  exit 1
fi

# Create a new branch for gh-pages deployment
DEPLOY_BRANCH="gh-pages"
echo "Switching to $DEPLOY_BRANCH branch..."
git checkout -B "$DEPLOY_BRANCH"

# Clear any existing files and move build files to the root
echo "Preparing deployment files..."
rm -rf ./*
cp -r "$BUILD_DIR"/* .

# Add and commit all changes
echo "Committing deployment changes..."
git add .
git commit -m "Deploy Docusaurus site"

# Push changes to the remote repository
echo "Pushing to GitHub..."
git push --force origin "$DEPLOY_BRANCH"

# Switch back to the original branch
echo "Switching back to branch $CURRENT_BRANCH..."
git checkout "$CURRENT_BRANCH"

# Clean up local gh-pages branch
git branch -D "$DEPLOY_BRANCH"

echo "Deployment complete! Your Docusaurus website should now be live on GitHub Pages."
```
