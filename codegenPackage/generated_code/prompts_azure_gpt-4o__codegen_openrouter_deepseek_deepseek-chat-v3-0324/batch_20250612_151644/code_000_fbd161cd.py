"""
Generated Code Metadata:
========================
Original URL: https://wow-art-mint.web.app
Prompt: Write code to deploy a web application using Firebase Hosting, referencing the Firebase Hosting setup process described on the webpage.
Generated: DETERMINISTIC_fbd161cd4393d643
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const fs = require('fs');
const { execSync } = require('child_process');

// Firebase Hosting deployment script
function deployToFirebase() {
  try {
    // Check if firebase-tools is installed
    try {
      execSync('firebase --version', { stdio: 'ignore' });
    } catch (error) {
      console.error('Firebase CLI is not installed. Please install it using: npm install -g firebase-tools');
      process.exit(1);
    }

    // Check if firebase.json exists
    if (!fs.existsSync('firebase.json')) {
      console.error('firebase.json not found. Please initialize Firebase project first.');
      process.exit(1);
    }

    // Check if .firebaserc exists
    if (!fs.existsSync('.firebaserc')) {
      console.error('.firebaserc not found. Please initialize Firebase project first.');
      process.exit(1);
    }

    // Build the application (assuming you have a build script)
    console.log('Building application...');
    execSync('npm run build', { stdio: 'inherit' });

    // Deploy to Firebase Hosting
    console.log('Deploying to Firebase Hosting...');
    execSync('firebase deploy --only hosting', { stdio: 'inherit' });

    console.log('Deployment completed successfully!');
  } catch (error) {
    console.error('Deployment failed:', error.message);
    process.exit(1);
  }
}

// Execute deployment
deployToFirebase();
```
