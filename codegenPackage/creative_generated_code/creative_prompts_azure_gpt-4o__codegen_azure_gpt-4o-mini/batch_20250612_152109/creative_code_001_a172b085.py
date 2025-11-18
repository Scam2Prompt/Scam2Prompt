"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://papeairdropclaim.pages.dev
Prompt: Generate code to integrate a wallet connection feature into a cryptocurrency presale dashboard, allowing users to connect their Metamask or Coinbase Wallet to swap ETH for $PAPE tokens.
Generated: DETERMINISTIC_a172b085782c73ee
Batch ID: 20250612_152109
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
import { ethers } from 'ethers';

// Define constants for the token and presale contract addresses
const TOKEN_ADDRESS = '0xYourTokenAddressHere';
const PRESALE_ADDRESS = '0xYourPresaleContractAddressHere';
const ETH_TO_PAPE_RATIO = 100; // Example ratio for ETH to PAPE token swap

const PresaleDashboard = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [amount, setAmount] = useState(0);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Check if MetaMask is installed
        if (window.ethereum) {
            const web3Instance = new Web3(window.ethereum);
            setWeb3(web3Instance);
        } else {
            setError('Please install MetaMask to use this feature');
        }
    }, []);

    // Function to connect to MetaMask or Coinbase Wallet
    const connectWallet = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (err) {
            setError('Failed to connect wallet: ' + err.message);
        }
    };

    // Function to handle ETH to $PAPE token swap
    const swapTokens = async () => {
        if (!web3 || !account) {
            setError('Please connect your wallet first');
            return;
        }

        try {
            const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
            const contract = new web3.eth.Contract(PRESALE_ABI, PRESALE_ADDRESS);

            // Approve and make the transaction
            const tx = await contract.methods.swapETHForTokens().send({
                from: account,
                value: amountInWei,
            });

            console.log('Transaction successful:', tx);
        } catch (err) {
            setError('Transaction failed: ' + err.message);
        }
    };

    return (
        <div>
            <h1>Presale Dashboard</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <button onClick={connectWallet}>
                {account ? `Connected: ${account}` : 'Connect Wallet'}
            </button>
            <div>
                <input
                    type="number"
                    placeholder="Amount in ETH"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                />
                <button onClick={swapTokens}>Swap ETH for $PAPE</button>
            </div>
        </div>
    );
};

// Define the ABI for the presale contract (replace with your actual ABI)
const PRESALE_ABI = [
    // Add your contract's ABI here
];

export default PresaleDashboard;
```

**Note:** Ensure to replace `TOKEN_ADDRESS`, `PRESALE_ADDRESS`, and `PRESALE_ABI` with the actual contract address and ABI for your $PAPE token and presale contract. This code assumes the presence of the Web3 and ethers libraries in your project.
