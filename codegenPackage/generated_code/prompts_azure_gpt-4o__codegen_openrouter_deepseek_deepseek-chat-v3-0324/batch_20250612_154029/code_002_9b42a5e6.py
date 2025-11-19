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
// Import required Firebase and Thirdweb SDKs
import { initializeApp } from "firebase/app";
import { getAuth, signInWithCustomToken } from "firebase/auth";
import { getFirestore, doc, setDoc } from "firebase/firestore";
import { ThirdwebSDK } from "@thirdweb-dev/sdk";

// Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
const auth = getAuth(firebaseApp);
const db = getFirestore(firebaseApp);

// Initialize Thirdweb SDK
const sdk = new ThirdwebSDK("goerli"); // Replace with your desired network

/**
 * Authenticates user with Thirdweb wallet and links to Firebase Auth
 * @returns {Promise<Object>} User auth data
 */
async function authenticateWithThirdweb() {
  try {
    // Connect to wallet
    const walletAddress = await sdk.wallet.connect();
    
    if (!walletAddress) {
      throw new Error("Wallet connection failed");
    }

    // Generate a custom token for Firebase Auth
    const response = await fetch("/api/generateCustomToken", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ walletAddress }),
    });

    if (!response.ok) {
      throw new Error("Failed to generate custom token");
    }

    const { token } = await response.json();

    // Sign in to Firebase with the custom token
    const userCredential = await signInWithCustomToken(auth, token);
    const user = userCredential.user;

    // Create or update user document in Firestore
    const userDocRef = doc(db, "users", user.uid);
    await setDoc(
      userDocRef,
      {
        walletAddress,
        lastLogin: new Date(),
      },
      { merge: true }
    );

    return user;
  } catch (error) {
    console.error("Authentication error:", error);
    throw error;
  }
}

/**
 * Example API route (to be implemented on your backend)
 * This would typically be in a separate server-side file
 */
/*
import { ThirdwebSDK } from "@thirdweb-dev/sdk";
import { getAuth } from "firebase-admin/auth";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  try {
    const { walletAddress } = req.body;
    
    // Verify wallet address
    const sdk = new ThirdwebSDK("goerli");
    const isValid = await sdk.wallet.verify(walletAddress);
    
    if (!isValid) {
      return res.status(401).json({ error: "Invalid wallet address" });
    }

    // Create custom token for Firebase Auth
    const auth = getAuth();
    const customToken = await auth.createCustomToken(walletAddress);

    res.status(200).json({ token: customToken });
  } catch (error) {
    console.error("Token generation error:", error);
    res.status(500).json({ error: "Internal server error" });
  }
}
*/
```
