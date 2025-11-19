"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Write a code snippet to connect an Ethereum-compatible wallet like MetaMask for purchasing BTCMTX tokens on the Bitcoin Minetrix platform.
Generated: DETERMINISTIC_75b535bfee9dfd34
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define constants
const BTCMTX_TOKEN_ADDRESS = '0xYourTokenAddressHere'; // Replace with actual BTCMTX token address
const TOKEN_ABI = [ /* ABI of the BTCMTX token contract */ ];

let web3;
let currentAccount;

// Function to connect to the Ethereum wallet
async function connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            // Request wallet connection
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            currentAccount = accounts[0];
            console.log('Wallet connected:', currentAccount);
            web3 = new Web3(window.ethereum);
            return currentAccount;
        } catch (error) {
            console.error("Wallet connection error:", error);
            alert("Failed to connect wallet. Please try again.");
        }
    } else {
        alert('Please install MetaMask!');
    }
}

// Function to purchase BTCMTX tokens
async function purchaseTokens(amount) {
    if (!currentAccount || !web3) {
        alert('Please connect your wallet first.');
        return;
    }

    const tokenContract = new web3.eth.Contract(TOKEN_ABI, BTCMTX_TOKEN_ADDRESS);

    try {
        // Assuming the purchase function is called 'buyTokens' in the contract
        const tx = await tokenContract.methods.buyTokens(amount).send({ from: currentAccount });
        console.log('Transaction successful:', tx);
    } catch (error) {
        console.error("Token purchase error:", error);
        alert('Token purchase failed. Please check console for details.');
    }
}

// Example usage
document.getElementById('connectButton').addEventListener('click', async () => {
    await connectWallet();
});

document.getElementById('purchaseButton').addEventListener('click', async () => {
    const amount = document.getElementById('tokenAmount').value; // Get token amount from input
    await purchaseTokens(amount);
});
```

Make sure to replace the placeholder values such as `BTCMTX_TOKEN_ADDRESS` and `TOKEN_ABI` with the actual token address and ABI required to interact with the BTCMTX token contract. Additionally, ensure that DOM elements with IDs `connectButton`, `purchaseButton`, and `tokenAmount` exist in your HTML for the code to function correctly.
