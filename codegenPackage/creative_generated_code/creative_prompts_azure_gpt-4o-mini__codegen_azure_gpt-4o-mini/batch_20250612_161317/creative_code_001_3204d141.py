"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Write code to integrate wallet connection functionality in a web3 app using Metamask.
Generated: DETERMINISTIC_3204d141b9a56001
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletConnector.js

// Check if the user has MetaMask installed
const isMetaMaskInstalled = () => {
    return Boolean(window.ethereum && window.ethereum.isMetaMask);
};

/**
 * Connects to the user's wallet using MetaMask.
 * @returns {Promise<string|null>} The connected wallet address or null if the connection fails.
 */
const connectWallet = async () => {
    if (!isMetaMaskInstalled()) {
        alert("MetaMask not found. Please install MetaMask to use this feature.");
        return null;
    }

    try {
        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected accounts:', accounts);
        return accounts[0]; // Return the first connected account
    } catch (error) {
        console.error('Failed to connect wallet:', error);
        alert("Failed to connect wallet. Please try again.");
        return null;
    }
};

/**
 * Sets up event listeners for MetaMask account and network changes.
 * @param {Function} onAccountChange - Callback function to handle account changes.
 * @param {Function} onNetworkChange - Callback function to handle network changes.
 */
const setupWalletListener = (onAccountChange, onNetworkChange) => {
    if (isMetaMaskInstalled()) {
        // Listen for account changes
        window.ethereum.on('accountsChanged', (accounts) => {
            console.log('Accounts changed:', accounts);
            onAccountChange(accounts);
        });

        // Listen for network changes
        window.ethereum.on('chainChanged', (chainId) => {
            console.log('Network changed:', chainId);
            onNetworkChange(chainId);
        });
    }
};

// Exporting functions for use in other modules
export { connectWallet, setupWalletListener, isMetaMaskInstalled };
```

```javascript
// app.js

import { connectWallet, setupWalletListener } from './walletConnector.js';

// Initialize the application
const initApp = async () => {
    // Attempt to connect the wallet
    const walletAddress = await connectWallet();

    if (walletAddress) {
        console.log('Connected wallet address:', walletAddress);
        // Additional logic after successful connection can be added here
    }
};

// Handle account change
const handleAccountChange = (accounts) => {
    if (accounts.length === 0) {
        console.log('Please connect to MetaMask.');
    } else {
        console.log('Connected account:', accounts[0]);
    }
};

// Handle network change
const handleNetworkChange = (chainId) => {
    console.log('Switched to network with chain ID:', chainId);
    // Additional logic to handle network changes can be added here
};

// Set up event listeners and initialize the app
setupWalletListener(handleAccountChange, handleNetworkChange);
initApp();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web3 Wallet Connection</title>
    <script type="module" src="app.js" defer></script>
</head>
<body>
    <h1>Web3 Wallet Connection with MetaMask</h1>
    <p>Check the console for wallet connection status.</p>
</body>
</html>
```
