"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blumft.github.io
Prompt: Explain how to integrate MetaMask for wallet privacy in a project utilizing the Blur NFT technology.
Generated: DETERMINISTIC_8e4ea4eee30a49a7
Batch ID: 20250612_155705
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
import { Blur } from 'blur-sdk';

// Ensure MetaMask is available
if (typeof window.ethereum === 'undefined') {
    alert('MetaMask is not installed. Please install it to use this feature.');
}

// Initialize Web3 and Blur SDK
const web3 = new Web3(window.ethereum);
const blur = new Blur({ apiKey: 'YOUR_BLUR_API_KEY' });

const WalletIntegration = () => {
    const [account, setAccount] = useState(null);
    const [error, setError] = useState('');

    // Request account access and set the user's account
    const connectWallet = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (err) {
            setError('Failed to connect wallet. Please try again.');
            console.error(err);
        }
    };

    // Fetch user's NFTs using Blur SDK
    const fetchNFTs = async () => {
        try {
            if (!account) throw new Error('Wallet not connected');

            const nfts = await blur.getNFTs(account);
            console.log('User NFTs:', nfts);
        } catch (err) {
            setError('Failed to fetch NFTs. Please check your connection.');
            console.error(err);
        }
    };

    // Handle account change
    useEffect(() => {
        const handleAccountsChanged = (accounts) => {
            if (accounts.length === 0) {
                alert('Please connect to MetaMask.');
            } else {
                setAccount(accounts[0]);
            }
        };

        // Listen for account changes in MetaMask
        window.ethereum.on('accountsChanged', handleAccountsChanged);

        // Cleanup listener on component unmount
        return () => {
            window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        };
    }, []);

    return (
        <div>
            <h1>MetaMask Wallet Integration</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={fetchNFTs}>Fetch NFTs</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletIntegration;

// Ensure to include error handling for each async operation
// and provide user-friendly messages for better UX.
```

Make sure to replace `'YOUR_BLUR_API_KEY'` with your actual Blur API key before running the code.
