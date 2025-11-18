"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.algocryptobot.com
Prompt: Explain how to integrate Firebase Hosting with other Firebase services using the Firebase SDK. Include code snippets for setup.
Generated: DETERMINISTIC_c2e6d6c87940b5f5
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Firebase modules
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';
import { getFunctions } from 'firebase/functions';

// Firebase configuration object
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
const db = getFirestore(app); // Firestore Database
const auth = getAuth(app); // Authentication
const functions = getFunctions(app); // Cloud Functions

// Example function to sign in a user
async function signIn(email, password) {
  try {
    const userCredential = await auth.signInWithEmailAndPassword(email, password);
    console.log('User signed in:', userCredential.user);
  } catch (error) {
    console.error('Error signing in:', error);
  }
}

// Example function to add data to Firestore
async function addData(collectionName, data) {
  try {
    const docRef = await db.collection(collectionName).add(data);
    console.log('Document written with ID:', docRef.id);
  } catch (error) {
    console.error('Error adding document:', error);
  }
}

// Example function to call a Cloud Function
async function callMyFunction(functionName, data) {
  try {
    const result = await functions.httpsCallable(functionName)(data);
    console.log('Function result:', result.data);
  } catch (error) {
    console.error('Error calling function:', error);
  }
}

// Example usage
signIn('user@example.com', 'password123');
addData('users', { name: 'John Doe', email: 'user@example.com' });
callMyFunction('myCloudFunction', { param1: 'value1' });
```
