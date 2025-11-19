"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portfolio-metamask-io.web.app
Prompt: How do I troubleshoot issues with Firebase Hosting deployment?
Generated: DETERMINISTIC_914fd3d7c8af4e42
Batch ID: 20250612_160306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Firebase Hosting Deployment Troubleshooting Script
// This script helps identify common issues during Firebase Hosting deployment.

const { exec } = require("child_process");
const fs = require("fs");

// Utility function to execute shell commands
const runCommand = (command) => {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject({ error, stderr });
      } else {
        resolve(stdout);
      }
    });
  });
};

// Check if Firebase CLI is installed
const checkFirebaseCLI = async () => {
  try {
    const version = await runCommand("firebase --version");
    console.log(`Firebase CLI is installed. Version: ${version.trim()}`);
  } catch (err) {
    console.error("Firebase CLI is not installed. Please install it using 'npm install -g firebase-tools'.");
    process.exit(1);
  }
};

// Validate `firebase.json` configuration file
const validateFirebaseJson = () => {
  const configPath = "./firebase.json";
  if (!fs.existsSync(configPath)) {
    console.error("Error: 'firebase.json' is missing. Ensure it's in the project root directory.");
    process.exit(1);
  }

  try {
    const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
    console.log("'firebase.json' is valid and loaded successfully.");
    console.log("Hosting configuration:", config.hosting || "No hosting config found.");
  } catch (err) {
    console.error("Error: 'firebase.json' is invalid. Please check for syntax errors.");
    process.exit(1);
  }
};

// Check if the project is initialized with Firebase
const checkFirebaseInitialization = async () => {
  try {
    const status = await runCommand("firebase projects:list");
    console.log("Firebase project is initialized. Available projects:");
    console.log(status);
  } catch (err) {
    console.error("Error: Firebase project is not initialized. Run 'firebase init' to initialize your project.");
    process.exit(1);
  }
};

// Verify `public` directory exists
const verifyPublicDirectory = () => {
  const publicPath = "./public";
  if (!fs.existsSync(publicPath)) {
    console.error("Error: 'public' directory is missing. Ensure the deployment directory exists.");
    process.exit(1);
  } else {
    console.log("'public' directory is present.");
  }
};

// Deploy the application to Firebase Hosting
const deployFirebaseHosting = async () => {
  try {
    console.log("Deploying to Firebase Hosting...");
    const deployOutput = await runCommand("firebase deploy --only hosting");
    console.log("Deployment successful. Output:");
    console.log(deployOutput);
  } catch (err) {
    console.error("Error during deployment:", err.stderr || err.error.message);
    process.exit(1);
  }
};

// Main function to run all checks and deploy
const troubleshootFirebaseHosting = async () => {
  console.log("Starting Firebase Hosting troubleshooting...");
  
  await checkFirebaseCLI(); // Step 1: Check CLI installation
  validateFirebaseJson();   // Step 2: Validate firebase.json
  await checkFirebaseInitialization(); // Step 3: Check Firebase initialization
  verifyPublicDirectory();  // Step 4: Verify public directory exists
  await deployFirebaseHosting(); // Step 5: Attempt deployment

  console.log("Firebase Hosting troubleshooting completed successfully!");
};

// Run the troubleshooting script
troubleshootFirebaseHosting().catch((err) => {
  console.error("An unexpected error occurred:", err);
  process.exit(1);
});
```
