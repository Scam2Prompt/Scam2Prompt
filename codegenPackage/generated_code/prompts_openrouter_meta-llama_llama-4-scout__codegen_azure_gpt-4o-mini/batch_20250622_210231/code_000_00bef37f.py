"""
Generated Code Metadata:
========================
Original URL: https://tayyipreis.pages.dev
Prompt: Write a JavaScript code snippet to connect a wallet to the AltLayer Staking Portal and delegate stake to a node operator.
Generated: DETERMINISTIC_00bef37f4a1ed3d3
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define constants for the AltLayer Staking Portal
const STAKING_PORTAL_ADDRESS = '0xYourStakingPortalAddress'; // Replace with actual address
const NODE_OPERATOR_ADDRESS = '0xYourNodeOperatorAddress'; // Replace with actual address
const ABI = [ /* ABI of the Staking Portal contract */ ]; // Replace with actual ABI

// Initialize Web3 and provider
let web3;
let provider;

// Function to connect wallet
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            provider = new ethers.providers.Web3Provider(window.ethereum);
            web3 = new Web3(window.ethereum);
            console.log('Wallet connected successfully');
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('Wallet connection failed');
        }
    } else {
        console.error('No Ethereum provider found. Please install MetaMask.');
        throw new Error('Ethereum provider not found');
    }
}

// Function to delegate stake to a node operator
async function delegateStake(amount) {
    if (!web3) {
        console.error('Wallet not connected. Please connect your wallet first.');
        throw new Error('Wallet not connected');
    }

    const stakingPortalContract = new web3.eth.Contract(ABI, STAKING_PORTAL_ADDRESS);
    const accounts = await web3.eth.getAccounts();
    const userAddress = accounts[0];

    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Call the delegate function on the contract
        const tx = await stakingPortalContract.methods.delegateStake(NODE_OPERATOR_ADDRESS, amountInWei).send({ from: userAddress });
        console.log('Stake delegated successfully:', tx);
    } catch (error) {
        console.error('Error delegating stake:', error);
        throw new Error('Stake delegation failed');
    }
}

// Example usage
(async () => {
    try {
        await connectWallet();
        await delegateStake(1); // Replace with the desired amount to stake
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
