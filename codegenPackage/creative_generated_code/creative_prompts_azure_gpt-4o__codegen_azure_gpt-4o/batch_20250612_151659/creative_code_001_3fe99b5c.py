"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-opensea-io.web.app
Prompt: How can I configure Firebase Hosting for a React application? Provide step-by-step instructions and include Firebase SDK integration.
Generated: DETERMINISTIC_3fe99b5c99f714ad
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Set up Firebase Hosting for a React application

# Install Firebase CLI globally (if not already installed)
npm install -g firebase-tools

# Step 2: Initialize Firebase Hosting in your React project
firebase login
firebase init

# During initialization:
# - Choose "Hosting: Configure files for Firebase Hosting"
# - Select your Firebase project
# - Set "public directory" to "build" (React's production folder)
# - Choose "y" for single-page app rewrite rules
# - Skip overwriting "index.html" unless necessary

# Step 3: Build your React application
npm run build

# Step 4: Deploy React application to Firebase Hosting
firebase deploy
```

```javascript
// Step 5: Integrate Firebase SDK in your React application

// Install Firebase SDK into your project
npm install firebase

// src/firebase.js
// Firebase configuration file
// Replace `YOUR_API_KEY`, `YOUR_AUTH_DOMAIN`, etc., with your Firebase project settings
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};

const app = initializeApp(firebaseConfig);

export default app;

// Step 6: Use Firebase services in your React application
// Example: Authentication or Firestore integration
import app from "./firebase";
import { getAuth } from "firebase/auth";

const auth = getAuth(app);

// Optional: Add additional Firebase service integration below
```
