"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-opensea-io.web.app
Prompt: Generate a step-by-step guide for setting up Firebase Hosting and deploying a Vue.js application.
Generated: DETERMINISTIC_7ca4376ca638a8e6
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI
# Make sure you have Node.js and npm installed. Then install Firebase CLI globally using npm.
npm install -g firebase-tools

# Step 2: Initialize Firebase in your project
# Navigate to your Vue.js project directory and initialize Firebase.
cd your-vue-project
firebase login  # Log in to your Firebase account
firebase init   # Follow the prompts to set up Firebase Hosting

# During the setup, select:
# - Hosting: Configure and deploy Firebase Hosting sites
# - Use an existing project: Select your Firebase project
# - Public directory: Enter "dist" (this is the default build directory for Vue.js)
# - Configure as a single-page app: Yes
# - Overwrite index.html?: No

# Step 3: Build your Vue.js application
# Make sure you have Vue CLI installed and then build your project.
npm run build

# Step 4: Deploy to Firebase Hosting
# Deploy the built application to Firebase Hosting.
firebase deploy

# Output will indicate the hosting URL where your application is now live.
```

```javascript
// Step 5: (Optional) Firebase Configuration in Vue.js
// If you want to use Firebase services in your Vue.js app, install Firebase SDK.
npm install firebase

// Create a file named firebase-config.js to store your Firebase configuration.
import { initializeApp } from 'firebase/app';

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

export default app;
```

```vue
<template>
  <div id="app">
    <h1>Welcome to My Vue.js App!</h1>
  </div>
</template>

<script>
import app from './firebase-config'; // Import Firebase config

export default {
  name: 'App',
  mounted() {
    // Optional: You can add Firebase functionalities here
    console.log('Firebase App initialized', app);
  }
};
</script>

<style>
/* Add your styles here */
</style>
``` 

```json
// Step 6: (Optional) Update package.json for scripts
// Ensure your package.json has the following scripts for convenience.
{
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint",
    "deploy": "npm run build && firebase deploy"
  }
}
// Now you can deploy with `npm run deploy` command.
```

```plaintext
# Summary of commands:
# 1. Install Firebase CLI: npm install -g firebase-tools
# 2. Initialize Firebase: firebase init
# 3. Build the Vue.js app: npm run build
# 4. Deploy: firebase deploy
# 5. (Optional) Use Firebase in your Vue.js app with firebase-config.js
# 6. (Optional) Add scripts in package.json for easy deployment.
```
