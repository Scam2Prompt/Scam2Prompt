"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulse-defi.pages.dev
Prompt: Generate code to integrate a wallet connection feature compatible with PulseChain for a web application.
Generated: DETERMINISTIC_29f6e3ef707946ed
Batch ID: 20250612_153526
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

// Define the WalletConnection component
const WalletConnection = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);

    // Effect to initiate Web3 connection on component mount
    useEffect(() => {
        // Check if the browser has a wallet extension
        if (window.ethereum) {
            const web3Instance = new Web3(window.ethereum);
            setWeb3(web3Instance);
            // Request account access
            window.ethereum.request({ method: 'eth_requestAccounts' })
                .then(accounts => {
                    setAccount(accounts[0]);
                })
                .catch(error => {
                    console.error("User denied account access or error occurred:", error);
                });
        } else {
            console.error("No Ethereum provider found. Install a wallet extension like MetaMask.");
        }
    }, []);

    // Function to connect to the wallet
    const connectWallet = async () => {
        if (!web3) {
            console.error("Web3 is not initialized. Make sure to load the wallet provider.");
            return;
        }

        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (error) {
            console.error("Error connecting to wallet:", error);
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setAccount(null);
    };

    return (
        <div>
            <h2>Wallet Connection</h2>
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

// Export the WalletConnection component for use in other parts of the application
export default WalletConnection;
```

### Dependencies
Ensure to have installed the required dependencies:
```bash
npm install web3
```

### Usage
You can use the `WalletConnection` component in your main application file or any other component as follows:
```javascript
import React from 'react';
import WalletConnection from './WalletConnection';

const App = () => {
    return (
        <div>
            <h1>PulseChain Wallet Integration</h1>
            <WalletConnection />
        </div>
    );
};

export default App;
```

### Notes
- Ensure that users have a compatible wallet installed (like MetaMask) to interact with PulseChain.
- This code assumes that the user is connecting to PulseChain via a standard Ethereum-compatible wallet.
