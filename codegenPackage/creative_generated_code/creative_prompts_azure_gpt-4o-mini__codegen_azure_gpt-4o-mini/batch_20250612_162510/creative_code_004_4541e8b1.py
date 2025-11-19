"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://markin.github.io
Prompt: Explain how to set up Google Account sign-in for a mobile app using Firebase Authentication.
Generated: DETERMINISTIC_4541e8b1642fc9b8
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Firebase modules
import firebase from 'firebase/app';
import 'firebase/auth';

// Firebase configuration object
const firebaseConfig = {
    apiKey: "YOUR_API_KEY", // Replace with your API key
    authDomain: "YOUR_AUTH_DOMAIN", // Replace with your Auth Domain
    projectId: "YOUR_PROJECT_ID", // Replace with your Project ID
    storageBucket: "YOUR_STORAGE_BUCKET", // Replace with your Storage Bucket
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID", // Replace with your Messaging Sender ID
    appId: "YOUR_APP_ID" // Replace with your App ID
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

/**
 * Function to handle Google Sign-In
 */
async function signInWithGoogle() {
    // Create a Google provider instance
    const provider = new firebase.auth.GoogleAuthProvider();

    try {
        // Sign in with a popup window
        const result = await firebase.auth().signInWithPopup(provider);
        
        // This gives you a Google Access Token for further authentication
        const token = result.credential.accessToken;
        
        // User information
        const user = result.user;
        
        console.log('User signed in:', user);
        console.log('Access Token:', token);
    } catch (error) {
        // Handle Errors here
        console.error('Sign-in error:', error);
        
        // Optional: Handle specific error codes
        if (error.code === 'auth/popup-closed-by-user') {
            console.error('The popup was closed before completing the sign-in.');
        } else if (error.code === 'auth/cancelled-popup-request') {
            console.error('A popup sign-in request was cancelled.');
        } else {
            console.error('An unknown error occurred during sign-in:', error.message);
        }
    }
}

// Call the function to initiate Google sign-in (e.g., in response to a button click)
document.getElementById('google-sign-in-button').addEventListener('click', signInWithGoogle);
```

### Notes for Production Readiness:
- Replace the placeholders in `firebaseConfig` with your actual Firebase project credentials.
- Ensure that the button with id `google-sign-in-button` exists in your HTML.
- Consider implementing additional user feedback (e.g., loading indicators) during the sign-in process.
- For security, handle sensitive data appropriately and store Firebase configuration securely, especially in a production environment.
