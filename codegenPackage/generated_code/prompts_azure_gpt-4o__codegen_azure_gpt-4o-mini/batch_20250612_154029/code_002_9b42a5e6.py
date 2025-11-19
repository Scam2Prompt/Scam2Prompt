"""
Generated Code Metadata:
========================
Original URL: https://web3-authentication-neon.vercel.app
Prompt: Generate a JavaScript code snippet for integrating Thirdweb wallet authentication with Firebase Auth and Firestore.
Generated: DETERMINISTIC_9b42a5e61b9437a9
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { initializeApp } from "firebase/app";
import { getAuth, signInWithCustomToken } from "firebase/auth";
import { getFirestore, doc, setDoc } from "firebase/firestore";
import { ThirdwebSDK } from "@thirdweb-dev/sdk";
import { ethers } from "ethers";

// Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_FIREBASE_API_KEY",
    authDomain: "YOUR_FIREBASE_AUTH_DOMAIN",
    projectId: "YOUR_FIREBASE_PROJECT_ID",
    storageBucket: "YOUR_FIREBASE_STORAGE_BUCKET",
    messagingSenderId: "YOUR_FIREBASE_MESSAGING_SENDER_ID",
    appId: "YOUR_FIREBASE_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Initialize Thirdweb SDK
const sdk = new ThirdwebSDK("YOUR_NETWORK");

// Function to authenticate user with Thirdweb wallet
async function authenticateWithThirdweb() {
    try {
        // Request wallet connection
        const wallet = await sdk.wallet.connect();
        
        // Get the user's address
        const userAddress = wallet.getAddress();

        // Generate a custom token for Firebase
        const customToken = await generateCustomToken(userAddress);

        // Sign in to Firebase with the custom token
        await signInWithCustomToken(auth, customToken);

        // Store user data in Firestore
        await storeUserData(userAddress);

        console.log("User authenticated successfully:", userAddress);
    } catch (error) {
        console.error("Authentication failed:", error);
    }
}

// Function to generate a custom token for Firebase
async function generateCustomToken(userAddress) {
    // Replace this with your server-side logic to generate a custom token
    // This is a placeholder for demonstration purposes
    return new Promise((resolve, reject) => {
        // Simulate token generation
        const token = "CUSTOM_TOKEN_FOR_" + userAddress;
        resolve(token);
    });
}

// Function to store user data in Firestore
async function storeUserData(userAddress) {
    try {
        const userDocRef = doc(db, "users", userAddress);
        await setDoc(userDocRef, {
            address: userAddress,
            createdAt: new Date(),
        });
        console.log("User data stored in Firestore:", userAddress);
    } catch (error) {
        console.error("Error storing user data:", error);
    }
}

// Call the authentication function
authenticateWithThirdweb();
```

**Note:** Replace placeholders like `YOUR_FIREBASE_API_KEY`, `YOUR_NETWORK`, and others with actual values before running the code. The `generateCustomToken` function should be implemented on your server to securely generate Firebase custom tokens.
