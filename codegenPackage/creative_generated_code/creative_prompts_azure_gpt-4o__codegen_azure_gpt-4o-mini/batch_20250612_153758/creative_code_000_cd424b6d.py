"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Write code to integrate a wallet connection feature for a trading platform, referencing the "Connect Wallet" functionality described on the Deeptrade UI webpage.
Generated: DETERMINISTIC_cd424b6df9e5cf99
Batch ID: 20250612_153758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Wallet connection component
const WalletConnect = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [error, setError] = useState(null);

    // Function to connect wallet
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]); // Set the first account
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance); // Initialize web3 instance
            } catch (err) {
                // Handle errors during account access
                setError('Failed to connect wallet: ' + err.message);
                console.error(err);
            }
        } else {
            setError('Please install MetaMask or another wallet extension.');
        }
    };

    // Effect to check if wallet is already connected
    useEffect(() => {
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setAccount(accounts[0]); // Set connected account
                    const web3Instance = new Web3(window.ethereum);
                    setWeb3(web3Instance); // Initialize web3 instance
                }
            } else {
                setError('Please install MetaMask or another wallet extension.');
            }
        };

        checkWalletConnection();
    }, []);

    // Render the wallet connection UI
    return (
        <div>
            <h2>Connect Your Wallet</h2>
            {error && <p className="error">{error}</p>}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={() => setAccount(null)}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnect;
```
