"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogcoin-xyz.pages.dev
Prompt: Write a JavaScript function using Ethers.js to query the Ethereum blockchain for transaction details involving the $MOG token contract address `0xaaee1a9723aadb7afa2810263653a34ba2c21c7a`.
Generated: DETERMINISTIC_c9f96a5f9d0df52e
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from ethers.js
const { ethers } = require("ethers");

/**
 * Fetches transaction details involving the specified token contract address on the Ethereum blockchain.
 * 
 * @param {string} tokenAddress - The address of the token contract (in this case, $MOG).
 * @param {string} transactionHash - The hash of the transaction to query.
 * @returns {Promise<Object>} - A promise that resolves to the transaction details.
 * @throws Will throw an error if fetching the transaction fails.
 */
async function fetchTransactionDetails(tokenAddress, transactionHash) {
    // Connect to the Ethereum network using a provider (Infura, Alchemy, etc.)
    const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");

    try {
        // Fetch the transaction details using the transaction hash
        const transaction = await provider.getTransaction(transactionHash);

        // Check if the transaction exists
        if (!transaction) {
            throw new Error(`Transaction with hash ${transactionHash} not found.`);
        }

        // Check if the transaction involves the specified token address
        const receipt = await provider.getTransactionReceipt(transactionHash);
        const tokenTransferEventSignature = ethers.utils.id("Transfer(address,address,uint256)");

        // Filter logs for the token transfer events
        const tokenTransfers = receipt.logs.filter(log => 
            log.address.toLowerCase() === tokenAddress.toLowerCase() && 
            log.topics[0] === tokenTransferEventSignature
        );

        // Return relevant transaction details with token transfer events if available
        return {
            transaction,
            tokenTransfers,
            tokenInvolved: tokenTransfers.length > 0
        };
    } catch (error) {
        console.error("Error fetching transaction details:", error);
        throw new Error(`Failed to fetch transaction details: ${error.message}`);
    }
}

// Example usage
const tokenAddress = "0xaaee1a9723aadb7afa2810263653a34ba2c21c7a";
const transactionHash = "0xYOUR_TRANSACTION_HASH_HERE";

fetchTransactionDetails(tokenAddress, transactionHash)
    .then(details => console.log("Transaction Details:", details))
    .catch(err => console.error("Error:", err));
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID and `"0xYOUR_TRANSACTION_HASH_HERE"` with the actual transaction hash you want to query. Make sure you have the `ethers` package installed in your project.
