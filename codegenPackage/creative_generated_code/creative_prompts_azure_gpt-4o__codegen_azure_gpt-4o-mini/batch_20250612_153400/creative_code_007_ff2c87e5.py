"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merlion.pages.dev
Prompt: Generate a step-by-step guide to integrate the Merlin ecosystem's Connect Wallet feature into a decentralized application (dApp).
Generated: DETERMINISTIC_ff2c87e5e71a71e8
Batch ID: 20250612_153400
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
import { MerlinConnect } from 'merlin-sdk'; // Assuming merlin-sdk is the package name

// Define the ConnectWallet component
const ConnectWallet = () => {
    // State to hold the wallet address and connection status
    const [walletAddress, setWalletAddress] = useState('');
    const [isConnected, setIsConnected] = useState(false);
    
    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    // Function to connect wallet
    const connectWallet = async () => {
        try {
            // Request account access if needed
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Set the wallet address and update connection status
            setWalletAddress(accounts[0]);
            setIsConnected(true);
        } catch (error) {
            // Handle errors (user rejected request, etc.)
            console.error('Connection error:', error);
            alert('Could not connect to wallet. Please try again.');
        }
    };

    // Function to disconnect wallet
    const disconnectWallet = () => {
        setWalletAddress('');
        setIsConnected(false);
    };

    // Effect to log wallet address when connected
    useEffect(() => {
        if (isConnected) {
            console.log('Connected wallet address:', walletAddress);
        }
    }, [isConnected, walletAddress]);

    return (
        <div>
            <h2>Connect to Wallet</h2>
            {!isConnected ? (
                <button onClick={connectWallet}>Connect Wallet</button>
            ) : (
                <div>
                    <p>Connected: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            )}
        </div>
    );
};

// Export the ConnectWallet component
export default ConnectWallet;
```
