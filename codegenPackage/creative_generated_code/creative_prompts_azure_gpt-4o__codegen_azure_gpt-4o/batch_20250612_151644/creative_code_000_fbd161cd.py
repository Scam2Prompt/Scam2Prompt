"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Write code to deploy a web application using Firebase Hosting, referencing the Firebase Hosting setup process described on the webpage.
Generated: DETERMINISTIC_fbd161cd4393d643
Batch ID: 20250612_151644
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-project-id.web.app": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI globally
# Make sure Node.js is installed on your system before running this.
npm install -g firebase-tools

# Step 2: Log in to Firebase
# This will open a browser window for authentication.
firebase login

# Step 3: Initialize Firebase in your project directory
# Navigate to your project folder and run the following command. 
# Select Hosting during initialization and associate it with a Firebase project.
firebase init

# Step 4: Build your web application
# If your web application uses a build process (e.g., React, Angular, Vue), 
# run the appropriate build command to generate production-ready files.
# Example for React:
npm run build

# Step 5: Deploy the application to Firebase Hosting
# Ensure the build files (e.g., "dist" or "build" directory) are located in the directory specified during Firebase initialization.
firebase deploy

# Step 6: Verify deployment
# After deployment, Firebase will provide a hosting URL (e.g., https://your-project-id.web.app).
# Visit the URL to verify your web application is live.
```

```javascript
// Optional: Example of a basic web app for Firebase Hosting.
const fs = require('fs');
const path = require('path');
const express = require('express');

const app = express();

// Middleware to serve static files from the "public" directory.
app.use(express.static(path.join(__dirname, 'public')));

// Route to handle requests.
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public/index.html'));
});

// Error handling middleware.
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});

// Start the server for local development.
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});

// Notes:
// 1. After development, ensure the "public" directory contains your production-ready web files.
// 2. Firebase Hosting will serve these files from the configured directory during deployment.
```

```json
// Example Firebase Hosting configuration (firebase.json).
{
  "hosting": {
    "public": "build", // Directory containing your web application (e.g., "build" or "dist").
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```
