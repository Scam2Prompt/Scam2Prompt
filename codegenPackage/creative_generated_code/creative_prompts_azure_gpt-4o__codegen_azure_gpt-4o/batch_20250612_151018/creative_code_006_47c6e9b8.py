"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Provide a step-by-step guide to install Docusaurus v2 and configure it for static site generation using GitHub Pages.
Generated: DETERMINISTIC_47c6e9b888dc8653
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://<USERNAME>.github.io": {
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
# Step 1: Ensure Node.js and npm are installed on your system
# Check Node.js version (should be at least v16.14.0)
node -v

# Check npm version (should be at least v6.x)
npm -v

# Step 2: Create a new Docusaurus project
npx create-docusaurus@latest my-docsite classic

# Step 3: Navigate to the project directory
cd my-docsite

# Step 4: Test the site locally
# Run the development server
npm run start
# This will start a development server at localhost:3000

# Step 5: Install GitHub Pages deployment package
npm install --save-dev gh-pages

# Step 6: Update the `docusaurus.config.js` file
# Open the file `docusaurus.config.js` inside the project folder and update the following fields:

/*
docusaurus.config.js

module.exports = {
  title: 'My Docsite', // Replace with your own title
  url: 'https://<USERNAME>.github.io', // Replace <USERNAME> with your GitHub username
  baseUrl: '/my-docsite/', // Replace "my-docsite" with your repository name
  ...
  trailingSlash: false, // Ensures compatibility with GitHub Pages
  deploymentBranch: 'gh-pages', // Specify deployment branch
  ...
  themeConfig: {
    ...
  },
};
*/

# Step 7: Create a GitHub repository
# Go to GitHub and create a new repository named `my-docsite`.

# Step 8: Initialize Git in the project folder and push the code to GitHub
git init
git remote add origin https://github.com/<USERNAME>/my-docsite.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

# Step 9: Configure deployment script
# Open `package.json` and add the following script in the "scripts" section:

/*
package.json

{
  ...
  "scripts": {
    ...
    "deploy": "docusaurus deploy",
    ...
  }
}
*/

# Step 10: Deploy the site to GitHub Pages
npm run deploy

# Step 11: Verify the deployment
# Go to https://<USERNAME>.github.io/my-docsite/ to view your published site.
```
