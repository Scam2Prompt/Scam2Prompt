"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.algocryptobot.com
Prompt: Write code to deploy a web application using Firebase Hosting, referencing the Firebase SDK setup process described in the documentation.
Generated: DETERMINISTIC_57058b262a37cae0
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required Dependencies: Ensure you have Node.js installed.
// 1. Install Firebase CLI (`npm install -g firebase-tools`) if you haven't already.
// 2. Run `firebase login` to authenticate your account before proceeding.

// Step 1: Initialize Firebase project
// Command in terminal: `firebase init`
// Follow the prompts to set up Hosting and associate with your Firebase project.

// Step 2: Write the deployment script.

const { exec } = require("child_process");
const fs = require("fs");
const path = require("path");

// Function to deploy the app using Firebase CLI
function deployFirebaseHosting() {
  try {
    // Check if firebase.json exists in the current directory
    const firebaseConfigPath = path.join(process.cwd(), "firebase.json");
    if (!fs.existsSync(firebaseConfigPath)) {
      throw new Error(
        "firebase.json not found. Ensure you have run 'firebase init' to set up your project."
      );
    }

    console.log("Starting Firebase Hosting deployment...");

    // Execute `firebase deploy` command
    const deployCommand = exec("firebase deploy");

    deployCommand.stdout.on("data", (data) => {
      console.log(`Output: ${data}`);
    });

    deployCommand.stderr.on("data", (data) => {
      console.error(`Error: ${data}`);
    });

    deployCommand.on("close", (code) => {
      if (code === 0) {
        console.log("Deployment successful!");
      } else {
        console.error(`Deployment failed with exit code ${code}`);
      }
    });
  } catch (error) {
    console.error(`Deployment Error: ${error.message}`);
  }
}

// Call the deployment function
deployFirebaseHosting();
```

Notes:
1. Before running this script, ensure that Firebase CLI is correctly installed and authenticated.
2. Test the script locally in a directory that contains your Firebase project files (`firebase.json` and hosting files).
3. Ensure you're authorized and have permissions to deploy to the Firebase project.
