"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-io-git-feat-app-debanker.vercel.app
Prompt: Provide an example of using the Rabby Wallet SDK to sign a transaction in a blockchain application.
Generated: DETERMINISTIC_fe6113268f66dde7
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Rabby Wallet SDK
import RabbyWallet from 'rabby-wallet-sdk';

// Function to sign a transaction using Rabby Wallet
async function signTransaction(transaction, chainId) {
    // Initialize Rabby Wallet SDK
    const rabbyWallet = new RabbyWallet();

    try {
        // Check if the wallet is connected
        const isConnected = await rabbyWallet.isConnected();
        if (!isConnected) {
            throw new Error('Wallet is not connected. Please connect your wallet.');
        }

        // Prepare the transaction data
        const txData = {
            from: transaction.from,
            to: transaction.to,
            value: transaction.value,
            gas: transaction.gas,
            gasPrice: transaction.gasPrice,
            data: transaction.data,
            chainId: chainId
        };

        // Sign the transaction
        const signedTransaction = await rabbyWallet.signTransaction(txData);

        // Return the signed transaction
        return signedTransaction;

    } catch (error) {
        // Handle errors appropriately
        console.error('An error occurred while signing the transaction:', error);
        throw new Error('Transaction signing failed: ' + error.message);
    }
}

// Example usage
const exampleTransaction = {
    from: '0xYourFromAddress',
    to: '0xYourToAddress',
    value: '0xValueInWei', // Value in Wei (e.g., '0xDE0B6B3A7640000' for 0.1 ETH)
    gas: '0x5208', // Gas limit (e.g., 21000 in hex)
    gasPrice: '0x3B9ACA00', // Gas price (e.g., 1 Gwei in hex)
    data: '0x', // Optional data field
};

const exampleChainId = 1; // Mainnet

// Execute signing the example transaction
signTransaction(exampleTransaction, exampleChainId)
    .then((signedTx) => {
        console.log('Signed transaction:', signedTx);
    })
    .catch((error) => {
        console.error('Error signing transaction:', error);
    });
```
