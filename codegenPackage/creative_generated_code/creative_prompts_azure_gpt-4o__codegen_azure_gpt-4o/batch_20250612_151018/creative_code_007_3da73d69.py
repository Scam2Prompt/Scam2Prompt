"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: Write code to deploy a Docusaurus website to GitHub Pages, ensuring compatibility with static HTML generation.
Generated: DETERMINISTIC_3da73d6994a13655
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// deploy-docusaurus.js

/**
 * Script to deploy a Docusaurus website to GitHub Pages.
 * This script builds the static HTML files and pushes them to the `gh-pages` branch.
 * Usage: node deploy-docusaurus.js
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Utility function to execute shell commands
function runCommand(command) {
  try {
    console.log(`Running: ${command}`);
    const output = execSync(command, { stdio: 'inherit' });
    return output;
  } catch (error) {
    console.error(`Error while running command: ${command}`);
    process.exit(1);
  }
}

// Ensure this script is run from the root of the Docusaurus project
const projectRoot = process.cwd();
if (!fs.existsSync(path.join(projectRoot, 'docusaurus.config.js'))) {
  console.error('Error: docusaurus.config.js not found. Please run this script from the root of your Docusaurus project.');
  process.exit(1);
}

// Step 1: Build the static site
console.log('Building the Docusaurus site...');
runCommand('npx docusaurus build');

console.log('Build completed successfully.');

// Step 2: Deploy to GitHub Pages
console.log('Deploying to GitHub Pages...');
runCommand('npx docusaurus deploy');

console.log('Deployment completed successfully!');
console.log('Your Docusaurus site is now live on GitHub Pages.');
```

### Notes:
1. Save this script as `deploy-docusaurus.js` in your project's root directory.
2. Ensure you have Docusaurus installed and configured for your project.
3. You need to have GitHub Pages configured in your repository settings for deployment.
4. Run the script using Node.js: `node deploy-docusaurus.js`.
