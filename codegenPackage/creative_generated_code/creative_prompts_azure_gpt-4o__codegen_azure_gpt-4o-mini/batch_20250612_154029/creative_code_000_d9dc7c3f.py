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
// Import necessary libraries from Firebase and Thirdweb
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithCustomToken, createUserWithEmailAndPassword } from 'firebase/auth';
import { getFirestore, doc, setDoc } from 'firebase/firestore';
import { ThirdwebSDK } from '@thirdweb-dev/sdk';

// Firebase configuration
const firebaseConfig = {
  apiKey: 'YOUR_FIREBASE_API_KEY',
  authDomain: 'YOUR_FIREBASE_AUTH_DOMAIN',
  projectId: 'YOUR_FIREBASE_PROJECT_ID',
  storageBucket: 'YOUR_FIREBASE_STORAGE_BUCKET',
  messagingSenderId: 'YOUR_FIREBASE_MESSAGING_SENDER_ID',
  appId: 'YOUR_FIREBASE_APP_ID'
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Initialize Thirdweb SDK
const sdk = new ThirdwebSDK('YOUR_CHAIN_NETWORK'); // e.g., 'mainnet', 'goerli'

// Function to authenticate user using Web3 wallet
async function authenticateWithWallet(walletAddress) {
  try {
    // Generate a custom token for the wallet address
    const token = await generateCustomToken(walletAddress);
    
    // Sign in the user with the custom token
    const userCredential = await signInWithCustomToken(auth, token);
    
    // Get the user information
    const user = userCredential.user;

    // Store user information in Firestore
    await setDoc(doc(db, 'users', user.uid), {
      walletAddress: walletAddress,
      email: user.email,
      createdAt: new Date()
    });

    console.log('User authenticated and data stored:', user);
  } catch (error) {
    console.error('Error during authentication:', error);
  }
}

// Function to create a custom token for the wallet address
async function generateCustomToken(walletAddress) {
  // Implement your logic to generate a custom token
  // This typically involves server-side logic to verify and sign the token
  // For demonstration purposes, return a mock token
  return 'MOCK_CUSTOM_TOKEN';
}

// Example usage: Call the function with a sample wallet address
authenticateWithWallet('0xYourWalletAddressHere');
```

**Note:** Replace placeholders like `YOUR_FIREBASE_API_KEY`, `YOUR_CHAIN_NETWORK`, and `0xYourWalletAddressHere` with actual values. The `generateCustomToken` function should contain logic to generate a valid token, often done on a server environment.
