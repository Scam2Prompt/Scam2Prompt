"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portfolio-metamask-io.firebaseapp.com
Prompt: Generate a script to verify the successful setup of Firebase Hosting and display a custom message on the hosted webpage.
Generated: DETERMINISTIC_4fbe5c4d18f13c10
Batch ID: 20250612_154157
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Firebase Admin SDK
const admin = require('firebase-admin');

// Initialize Firebase Admin SDK
admin.initializeApp({
    credential: admin.credential.applicationDefault(),
});

// Function to verify the Firebase Hosting setup
async function verifyHostingSetup() {
    try {
        // Get the project ID from the environment variables
        const projectId = process.env.GOOGLE_CLOUD_PROJECT;

        // Check if the project ID is set
        if (!projectId) {
            throw new Error('Project ID is not set. Please ensure you have configured your environment variables correctly.');
        }

        console.log(`Verifying Firebase Hosting setup for project: ${projectId}`);

        // This URL structure assumes default hosting setup; change accordingly
        const hostingUrl = `https://<your-project-id>.web.app/`;

        // Fetch the hosting URL to check if it is reachable
        const response = await fetch(hostingUrl);

        // Check if the response is successful
        if (response.ok) {
            console.log('Firebase Hosting is set up correctly.');
            console.log('You can access your website at:', hostingUrl);
            displayCustomMessage();
        } else {
            throw new Error(`Failed to access Firebase Hosting URL: ${hostingUrl}. Status Code: ${response.status}`);
        }
    } catch (error) {
        console.error('Error verifying Firebase Hosting setup:', error.message);
    }
}

// Function to display a custom message on the hosted webpage
function displayCustomMessage() {
    // Create a message to be displayed on the webpage
    const message = 'Firebase Hosting is successfully set up!';

    // Log the message to the console
    console.log(message);

    // Display the message on the webpage
    document.body.innerHTML = `<h1>${message}</h1>`;
}

// Execute the function to verify the hosting setup
verifyHostingSetup();
```

**Note**: Please make sure to replace `<your-project-id>` with your actual Firebase project ID in the `hostingUrl` variable. Additionally, ensure you have the `node-fetch` package installed for the fetch functionality.
