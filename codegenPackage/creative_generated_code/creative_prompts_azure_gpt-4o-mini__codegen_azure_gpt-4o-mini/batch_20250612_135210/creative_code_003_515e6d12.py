"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-wallet-demo.vercel.app
Prompt: Generate a script that calculates gas fees for transactions when using MetaMask.
Generated: DETERMINISTIC_515e6d1293669316
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// gasFeeCalculator.js
// This script calculates gas fees for Ethereum transactions using MetaMask.

// Import necessary libraries
const Web3 = require('web3');

// Initialize Web3 instance connected to MetaMask
const web3 = new Web3(window.ethereum);

// Function to calculate gas fees
async function calculateGasFees(transaction) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get current gas price from the Ethereum network
        const gasPrice = await web3.eth.getGasPrice();

        // Estimate the gas limit for the transaction
        const gasLimit = await web3.eth.estimateGas(transaction);

        // Calculate total gas fees in Wei
        const totalGasFee = BigInt(gasPrice) * BigInt(gasLimit);

        // Convert gas fee from Wei to Ether
        const totalGasFeeInEther = web3.utils.fromWei(totalGasFee.toString(), 'ether');

        return {
            gasPrice: web3.utils.fromWei(gasPrice, 'gwei'), // Convert gas price to Gwei for readability
            gasLimit,
            totalGasFeeInEther
        };
    } catch (error) {
        console.error('Error calculating gas fees:', error);
        throw new Error('Failed to calculate gas fees. Please check your transaction and try again.');
    }
}

// Example usage of the calculateGasFees function
(async () => {
    // Define the transaction object
    const transaction = {
        to: '0xRecipientAddress', // Replace with the recipient's address
        value: web3.utils.toWei('0.01', 'ether'), // Amount to send in Wei
        data: '0x', // Optional data field for contract interactions
    };

    try {
        const gasFees = await calculateGasFees(transaction);
        console.log('Gas Price (Gwei):', gasFees.gasPrice);
        console.log('Gas Limit:', gasFees.gasLimit);
        console.log('Total Gas Fee (Ether):', gasFees.totalGasFeeInEther);
    } catch (error) {
        console.error('Failed to fetch gas fees:', error.message);
    }
})();
```
