"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-authentication-neon.vercel.app
Prompt: How do I implement wallet-based authentication in a Web3 app using Thirdweb and Firebase Firestore?
Generated: DETERMINISTIC_dd6162da9a477ecf
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import { useAuth } from 'reactfire';
import { useWallet } from '@thirdweb-dev/react';
import { Firestore, getFirestore, doc, setDoc, getDoc } from 'firebase/firestore';
import { initializeApp } from 'firebase/app';

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
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Wallet authentication component
const WalletAuth = () => {
    const { connect, address, disconnect } = useWallet();
    const auth = useAuth();
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const checkUser = async () => {
            setLoading(true);
            try {
                // Check if user is already authenticated
                if (address) {
                    const userDoc = await getDoc(doc(db, "users", address));
                    if (userDoc.exists()) {
                        setUser(userDoc.data());
                    } else {
                        // Register new user if not exists
                        await registerUser(address);
                    }
                }
            } catch (error) {
                console.error("Error fetching user data: ", error);
            } finally {
                setLoading(false);
            }
        };

        checkUser();
    }, [address]);

    // Function to register a new user
    const registerUser = async (address) => {
        try {
            await setDoc(doc(db, "users", address), { walletAddress: address });
            setUser({ walletAddress: address });
        } catch (error) {
            console.error("Error registering user: ", error);
        }
    };

    // Function to handle wallet connection
    const handleConnect = async () => {
        try {
            await connect();
        } catch (error) {
            console.error("Error connecting wallet: ", error);
        }
    };

    // Function to handle wallet disconnection
    const handleDisconnect = async () => {
        try {
            disconnect();
            setUser(null);
        } catch (error) {
            console.error("Error disconnecting wallet: ", error);
        }
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            {user ? (
                <div>
                    <h3>Welcome, {user.walletAddress}</h3>
                    <button onClick={handleDisconnect}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={handleConnect}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletAuth;
```
