"""
Generated Code Metadata:
========================
Original URL: https://web3-authentication-neon.vercel.app
Prompt: Create a React component that uses Thirdweb to authenticate users with their wallets and stores user data in Firebase Firestore.
Generated: DETERMINISTIC_5c59149cfdbbc2b0
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import { useWallet } from '@thirdweb-dev/react'; // Thirdweb wallet hook
import { initializeApp } from 'firebase/app'; // Firebase app initialization
import { getFirestore, doc, setDoc } from 'firebase/firestore'; // Firestore functions
import { ToastContainer, toast } from 'react-toastify'; // For notifications
import 'react-toastify/dist/ReactToastify.css'; // Toast CSS

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
const db = getFirestore(app);

// UserAuthentication component
const UserAuthentication = () => {
  const { connectWallet, address, disconnectWallet } = useWallet(); // Thirdweb wallet methods
  const [userData, setUserData] = useState(null); // State to hold user data

  // Effect to handle user authentication
  useEffect(() => {
    if (address) {
      // If user is connected, store user data in Firestore
      storeUserData(address);
    }
  }, [address]);

  // Function to connect wallet
  const handleConnectWallet = async () => {
    try {
      await connectWallet(); // Connect wallet
      toast.success("Wallet connected successfully!"); // Notify success
    } catch (error) {
      console.error("Error connecting wallet:", error);
      toast.error("Failed to connect wallet."); // Notify error
    }
  };

  // Function to disconnect wallet
  const handleDisconnectWallet = async () => {
    try {
      await disconnectWallet(); // Disconnect wallet
      setUserData(null); // Clear user data
      toast.info("Wallet disconnected."); // Notify disconnection
    } catch (error) {
      console.error("Error disconnecting wallet:", error);
      toast.error("Failed to disconnect wallet."); // Notify error
    }
  };

  // Function to store user data in Firestore
  const storeUserData = async (userAddress) => {
    try {
      const userDoc = doc(db, 'users', userAddress); // Reference to user document
      await setDoc(userDoc, { address: userAddress, timestamp: new Date() }, { merge: true }); // Store user data
      setUserData({ address: userAddress }); // Update state with user data
      toast.success("User data stored successfully!"); // Notify success
    } catch (error) {
      console.error("Error storing user data:", error);
      toast.error("Failed to store user data."); // Notify error
    }
  };

  return (
    <div>
      <h1>User Authentication with Wallet</h1>
      {address ? (
        <div>
          <p>Connected Wallet: {address}</p>
          <button onClick={handleDisconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnectWallet}>Connect Wallet</button>
      )}
      <ToastContainer /> {/* Toast notifications container */}
    </div>
  );
};

export default UserAuthentication;
```

**Note:** Replace the placeholders in `firebaseConfig` with your actual Firebase project configuration values.
