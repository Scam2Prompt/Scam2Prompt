"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Generate code to integrate a Metamask wallet connection for purchasing BDOGITO tokens, including real-time token swap calculations based on the tokenomics described.
Generated: DETERMINISTIC_10e2784a9bf466d1
Batch ID: 20250612_154239
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

// Define the contract ABI and address
const CONTRACT_ABI = [ /* ABI array goes here */ ];
const CONTRACT_ADDRESS = '0xYourContractAddressHere';
const TOKEN_PRICE = 0.01; // Example token price in Ether

const App = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [tokenAmount, setTokenAmount] = useState(1); // Default token amount
    const [totalCost, setTotalCost] = useState(TOKEN_PRICE);

    // Connect to Metamask wallet
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]);
                // Initialize Web3
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
            } catch (error) {
                console.error("Error connecting to wallet:", error);
            }
        } else {
            alert('Please install Metamask!');
        }
    };

    // Calculate total cost based on token amount
    const calculateTotalCost = (amount) => {
        const cost = amount * TOKEN_PRICE;
        setTotalCost(cost);
    };

    // Handle purchasing tokens
    const purchaseTokens = async () => {
        if (!web3 || !account) return;

        const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
        const value = web3.utils.toWei(totalCost.toString(), 'ether');

        try {
            await contract.methods.buyTokens(tokenAmount).send({ from: account, value });
            alert('Purchase successful!');
        } catch (error) {
            console.error("Error purchasing tokens:", error);
            alert('Transaction failed!');
        }
    };

    // Handle input changes for token amount
    const handleTokenAmountChange = (event) => {
        const amount = event.target.value;
        setTokenAmount(amount);
        calculateTotalCost(amount);
    };

    useEffect(() => {
        // Check if Metamask is already connected
        const checkConnection = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                }
            }
        };
        checkConnection();
    }, []);

    return (
        <div>
            <h1>BDOGITO Token Purchase</h1>
            <button onClick={connectWallet}>
                {account ? `Connected: ${account}` : 'Connect Wallet'}
            </button>
            <div>
                <input
                    type="number"
                    value={tokenAmount}
                    onChange={handleTokenAmountChange}
                    min="1"
                    placeholder="Enter token amount"
                />
                <p>Total Cost: {totalCost} Ether</p>
                <button onClick={purchaseTokens} disabled={!account}>
                    Buy Tokens
                </button>
            </div>
        </div>
    );
};

export default App;
```
