"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: Provide an example of connecting a crypto wallet using Thirdweb and storing user authentication data in Firebase Auth and Firestore.
Generated: DETERMINISTIC_2dc5ce7136a89e52
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
import { ThirdwebProvider, useWallet } from '@thirdweb-dev/react';
import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

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
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

const App = () => {
  const { connectWallet, wallet } = useWallet();
  const [user, setUser] = useState(null);
  const db = firebase.firestore();

  // Function to handle wallet connection
  const handleWalletConnect = async () => {
    try {
      // Connect the wallet
      const connectedWallet = await connectWallet('injected');
      console.log('Wallet connected:', connectedWallet);

      // Store user authentication data in Firebase
      const userUID = connectedWallet.address;
      const userRef = db.collection('users').doc(userUID);

      // Set user data in Firestore if it doesn't exist
      const userDoc = await userRef.get();
      if (!userDoc.exists) {
        await userRef.set({
          address: userUID,
          createdAt: firebase.firestore.FieldValue.serverTimestamp()
        });
      }

      // Update state with user information
      setUser({ address: userUID });
    } catch (error) {
      console.error('Error connecting wallet or saving user:', error);
    }
  };

  // Effect to handle user state
  useEffect(() => {
    const unsubscribe = firebase.auth().onAuthStateChanged((firebaseUser) => {
      if (firebaseUser) {
        setUser({ address: firebaseUser.uid });
      } else {
        setUser(null);
      }
    });

    return () => unsubscribe(); // Clean up subscription on unmount
  }, []);

  return (
    <div>
      <h1>Connect Your Crypto Wallet</h1>
      {user ? (
        <p>Connected Wallet Address: {user.address}</p>
      ) : (
        <button onClick={handleWalletConnect}>Connect Wallet</button>
      )}
    </div>
  );
};

// Wrap the App component with ThirdwebProvider for wallet context
const Root = () => {
  return (
    <ThirdwebProvider>
      <App />
    </ThirdwebProvider>
  );
};

// Export the Root component
export default Root;
```

**Note**: Replace the placeholders in the `firebaseConfig` object with your actual Firebase project credentials. Ensure you have the required dependencies (`@thirdweb-dev/react`, `firebase`, `react`) installed in your project for the code to work.
