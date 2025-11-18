"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerswap.pages.dev
Prompt: Suggest a method for integrating Layerswap's wallet connection feature into a decentralized application (dApp).
Generated: DETERMINISTIC_f734c6e3328009a1
Batch ID: 20250612_150048
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
import { ethers } from 'ethers';

// Define the WalletConnect component
const WalletConnect = () => {
    // State to hold the connected wallet address
    const [walletAddress, setWalletAddress] = useState(null);
    
    // Function to connect to Layerswap wallet
    const connectWallet = async () => {
        try {
            // Check if the browser has an Ethereum provider
            if (window.ethereum) {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Set the first account as the connected wallet address
                setWalletAddress(accounts[0]);
            } else {
                alert('Please install a wallet extension like MetaMask.');
            }
        } catch (error) {
            console.error("Error connecting to wallet: ", error);
            alert('Failed to connect wallet: ' + error.message);
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setWalletAddress(null);
        // Implement any additional disconnection logic if needed
    };

    // Effect to set up event listeners (optional)
    useEffect(() => {
        const handleAccountsChanged = (accounts) => {
            if (accounts.length > 0) {
                setWalletAddress(accounts[0]);
            } else {
                disconnectWallet();
            }
        };

        // Add event listener for account changes
        window.ethereum.on('accountsChanged', handleAccountsChanged);

        // Cleanup function to remove the event listener
        return () => {
            window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        };
    }, []);

    return (
        <div>
            <h2>Wallet Connection</h2>
            {walletAddress ? (
                <div>
                    <p>Connected Wallet: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the WalletConnect component
export default WalletConnect;
```
