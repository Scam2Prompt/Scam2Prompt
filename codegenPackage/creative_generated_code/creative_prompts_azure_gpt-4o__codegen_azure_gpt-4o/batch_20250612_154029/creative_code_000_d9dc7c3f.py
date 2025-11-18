"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: Write code to implement Web3 wallet authentication using Thirdweb and Firebase, ensuring user accounts are created in Firebase Auth and documents are stored in Firestore.
Generated: DETERMINISTIC_d9dc7c3f0ab88dec
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
import { ThirdwebSDK } from "@thirdweb-dev/sdk";
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";

// Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_FIREBASE_API_KEY",
  authDomain: "YOUR_FIREBASE_AUTH_DOMAIN",
  projectId: "YOUR_FIREBASE_PROJECT_ID",
  storageBucket: "YOUR_FIREBASE_STORAGE_BUCKET",
  messagingSenderId: "YOUR_FIREBASE_MESSAGING_SENDER_ID",
  appId: "YOUR_FIREBASE_APP_ID",
};

// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

// Initialize Firestore
const firestore = firebase.firestore();

// Function to authenticate using Web3 Wallet and Firebase
async function authenticateWithWeb3() {
  try {
    // Initialize Thirdweb SDK
    const sdk = new ThirdwebSDK("ethereum"); // Replace with desired chain

    // Prompt the user to connect their wallet
    const walletAddress = (await sdk.wallet.connect()).address;

    console.log(`Wallet connected: ${walletAddress}`);

    // Generate a nonce for signature
    const nonce = Math.random().toString(36).substring(2);

    // Ask the user to sign the nonce
    const signature = await sdk.wallet.sign(nonce);

    console.log(`Signature obtained: ${signature}`);

    // Verify the signature server-side (mock verification here)
    const isSignatureValid = true; // Replace with actual server-side verification logic
    if (!isSignatureValid) {
      throw new Error("Invalid signature.");
    }

    // Use wallet address as the unique identifier for Firebase
    const firebaseCredential = firebase.auth().signInWithCustomToken(
      await createFirebaseCustomToken(walletAddress)
    );

    // Create or update user document in Firestore
    const userRef = firestore.collection("users").doc(walletAddress);
    await userRef.set(
      {
        walletAddress,
        createdAt: firebase.firestore.FieldValue.serverTimestamp(),
        lastLogin: firebase.firestore.FieldValue.serverTimestamp(),
      },
      { merge: true } // Merge in case the document already exists
    );

    console.log(`User authenticated and stored in Firestore: ${walletAddress}`);
  } catch (error) {
    console.error("Authentication failed:", error.message);
    alert("Authentication failed. Please try again later.");
  }
}

// Function to create Firebase custom token (mock implementation)
async function createFirebaseCustomToken(walletAddress) {
  // Replace this with actual logic to generate a Firebase custom token server-side
  // using your server SDK or Firebase Admin SDK.
  return Promise.resolve(`mock-token-for-${walletAddress}`);
}

// Run the authentication function
authenticateWithWeb3();
```

> Replace placeholders like `YOUR_FIREBASE_API_KEY` and `YOUR_FIREBASE_PROJECT_ID` with your actual Firebase project configuration values.
