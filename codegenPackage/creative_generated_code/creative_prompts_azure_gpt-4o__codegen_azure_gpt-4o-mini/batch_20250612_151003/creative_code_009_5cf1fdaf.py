"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentraland-orig.web.app
Prompt: Provide a step-by-step guide to implement wallet connection for Decentraland in a React application.
Generated: DETERMINISTIC_5cf1fdafdf3cd406
Batch ID: 20250612_151003
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
import { ethers } from 'ethers';

// Define the main component
const WalletConnection = () => {
    // State to store the current wallet address and error messages
    const [walletAddress, setWalletAddress] = useState(null);
    const [error, setError] = useState(null);

    // Function to request wallet connection
    const connectWallet = async () => {
        try {
            // Check if window.ethereum is available
            if (!window.ethereum) {
                throw new Error('MetaMask is not installed. Please install it to use this feature.');
            }

            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Set the first account as the connected wallet address
            setWalletAddress(accounts[0]);
            setError(null);
        } catch (err) {
            // Handle errors and set error messages
            setError(err.message);
            console.error('Error connecting to wallet:', err);
        }
    };

    // Function to disconnect wallet
    const disconnectWallet = () => {
        setWalletAddress(null);
        setError(null);
    };

    // UseEffect to log address change (optional)
    useEffect(() => {
        if (walletAddress) {
            console.log('Connected wallet address:', walletAddress);
        }
    }, [walletAddress]);

    return (
        <div>
            <h1>Decentraland Wallet Connection</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {walletAddress ? (
                <div>
                    <p>Connected Wallet: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the component as default
export default WalletConnection;
```

### Instructions to Use:
1. Ensure you have `ethers` library installed by running `npm install ethers`.
2. Place the above code in a file named `WalletConnection.js`.
3. Import and use the `<WalletConnection />` component in your main application file (e.g., `App.js`).
4. Make sure MetaMask or another Ethereum wallet is installed in your browser for this code to function properly.
