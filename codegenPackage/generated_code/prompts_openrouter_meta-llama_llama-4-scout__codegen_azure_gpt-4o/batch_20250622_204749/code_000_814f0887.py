"""
Generated Code Metadata:
========================
Original URL: https://collectiverse-dev.firebaseapp.com
Prompt: "How to enable JavaScript in a Firebase application to ensure proper functionality?"
Generated: DETERMINISTIC_814f088788ec7b6a
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Firebase Application Initialization Script
 * This script enables JavaScript functionality in a Firebase application
 * and ensures proper setup and error handling.
 */

// Import Firebase SDKs (Ensure these are installed via npm or included in your project)
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

/**
 * Firebase configuration object.
 * Replace the values below with your Firebase project's configuration.
 */
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};

// Initialize Firebase application
let firebaseApp;
try {
  firebaseApp = initializeApp(firebaseConfig);
  console.log("Firebase initialized successfully.");
} catch (error) {
  console.error("Error initializing Firebase:", error);
  // Handle initialization error (e.g., invalid config)
}

// Initialize Firebase services
let auth, firestore, storage;
try {
  auth = getAuth(firebaseApp);
  firestore = getFirestore(firebaseApp);
  storage = getStorage(firebaseApp);
  console.log("Firebase services initialized successfully.");
} catch (error) {
  console.error("Error initializing Firebase services:", error);
  // Handle service initialization error
}

/**
 * Example function to demonstrate Firebase functionality.
 * This function writes data to Firestore and handles errors.
 */
async function writeToFirestore(collectionName, data) {
  try {
    const docRef = await firestore.collection(collectionName).add(data);
    console.log("Document written with ID:", docRef.id);
  } catch (error) {
    console.error("Error writing document to Firestore:", error);
    // Handle Firestore write error
  }
}

// Example usage of the writeToFirestore function
writeToFirestore("exampleCollection", { name: "John Doe", age: 30 });

/**
 * Ensure proper functionality by verifying Firebase services are working.
 * Add additional functionality as needed for your application.
 */
```
