"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: How can I use Thirdweb's wallet authentication feature to manage user sessions in Firebase Auth and Firestore?
Generated: DETERMINISTIC_2cf8506a9cbdaeb1
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from Firebase and Thirdweb
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithCustomToken } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { ThirdwebSDK } from '@thirdweb-dev/sdk';

// Firebase configuration
const firebaseConfig = {
  apiKey: 'YOUR_FIREBASE_API_KEY',
  authDomain: 'YOUR_FIREBASE_AUTH_DOMAIN',
  projectId: 'YOUR_FIREBASE_PROJECT_ID',
  storageBucket: 'YOUR_FIREBASE_STORAGE_BUCKET',
  messagingSenderId: 'YOUR_FIREBASE_MESSAGING_SENDER_ID',
  appId: 'YOUR_FIREBASE_APP_ID',
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Initialize Thirdweb SDK
const sdk = new ThirdwebSDK("YOUR_NETWORK");

// Function to authenticate user with Thirdweb wallet
async function authenticateUser(walletAddress) {
    try {
        // Generate a JWT token using the wallet address
        const token = await sdk.auth.createToken(walletAddress);

        // Sign in to Firebase using the custom token
        const firebaseUserCredential = await signInWithCustomToken(auth, token);

        // User is authenticated, return user information
        return firebaseUserCredential.user;
    } catch (error) {
        console.error("Error authenticating user:", error);
        throw new Error("Authentication failed, please try again later.");
    }
}

// Function to save user data to Firestore
async function saveUserDataToFirestore(user) {
    try {
        const userDocRef = db.collection('users').doc(user.uid);

        // Check if user document exists
        const doc = await userDocRef.get();
        if (!doc.exists) {
            // Create a new user document if it does not exist
            await userDocRef.set({
                walletAddress: user.email, // Assuming wallet address is stored as email
                createdAt: new Date(),
                updatedAt: new Date(),
            });
        } else {
            // Update existing user document with the current timestamp
            await userDocRef.update({
                updatedAt: new Date(),
            });
        }
    } catch (error) {
        console.error("Error saving user data to Firestore:", error);
        throw new Error("Failed to save user data, please try again later.");
    }
}

// Main function to handle authentication and user data creation
async function handleUserAuthentication(walletAddress) {
    try {
        const user = await authenticateUser(walletAddress);
        await saveUserDataToFirestore(user);
        console.log("User authenticated and data saved successfully:", user);
    } catch (error) {
        console.error("Error handling user authentication:", error);
    }
}

// Example usage
const walletAddress = 'USER_WALLET_ADDRESS'; // Replace with actual user wallet address
handleUserAuthentication(walletAddress);
```

Make sure to replace placeholders like `YOUR_FIREBASE_API_KEY`, `YOUR_NETWORK`, and `USER_WALLET_ADDRESS` with actual values before running the code.
