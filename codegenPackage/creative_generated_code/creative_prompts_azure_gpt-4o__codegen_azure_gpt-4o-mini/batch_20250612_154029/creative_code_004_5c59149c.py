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

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { useWallet } from '@thirdweb-dev/react'; // Thirdweb wallet hook
import firebase from 'firebase/app'; // Firebase core
import 'firebase/firestore'; // Firestore

// Initialize Firebase (ensure you replace this config with your Firebase project details)
const firebaseConfig = {
  apiKey: "YOUR_FIREBASE_API_KEY",
  authDomain: "YOUR_FIREBASE_AUTH_DOMAIN",
  projectId: "YOUR_FIREBASE_PROJECT_ID",
  storageBucket: "YOUR_FIREBASE_STORAGE_BUCKET",
  messagingSenderId: "YOUR_FIREBASE_MESSAGING_SENDER_ID",
  appId: "YOUR_FIREBASE_APP_ID"
};

// Initialize Firebase app and Firestore
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}
const firestore = firebase.firestore();

// UserAuthentication component
const UserAuthentication = () => {
  const { connect, disconnect, address, error } = useWallet(); // Wallet connection
  const [userData, setUserData] = useState(null); // State to hold user data

  // Effect to fetch user data from Firestore on wallet connection
  useEffect(() => {
    const fetchUserData = async () => {
      if (address) {
        try {
          const doc = await firestore.collection('users').doc(address).get();
          if (doc.exists) {
            setUserData(doc.data());
          } else {
            // If document does not exist, create a new user
            await firestore.collection('users').doc(address).set({
              walletAddress: address,
              createdAt: firebase.firestore.FieldValue.serverTimestamp(),
            });
            setUserData({ walletAddress: address });
          }
        } catch (err) {
          console.error("Error fetching user data:", err);
        }
      }
    };

    fetchUserData();
  }, [address]);

  // Handle wallet connection
  const handleConnect = async () => {
    try {
      await connect();
    } catch (err) {
      console.error("Error connecting wallet:", err);
    }
  };

  // Handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect();
      setUserData(null); // Clear user data on disconnect
    } catch (err) {
      console.error("Error disconnecting wallet:", err);
    }
  };

  return (
    <div>
      <h1>User Authentication with Thirdweb</h1>
      {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}
      {address ? (
        <div>
          <p>Connected Wallet: {address}</p>
          <button onClick={handleDisconnect}>Disconnect</button>
          {userData && <p>User Data: {JSON.stringify(userData)}</p>}
        </div>
      ) : (
        <button onClick={handleConnect}>Connect Wallet</button>
      )}
    </div>
  );
};

export default UserAuthentication;
```
