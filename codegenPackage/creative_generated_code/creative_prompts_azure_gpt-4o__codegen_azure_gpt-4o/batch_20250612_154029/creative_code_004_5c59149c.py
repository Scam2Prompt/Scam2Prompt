"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: Create a React component that uses Thirdweb to authenticate users with their wallets and stores user data in Firebase Firestore.
Generated: DETERMINISTIC_5c59149cfdbbc2b0
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and dependencies
import React, { useState, useEffect } from 'react';
import { ConnectWallet, useAddress } from "@thirdweb-dev/react"; // Thirdweb for wallet authentication
import firebase from "firebase/app"; // Firebase core
import "firebase/firestore"; // Firebase Firestore

// Firebase configuration object (replace with your own Firebase project details)
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};

// Initialize Firebase (ensure it's initialized only once)
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

// Firestore reference
const firestore = firebase.firestore();

// React Component: WalletAuth
const WalletAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false); // State to track authentication
  const [userData, setUserData] = useState(null); // State to store user data
  const address = useAddress(); // Thirdweb hook to get wallet address

  // Function to store user data in Firestore
  const storeUserData = async (walletAddress) => {
    try {
      // Check if user already exists
      const userRef = firestore.collection('users').doc(walletAddress);
      const doc = await userRef.get();

      if (!doc.exists) {
        // Create a new user document if it doesn't exist
        await userRef.set({
          walletAddress: walletAddress,
          createdAt: firebase.firestore.FieldValue.serverTimestamp(),
        });
      } else {
        console.log("User already exists in Firestore.");
      }

      // Fetch and set user data from Firestore
      const userData = await userRef.get();
      setUserData(userData.data());
      setIsAuthenticated(true);
    } catch (error) {
      console.error("Error storing user data in Firestore:", error);
    }
  };

  // Effect to monitor wallet connection and handle authentication
  useEffect(() => {
    if (address) {
      storeUserData(address); // Store user data when wallet is connected
    } else {
      setIsAuthenticated(false); // Reset authentication state if no wallet address
      setUserData(null); // Clear user data
    }
  }, [address]);

  return (
    <div>
      <h1>Wallet Authentication with Thirdweb and Firebase</h1>
      {/* ConnectWallet button for user to authenticate */}
      <ConnectWallet />

      {/* Conditional rendering based on authentication status */}
      {isAuthenticated ? (
        <div>
          <h2>Welcome, authenticated user!</h2>
          <p>Your wallet address: {userData?.walletAddress}</p>
        </div>
      ) : (
        <p>Please connect your wallet to authenticate.</p>
      )}
    </div>
  );
};

export default WalletAuth;
```
