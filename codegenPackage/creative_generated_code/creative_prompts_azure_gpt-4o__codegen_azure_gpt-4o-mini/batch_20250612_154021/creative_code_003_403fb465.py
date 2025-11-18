"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Generate a step-by-step guide to deploy a React application using Firebase Hosting, including Firebase CLI commands.
Generated: DETERMINISTIC_403fb46538cbc7c8
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI
npm install -g firebase-tools

# Step 2: Log in to Firebase
firebase login

# Step 3: Create a Firebase project
# This step requires you to have a Firebase account and to create a project in the Firebase console.
# You can use the Firebase console or run the following command to create a new project:
firebase projects:create your-project-id

# Step 4: Initialize Firebase in your React project
# Navigate to your React project directory
cd your-react-app

# Initialize Firebase
firebase init

# During the initialization, select the following options:
# 1. Hosting: Configure and deploy Firebase Hosting sites
# 2. Use an existing project: Select your Firebase project created in Step 3
# 3. Set the public directory: Enter 'build' (assuming you're using Create React App)
# 4. Configure as a single-page app: Answer 'Yes'
# 5. Overwrite index.html: Answer 'No' (if you want to keep your existing index.html)

# Step 5: Build your React application
npm run build

# Step 6: Deploy to Firebase Hosting
firebase deploy

# Step 7: Access your deployed application
# After deployment, Firebase will provide a hosting URL. You can access your application using that URL.
```

```javascript
// To ensure a smooth deployment, here's a sample script to automate the build and deployment process:

const { exec } = require('child_process');

// Function to run shell commands
const runCommand = (command) => {
    return new Promise((resolve, reject) => {
        exec(command, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing command: ${command}\n`, stderr);
                reject(error);
            } else {
                console.log(`Command executed successfully: ${command}\n`, stdout);
                resolve(stdout);
            }
        });
    });
};

// Main function to build and deploy the React app
const deployReactApp = async () => {
    try {
        // Build the React app
        await runCommand('npm run build');

        // Deploy to Firebase
        await runCommand('firebase deploy');
    } catch (error) {
        console.error('Deployment failed:', error);
    }
};

// Execute the deployment process
deployReactApp();
```
