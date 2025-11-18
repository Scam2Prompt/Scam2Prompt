"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.algocryptobot.com
Prompt: How can I configure Firebase Hosting for a project after completing the setup? Provide code examples and steps based on Firebase SDK.
Generated: DETERMINISTIC_790e2419edcefa7a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI globally if you haven't done it yet
npm install -g firebase-tools
```

```bash
# Step 2: Initialize Firebase in your project directory
firebase init hosting
```
```json
{
  "hosting": {
    "public": "dist", // Directory that contains your built files
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [ // Optional: Configure rewrites if using frameworks like React or Angular
      {
        "source": "/**",
        "destination": "/index.html"
      }
    ]
  }
}
```

```javascript
// Step 3: Import and configure Firebase in your application (e.g., in app.js or main.js)

// Import the Firebase modules
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID",
};

// Initialize Firebase
try {
    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    const auth = getAuth(app);
    console.log("Firebase initialized successfully.");
} catch (error) {
    console.error("Error initializing Firebase:", error);
}
```

```bash
# Step 4: Build your project (if applicable)
npm run build
```

```bash
# Step 5: Deploy your application to Firebase Hosting
firebase deploy --only hosting
```
