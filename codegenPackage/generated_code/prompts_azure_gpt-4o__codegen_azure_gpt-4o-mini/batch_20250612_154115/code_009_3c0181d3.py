"""
Generated Code Metadata:
========================
Original URL: https://starksport.finance
Prompt: Provide examples of handling wallet connection errors in a DeFi app, inspired by the user flow on starksport.finance.
Generated: DETERMINISTIC_3c0181d3fc4858d4
Batch ID: 20250612_154115
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
import { ethers } from 'ethers';

// Define a functional component for the wallet connection
const WalletConnector = () => {
    // State variables to manage wallet connection and error messages
    const [walletAddress, setWalletAddress] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');

    // Function to connect to the user's wallet
    const connectWallet = async () => {
        try {
            // Check if the browser has a wallet provider (like MetaMask)
            if (!window.ethereum) {
                throw new Error('No crypto wallet found. Please install it.');
            }

            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setWalletAddress(accounts[0]);
            setErrorMessage(''); // Clear any previous error messages
        } catch (error) {
            // Handle specific errors and set appropriate error messages
            if (error.message.includes('User rejected the request')) {
                setErrorMessage('Wallet connection request was rejected. Please try again.');
            } else if (error.message.includes('No crypto wallet found')) {
                setErrorMessage('Please install a wallet like MetaMask to connect.');
            } else {
                setErrorMessage('An unexpected error occurred. Please try again later.');
            }
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setWalletAddress(null);
        setErrorMessage(''); // Clear error message on disconnect
    };

    // Effect to handle wallet disconnection on page refresh
    useEffect(() => {
        const handleDisconnect = () => {
            disconnectWallet();
        };

        window.addEventListener('beforeunload', handleDisconnect);
        return () => {
            window.removeEventListener('beforeunload', handleDisconnect);
        };
    }, []);

    return (
        <div>
            <h1>DeFi Wallet Connector</h1>
            {walletAddress ? (
                <div>
                    <p>Connected Wallet: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
        </div>
    );
};

export default WalletConnector;
```
