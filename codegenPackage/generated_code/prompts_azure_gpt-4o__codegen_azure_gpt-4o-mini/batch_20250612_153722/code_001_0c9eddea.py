"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Create a decentralized exchange (DEX) interface for trading PENGWU tokens, incorporating features like PENGWUSwap mentioned on the website.
Generated: DETERMINISTIC_0c9eddeab9d52a7e
Batch ID: 20250612_153722
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
import { PENGWU_ABI, PENGWU_ADDRESS } from './constants'; // Import ABI and contract address

// Initialize Web3
const web3 = new Web3(window.ethereum);

// DEX Component
const DEX = () => {
    const [account, setAccount] = useState('');
    const [balance, setBalance] = useState(0);
    const [amount, setAmount] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    // Load account and balance on component mount
    useEffect(() => {
        const loadAccount = async () => {
            try {
                const accounts = await web3.eth.requestAccounts();
                setAccount(accounts[0]);
                await loadBalance(accounts[0]);
            } catch (err) {
                setError('Failed to load account. Please connect your wallet.');
            }
        };
        loadAccount();
    }, []);

    // Load PENGWU token balance
    const loadBalance = async (account) => {
        const contract = new web3.eth.Contract(PENGWU_ABI, PENGWU_ADDRESS);
        const balance = await contract.methods.balanceOf(account).call();
        setBalance(web3.utils.fromWei(balance, 'ether'));
    };

    // Handle token swap
    const handleSwap = async () => {
        setLoading(true);
        setError('');
        try {
            const contract = new web3.eth.Contract(PENGWU_ABI, PENGWU_ADDRESS);
            const amountInWei = web3.utils.toWei(amount, 'ether');
            await contract.methods.swap(amountInWei).send({ from: account });
            await loadBalance(account); // Refresh balance after swap
        } catch (err) {
            setError('Swap failed. Please check your input and try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>PENGWU DEX Interface</h1>
            <p>Account: {account}</p>
            <p>Balance: {balance} PENGWU</p>
            <input
                type="text"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="Amount to swap"
            />
            <button onClick={handleSwap} disabled={loading}>
                {loading ? 'Swapping...' : 'Swap PENGWU'}
            </button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default DEX;
```

```javascript
// constants.js
export const PENGWU_ABI = [
    // Add the ABI of the PENGWU token contract here
];

export const PENGWU_ADDRESS = '0xYourTokenContractAddress'; // Replace with the actual contract address
```

```json
// package.json
{
  "name": "pengwu-dex",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "web3": "^1.6.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```
