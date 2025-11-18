"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-brc20.pages.dev
Prompt: Generate JavaScript code using Web3.js to connect to the BRC-20 DEX smart contract, retrieve the current exchange rate for $BRC20DEX tokens, and allow users to purchase tokens.
Generated: DETERMINISTIC_4dbd04c612551401
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { abi: dexAbi } = require('./BRC20DEX.json'); // ABI of the BRC-20 DEX smart contract

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Define the BRC-20 DEX smart contract address (replace with the actual address)
const dexAddress = '0xYourDexContractAddress';

// Create a contract instance
const dexContract = new web3.eth.Contract(dexAbi, dexAddress);

// Function to get the current exchange rate for $BRC20DEX tokens
async function getExchangeRate() {
    try {
        const exchangeRate = await dexContract.methods.getExchangeRate().call();
        console.log('Current Exchange Rate:', exchangeRate);
        return exchangeRate;
    } catch (error) {
        console.error('Error while fetching exchange rate:', error);
        throw new Error('Unable to fetch exchange rate');
    }
}

// Function to purchase $BRC20DEX tokens
async function purchaseTokens(amountInEther) {
    if (!window.ethereum) {
        console.error('Ethereum provider not detected');
        return;
    }

    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    const accounts = await web3.eth.getAccounts();
    const buyerAddress = accounts[0];

    try {
        // Convert amount from Ether to Wei
        const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

        // Call the purchase function of the smart contract
        const tx = await dexContract.methods.purchaseTokens(amountInWei).send({ from: buyerAddress, value: amountInWei });

        console.log('Transaction successful:', tx);
        return tx;
    } catch (error) {
        console.error('Error while purchasing tokens:', error);
        throw new Error('Transaction failed');
    }
}

// Example usage
(async () => {
    try {
        const rate = await getExchangeRate();
        console.log('Rate:', rate);

        // Purchase tokens (example with 0.1 Ether)
        await purchaseTokens(0.1);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
