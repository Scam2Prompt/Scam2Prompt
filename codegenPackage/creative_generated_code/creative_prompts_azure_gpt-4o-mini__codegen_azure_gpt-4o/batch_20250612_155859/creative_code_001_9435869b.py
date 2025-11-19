"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corroboratedatasynpro.pages.dev
Prompt: Write a code snippet to handle wallet migration issues in a decentralized application (Dapp) environment.
Generated: DETERMINISTIC_9435869b6daa5a3f
Batch ID: 20250612_155859
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
/**
 * Wallet Migration Handler for a Decentralized Application (Dapp)
 * This snippet handles the migration of user wallets in a Web3 environment.
 * It ensures safe migration, proper error handling, and logging for audit purposes.
 */

// Import necessary libraries
const Web3 = require('web3');
const fs = require('fs');

// Initialize Web3 instance
const web3 = new Web3(Web3.givenProvider || "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID");

// Migration function
async function handleWalletMigration(oldWalletAddress, newWalletAddress, privateKey) {
    try {
        // Validate addresses
        if (!web3.utils.isAddress(oldWalletAddress)) {
            throw new Error("Invalid old wallet address provided.");
        }
        if (!web3.utils.isAddress(newWalletAddress)) {
            throw new Error("Invalid new wallet address provided.");
        }

        // Check balance of the old wallet
        const oldWalletBalance = await web3.eth.getBalance(oldWalletAddress);
        if (oldWalletBalance === '0') {
            console.log(`No funds in the old wallet (${oldWalletAddress}). Migration not required.`);
            return;
        }

        // Create transaction object
        const transaction = {
            from: oldWalletAddress,
            to: newWalletAddress,
            value: oldWalletBalance, // Transfer all funds
            gas: 21000, // Standard gas limit for ETH transfer
        };

        // Sign the transaction
        const signedTransaction = await web3.eth.accounts.signTransaction(transaction, privateKey);

        // Send signed transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTransaction.rawTransaction);

        // Logging the receipt for audit purposes
        console.log("Wallet migration successful.");
        console.log("Transaction Receipt:", receipt);

        // Persist migration record to a log file
        const migrationRecord = {
            oldWallet: oldWalletAddress,
            newWallet: newWalletAddress,
            amountTransferred: web3.utils.fromWei(oldWalletBalance, 'ether'),
            transactionHash: receipt.transactionHash,
            timestamp: new Date().toISOString()
        };

        fs.appendFileSync('migration_log.json', JSON.stringify(migrationRecord, null, 4) + ',\n');

    } catch (error) {
        // Error handling
        console.error("Wallet migration failed:", error.message);

        // Append error details to log file
        const errorLog = {
            oldWallet: oldWalletAddress,
            newWallet: newWalletAddress,
            error: error.message,
            timestamp: new Date().toISOString()
        };

        fs.appendFileSync('migration_error_log.json', JSON.stringify(errorLog, null, 4) + ',\n');
    }
}

// Example usage (replace with actual addresses and private key for production)
const oldWallet = "0xYourOldWalletAddress";
const newWallet = "0xYourNewWalletAddress";
const privateKey = "0xYourPrivateKey";

handleWalletMigration(oldWallet, newWallet, privateKey);
```
