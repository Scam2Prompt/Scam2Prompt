"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mapledefi.finance
Prompt: Create a step-by-step guide for integrating wallet connection into a decentralized finance app using the Maple DeFi Finance approach.
Generated: DETERMINISTIC_e23f5bbdbc42421c
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
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Define the WalletConnect component
const WalletConnect = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
  
    // Check if the user has a wallet and connect
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access from the user
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
                setAccount(accounts[0]);
                toast.success('Wallet connected successfully!');
            } catch (error) {
                // Handle errors gracefully
                toast.error('Could not connect to wallet. Please try again.');
                console.error("Wallet connection error: ", error);
            }
        } else {
            // Prompt user to install Metamask
            toast.warn('Please install MetaMask to use this feature.');
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setAccount(null);
        setWeb3(null);
        toast.info('Wallet disconnected.');
    };

    // Hook to handle wallet connection on component mount
    useEffect(() => {
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                    const web3Instance = new Web3(window.ethereum);
                    setWeb3(web3Instance);
                    toast.info('Wallet already connected.');
                }
            }
        };

        checkWalletConnection();
    }, []);

    return (
        <div>
            <h1>Wallet Connection</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
            <ToastContainer />
        </div>
    );
};

// Export the WalletConnect component
export default WalletConnect;
```
