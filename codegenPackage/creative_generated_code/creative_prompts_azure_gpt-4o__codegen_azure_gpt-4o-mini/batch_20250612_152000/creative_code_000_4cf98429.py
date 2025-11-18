"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portfolio-metamask-io.web.app
Prompt: Write code to deploy a web application using Firebase Hosting, including steps to initialize Firebase and configure the hosting setup.
Generated: DETERMINISTIC_4cf98429f5cad108
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI globally if it's not already installed
npm install -g firebase-tools

# Step 2: Log into Firebase
firebase login

# Step 3: Create a new Firebase project (if you haven't already)
# Note: This step is done in the Firebase console, then you'll use the project ID in the next step.

# Step 4: Initialize Firebase in your project directory
firebase init

# Explanation of the init command:
# - Select Hosting by using space to select and enter to confirm.
# - Choose the project you created earlier.
# - Set the public directory (e.g., "public").
# - Configure it as a single-page app if needed (answer 'yes' for SPA).
# - Choose whether to overwrite your existing index.html file (if present).

# Step 5: Build your web application (if applicable)
# This step depends on the framework you are using (e.g., React, Angular, Vue).
# For example, if using React:
npm run build

# Step 6: Deploy the application to Firebase Hosting
firebase deploy
```

```javascript
// If you're writing code for your web app, here's an example of a basic HTML file:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your App Title</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Welcome to Your Firebase Hosted App</h1>
    <p>This is a sample web application deployed on Firebase Hosting.</p>
    
    <script src="script.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
```

```javascript
// Example JavaScript file (script.js) for front-end logic

// Check if the Firebase app is initialized
try {
    // Import and configure Firebase
    import { initializeApp } from 'firebase/app';
    import { getAnalytics } from 'firebase/analytics';

    const firebaseConfig = {
        apiKey: "YOUR_API_KEY",
        authDomain: "YOUR_AUTH_DOMAIN",
        projectId: "YOUR_PROJECT_ID",
        storageBucket: "YOUR_STORAGE_BUCKET",
        messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
        appId: "YOUR_APP_ID",
        measurementId: "YOUR_MEASUREMENT_ID"
    };

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    const analytics = getAnalytics(app);
    
    console.log("Firebase initialized successfully.");
} catch (error) {
    console.error("Error initializing Firebase: ", error);
}
```
