"""
Generated Code Metadata:
========================
Original URL: https://zencha.finance
Prompt: Suggest best practices for designing a user interface for connecting cryptocurrency wallets in a DeFi app, inspired by Zencha Finance's "Connect Wallet" feature.
Generated: DETERMINISTIC_d45fbf0dac81892d
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './ConnectWallet.css'; // Importing CSS for styling

// ConnectWallet component for connecting cryptocurrency wallets
const ConnectWallet = () => {
    // State to manage wallet connection status and selected wallet
    const [isConnected, setIsConnected] = useState(false);
    const [walletAddress, setWalletAddress] = useState('');
    const [error, setError] = useState('');

    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setWalletAddress(accounts[0]);
            setIsConnected(true);
            setError('');
        } catch (err) {
            // Handle errors during wallet connection
            console.error('Error connecting to wallet:', err);
            setError('Failed to connect wallet. Please try again.');
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setWalletAddress('');
        setIsConnected(false);
    };

    // Effect to handle wallet disconnection
    useEffect(() => {
        const handleDisconnect = () => {
            disconnectWallet();
        };

        // Listen for account changes
        window.ethereum.on('accountsChanged', handleDisconnect);

        // Cleanup listener on component unmount
        return () => {
            window.ethereum.removeListener('accountsChanged', handleDisconnect);
        };
    }, []);

    return (
        <div className="connect-wallet">
            <h2>Connect Your Wallet</h2>
            {error && <div className="error-message">{error}</div>}
            {isConnected ? (
                <div className="wallet-info">
                    <p>Connected: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default ConnectWallet;
```

```css
/* ConnectWallet.css */

/* Basic styling for the Connect Wallet component */
.connect-wallet {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
}

h2 {
    margin-bottom: 20px;
}

button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #0056b3;
}

.wallet-info {
    margin-top: 10px;
}

.error-message {
    color: red;
    margin-bottom: 10px;
}
```
