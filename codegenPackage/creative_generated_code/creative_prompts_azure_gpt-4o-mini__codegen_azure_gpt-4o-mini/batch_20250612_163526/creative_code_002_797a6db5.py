"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Explain how to manage account balances in a DApp with Web3 React and MetaMask integration.
Generated: DETERMINISTIC_797a6db5c631638a
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React and Web3
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Ensure that the DApp can only operate if the user has MetaMask installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this DApp');
}

const App = () => {
    const [account, setAccount] = useState('');
    const [balance, setBalance] = useState('0');
    const [web3, setWeb3] = useState(null);

    // Initialize Web3 and load user account on component mount
    useEffect(() => {
        const initializeWeb3 = async () => {
            try {
                // Request account access from MetaMask
                await window.ethereum.request({ method: 'eth_requestAccounts' });

                // Create a Web3 instance
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);

                // Get the user's account
                const accounts = await web3Instance.eth.getAccounts();
                setAccount(accounts[0]);

                // Load the account balance
                await loadAccountBalance(web3Instance, accounts[0]);
            } catch (error) {
                console.error('Error initializing Web3:', error);
                alert('Failed to load Web3 or accounts. Check console for details.');
            }
        };

        initializeWeb3();
    }, []);

    // Function to load the account balance
    const loadAccountBalance = async (web3Instance, account) => {
        try {
            const balanceWei = await web3Instance.eth.getBalance(account);
            const balanceEth = web3Instance.utils.fromWei(balanceWei, 'ether');
            setBalance(balanceEth);
        } catch (error) {
            console.error('Error loading balance:', error);
            alert('Failed to load account balance. Check console for details.');
        }
    };

    return (
        <div>
            <h1>Account Balance DApp</h1>
            {account ? (
                <div>
                    <h2>Account: {account}</h2>
                    <h3>Balance: {balance} ETH</h3>
                </div>
            ) : (
                <h2>Please connect your MetaMask wallet.</h2>
            )}
        </div>
    );
};

export default App;
```

This code is a complete React component that handles the management of account balances in a decentralized application (DApp) using Web3.js and MetaMask. It includes error handling, proper initialization, and ensures a user-friendly experience.
