"""
Generated Code Metadata:
========================
Original URL: https://hodl-tracking.web.app
Prompt: Generate a script to initialize Firebase Hosting for a project, ensuring the setup aligns with Firebase Hosting guidelines.
Generated: DETERMINISTIC_eb151477998de881
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the Firebase Admin SDK
const admin = require('firebase-admin');
// Import the Firebase CLI
const { exec } = require('child_process');

// Initialize the Firebase Admin SDK
admin.initializeApp({
    credential: admin.credential.applicationDefault(),
});

// Function to initialize Firebase Hosting
async function initializeFirebaseHosting(projectId) {
    try {
        // Check if the project ID is provided
        if (!projectId) {
            throw new Error('Project ID is required to initialize Firebase Hosting.');
        }

        // Change directory to the project folder
        process.chdir(`./${projectId}`);

        // Run Firebase initialization command
        await runCommand('firebase init hosting');

        console.log(`Firebase Hosting has been initialized for project: ${projectId}`);
    } catch (error) {
        console.error('Error initializing Firebase Hosting:', error.message);
    }
}

// Function to run shell commands
function runCommand(command) {
    return new Promise((resolve, reject) => {
        exec(command, (error, stdout, stderr) => {
            if (error) {
                reject(`Error executing command: ${stderr || stdout}`);
            } else {
                resolve(stdout);
            }
        });
    });
}

// Example usage
const projectId = 'your-firebase-project-id'; // Replace with your Firebase project ID
initializeFirebaseHosting(projectId);
```

Make sure to replace `'your-firebase-project-id'` with your actual Firebase project ID before running the script. Ensure that you have the Firebase CLI installed and configured on your machine.
