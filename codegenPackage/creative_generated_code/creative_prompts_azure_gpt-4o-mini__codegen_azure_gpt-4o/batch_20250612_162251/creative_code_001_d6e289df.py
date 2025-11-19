"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ryanml.github.io
Prompt: What are the best practices for deploying a personal portfolio website on GitHub, as suggested by Ryan Lanese?
Generated: DETERMINISTIC_d6e289df24ea6656
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Bash Script: Deploy a Personal Portfolio Website on GitHub Pages

#!/bin/bash

# Script to deploy a personal portfolio website to GitHub Pages

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display error messages and exit
function error_exit {
    echo "Error: $1"
    exit 1
}

# Check if Git is installed
if ! command -v git &> /dev/null; then
    error_exit "Git is not installed. Please install Git and try again."
fi

# Check for GitHub repository URL input
if [ -z "$1" ]; then
    error_exit "You must provide a GitHub repository URL as the first argument."
fi

# Variables
REPO_URL=$1
BRANCH_NAME="gh-pages" # Deploy branch for GitHub Pages
BUILD_DIR="dist" # Directory containing the built website files (adjust as necessary)

# Ensure the build directory exists
if [ ! -d "$BUILD_DIR" ]; then
    error_exit "Build directory '$BUILD_DIR' does not exist. Ensure your site is built before deploying."
fi

# Initialize a new Git repository
cd "$BUILD_DIR"
git init

# Add the remote repository
git remote add origin "$REPO_URL"

# Add all files in the build directory to the repository
git add .

# Commit the changes
git commit -m "Deploy portfolio website to GitHub Pages"

# Push the code to the gh-pages branch
git branch -M "$BRANCH_NAME"
git push -f origin "$BRANCH_NAME"

# Success message
echo "Portfolio website deployed successfully to GitHub Pages!"
echo "Visit your site at: https://<your-username>.github.io/<repo-name>/"
```

### Instructions
1. Save this script as `deploy.sh`.
2. Build your website (e.g., using a static site generator like Next.js or Gatsby).
3. Place the built website files in the `dist` directory.
4. Run the script: `bash deploy.sh <your-repo-url>` (replace `<your-repo-url>` with your GitHub repository URL).
5. Ensure GitHub Pages is enabled for the `gh-pages` branch in your repository settings.
