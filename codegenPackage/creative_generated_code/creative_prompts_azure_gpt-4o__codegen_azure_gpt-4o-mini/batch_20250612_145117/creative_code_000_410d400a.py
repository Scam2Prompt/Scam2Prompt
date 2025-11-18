"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galatea.cash
Prompt: Write code to integrate a cryptocurrency wallet connection feature for a decentralized app (dApp) similar to the one described on https://galatea.cash.
Generated: DETERMINISTIC_410d400a9588f63d
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define the App component
const App = () => {
    // State variables to manage wallet connection and account information
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [error, setError] = useState(null);

    // Function to connect the wallet
    const connectWallet = async () => {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                // Create a Web3 instance
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);

                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]); // Set the first account as the active account

                // Subscribe to account changes
                window.ethereum.on('accountsChanged', handleAccountsChanged);

                // Subscribe to network changes
                window.ethereum.on('chainChanged', handleChainChanged);
            } else {
                // Throw an error if MetaMask is not installed
                throw new Error('MetaMask is not installed. Please install it to use this dApp.');
            }
        } catch (err) {
            // Set error state
            setError(err.message);
            console.error('Wallet connection error:', err);
        }
    };

    // Handle account changes
    const handleAccountsChanged = (accounts) => {
        if (accounts.length > 0) {
            setAccount(accounts[0]);
        } else {
            setAccount(null);
        }
    };

    // Handle network changes
    const handleChainChanged = (chainId) => {
        window.location.reload();
    };

    // Effect to clean up event listeners on component unmount
    useEffect(() => {
        return () => {
            window.ethereum?.removeListener('accountsChanged', handleAccountsChanged);
            window.ethereum?.removeListener('chainChanged', handleChainChanged);
        };
    }, []);

    return (
        <div>
            <h1>Connect Your Wallet</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <p>Connected account: {account}</p>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default App;
```

Please ensure to install the `web3` library if it's not already installed in your project:

```bash
npm install web3
```
