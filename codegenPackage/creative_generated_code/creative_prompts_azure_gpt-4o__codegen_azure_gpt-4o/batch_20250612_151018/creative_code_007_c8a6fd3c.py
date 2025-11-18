"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Demonstrate how to deploy a Docusaurus website to GitHub Pages with static HTML files generated from Markdown.
Generated: DETERMINISTIC_c8a6fd3c2e888ce9
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/": {
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
# Install Docusaurus CLI globally (make sure you have Node.js and npm installed)
npm install -g @docusaurus/init

# Create a new Docusaurus project
npx create-docusaurus@latest my-website classic

# Navigate to the project directory
cd my-website

# Build static HTML files from Markdown content
npm run build

# Install GitHub Pages package to deploy
npm install gh-pages --save-dev

# Add deployment script to package.json
# Open package.json and add the following under "scripts":
# "deploy": "gh-pages -d build"
#
# Explanation:
# - "gh-pages -d build" deploys the contents of the "build" directory to GitHub Pages

# Commit initial changes to git (if not already done)
git init
git add .
git commit -m "Initial Docusaurus setup"

# Push the code to a GitHub repository (replace <USERNAME> and <REPO> with your GitHub username and repository name)
git remote add origin https://github.com/<USERNAME>/<REPO>.git
git branch -M main
git push -u origin main

# Deploy to GitHub Pages using the npm script
npm run deploy

# Your website is now live on GitHub Pages at:
# https://<USERNAME>.github.io/<REPO>
```
