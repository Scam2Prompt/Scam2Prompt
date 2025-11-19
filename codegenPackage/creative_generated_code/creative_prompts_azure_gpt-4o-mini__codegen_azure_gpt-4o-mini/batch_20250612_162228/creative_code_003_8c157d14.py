"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-apedvip.pages.dev
Prompt: Write a code snippet to connect a wallet for participating in a cryptocurrency presale like APED.
Generated: DETERMINISTIC_8c157d14ed6968ad
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // For interacting with the Ethereum blockchain
import { ethers } from 'ethers'; // Ethers.js for wallet connection and transaction handling

// Define constants for the presale contract
const PRESALE_CONTRACT_ADDRESS = '0xYourPresaleContractAddress';
const PRESALE_ABI = [ /* ABI array here */ ];

// Initialize Web3 or Ethers provider
let web3;
let provider;

// Function to connect wallet
async function connectWallet() {
    try {
        // Check if the browser has an Ethereum provider (like MetaMask)
        if (window.ethereum) {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Initialize Web3 with the injected provider
            web3 = new Web3(window.ethereum);
            console.log('Wallet connected successfully');
        } else {
            console.error('No Ethereum provider found. Please install MetaMask.');
        }
    } catch (error) {
        console.error('Failed to connect wallet:', error);
    }
}

// Function to participate in the presale
async function participateInPresale(amount) {
    try {
        // Check if the wallet is connected
        if (!web3) {
            throw new Error('Wallet not connected. Please connect your wallet first.');
        }

        // Create a contract instance
        const presaleContract = new web3.eth.Contract(PRESALE_ABI, PRESALE_CONTRACT_ADDRESS);

        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Convert amount to Wei (smallest unit of Ether)
        const weiAmount = web3.utils.toWei(amount.toString(), 'ether');

        // Call the presale contract's participate function
        const tx = await presaleContract.methods.participate().send({
            from: userAddress,
            value: weiAmount,
        });

        console.log('Participation successful:', tx);
    } catch (error) {
        console.error('Failed to participate in presale:', error);
    }
}

// Example usage
document.getElementById('connectWalletButton').onclick = connectWallet;
document.getElementById('participateButton').onclick = () => {
    const amount = document.getElementById('amountInput').value;
    participateInPresale(amount);
};
```
