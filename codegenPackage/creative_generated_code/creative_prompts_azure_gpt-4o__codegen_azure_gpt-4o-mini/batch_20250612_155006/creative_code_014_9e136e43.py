"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Provide a code snippet to create a decentralized application (dApp) on Sui that leverages its scalable infrastructure for high transaction throughput.
Generated: DETERMINISTIC_9e136e43ba18fd65
Batch ID: 20250612_155006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.testnet.sui.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { SuiClient, SuiTransaction, SuiTransactionBuilder } from '@mysten/sui.js';

// Constants for the Sui network
const SUI_NODE_URL = "https://fullnode.testnet.sui.io"; // Replace with appropriate Sui node URL
const PRIVATE_KEY = "your_private_key"; // Replace with your own private key for authentication

// Initialize the Sui client
const client = new SuiClient(SUI_NODE_URL);

/**
 * Function to create a new transaction on the Sui network
 * @param {string} recipient - The address of the recipient
 * @param {number} amount - The amount of SUI to send
 * @returns {string} - Transaction hash if successful
 */
async function createTransaction(recipient, amount) {
    try {
        // Validate input parameters
        if (!recipient || !amount || amount <= 0) {
            throw new Error("Invalid recipient address or amount.");
        }

        // Create the transaction
        const transaction = new SuiTransactionBuilder()
            .addTransferTransaction(recipient, amount)
            .build();

        // Sign the transaction
        const signedTransaction = await client.signTransaction(transaction, PRIVATE_KEY);

        // Submit the transaction to the Sui network
        const response = await client.executeTransaction(signedTransaction);

        console.log("Transaction successful:", response.transactionHash);
        return response.transactionHash;
    } catch (error) {
        console.error("Error creating transaction:", error.message);
        throw error; // Re-throw the error for further handling
    }
}

// Example usage of the createTransaction function
(async () => {
    const recipientAddress = "recipient_address"; // Replace with actual recipient address
    const amountToSend = 10; // Amount in SUI to send

    try {
        const transactionHash = await createTransaction(recipientAddress, amountToSend);
        console.log("Transaction Hash:", transactionHash);
    } catch (error) {
        console.error("Failed to create transaction:", error.message);
    }
})();
```
