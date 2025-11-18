"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer3quest.pages.dev
Prompt: Write a script to integrate a Web3 wallet connection feature using the tools and guidelines provided in the Layer3 documentation.
Generated: DETERMINISTIC_09c095343f39b2d2
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and frameworks
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers'; // Ethereum library for interacting with the blockchain
import Layer3 from 'layer3-sdk'; // Hypothetical Layer3 SDK for wallet integration

// WalletConnection component to handle wallet connection
const WalletConnection = () => {
    // State to manage wallet connection status and account address
    const [connected, setConnected] = useState(false);
    const [account, setAccount] = useState('');
    const [error, setError] = useState('');

    // Function to connect to the user's Web3 wallet
    const connectWallet = async () => {
        try {
            // Check if the browser has a Web3 provider (like MetaMask)
            if (window.ethereum) {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]); // Set the connected account
                setConnected(true); // Update connection status
            } else {
                setError('Please install a Web3 wallet such as MetaMask.');
            }
        } catch (err) {
            // Handle errors during wallet connection
            setError(`Connection failed: ${err.message}`);
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setAccount(''); // Clear the account
        setConnected(false); // Update connection status
    };

    // Effect to alert user when wallet is connected
    useEffect(() => {
        if (connected) {
            console.log(`Wallet connected: ${account}`);
        }
    }, [connected, account]);

    return (
        <div>
            <h1>Web3 Wallet Connection</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {!connected ? (
                <button onClick={connectWallet}>Connect Wallet</button>
            ) : (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            )}
        </div>
    );
};

export default WalletConnection;

// Usage
// To use this component, import it into your main application file (e.g., App.js) and include <WalletConnection /> in the JSX.
```
