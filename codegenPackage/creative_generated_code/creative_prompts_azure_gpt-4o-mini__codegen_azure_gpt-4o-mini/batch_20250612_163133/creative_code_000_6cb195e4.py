"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: How can I use Firebase Hosting to deploy my web application effectively?
Generated: DETERMINISTIC_6cb195e438de9dfb
Batch ID: 20250612_163133
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

# Step 2: Initialize Firebase in your project directory
firebase init hosting

# Step 3: Choose the Firebase project you want to deploy
# Follow the prompts to configure Firebase Hosting

# Step 4: Build your web application
# Assuming you have a build script defined in package.json, run:
npm run build

# Step 5: Deploy your web application to Firebase Hosting
firebase deploy

# Note: Make sure to replace 'public' in 'firebase.json' with your build directory if it's different.
```

```json
// firebase.json
{
  "hosting": {
    "public": "dist", // Adjust this based on your build output directory
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
```

```bash
# Error handling during deployment
# Check if the deploy was successful
if [ $? -ne 0 ]; then
  echo "Deployment failed. Please check the error messages above."
  exit 1
fi

echo "Deployment successful! Your app is live."
```

```javascript
// Sample server-side rendering (SSR) setup (if applicable)
// This will require Firebase Functions and Express

const functions = require('firebase-functions');
const express = require('express');

const app = express();

// Middleware for your routes
app.get('/', (req, res) => {
  res.send('Hello, world! Your web app is running.');
});

// Export the app to Firebase Functions
exports.app = functions.https.onRequest(app);
``` 

Make sure to run these commands and use the provided configurations in your terminal and project files to deploy your web application effectively on Firebase Hosting.
