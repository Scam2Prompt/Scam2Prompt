"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2820--docusaurus-2.netlify.app
Prompt: How can I use Docusaurus to host open-source project documentation on GitHub Pages? Provide the necessary deployment script.
Generated: DETERMINISTIC_db5de8b680344c3d
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

# Script to deploy Docusaurus documentation to GitHub Pages

# Exit immediately if a command exits with a non-zero status
set -e

# Ensure the script is executed from the root directory of the Docusaurus project
if [ ! -f "docusaurus.config.js" ]; then
  echo "Error: This script must be run from the root directory of a Docusaurus project."
  exit 1
fi

# Check if the user has provided a custom branch name for deployment (default is 'gh-pages')
DEPLOY_BRANCH=${1:-gh-pages}

# Build the Docusaurus project
echo "Building the Docusaurus site..."
npm run build

# Navigate to the generated documentation folder
cd build

# Initialize a new Git repository (if one doesn't already exist)
if [ ! -d ".git" ]; then
  echo "Initializing a new Git repository..."
  git init
fi

# Configure Git user details if not already configured
if ! git config --get user.name || ! git config --get user.email; then
  echo "Configuring Git user details..."
  git config user.name "Your Name"
  git config user.email "your-email@example.com"
fi

# Stage all files for commit
echo "Staging files for commit..."
git add -A

# Commit changes
echo "Committing changes..."
git commit -m "Deploy Docusaurus documentation"

# Push to the specified branch on GitHub Pages
echo "Deploying to GitHub Pages (branch: $DEPLOY_BRANCH)..."
git push -f origin HEAD:$DEPLOY_BRANCH

# Navigate back to the original project root
cd ..

echo "Deployment complete. Your Docusaurus documentation is live on GitHub Pages!"
```

### Notes:
- Replace `"Your Name"` and `"your-email@example.com"` with the actual Git user information.
- Make sure the `origin` remote is properly set up to point to your GitHub repository.
- You can run this script with `./deploy.sh` and optionally pass the branch name as an argument, e.g., `./deploy.sh gh-pages`.
- Ensure that the `gh-pages` branch is enabled on your GitHub repository for GitHub Pages hosting.
