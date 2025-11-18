"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Generate a step-by-step guide for deploying a Docusaurus site with static HTML files via GitHub Pages.
Generated: DETERMINISTIC_b56502c62a8c28ee
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Docusaurus CLI globally
npm install -g @docusaurus/init

# Step 2: Scaffold a new Docusaurus project
npx docusaurus-init

# Step 3: Navigate into the project directory
cd <your-docusaurus-project-name>

# Step 4: Build the static site
# This generates static HTML, JS, and CSS files in the "build" folder.
npm run build

# Step 5: Install the "gh-pages" package to deploy the site to GitHub Pages
npm install --save-dev gh-pages

# Step 6: Add a deploy script to the "package.json"
# Open the "package.json" file and add the following entry under "scripts":
# 
# "scripts": {
#   ...
#   "deploy": "GIT_USER=<your-github-username> USE_SSH=true npm run docusaurus deploy"
# }

# Replace `<your-github-username>` with your GitHub username.

# Step 7: Push the project to GitHub
# Initialize a Git repository (if not already initialized)
git init
git add .
git commit -m "Initial commit"

# Link the repository to GitHub (replace <your-repo-url> with your GitHub repository URL)
git remote add origin <your-repo-url>

# Push the code to the main branch
git branch -M main
git push -u origin main

# Step 8: Deploy to GitHub Pages
npm run deploy

# The site should now be live on GitHub Pages at:
# https://<your-github-username>.github.io/<repository-name>/

# Tip: To verify deployment settings, ensure the "gh-pages" branch in your repository
# contains the static files.
```
