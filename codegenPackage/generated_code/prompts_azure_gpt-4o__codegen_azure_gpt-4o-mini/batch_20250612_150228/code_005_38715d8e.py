"""
Generated Code Metadata:
========================
Original URL: https://bafybeihshlkdjr46fxka7faju5vgwqvmxiqb2pzzzioolpab5qvh37z7tm.ipfs.dweb.link
Prompt: Provide an example of building Bitcoin-aware applications using the Hemi Bitcoin Kit (hBK) with EVM compatibility.
Generated: DETERMINISTIC_38715d8e503c771b
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from the Hemi Bitcoin Kit (hBK)
const { HemiClient, TransactionBuilder, Wallet } = require('hbk-sdk');

// Configuration for connecting to the Bitcoin network
const config = {
    network: 'testnet', // Use 'mainnet' for production
    apiKey: 'YOUR_API_KEY', // Replace with your actual API key
};

// Initialize the Hemi client
const client = new HemiClient(config);

// Function to create a new wallet
async function createWallet() {
    try {
        const wallet = await Wallet.create();
        console.log('Wallet created successfully:', wallet);
        return wallet;
    } catch (error) {
        console.error('Error creating wallet:', error);
        throw new Error('Wallet creation failed');
    }
}

// Function to build and send a Bitcoin transaction
async function sendTransaction(wallet, recipientAddress, amount) {
    try {
        // Create a new transaction builder
        const txBuilder = new TransactionBuilder();

        // Add the recipient and amount to the transaction
        txBuilder.addOutput(recipientAddress, amount);

        // Sign the transaction with the wallet's private key
        const signedTx = await txBuilder.sign(wallet.privateKey);

        // Send the transaction to the Bitcoin network
        const txHash = await client.sendTransaction(signedTx);
        console.log('Transaction sent successfully, TX Hash:', txHash);
        return txHash;
    } catch (error) {
        console.error('Error sending transaction:', error);
        throw new Error('Transaction sending failed');
    }
}

// Main function to execute the Bitcoin-aware application
async function main() {
    try {
        // Create a new wallet
        const wallet = await createWallet();

        // Define recipient address and amount to send (in satoshis)
        const recipientAddress = 'recipient_bitcoin_address'; // Replace with actual address
        const amount = 100000; // Amount in satoshis (0.001 BTC)

        // Send the transaction
        const txHash = await sendTransaction(wallet, recipientAddress, amount);
        console.log('Transaction completed with hash:', txHash);
    } catch (error) {
        console.error('Application error:', error);
    }
}

// Execute the main function
main();
```

**Note:** Replace `'YOUR_API_KEY'` and `'recipient_bitcoin_address'` with actual values before running the code. Ensure that you have the `hbk-sdk` library installed in your project.
