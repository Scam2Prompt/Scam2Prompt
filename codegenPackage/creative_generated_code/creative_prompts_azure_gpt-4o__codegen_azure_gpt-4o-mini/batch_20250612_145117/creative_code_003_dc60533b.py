"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuu.finance
Prompt: Provide code for detecting and handling wallet connection events in a React-based DeFi app, mimicking the "Connect Wallet" feature on kuu.finance.
Generated: DETERMINISTIC_dc60533bc3def017
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
import { ethers } from 'ethers';

// Define the ConnectWallet component
const ConnectWallet = () => {
    // Define state variables for wallet address and connection status
    const [walletAddress, setWalletAddress] = useState(null);
    const [isConnected, setIsConnected] = useState(false);

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Check if the browser has MetaMask installed
            if (!window.ethereum) {
                alert('MetaMask is required. Please install it to use this feature.');
                return;
            }

            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setWalletAddress(accounts[0]); // Set the connected wallet address
            setIsConnected(true); // Update connection status

            // Log connection event
            console.log(`Connected to wallet: ${accounts[0]}`);
        } catch (error) {
            // Handle errors during wallet connection
            console.error('Error connecting to wallet:', error);
            alert('Failed to connect to wallet. Please try again.');
        }
    };

    // Function to handle wallet disconnection
    const disconnectWallet = () => {
        setWalletAddress(null); // Clear wallet address
        setIsConnected(false); // Update connection status
        console.log('Wallet disconnected');
    };

    // Effect to handle wallet connection events
    useEffect(() => {
        // Check if wallet is already connected
        const checkIfWalletIsConnected = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setWalletAddress(accounts[0]);
                    setIsConnected(true);
                }
            }
        };

        // Listen for wallet account changes
        const handleAccountsChanged = (accounts) => {
            if (accounts.length > 0) {
                setWalletAddress(accounts[0]);
            } else {
                disconnectWallet();
            }
        };

        // Check wallet connection on component mount
        checkIfWalletIsConnected();

        // Event listener for account changes
        window.ethereum.on('accountsChanged', handleAccountsChanged);

        // Cleanup event listener on component unmount
        return () => {
            window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        };
    }, []);

    return (
        <div>
            {/* Display connection status and wallet address */}
            {isConnected ? (
                <div>
                    <p>Connected as: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the ConnectWallet component
export default ConnectWallet;
```
