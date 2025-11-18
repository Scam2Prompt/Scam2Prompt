"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibtcfgrhknlfhnz2c5cddfnsoje4dumrc3wsyoikx2pwuf6fbcsr4.ipfs.dweb.link
Prompt: Recommend APIs or libraries from the MetaMask Developer Docs that can be used to implement EIP-1559 transaction fee calculations in a decentralized application.
Generated: DETERMINISTIC_d38edf2586d21d1f
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from MetaMask
const { ethers } = require('ethers'); // Ethers.js for interacting with Ethereum
const { detectProvider } = require('@metamask/detect-provider'); // Detect MetaMask provider

// Function to calculate EIP-1559 transaction fees
async function calculateEIP1559Fees() {
    try {
        // Detect and connect MetaMask provider
        const provider = await detectProvider();
        if (!provider) {
            throw new Error('MetaMask not detected. Please install MetaMask.');
        }

        // Connect to Ethereum using ethers.js
        const web3Provider = new ethers.providers.Web3Provider(provider);

        // Get the current network's fee data (base fee, priority fee, etc.)
        const feeData = await web3Provider.getFeeData();

        // Check that fee data was retrieved successfully
        if (!feeData || !feeData.maxFeePerGas || !feeData.maxPriorityFeePerGas) {
            throw new Error('Failed to retrieve fee data. Make sure you are connected to a supported Ethereum network.');
        }

        // Log EIP-1559 fee information
        console.log('Current EIP-1559 fee data:');
        console.log(`Base Fee: ${ethers.utils.formatUnits(feeData.gasPrice, 'gwei')} gwei`);
        console.log(`Max Fee Per Gas: ${ethers.utils.formatUnits(feeData.maxFeePerGas, 'gwei')} gwei`);
        console.log(`Max Priority Fee Per Gas: ${ethers.utils.formatUnits(feeData.maxPriorityFeePerGas, 'gwei')} gwei`);

        // Return structured fee data for further use
        return {
            baseFeePerGas: ethers.utils.formatUnits(feeData.gasPrice, 'gwei'),
            maxFeePerGas: ethers.utils.formatUnits(feeData.maxFeePerGas, 'gwei'),
            maxPriorityFeePerGas: ethers.utils.formatUnits(feeData.maxPriorityFeePerGas, 'gwei'),
        };
    } catch (error) {
        // Handle and log any errors
        console.error('Error while calculating EIP-1559 fees:', error.message);
        throw error; // Rethrow error for further handling
    }
}

// Example usage of the calculateEIP1559Fees function
(async () => {
    try {
        const fees = await calculateEIP1559Fees();
        console.log('EIP-1559 Fee Calculation Result:', fees);
    } catch (error) {
        console.error('Failed to calculate fees:', error.message);
    }
})();
```
