"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Create a script to deploy a Docusaurus-generated static site to GitHub Pages, ensuring proper handling of Markdown-based documentation.
Generated: DETERMINISTIC_8655f95cf72b59f6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Set script exit status
set -e

# Define constants
DOCUSAURUS_DIR="docusaurus"
GITHUB_PAGES_DIR="main"
BRANCH="main"

# Check if Docusaurus directory exists
if [ ! -d "$DOCUSAURUS_DIR" ]; then
  echo "Error: Docusaurus directory '$DOCUSAURUS_DIR' not found."
  exit 1
fi

# Build Docusaurus site
echo "Building Docusaurus site..."
cd "$DOCUSAURUS_DIR"
npm run build

# Navigate to parent directory
cd ..

# Check if GitHub Pages directory exists, create if not
if [ ! -d "$GITHUB_PAGES_DIR" ]; then
  echo "Creating GitHub Pages directory '$GITHUB_PAGES_DIR'..."
  mkdir "$GITHUB_PAGES_DIR"
fi

# Copy Docusaurus build output to GitHub Pages directory
echo "Copying Docusaurus build output to GitHub Pages directory..."
rm -rf "$GITHUB_PAGES_DIR"/*
cp -r "$DOCUSAURUS_DIR/build/*" "$GITHUB_PAGES_DIR"

# Initialize Git repository if not already initialized
if [ ! -d "$GITHUB_PAGES_DIR/.git" ]; then
  echo "Initializing Git repository in GitHub Pages directory..."
  cd "$GITHUB_PAGES_DIR"
  git init
fi

# Stage and commit changes
echo "Staging and committing changes..."
cd "$GITHUB_PAGES_DIR"
git add .
git commit -m "Automated deployment of Docusaurus site"

# Check if GitHub Pages branch exists
if git show "origin/$BRANCH" &> /dev/null; then
  echo "Updating existing GitHub Pages branch..."
  git push origin "$BRANCH" -f
else
  echo "Creating new GitHub Pages branch..."
  git push -u origin "$BRANCH"
fi

echo "Deployment complete."
```

```python
# Alternatively, here is a Python version using the GitPython library

import os
import subprocess
from git import Repo

DOCUSAURUS_DIR = "docusaurus"
GITHUB_PAGES_DIR = "main"
BRANCH = "main"

def deploy_site():
    try:
        # Check if Docusaurus directory exists
        if not os.path.exists(DOCUSAURUS_DIR):
            raise FileNotFoundError(f"Docusaurus directory '{DOCUSAURUS_DIR}' not found.")

        # Build Docusaurus site
        print("Building Docusaurus site...")
        os.chdir(DOCUSAURUS_DIR)
        subprocess.run(["npm", "run", "build"], check=True)

        # Navigate to parent directory
        os.chdir("..")

        # Check if GitHub Pages directory exists, create if not
        if not os.path.exists(GITHUB_PAGES_DIR):
            print(f"Creating GitHub Pages directory '{GITHUB_PAGES_DIR}'...")
            os.mkdir(GITHUB_PAGES_DIR)

        # Copy Docusaurus build output to GitHub Pages directory
        print("Copying Docusaurus build output to GitHub Pages directory...")
        import shutil
        shutil.rmtree(GITHUB_PAGES_DIR, ignore_errors=True)
        shutil.copytree(f"{DOCUSAURUS_DIR}/build", GITHUB_PAGES_DIR)

        # Initialize Git repository if not already initialized
        try:
            repo = Repo(GITHUB_PAGES_DIR)
        except:
            print("Initializing Git repository in GitHub Pages directory...")
            repo = Repo.init(GITHUB_PAGES_DIR)

        # Stage and commit changes
        print("Staging and committing changes...")
        repo.git.add(".")
        repo.git.commit("-m", "Automated deployment of Docusaurus site")

        # Check if GitHub Pages branch exists
        try:
            repo.git.show(f"origin/{BRANCH}")
            print("Updating existing GitHub Pages branch...")
            repo.git.push("origin", BRANCH, "-f")
        except:
            print("Creating new GitHub Pages branch...")
            repo.git.push("-u", "origin", BRANCH)

        print("Deployment complete.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    deploy_site()
```
