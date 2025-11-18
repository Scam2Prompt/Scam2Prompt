"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-blockchain-eight.vercel.app
Prompt: Generate a React.js component for connecting a cryptocurrency wallet, similar to the "Connect Wallet" functionality on the Opeasea Clone website.
Generated: DETERMINISTIC_e9b4edd510cd970c
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';

// Import appropriate libraries for wallet connection
import { ethers } from 'ethers';

const ConnectWallet = () => {
    // State to hold the current account and connection status
    const [account, setAccount] = useState(null);
    const [isConnected, setIsConnected] = useState(false);
    const [error, setError] = useState(null);

    // Function to connect to wallet
    const connectWallet = async () => {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                const provider = new ethers.providers.Web3Provider(window.ethereum);
                // Request account access
                await provider.send("eth_requestAccounts", []);
                const signer = provider.getSigner();
                const address = await signer.getAddress();
                
                // Update state with the connected account
                setAccount(address);
                setIsConnected(true);
            } else {
                setError('MetaMask is not installed. Please install it to use this feature.');
            }
        } catch (err) {
            setError('Connection failed. Please try again.');
            console.error(err); // Log the error for debugging
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setAccount(null);
        setIsConnected(false);
    };

    // Effect to handle wallet connection state changes
    useEffect(() => {
        const checkIfWalletIsConnected = async () => {
            if (window.ethereum) {
                const provider = new ethers.providers.Web3Provider(window.ethereum);
                const accounts = await provider.listAccounts();
                if (accounts.length) {
                    setAccount(accounts[0]);
                    setIsConnected(true);
                }
            }
        };
        checkIfWalletIsConnected();
    }, []);
    
    return (
        <div>
            {error && <div className="error">{error}</div>} {/* Display error if any */}
            {isConnected ? (
                <div>
                    <p>Connected as: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default ConnectWallet;
```

**Note:** Ensure you have the `ethers.js` library installed in your project for this code to work. You can install it using npm:

```bash
npm install ethers
```
