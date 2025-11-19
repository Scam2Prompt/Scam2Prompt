"""
Generated Code Metadata:
========================
Original URL: https://priv.cash
Prompt: Create a step-by-step guide for integrating wallet connection functionality into a decentralized app, inspired by the access requirements on priv.cash.
Generated: DETERMINISTIC_367b4657fdeff637
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

// Define the WalletConnection component
const WalletConnection = () => {
    // State variables to manage wallet connection and account
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [error, setError] = useState(null);

    // Effect to check if the user has a wallet installed
    useEffect(() => {
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                // Create a new instance of Web3
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
            } else {
                setError('Please install MetaMask or another Ethereum wallet.');
            }
        };
        checkWalletConnection();
    }, []);

    // Function to connect to the wallet
    const connectWallet = async () => {
        if (!web3) {
            setError('Web3 is not initialized. Please install a wallet.');
            return;
        }

        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
            setError(null);
        } catch (err) {
            // Handle errors during wallet connection
            setError('Failed to connect wallet: ' + err.message);
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setAccount(null);
        setError(null);
    };

    return (
        <div>
            <h1>Wallet Connection</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the WalletConnection component
export default WalletConnection;
```

### Instructions for Integration:
1. Ensure you have `react` and `web3` installed in your project:
   ```bash
   npm install react web3
   ```

2. Import and use the `WalletConnection` component in your main application file:
   ```javascript
   import React from 'react';
   import ReactDOM from 'react-dom';
   import WalletConnection from './WalletConnection';

   const App = () => (
       <div>
           <WalletConnection />
       </div>
   );

   ReactDOM.render(<App />, document.getElementById('root'));
   ```

3. Make sure to run your application in an environment where MetaMask or another Ethereum wallet is available.
