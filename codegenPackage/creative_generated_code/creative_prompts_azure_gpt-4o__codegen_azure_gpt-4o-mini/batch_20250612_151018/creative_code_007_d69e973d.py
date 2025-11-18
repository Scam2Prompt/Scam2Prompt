"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Write a script to deploy a Docusaurus site to GitHub Pages, ensuring the static HTML files are correctly generated and served.
Generated: DETERMINISTIC_d69e973d81dfc343
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

# Script to deploy a Docusaurus site to GitHub Pages

# Exit immediately if a command exits with a non-zero status
set -e

# Constants
DOCUSAURUS_DIR="your-docusaurus-directory"  # Replace with your Docusaurus project directory
BUILD_DIR="$DOCUSAURUS_DIR/build"
BRANCH="gh-pages"  # Default branch for GitHub Pages

# Function to clean up the old build
cleanup() {
    echo "Cleaning up old build..."
    rm -rf $BUILD_DIR
}

# Function to build the Docusaurus site
build_site() {
    echo "Building the Docusaurus site..."
    cd $DOCUSAURUS_DIR
    npm install  # Install dependencies
    npm run build  # Build the site
}

# Function to deploy the build to GitHub Pages
deploy() {
    echo "Deploying to GitHub Pages..."
    # Navigate to the build directory
    cd $BUILD_DIR

    # Initialize a new Git repository
    git init
    git add .
    git commit -m "Deploy to GitHub Pages: $(date +'%Y-%m-%d %H:%M:%S')"

    # Push to the gh-pages branch
    git push -f git@github.com:yourusername/yourrepo.git master:$BRANCH  # Replace with your GitHub username and repository
}

# Main script execution
main() {
    cleanup
    build_site
    deploy
    echo "Deployment successful!"
}

# Run the main function
main
```

### Usage Instructions:
1. Replace `your-docusaurus-directory` with the path to your Docusaurus project folder.
2. Update `git@github.com:yourusername/yourrepo.git` with your actual GitHub repository URL.
3. Make the script executable: `chmod +x deploy.sh`
4. Run the script: `./deploy.sh`
