"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-dogecoin20.pages.dev
Prompt: Generate code to connect a decentralized wallet (e.g., MetaMask) to the DOGE20 presale widget for purchasing tokens using ETH, BNB, or USDT.
Generated: DETERMINISTIC_e8f25e1c7008e256
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';  // Web3 library for Ethereum interaction
import { ethers } from 'ethers';  // Ethers.js for handling Ethereum transactions

// Constants
const DOGE20_CONTRACT_ADDRESS = '0xYourDoge20ContractAddress'; // Replace with actual DOGE20 contract address
const ABI = [ /* ABI array here */ ]; // Replace with the actual ABI of the DOGE20 contract

// Initialize Web3
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
} else {
    console.error('MetaMask is not installed. Please install it to use this feature.');
    alert('Please install MetaMask to connect your wallet.');
}

// Function to connect to MetaMask
async function connectWallet() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Failed to connect to wallet:', error);
        alert('Failed to connect to wallet. Please check console for details.');
    }
}

// Function to purchase DOGE20 tokens
async function purchaseTokens(amount, currency) {
    const account = await connectWallet();

    if (!account) return; // Exit if wallet connection failed

    // Get contract instance
    const contract = new web3.eth.Contract(ABI, DOGE20_CONTRACT_ADDRESS);

    // Convert amount based on currency
    let transactionValue;
    if (currency === 'ETH' || currency === 'BNB') {
        transactionValue = web3.utils.toWei(amount.toString(), 'ether'); // Convert amount to Wei
    } else if (currency === 'USDT') {
        // For USDT, we need to approve the token transfer before calling the contract function
        const usdtContractAddress = '0xYourUSDTContractAddress'; // Replace with actual USDT contract address
        const usdtContract = new web3.eth.Contract(ABI, usdtContractAddress);
        await usdtContract.methods.approve(DOGE20_CONTRACT_ADDRESS, amount).send({ from: account });
        console.log('USDT approved for transfer.');
        return; // Exit after approval
    } else {
        console.error('Unsupported currency:', currency);
        alert('Unsupported currency. Please select ETH, BNB, or USDT.');
        return;
    }

    // Call the purchase function from the DOGE20 contract
    try {
        await contract.methods.purchaseTokens(amount).send({ from: account, value: transactionValue });
        console.log('Tokens purchased successfully!');
        alert('Tokens purchased successfully!');
    } catch (error) {
        console.error('Error purchasing tokens:', error);
        alert('Error purchasing tokens. Please check console for details.');
    }
}

// Event Listener for Purchase Button
document.getElementById('purchaseButton').addEventListener('click', () => {
    const amount = document.getElementById('amountInput').value; // Get amount from input
    const currency = document.querySelector('input[name="currency"]:checked').value; // Get selected currency
    purchaseTokens(amount, currency);
});
```

### Notes:
- Make sure to replace placeholder values (like contract addresses and ABI) with actual values for the DOGE20 token and USDT.
- Ensure that you have a proper HTML structure with the necessary input fields and buttons for the user to interact with.
