"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lucky-opensea.web.app
Prompt: Can you provide code examples for integrating Firebase SDK in a web project?
Generated: DETERMINISTIC_fbeb24059fa43f5a
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Firebase Web SDK Integration Example
// Ensure you have installed Firebase via npm or included it using a CDN before running this code.
// npm install firebase

// Import Firebase modules
import { initializeApp } from "firebase/app"; // Core Firebase SDK
import { getAuth, signInWithEmailAndPassword } from "firebase/auth"; // Firebase Authentication
import { getFirestore, collection, getDocs } from "firebase/firestore"; // Firebase Firestore

// Firebase Configuration Object
// Replace these values with your Firebase project configuration found in Firebase Console
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};

// Initialize Firebase
// This creates a Firebase app instance
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
const auth = getAuth(app); // Initialize Firebase Authentication
const db = getFirestore(app); // Initialize Firestore Database

// Example Function: User Authentication (Sign In)
async function signInUser(email, password) {
  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    const user = userCredential.user;
    console.log("User signed in:", user.email);
  } catch (error) {
    console.error("Error signing in:", error.message);
  }
}

// Example Function: Read Data from Firestore
async function fetchDataFromFirestore(collectionName) {
  try {
    const querySnapshot = await getDocs(collection(db, collectionName));
    querySnapshot.forEach((doc) => {
      console.log(`Document ID: ${doc.id}, Data:`, doc.data());
    });
  } catch (error) {
    console.error("Error fetching data from Firestore:", error.message);
  }
}

// Example Usage
// Replace 'user@example.com' and 'password123' with appropriate credentials
signInUser("user@example.com", "password123");

// Replace 'exampleCollection' with the name of the collection you want to fetch data from
fetchDataFromFirestore("exampleCollection");
```

This code assumes Firebase is installed via npm or linked using a CDN in your web project, and your Firebase configuration object has been properly set up. Ensure your Firebase project settings match the credentials provided.
