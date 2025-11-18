"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodl-tracking.web.app
Prompt: Write a script to automate the deployment process for Firebase Hosting, including authentication and resource allocation steps.
Generated: DETERMINISTIC_f3a74dd467bdbed8
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// deployFirebase.js
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuration
const firebaseConfigFile = path.join(__dirname, 'firebaseConfig.json'); // Path to Firebase configuration file
const projectId = 'YOUR_PROJECT_ID'; // Replace with your Firebase project ID

// Function to check if Firebase CLI is installed
const checkFirebaseCLI = () => {
    return new Promise((resolve, reject) => {
        exec('firebase --version', (error, stdout) => {
            if (error) {
                reject(new Error('Firebase CLI is not installed. Please install Firebase CLI to proceed.'));
            } else {
                resolve(stdout.trim());
            }
        });
    });
};

// Function to authenticate user to Firebase
const authenticateFirebase = () => {
    return new Promise((resolve, reject) => {
        exec('firebase login', (error) => {
            if (error) {
                reject(new Error('Failed to authenticate with Firebase. Please try again.'));
            } else {
                resolve('Authentication successful.');
            }
        });
    });
};

// Function to initialize Firebase Hosting
const initializeFirebaseHosting = () => {
    return new Promise((resolve, reject) => {
        exec('firebase init hosting --project ' + projectId + ' --non-interactive', (error) => {
            if (error) {
                reject(new Error('Failed to initialize Firebase Hosting.'));
            } else {
                resolve('Firebase Hosting initialized successfully.');
            }
        });
    });
};

// Function to deploy to Firebase Hosting
const deployToFirebase = () => {
    return new Promise((resolve, reject) => {
        exec('firebase deploy --only hosting', (error) => {
            if (error) {
                reject(new Error('Deployment failed. Please check the logs for details.'));
            } else {
                resolve('Deployment to Firebase Hosting was successful.');
            }
        });
    });
};

// Main function to automate the deployment process
const automateDeployment = async () => {
    try {
        // Check if the Firebase CLI is installed
        await checkFirebaseCLI();
        console.log('Firebase CLI is installed.');

        // Authenticate user
        await authenticateFirebase();
        console.log('Authenticated successfully.');

        // Initialize Firebase Hosting
        await initializeFirebaseHosting();
        console.log('Firebase Hosting initialized.');

        // Deploy to Firebase Hosting
        const deployMessage = await deployToFirebase();
        console.log(deployMessage);
    } catch (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1); // Exit with error code
    }
};

// Start the deployment process
automateDeployment();
```

### Notes:
- Ensure you have Node.js installed to run this script.
- Replace `YOUR_PROJECT_ID` with your actual Firebase project ID.
- Ensure that you have `firebase-tools` installed globally (`npm install -g firebase-tools`).
