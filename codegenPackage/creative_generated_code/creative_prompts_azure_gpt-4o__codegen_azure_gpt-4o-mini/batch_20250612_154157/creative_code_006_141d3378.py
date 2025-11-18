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
// Import required modules
const { exec } = require('child_process');
const path = require('path');

// Define the project directory and Firebase project ID
const projectDir = path.join(__dirname, 'your-web-project'); // Replace with your web project directory
const firebaseProjectId = 'your-firebase-project-id'; // Replace with your Firebase project ID

// Function to deploy the project to Firebase Hosting
function deployToFirebase() {
    return new Promise((resolve, reject) => {
        // Change directory to the project directory
        process.chdir(projectDir);

        // Execute the Firebase deployment command
        exec(`firebase deploy --project ${firebaseProjectId}`, (error, stdout, stderr) => {
            if (error) {
                // Log the error and reject the promise
                console.error(`Error deploying to Firebase: ${error.message}`);
                return reject(`Deployment failed: ${error.message}`);
            }

            if (stderr) {
                // Log any warnings or errors captured in stderr
                console.error(`Error output: ${stderr}`);
            }

            // Log the standard output and resolve the promise
            console.log(`Deployment output: ${stdout}`);
            resolve(`Deployment successful: ${stdout}`);
        });
    });
}

// Main function to run the deployment
async function main() {
    try {
        console.log('Starting Firebase deployment...');
        const result = await deployToFirebase();
        console.log(result);
    } catch (error) {
        console.error(`Deployment error: ${error}`);
        process.exit(1); // Exit with a failure code
    }
}

// Execute the main function
main();
```

### Instructions to Use:
1. Replace `your-web-project` with the actual directory of your web project.
2. Replace `your-firebase-project-id` with your actual Firebase project ID.
3. Ensure that the Firebase CLI is installed and that you've authenticated with `firebase login`.
4. Run the script using Node.js: `node deploy-script.js`.
