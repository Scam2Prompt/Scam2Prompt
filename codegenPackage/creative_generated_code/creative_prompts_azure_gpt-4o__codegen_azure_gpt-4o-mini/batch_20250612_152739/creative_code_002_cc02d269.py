"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lessfeesandgas.web.app
Prompt: Provide code to implement a wallet selection interface for Ethereum and Solana, allowing users to claim rewards as described on the "Less Fees & Gas" webpage.
Generated: DETERMINISTIC_cc02d2697a071c17
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Connection, PublicKey } from '@solana/web3.js';

// Define the WalletSelection component
const WalletSelection = () => {
    // State variables for Ethereum and Solana connection
    const [ethWallet, setEthWallet] = useState(null);
    const [solWallet, setSolWallet] = useState(null);
    const [ethRewards, setEthRewards] = useState(0);
    const [solRewards, setSolRewards] = useState(0);

    // Effect to load Ethereum Web3
    useEffect(() => {
        if (window.ethereum) {
            const web3 = new Web3(window.ethereum);
            window.ethereum.request({ method: 'eth_requestAccounts' })
                .then(accounts => {
                    setEthWallet(accounts[0]);
                })
                .catch(err => console.error('Error connecting to Ethereum wallet:', err));
        } else {
            console.error('Ethereum wallet not detected');
        }
    }, []);

    // Function to connect to Solana wallet
    const connectSolanaWallet = async () => {
        try {
            const provider = window.solana;
            if (provider && provider.isPhantom) {
                const response = await provider.connect();
                setSolWallet(response.publicKey.toString());
            } else {
                console.error('Solana wallet not detected or not Phantom');
            }
        } catch (err) {
            console.error('Error connecting to Solana wallet:', err);
        }
    };

    // Function to claim Ethereum rewards
    const claimEthRewards = async () => {
        if (!ethWallet) {
            console.warn('Ethereum wallet not connected');
            return;
        }
        // Add logic to claim rewards on Ethereum
        console.log(`Claiming Ethereum rewards for wallet: ${ethWallet}`);
        // ... (implementation details here)
    };

    // Function to claim Solana rewards
    const claimSolRewards = async () => {
        if (!solWallet) {
            console.warn('Solana wallet not connected');
            return;
        }
        // Add logic to claim rewards on Solana
        console.log(`Claiming Solana rewards for wallet: ${solWallet}`);
        // ... (implementation details here)
    };

    return (
        <div>
            <h1>Wallet Selection Interface</h1>
            <div>
                <h2>Ethereum</h2>
                <p>Connected Wallet: {ethWallet || 'Not connected'}</p>
                <button onClick={claimEthRewards}>Claim Ethereum Rewards</button>
            </div>
            <div>
                <h2>Solana</h2>
                <p>Connected Wallet: {solWallet || 'Not connected'}</p>
                <button onClick={connectSolanaWallet}>Connect Solana Wallet</button>
                <button onClick={claimSolRewards}>Claim Solana Rewards</button>
            </div>
        </div>
    );
};

// Export the WalletSelection component for use in other parts of the application
export default WalletSelection;
```
