"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Show how to set up Web3Modal with custom themes and styles in a blockchain application.
Generated: DETERMINISTIC_c07f5d7ef2183423
Batch ID: 20250612_150030
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
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

// Define a functional component
const App = () => {
    // State variables for provider and account
    const [provider, setProvider] = useState(null);
    const [account, setAccount] = useState('');

    // Initialize Web3Modal
    const web3Modal = new Web3Modal({
        // Customize the theme and styles
        theme: {
            background: "#ffffff", // Background color
            main: "#1c1c1c", // Main color (buttons, links)
            secondary: "#0070f3", // Secondary color
            border: "#eaeaea", // Border color
            hover: "#f5f5f5", // Hover color
        },
        cacheProvider: true, // Enable caching of provider
        providerOptions: {} // Additional provider options can be added here
    });

    // Function to connect to a wallet
    const connectWallet = async () => {
        try {
            // Open the modal to connect
            const connection = await web3Modal.connect();
            // Create an ethers provider
            const ethersProvider = new ethers.providers.Web3Provider(connection);
            setProvider(ethersProvider);
            
            // Get the user's account
            const signer = ethersProvider.getSigner();
            const userAccount = await signer.getAddress();
            setAccount(userAccount);
        } catch (error) {
            console.error("Connection error: ", error);
        }
    };

    // Function to disconnect wallet
    const disconnectWallet = async () => {
        try {
            await web3Modal.clearCachedProvider(); // Clear the cache
            setAccount(''); // Reset account state
            setProvider(null); // Reset provider state
        } catch (error) {
            console.error("Disconnection error: ", error);
        }
    };

    // Effect to handle connection status
    useEffect(() => {
        const init = async () => {
            // Check for cached provider
            const cachedProvider = web3Modal.cachedProvider;
            if (cachedProvider) {
                await connectWallet(); // Attempt to connect
            }
        };
        init();
    }, []);

    return (
        <div style={{ padding: "20px", textAlign: "center" }}>
            <h1>Web3Modal Example</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the component as default
export default App;
```
