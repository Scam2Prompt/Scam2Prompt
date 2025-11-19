"""
Generated Code Metadata:
========================
Original URL: https://activity-opensea-io.web.app
Prompt: Provide an example of using Firebase Hosting to serve static files and connect it to a custom domain.
Generated: DETERMINISTIC_00658db617e29002
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Firebase Hosting Configuration and Deployment Script**
===========================================================

### Prerequisites

*   Firebase CLI installed (`npm install -g firebase-tools`)
*   Firebase account and project set up
*   Custom domain configured

### `firebase.json` Configuration File
```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

### `deploy.js` Deployment Script
```javascript
// Import required modules
const fs = require('fs');
const { exec } = require('child_process');
const readline = require('readline');

// Set up readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to login to Firebase
async function loginToFirebase() {
  try {
    // Run Firebase CLI login command
    await new Promise((resolve, reject) => {
      exec('firebase login', (error) => {
        if (error) {
          reject(error);
        } else {
          resolve();
        }
      });
    });
    console.log('Logged in to Firebase successfully');
  } catch (error) {
    console.error('Error logging in to Firebase:', error);
    process.exit(1);
  }
}

// Function to initialize Firebase project
async function initFirebaseProject() {
  try {
    // Run Firebase CLI init command
    await new Promise((resolve, reject) => {
      exec('firebase init', (error) => {
        if (error) {
          reject(error);
        } else {
          resolve();
        }
      });
    });
    console.log('Initialized Firebase project successfully');
  } catch (error) {
    console.error('Error initializing Firebase project:', error);
    process.exit(1);
  }
}

// Function to deploy to Firebase Hosting
async function deployToFirebaseHosting() {
  try {
    // Run Firebase CLI deploy command
    await new Promise((resolve, reject) => {
      exec('firebase deploy --only hosting', (error) => {
        if (error) {
          reject(error);
        } else {
          resolve();
        }
      });
    });
    console.log('Deployed to Firebase Hosting successfully');
  } catch (error) {
    console.error('Error deploying to Firebase Hosting:', error);
    process.exit(1);
  }
}

// Function to configure custom domain
async function configureCustomDomain() {
  try {
    // Run Firebase CLI hosting:configure command
    await new Promise((resolve, reject) => {
      exec('firebase hosting:configure', (error) => {
        if (error) {
          reject(error);
        } else {
          resolve();
        }
      });
    });
    console.log('Configured custom domain successfully');
  } catch (error) {
    console.error('Error configuring custom domain:', error);
    process.exit(1);
  }
}

// Main deployment function
async function deploy() {
  // Login to Firebase
  await loginToFirebase();

  // Initialize Firebase project
  await initFirebaseProject();

  // Deploy to Firebase Hosting
  await deployToFirebaseHosting();

  // Configure custom domain
  rl.question('Enter your custom domain (e.g., example.com): ', async (domain) => {
    try {
      // Verify domain ownership and configure
      await new Promise((resolve, reject) => {
        exec(`firebase hosting:configure --domain ${domain}`, (error) => {
          if (error) {
            reject(error);
          } else {
            resolve();
          }
        });
      });
      console.log(`Configured custom domain ${domain} successfully`);
      rl.close();
    } catch (error) {
      console.error(`Error configuring custom domain ${domain}:`, error);
      rl.close();
      process.exit(1);
    }
  });
}

// Run deployment function
deploy();
```

### `index.html` Example File
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Firebase Hosting Example</title>
</head>
<body>
  <h1>Welcome to Firebase Hosting!</h1>
</body>
</html>
```

### Usage

1.  Create a new directory for your project and navigate to it in your terminal.
2.  Run `npm init` to create a `package.json` file.
3.  Install required modules by running `npm install`.
4.  Create a `firebase.json` file with the provided configuration.
5.  Create a `deploy.js` file with the provided deployment script.
6.  Create a `public` directory and add your static files (e.g., `index.html`).
7.  Run `node deploy.js` to deploy your static files to Firebase Hosting and configure your custom domain.

**Note:** Make sure to replace the `example.com` domain with your actual custom domain. Also, ensure that you have the necessary permissions and credentials set up for your Firebase project.
