"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-alert-offers-opensea.web.app
Prompt: Explain how to troubleshoot common issues when deploying a web app to Firebase Hosting and provide code snippets for debugging.
Generated: DETERMINISTIC_74e726afcd6f64c7
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Firebase Admin SDK
const admin = require('firebase-admin');

// Initialize Firebase Admin SDK
admin.initializeApp({
  credential: admin.credential.applicationDefault(),
});

// Function to deploy a web app to Firebase Hosting
async function deployWebApp() {
  try {
    // Check if Firebase CLI is installed
    const { execSync } = require('child_process');
    execSync('firebase --version', { stdio: 'ignore' });

    // Run Firebase deploy command
    console.log("Starting deployment...");
    execSync('firebase deploy', { stdio: 'inherit' });
    console.log("Deployment successful!");
  } catch (error) {
    handleError(error);
  }
}

// Function to handle errors during deployment
function handleError(error) {
  console.error("An error occurred during deployment:");
  
  // Log the error message
  console.error(error.message);

  // Check for specific error codes and handle accordingly
  if (error.message.includes('command not found')) {
    console.error("Firebase CLI is not installed. Please install it using: npm install -g firebase-tools");
  } else if (error.message.includes('not authorized')) {
    console.error("You are not authorized to deploy. Please login using: firebase login");
  } else if (error.message.includes('BUILD_FAILURE')) {
    console.error("There was a build failure. Check your build configuration.");
  } else {
    console.error("Unknown error occurred. Please check your configuration.");
  }
}

// Function to check Firebase project configuration
async function checkFirebaseConfig() {
  try {
    const config = await admin.firestore().collection('config').doc('app').get();
    if (!config.exists) {
      throw new Error("Firebase configuration document does not exist.");
    }
    console.log("Firebase configuration loaded successfully.");
  } catch (error) {
    handleError(error);
  }
}

// Execute deployment and configuration check
(async () => {
  await checkFirebaseConfig();
  await deployWebApp();
})();
```

### Notes:
- This code snippet demonstrates how to deploy a web app to Firebase Hosting with error handling.
- It includes functions for both deployment and configuration checking, providing clear error messages for common issues.
- Ensure that you have installed the Firebase Admin SDK and Firebase CLI to execute this code.
