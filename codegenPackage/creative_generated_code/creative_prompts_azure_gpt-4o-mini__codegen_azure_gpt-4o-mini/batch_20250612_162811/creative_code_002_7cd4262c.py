"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Write code to integrate wallet connection and disconnection features in a web application similar to Monad Whiteboard NFT.
Generated: DETERMINISTIC_7cd4262c5a59d166
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletIntegration.js

// Import necessary libraries
import Web3 from 'web3';
import { useState, useEffect } from 'react';

// Initialize the Web3 instance
let web3;

// Function to check if the wallet is connected
const checkWalletConnected = async () => {
    if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        return accounts.length > 0 ? accounts[0] : null;
    }
    return null;
};

// Custom hook for wallet connection management
export const useWalletConnection = () => {
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Check if wallet is connected on component mount
        const fetchAccount = async () => {
            try {
                const connectedAccount = await checkWalletConnected();
                setAccount(connectedAccount);
            } catch (err) {
                console.error("Error checking wallet connection:", err);
                setError('Failed to check wallet connection.');
            }
        };

        fetchAccount();
    }, []);

    // Function to connect wallet
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]);
            } catch (err) {
                console.error("Error connecting wallet:", err);
                setError('Failed to connect wallet.');
            }
        } else {
            setError('MetaMask or another Ethereum wallet provider is required.');
        }
    };

    // Function to disconnect wallet
    const disconnectWallet = () => {
        setAccount(null);
        // Additional logic to handle disconnection can be added here
    };

    return { account, connectWallet, disconnectWallet, error };
};

// WalletConnectButton.js
import React from 'react';
import { useWalletConnection } from './walletIntegration';

const WalletConnectButton = () => {
    const { account, connectWallet, disconnectWallet, error } = useWalletConnection();

    return (
        <div>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Connected: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnectButton;

// Main application file (e.g., App.js)
import React from 'react';
import WalletConnectButton from './WalletConnectButton';

const App = () => {
    return (
        <div>
            <h1>Monad Whiteboard NFT</h1>
            <WalletConnectButton />
        </div>
    );
};

export default App;
```
