"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Write code to integrate a wallet connection feature for Masa's blockchain-based rewards system using Web3.js or ethers.js.
Generated: DETERMINISTIC_c534bdfc8df4b4aa
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers"; // Using ethers.js for wallet connection
import React, { useState, useEffect } from "react";

// Define the WalletConnector component
const WalletConnector = () => {
    // State variables to manage wallet connection status and user address
    const [provider, setProvider] = useState(null);
    const [walletAddress, setWalletAddress] = useState(null);
    const [error, setError] = useState(null);

    // Function to connect to the user's wallet
    const connectWallet = async () => {
        try {
            // Check if the window object has a provider
            if (window.ethereum) {
                // Create a new provider from window.ethereum
                const provider = new ethers.providers.Web3Provider(window.ethereum);
                // Request account access if needed
                await provider.send("eth_requestAccounts", []);
                // Get the signer (the user's wallet)
                const signer = provider.getSigner();
                // Get the user's address
                const address = await signer.getAddress();
                
                // Update state with the provider and wallet address
                setProvider(provider);
                setWalletAddress(address);
            } else {
                // Set error if the user does not have an Ethereum wallet
                setError("Please install MetaMask or another Ethereum wallet.");
            }
        } catch (err) {
            // Handle errors during wallet connection
            setError("Failed to connect wallet: " + err.message);
        }
    };

    // Function to disconnect the wallet (optional)
    const disconnectWallet = () => {
        setProvider(null);
        setWalletAddress(null);
        setError(null);
    };

    // Render the wallet connection component
    return (
        <div>
            <h2>Masa Blockchain Wallet Connection</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {walletAddress ? (
                <div>
                    <p>Connected as: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the WalletConnector component for use in other parts of the application
export default WalletConnector;
```

### Dependencies
To run this code, make sure you have the following dependencies installed:
```bash
npm install ethers react
```

### Usage
You can import and use the `WalletConnector` component in your main application file (e.g., `App.js`) as follows:
```javascript
import React from 'react';
import WalletConnector from './WalletConnector';

const App = () => {
    return (
        <div>
            <WalletConnector />
        </div>
    );
};

export default App;
```
