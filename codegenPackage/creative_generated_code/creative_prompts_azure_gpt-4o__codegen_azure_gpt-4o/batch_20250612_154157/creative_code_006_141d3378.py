"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portfolio-metamask-io.firebaseapp.com
Prompt: Create a Node.js script to automate the deployment of a web project to Firebase Hosting using the Firebase CLI.
Generated: DETERMINISTIC_141d3378db9fba08
Batch ID: 20250612_154157
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
#!/usr/bin/env node

/**
 * Script to automate the deployment of a web project to Firebase Hosting
 * using the Firebase CLI.
 * 
 * Requirements:
 * - Firebase CLI must be installed: `npm install -g firebase-tools`
 * - User must be logged in to Firebase using `firebase login`
 * - A Firebase project must be initialized in the working directory: `firebase init`
 */

const { exec } = require('child_process');
const path = require('path');

// Function to execute shell commands and return a promise
const executeCommand = (command) => {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject(`Error: ${error.message}`);
      } else if (stderr) {
        reject(`Error: ${stderr}`);
      } else {
        resolve(stdout.trim());
      }
    });
  });
};

// Function to deploy the project to Firebase Hosting
const deployToFirebase = async () => {
  try {
    console.log('Starting Firebase deployment process...');

    // Step 1: Check if Firebase CLI is installed
    console.log('Checking for Firebase CLI...');
    const firebaseVersion = await executeCommand('firebase --version');
    console.log(`Firebase CLI version: ${firebaseVersion}`);

    // Step 2: Ensure user is logged in
    console.log('Checking Firebase login status...');
    const loginStatus = await executeCommand('firebase login:list');
    if (!loginStatus.includes('User')) {
      throw new Error('Not logged in to Firebase. Please run `firebase login`.');
    }
    console.log('Firebase login verified.');

    // Step 3: Deploy project to Firebase Hosting
    console.log('Deploying project to Firebase Hosting...');
    const deploymentOutput = await executeCommand('firebase deploy --only hosting');
    console.log('Deployment complete:\n', deploymentOutput);

    console.log('Project successfully deployed to Firebase Hosting!');
  } catch (error) {
    console.error(`Deployment failed: ${error}`);
    process.exit(1); // Exit with error status
  }
};

// Main function to execute the deployment logic
const main = async () => {
  console.log('Automated Firebase Hosting deployment script');
  console.log('--------------------------------------------');

  // Change to the project directory (optional, modify as needed)
  const projectDir = path.resolve(__dirname);
  console.log(`Switching to project directory: ${projectDir}`);
  process.chdir(projectDir);

  // Execute deployment
  await deployToFirebase();
};

// Run the script
main();
```
