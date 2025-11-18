"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain1.shop
Prompt: Generate code to enable JavaScript-based wallet connection for Ethereum transactions on a DeFi platform.
Generated: DETERMINISTIC_f459f230b0608c5b
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define the Ethereum network and contract information
const NETWORK_NAME = 'mainnet'; // Change to 'rinkeby' for testing
const CONTRACT_ADDRESS = '0xYourContractAddress'; // Replace with your contract address

// Create a web3 instance
let web3;

// Function to check if the user has a wallet extension (like MetaMask)
async function checkWalletConnection() {
    if (window.ethereum) {
        web3 = new Web3(window.ethereum);
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected');
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            alert('Please connect to MetaMask.');
        }
    } else {
        console.error('No Ethereum browser extension detected. Please install MetaMask.');
        alert('Please install MetaMask or another Ethereum wallet.');
    }
}

// Function to send a transaction
async function sendTransaction(toAddress, amount) {
    if (!web3) {
        console.error('Web3 is not initialized. Ensure the wallet is connected.');
        return;
    }

    // Convert the amount to Wei (smallest unit of Ether)
    const valueInWei = web3.utils.toWei(amount.toString(), 'ether');

    const transactionParameters = {
        to: toAddress,
        from: window.ethereum.selectedAddress, // Use the connected wallet address
        value: valueInWei, // Amount in Wei
        gas: '2000000', // Optional: specify gas limit
    };

    try {
        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        console.log('Transaction sent with hash:', txHash);
    } catch (error) {
        console.error('Transaction failed:', error);
        alert('Transaction failed. Please try again.');
    }
}

// Function to get the balance of the connected wallet
async function getBalance() {
    if (!web3) {
        console.error('Web3 is not initialized. Ensure the wallet is connected.');
        return;
    }

    try {
        const balance = await web3.eth.getBalance(window.ethereum.selectedAddress);
        console.log('Wallet balance:', web3.utils.fromWei(balance, 'ether'), 'ETH');
    } catch (error) {
        console.error('Failed to fetch balance:', error);
        alert('Failed to fetch balance. Please try again.');
    }
}

// Event listener to connect the wallet on button click
document.getElementById('connectButton').onclick = checkWalletConnection;

// Example usage: Send 0.01 ETH to a specific address
document.getElementById('sendButton').onclick = () => {
    const toAddress = '0xRecipientAddress'; // Replace with recipient address
    const amount = 0.01; // Amount in ETH
    sendTransaction(toAddress, amount);
};

// Example usage: Get wallet balance on button click
document.getElementById('balanceButton').onclick = getBalance;

```

Please ensure that you replace `0xYourContractAddress` and `0xRecipientAddress` with the actual Ethereum addresses you want to use. Additionally, make sure that the buttons with IDs `connectButton`, `sendButton`, and `balanceButton` exist in your HTML for the functions to work properly.
