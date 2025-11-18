"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapptoolkit.com
Prompt: Provide a code example for building a wallet login system using WalletConnect's Web3Modal SDK, supporting browser extensions and mobile wallets.
Generated: DETERMINISTIC_aae1ea5350a90c66
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and packages
import React, { useState, useEffect } from 'react';
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

// Define a functional component for the Wallet Login System
const WalletLogin = () => {
    const [provider, setProvider] = useState(null);
    const [signer, setSigner] = useState(null);
    const [account, setAccount] = useState(null);
    
    // Configure the Web3Modal instance
    const web3Modal = new Web3Modal({
        cacheProvider: true, // optional
        providerOptions: {}, // Add any wallet providers here
    });

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Open the wallet selection modal
            const instance = await web3Modal.connect();
            const newProvider = new ethers.providers.Web3Provider(instance);
            const newSigner = newProvider.getSigner();
            
            setProvider(newProvider);
            setSigner(newSigner);

            // Retrieve the user's account address
            const userAccount = await newSigner.getAddress();
            setAccount(userAccount);
        } catch (error) {
            console.error("Failed to connect wallet:", error);
            alert("Failed to connect wallet. Please try again.");
        }
    };

    // Function to disconnect from the wallet
    const disconnectWallet = async () => {
        try {
            await web3Modal.clearCachedProvider();
            setProvider(null);
            setSigner(null);
            setAccount(null);
        } catch (error) {
            console.error("Failed to disconnect wallet:", error);
        }
    };

    // Effect to check if a provider is already cached
    useEffect(() => {
        const checkCachedProvider = async () => {
            const cachedProvider = await web3Modal.cachedProvider;
            if (cachedProvider) {
                connectWallet(); // Automatically connect if cached
            }
        };
        checkCachedProvider();
    }, []);

    return (
        <div>
            <h1>Wallet Login System</h1>
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

export default WalletLogin;
```

### Instructions for Usage:
1. Install the required packages:
   ```bash
   npm install web3modal ethers
   ```
2. Import and use the `WalletLogin` component in your application where you want the wallet login functionality.
3. Ensure your application is set up to work with Ethereum and has the necessary configurations for wallet providers if needed.
