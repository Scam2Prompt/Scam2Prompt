"""
Generated Code Metadata:
========================
Original URL: https://dcqqx.com
Prompt: Generate a script using ethers.js to check the status of Ethereum transactions on a DeFi platform that requires JavaScript.
Generated: DETERMINISTIC_e275de02cd08267c
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the ethers library
const { ethers } = require("ethers");

// Define the provider (Infura, Alchemy, or any Ethereum node provider)
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");

// Function to check the status of a transaction
async function checkTransactionStatus(transactionHash) {
    try {
        // Fetch the transaction receipt using the transaction hash
        const receipt = await provider.getTransactionReceipt(transactionHash);

        // Check if the receipt is null (transaction not found)
        if (!receipt) {
            console.log(`Transaction ${transactionHash} not found.`);
            return;
        }

        // Log the transaction status
        const status = receipt.status === 1 ? "Success" : "Failed";
        console.log(`Transaction Hash: ${transactionHash}`);
        console.log(`Block Number: ${receipt.blockNumber}`);
        console.log(`Status: ${status}`);
        console.log(`Gas Used: ${receipt.gasUsed.toString()}`);
        console.log(`Cumulative Gas Used: ${receipt.cumulativeGasUsed.toString()}`);
        console.log(`From: ${receipt.from}`);
        console.log(`To: ${receipt.to}`);
    } catch (error) {
        // Handle errors gracefully
        console.error(`Error fetching transaction status: ${error.message}`);
    }
}

// Example usage: Replace with a valid transaction hash
const transactionHash = "0xYourTransactionHashHere";
checkTransactionStatus(transactionHash);
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID and `"0xYourTransactionHashHere"` with a valid Ethereum transaction hash to test the script.
