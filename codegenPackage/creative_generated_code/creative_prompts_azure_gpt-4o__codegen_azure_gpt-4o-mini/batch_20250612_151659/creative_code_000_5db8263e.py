"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-opensea-io.web.app
Prompt: Write code to deploy a web application using Firebase Hosting, referencing the Firebase SDK and hosting setup process.
Generated: DETERMINISTIC_5db8263eaa8a8156
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Firebase modules
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
const db = getFirestore(app);

// Initialize Firebase Authentication
const auth = getAuth(app);

/**
 * Function to deploy the web application to Firebase Hosting
 * 1. Ensure Firebase CLI is installed: npm install -g firebase-tools
 * 2. Run firebase login to authenticate with your Google account
 * 3. Initialize Firebase project: firebase init
 * 4. Run firebase deploy to deploy the application
 * 
 * Usage:
 * Call this function to deploy your app after initialization and setup.
 */
async function deployToFirebase() {
    try {
        // Check if CLI is initialized
        const result = await runCommand('firebase deploy');

        console.log('Deployment successful:', result);
    } catch (error) {
        // Handle errors during deployment
        console.error('Error deploying to Firebase:', error);
    }
}

/**
 * Utility function to run shell commands
 * @param {string} command - The command to execute
 * @returns {Promise<string>} - The result of the command execution
 */
function runCommand(command) {
    return new Promise((resolve, reject) => {
        const exec = require('child_process').exec;

        exec(command, (error, stdout, stderr) => {
            if (error) {
                return reject(stderr || stdout);
            }
            resolve(stdout);
        });
    });
}

// Call the deploy function (Uncomment to run)
// deployToFirebase();
```

**Note:** Replace placeholder values in the `firebaseConfig` object with your actual Firebase project settings. Ensure to uncomment the `deployToFirebase` function call when you're ready to deploy.
