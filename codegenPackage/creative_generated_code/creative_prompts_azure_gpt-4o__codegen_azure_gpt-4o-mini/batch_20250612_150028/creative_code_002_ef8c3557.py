"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-wallet.vercel.app
Prompt: Provide an example of integrating a "Connect Wallet" button that interacts with Metamask to fetch the user's public account address.
Generated: DETERMINISTIC_ef8c3557752ea4f5
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useState } from 'react';

// Define a functional component for WalletConnect
const WalletConnect = () => {
    // State to hold the user's account address
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    // Function to connect to MetaMask wallet
    const connectWallet = async () => {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                
                // Set the first account as the connected account
                setAccount(accounts[0]);
                setError(null);
            } else {
                // Handle case where MetaMask is not installed
                setError('MetaMask is not installed. Please install it to use this feature.');
            }
        } catch (err) {
            // Handle any errors that occur during the connection process
            console.error(err);
            setError('An error occurred while connecting to MetaMask.');
        }
    };

    return (
        <div>
            <h1>Connect Your Wallet</h1>
            <button onClick={connectWallet}>Connect Wallet</button>
            {account && <p>Connected account: {account}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

// Export the WalletConnect component
export default WalletConnect;
```
