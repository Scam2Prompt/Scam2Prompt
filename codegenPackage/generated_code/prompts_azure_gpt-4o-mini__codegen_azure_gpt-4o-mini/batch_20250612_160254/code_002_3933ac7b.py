"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Create a JavaScript function that allows users to buy PLRT tokens during the presale, ensuring it integrates with the Binance Smart Chain.
Generated: DETERMINISTIC_3933ac7b5e295791
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Importing necessary libraries
const Web3 = require('web3');

// Define the contract ABI and address
const contractABI = [ /* ABI array goes here */ ];
const contractAddress = '0xYourContractAddressHere';

// Initialize Web3 with a provider
const web3 = new Web3(window.ethereum);

// Function to buy PLRT tokens during the presale
async function buyPLRTTokens(amountInEther) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Convert the amount from Ether to Wei
        const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

        // Create a contract instance
        const contract = new web3.eth.Contract(contractABI, contractAddress);

        // Call the buy function of the contract
        const transaction = await contract.methods.buyTokens().send({
            from: userAddress,
            value: amountInWei,
            gas: 2000000 // Set a gas limit
        });

        // Log the transaction receipt
        console.log('Transaction successful:', transaction);
    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while buying PLRT tokens:', error.message);
        alert('Transaction failed: ' + error.message);
    }
}

// Example usage: Call the function to buy 0.1 PLRT tokens
// buyPLRTTokens(0.1);
```

**Note:** Replace `/* ABI array goes here */` with the actual ABI of your smart contract and `0xYourContractAddressHere` with the actual contract address. The `buyTokens` method should be defined in your smart contract.
