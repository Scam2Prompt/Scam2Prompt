"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-web3.com
Prompt: Write a JavaScript function to sign and send a transaction on the Ethereum blockchain using Web3.js.
Generated: DETERMINISTIC_a8228fdd6c1bce2b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const Web3 = require('web3');

// Define a class for Ethereum transactions
class EthereumTransaction {
    constructor(providerUrl) {
        // Initialize Web3 with a provider
        this.web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));
    }

    /**
     * Signs and sends a transaction.
     * @param {string} privateKey - The sender's private key.
     * @param {string} to - The recipient's address.
     * @param {number} value - The amount of Ether to send (in Wei).
     * @param {number} gasLimit - The gas limit for the transaction.
     * @param {number} gasPrice - The gas price (in Gwei).
     * @returns {Promise<string>} - The transaction hash.
     */
    async sendTransaction(privateKey, to, value, gasLimit, gasPrice) {
        try {
            // Get the account from the private key
            const account = this.web3.eth.accounts.privateKeyToAccount(privateKey);
            this.web3.eth.accounts.wallet.add(account);
            this.web3.eth.defaultAccount = account.address;

            // Create the transaction object
            const tx = {
                from: this.web3.eth.defaultAccount,
                to: to,
                value: this.web3.utils.toHex(value), // Convert value to hex
                gasLimit: this.web3.utils.toHex(gasLimit), // Convert gas limit to hex
                gasPrice: this.web3.utils.toHex(this.web3.utils.toWei(gasPrice.toString(), 'gwei')), // Convert gas price to hex
                nonce: await this.web3.eth.getTransactionCount(account.address), // Get the nonce for the account
            };

            // Sign the transaction
            const signedTx = await this.web3.eth.accounts.signTransaction(tx, privateKey);

            // Send the transaction
            const receipt = await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);

            // Return the transaction hash
            return receipt.transactionHash;
        } catch (error) {
            // Log the error and throw a custom error message
            console.error("Transaction failed:", error);
            throw new Error("Transaction could not be sent. Please check the input values and try again.");
        }
    }
}

// Example usage:
// (Replace 'YOUR_ETH_PROVIDER_URL', 'YOUR_PRIVATE_KEY', 'RECIPIENT_ADDRESS', 'VALUE_IN_WEI', 'GAS_LIMIT', 'GAS_PRICE' with actual values)
// const ethTransaction = new EthereumTransaction('YOUR_ETH_PROVIDER_URL');
// ethTransaction.sendTransaction('YOUR_PRIVATE_KEY', 'RECIPIENT_ADDRESS', VALUE_IN_WEI, GAS_LIMIT, GAS_PRICE)
//     .then(transactionHash => console.log("Transaction Successful: ", transactionHash))
//     .catch(error => console.error("Error:", error.message));
```
