"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Write a script to deploy a Docusaurus website to GitHub Pages, ensuring the static HTML files are generated correctly.
Generated: DETERMINISTIC_99b6e6c57e1a43a1
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
// Script to deploy a Docusaurus website to GitHub Pages
// Requires Node.js and the Docusaurus CLI to be installed

const { execSync } = require("child_process");
const fs = require("fs");

// Utility function to execute shell commands
function runCommand(command) {
  try {
    console.log(`Running: ${command}`);
    const output = execSync(command, { stdio: "inherit" });
    return output;
  } catch (error) {
    console.error(`Error executing command: ${command}`);
    process.exit(1);
  }
}

// Check if 'docusaurus.config.js' exists in the current directory
const docusaurusConfigPath = "./docusaurus.config.js";
if (!fs.existsSync(docusaurusConfigPath)) {
  console.error("Error: docusaurus.config.js not found in the current directory.");
  process.exit(1);
}

// Generate static HTML files using the Docusaurus CLI
console.log("Generating static files...");
runCommand("npx docusaurus build");

// Deploy the site to GitHub Pages
console.log("Deploying to GitHub Pages...");
runCommand("npx docusaurus deploy");

console.log("Deployment complete.");
```

### Instructions to Use
1. Save the script as `deploy-docusaurus.js` in the root of your Docusaurus project folder.
2. Ensure Node.js is installed on your system.
3. Run the script with `node deploy-docusaurus.js`.

### Prerequisites
- Docusaurus CLI must be installed (`npm install --save docusaurus`).
- Your Docusaurus project must have a valid `docusaurus.config.js` file.
- Ensure your GitHub repository has been configured in `docusaurus.config.js` for deployment.
