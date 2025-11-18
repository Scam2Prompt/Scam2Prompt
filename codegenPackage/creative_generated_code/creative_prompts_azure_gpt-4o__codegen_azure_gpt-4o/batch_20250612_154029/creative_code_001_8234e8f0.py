"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: How can I use Thirdweb to authenticate users via their crypto wallets and link this authentication to Firebase Auth and Firestore?
Generated: DETERMINISTIC_8234e8f0bf116adf
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and libraries
import { ThirdwebSDK } from "@thirdweb-dev/sdk"; // For Thirdweb authentication
import firebase from "firebase/app"; // Firebase core
import "firebase/auth"; // Firebase auth module
import "firebase/firestore"; // Firebase Firestore module

// Firebase configuration object (replace with your own config settings)
const firebaseConfig = {
  apiKey: "YOUR_FIREBASE_API_KEY",
  authDomain: "YOUR_FIREBASE_AUTH_DOMAIN",
  projectId: "YOUR_FIREBASE_PROJECT_ID",
  storageBucket: "YOUR_FIREBASE_STORAGE_BUCKET",
  messagingSenderId: "YOUR_FIREBASE_MESSAGING_SENDER_ID",
  appId: "YOUR_FIREBASE_APP_ID",
};

// Initialize Firebase if not already initialized
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

// Firebase services
const auth = firebase.auth();
const firestore = firebase.firestore();

// Function to authenticate users via their crypto wallet and link to Firebase
async function authenticateWithWallet() {
  try {
    // Step 1: Initialize Thirdweb SDK
    const sdk = new ThirdwebSDK("mainnet"); // Use Ethereum mainnet (or adjust for other networks)

    // Step 2: Request wallet connection
    const walletAddress = await sdk.wallet.connect(); // MetaMask or other wallet connection prompt

    // Step 3: Generate a nonce for authentication
    const nonce = await sdk.auth.generateNonce();

    // Step 4: Have the user sign the nonce with their wallet
    const signature = await sdk.wallet.sign(nonce);

    // Step 5: Verify the signature using Thirdweb Auth
    const verifiedPayload = await sdk.auth.verify(walletAddress, signature);

    // Step 6: Use Firebase custom token authentication
    const customToken = await createFirebaseCustomToken(walletAddress);
    await auth.signInWithCustomToken(customToken);

    // Step 7: Store user data in Firestore
    const userDocRef = firestore.collection("users").doc(walletAddress);
    await userDocRef.set(
      {
        walletAddress: walletAddress,
        authenticatedAt: firebase.firestore.FieldValue.serverTimestamp(),
      },
      { merge: true }
    );

    console.log("User authenticated and linked to Firebase successfully!");
  } catch (error) {
    console.error("Error during wallet authentication:", error);
  }
}

// Function to create a Firebase custom token for the user
async function createFirebaseCustomToken(walletAddress) {
  try {
    // Placeholder: Replace this with your server-side logic to generate Firebase custom tokens
    const response = await fetch("/generateFirebaseToken", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ walletAddress }),
    });

    if (!response.ok) {
      throw new Error("Failed to generate Firebase custom token");
    }

    const { customToken } = await response.json();
    return customToken;
  } catch (error) {
    console.error("Error generating Firebase custom token:", error);
    throw error;
  }
}

// Usage example (e.g., on a button click)
document.getElementById("authenticateButton").addEventListener("click", authenticateWithWallet);
```

### Notes:
1. Replace `/generateFirebaseToken` with the endpoint for your server-side logic to generate Firebase custom tokens.
2. Ensure proper server-side implementation of Firebase custom token generation securely tied to wallet verification.
