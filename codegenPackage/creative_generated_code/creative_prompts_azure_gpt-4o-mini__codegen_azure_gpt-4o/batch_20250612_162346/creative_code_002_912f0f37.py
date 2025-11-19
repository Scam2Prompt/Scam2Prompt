"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-alert-offers-opensea.web.app
Prompt: Can you provide a code example for integrating Firebase SDK in a web project?
Generated: DETERMINISTIC_912f0f37589f1a2c
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Firebase modules
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';
import { getStorage } from 'firebase/storage';

// Firebase configuration object
// Replace the placeholders with your actual Firebase project configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};

// Initialize Firebase App
try {
  const firebaseApp = initializeApp(firebaseConfig);
  console.log('Firebase successfully initialized');
} catch (error) {
  console.error('Error initializing Firebase:', error);
}

// Initialize Firebase services
let firestore, auth, storage;
try {
  firestore = getFirestore();
  auth = getAuth();
  storage = getStorage();
  console.log('Firebase services initialized: Firestore, Auth, Storage');
} catch (error) {
  console.error('Error initializing Firebase services:', error);
}

// Export Firebase services for use in the application
export { firebaseApp, firestore, auth, storage };

// Usage example (optional):
// import { firestore } from './firebaseSetup';
// firestore.collection('users').get().then(...);
```
