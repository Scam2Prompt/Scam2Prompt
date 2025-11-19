"""
Generated Code Metadata:
========================
Original URL: https://mogcoin-xyz.pages.dev
Prompt: Write a JavaScript function using Ethers.js to query the Ethereum blockchain for transaction details involving the $MOG token contract address `0xaaee1a9723aadb7afa2810263653a34ba2c21c7a`.
Generated: DETERMINISTIC_c9f96a5f9d0df52e
Batch ID: 20250612_153526
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

/**
 * Fetch transaction details for a specific token contract address on the Ethereum blockchain.
 * 
 * @param {string} tokenAddress - The contract address of the token (e.g., $MOG token).
 * @param {string} transactionHash - The hash of the transaction to query.
 * @returns {Promise<Object>} - A promise that resolves to the transaction details.
 * @throws {Error} - Throws an error if the transaction cannot be found or if there is a network issue.
 */
async function getTransactionDetails(tokenAddress, transactionHash) {
    // Connect to the Ethereum network (using default provider)
    const provider = ethers.getDefaultProvider();

    try {
        // Fetch the transaction details using the transaction hash
        const transaction = await provider.getTransaction(transactionHash);

        // Check if the transaction exists
        if (!transaction) {
            throw new Error(`Transaction with hash ${transactionHash} not found.`);
        }

        // Check if the transaction involves the specified token contract
        if (transaction.to && transaction.to.toLowerCase() === tokenAddress.toLowerCase()) {
            return {
                hash: transaction.hash,
                from: transaction.from,
                to: transaction.to,
                value: ethers.utils.formatEther(transaction.value), // Convert value from wei to ether
                gasPrice: ethers.utils.formatUnits(transaction.gasPrice, 'gwei'), // Convert gas price to gwei
                gasLimit: transaction.gasLimit.toString(),
                blockNumber: transaction.blockNumber,
                timestamp: (await provider.getBlock(transaction.blockNumber)).timestamp,
            };
        } else {
            throw new Error(`Transaction does not involve the token contract at address ${tokenAddress}.`);
        }
    } catch (error) {
        // Handle errors (e.g., network issues, invalid transaction hash)
        console.error("Error fetching transaction details:", error.message);
        throw new Error("Failed to fetch transaction details. Please check the transaction hash and try again.");
    }
}

// Example usage (uncomment to run):
// getTransactionDetails('0xaaee1a9723aadb7afa2810263653a34ba2c21c7a', 'YOUR_TRANSACTION_HASH_HERE')
//     .then(details => console.log(details))
//     .catch(error => console.error(error));
```
