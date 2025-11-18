"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Write a script to deploy a Docusaurus website to GitHub Pages, ensuring static HTML files are generated and published correctly.
Generated: DETERMINISTIC_737e48f14495b235
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
 * This script uses the Docusaurus CLI to build the static site 
 * and then publishes it to GitHub Pages.
 * 
 * Requirements:
 * - Node.js installed
 * - Docusaurus project initialized
 * - `gh-pages` package installed
 */

const { exec } = require('child_process'); // Import exec for command execution
const path = require('path'); // Path module for handling file paths

// Helper function to execute shell commands and handle errors
const runCommand = (command) => {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing command: ${command}`);
        console.error(`Error: ${error.message}`);
        reject(error);
      } else if (stderr) {
        console.error(`Command STDERR: ${stderr}`);
      }
      resolve(stdout);
    });
  });
};

// Main deployment function
const deployDocusaurus = async () => {
  try {
    console.log('Starting Docusaurus deployment process...');

    // Step 1: Build the static site
    console.log('Building static HTML files...');
    await runCommand('npx docusaurus build');
    console.log('Static HTML files generated successfully.');

    // Step 2: Publish the built site to GitHub Pages
    console.log('Deploying to GitHub Pages...');
    await runCommand('npx docusaurus deploy');
    console.log('Website deployed successfully to GitHub Pages.');
  } catch (error) {
    console.error('Deployment failed. See error details above.');
    process.exit(1); // Exit with failure status code
  }
};

// Execute the deployment function
deployDocusaurus();
```

### Usage Instructions:
1. Ensure you are in the root directory of your Docusaurus project.
2. Save the script as `deploy-docusaurus.js`.
3. Run the script using `node deploy-docusaurus.js`.
