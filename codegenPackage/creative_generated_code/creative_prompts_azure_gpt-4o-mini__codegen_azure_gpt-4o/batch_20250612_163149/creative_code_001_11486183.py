"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: Write a code snippet to authenticate users with their wallets and store their information in Firestore using Thirdweb and Firebase.
Generated: DETERMINISTIC_114861839e305314
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
import { ThirdwebSDK } from "@thirdweb-dev/sdk";
import { initializeApp } from "firebase/app";
import { getFirestore, doc, setDoc } from "firebase/firestore";

// Firebase configuration object
const firebaseConfig = {
  apiKey: "YOUR_FIREBASE_API_KEY",
  authDomain: "YOUR_FIREBASE_AUTH_DOMAIN",
  projectId: "YOUR_FIREBASE_PROJECT_ID",
  storageBucket: "YOUR_FIREBASE_STORAGE_BUCKET",
  messagingSenderId: "YOUR_FIREBASE_MESSAGING_SENDER_ID",
  appId: "YOUR_FIREBASE_APP_ID",
};

// Initialize Firebase app and Firestore
const firebaseApp = initializeApp(firebaseConfig);
const db = getFirestore(firebaseApp);

// Initialize Thirdweb SDK
const sdk = new ThirdwebSDK("ethereum"); // Use the appropriate chain (e.g., "polygon", "ethereum")

/**
 * Function to authenticate a user with their wallet and store their information in Firestore
 * @param {string} walletAddress - The user's wallet address
 * @returns {Promise<void>} Resolves when the user data is stored successfully
 */
async function authenticateAndStoreUser(walletAddress) {
  try {
    // Generate a message for the user to sign
    const message = `Authentication request at ${new Date().toISOString()}`;

    // Prompt the user to sign the message with their wallet
    const signature = await sdk.wallet.sign(message);

    // Verify the signature
    const isValidSignature = await sdk.wallet.verify(message, signature, walletAddress);

    if (!isValidSignature) {
      throw new Error("Invalid wallet signature.");
    }

    // Prepare user data for Firestore
    const userData = {
      walletAddress,
      authenticatedAt: new Date().toISOString(),
    };

    // Store the user data in Firestore
    await setDoc(doc(db, "users", walletAddress), userData);

    console.log("User authenticated and stored successfully:", userData);
  } catch (error) {
    console.error("Error authenticating or storing user:", error.message);
    throw error; // Rethrow the error for upstream handling
  }
}

// Example usage
(async () => {
  const walletAddress = "0x1234567890abcdef1234567890abcdef12345678"; // Replace with the user's wallet address
  await authenticateAndStoreUser(walletAddress);
})();
```
