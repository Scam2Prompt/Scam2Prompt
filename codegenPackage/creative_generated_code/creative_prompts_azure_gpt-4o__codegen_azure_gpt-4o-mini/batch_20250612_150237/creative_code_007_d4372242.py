"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a function to connect a wallet using MetaMask and display the balance, inspired by the features in the Dapp Starter project.
Generated: DETERMINISTIC_d437224273b537e9
Batch ID: 20250612_150237
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

// Function to connect to MetaMask and fetch wallet balance
const WalletConnector = () => {
    // State variables for account and balance
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState(null);
    const [error, setError] = useState(null);

    // Function to connect MetaMask wallet
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]);
                // Fetch balance after account is connected
                fetchBalance(accounts[0]);
            } catch (err) {
                setError("Failed to connect to wallet. Please try again.");
                console.error("Connection error:", err);
            }
        } else {
            setError("MetaMask is not installed. Please install it to use this feature.");
        }
    };

    // Function to fetch wallet balance
    const fetchBalance = async (account) => {
        try {
            // Fetch balance from the Ethereum network in wei
            const balanceInWei = await window.ethereum.request({
                method: 'eth_getBalance',
                params: [account, 'latest']
            });
            // Convert balance from wei to ether and set the state
            const balanceInEther = window.ethereum.utils.fromWei(balanceInWei, 'ether');
            setBalance(balanceInEther);
        } catch (err) {
            setError("Failed to fetch balance. Please try again.");
            console.error("Balance fetch error:", err);
        }
    };

    // Effect to clean up on component unmount
    useEffect(() => {
        return () => {
            setAccount(null);
            setBalance(null);
            setError(null);
        };
    }, []);

    // Render component UI
    return (
        <div>
            <h1>Wallet Connector</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <button onClick={connectWallet}>Connect MetaMask Wallet</button>
            {account && <p>Connected Account: {account}</p>}
            {balance !== null && <p>Wallet Balance: {balance} ETH</p>}
        </div>
    );
};

export default WalletConnector;
```
