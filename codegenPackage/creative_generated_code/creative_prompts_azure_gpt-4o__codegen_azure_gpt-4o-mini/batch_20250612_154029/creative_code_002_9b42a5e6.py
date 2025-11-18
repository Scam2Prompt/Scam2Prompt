"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: Generate a JavaScript code snippet for integrating Thirdweb wallet authentication with Firebase Auth and Firestore.
Generated: DETERMINISTIC_9b42a5e61b9437a9
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Thirdweb, Firebase, and Firestore
import { ThirdwebAuth } from "@thirdweb-dev/auth";
import { initializeApp } from "firebase/app";
import { getAuth, signInWithCustomToken } from "firebase/auth";
import { getFirestore, doc, setDoc } from "firebase/firestore";

// Firebase configuration object
const firebaseConfig = {
    apiKey: "YOUR_FIREBASE_API_KEY",
    authDomain: "YOUR_FIREBASE_AUTH_DOMAIN",
    projectId: "YOUR_FIREBASE_PROJECT_ID",
    storageBucket: "YOUR_FIREBASE_STORAGE_BUCKET",
    messagingSenderId: "YOUR_FIREBASE_MESSAGING_SENDER_ID",
    appId: "YOUR_FIREBASE_APP_ID"
};

// Initialize Firebase app
const firebaseApp = initializeApp(firebaseConfig);

// Initialize Firebase Auth and Firestore
const auth = getAuth(firebaseApp);
const db = getFirestore(firebaseApp);

// Initialize Thirdweb Auth
const thirdwebAuth = new ThirdwebAuth({
    // Ensure to provide your Thirdweb SDK configuration here
    domain: "YOUR_DOMAIN",
    apiKey: "YOUR_THIRDWEB_API_KEY",
});

// Function to authenticate user with Thirdweb wallet and sign in with Firebase
async function authenticateWithThirdweb(walletAddress) {
    try {
        // Authenticate with Thirdweb and get a custom token
        const customToken = await thirdwebAuth.authenticate(walletAddress);

        // Use the custom token to sign in to Firebase
        await signInWithCustomToken(auth, customToken);

        // User is authenticated, we can now save user data to Firestore
        const userDocRef = doc(db, "users", walletAddress);
        await setDoc(userDocRef, {
            address: walletAddress,
            lastLogin: new Date(),
        }, { merge: true });

        console.log("User authenticated and data saved to Firestore.");
    } catch (error) {
        console.error("Error during authentication:", error);
        // Handle specific errors (optional)
        switch (error.code) {
            case 'auth/invalid-custom-token':
                console.error("The custom token format is incorrect.");
                break;
            case 'auth/user-not-found':
                console.error("No user found for the provided wallet address.");
                break;
            default:
                console.error("An unexpected error occurred:", error.message);
        }
    }
}

// Example usage: Call this function with the user's wallet address
// authenticateWithThirdweb("0xYourWalletAddressHere");
```

Make sure to replace the placeholders in the firebaseConfig and the ThirdwebAuth initialization with your actual configuration values.
