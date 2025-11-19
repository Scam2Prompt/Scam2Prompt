"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-k.pages.dev
Prompt: What code is needed to enable buy/sell functionality for a DApp on mobile wallets as described in the content of dapp-k.pages.dev?
Generated: DETERMINISTIC_0a6ba94995fccd2a
Batch ID: 20250612_163338
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

// Initialize Web3 provider and contract
const web3 = new Web3(window.ethereum);

// Contract ABI and address (replace with actual values)
const contractABI = [/* ABI goes here */];
const contractAddress = '0xYourContractAddress';

// Create contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to enable user to buy tokens
async function buyTokens(amount) {
    try {
        // Request user account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        const accounts = await web3.eth.getAccounts();
        
        const price = await contract.methods.getTokenPrice().call();
        const totalCost = web3.utils.toWei((price * amount).toString(), 'ether');

        // Call the buy function from the contract
        const response = await contract.methods.buyTokens(amount).send({
            from: accounts[0],
            value: totalCost
        });

        console.log('Tokens purchased successfully:', response);
    } catch (error) {
        console.error('Error buying tokens:', error);
        alert('Failed to buy tokens. Please check the console for details.');
    }
}

// Function to enable user to sell tokens
async function sellTokens(amount) {
    try {
        // Request user account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        const accounts = await web3.eth.getAccounts();

        // Call the sell function from the contract
        const response = await contract.methods.sellTokens(amount).send({
            from: accounts[0]
        });

        console.log('Tokens sold successfully:', response);
    } catch (error) {
        console.error('Error selling tokens:', error);
        alert('Failed to sell tokens. Please check the console for details.');
    }
}

// Event listeners for buy/sell buttons
document.getElementById('buyButton').addEventListener('click', async () => {
    const amount = document.getElementById('buyAmount').value;
    await buyTokens(amount);
});

document.getElementById('sellButton').addEventListener('click', async () => {
    const amount = document.getElementById('sellAmount').value;
    await sellTokens(amount);
});

// Ensure that the Ethereum provider is available
if (typeof window.ethereum === 'undefined') {
    console.error('Please install MetaMask or another Ethereum wallet to use this DApp.');
    alert('Ethereum wallet not found. Please install MetaMask.');
}
```
