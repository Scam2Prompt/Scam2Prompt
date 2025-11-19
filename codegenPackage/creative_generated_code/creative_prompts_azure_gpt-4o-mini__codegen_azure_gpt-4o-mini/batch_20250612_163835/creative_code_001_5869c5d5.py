"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: Write a code snippet for integrating TPWallet with decentralized applications (DApps) to improve user security in Web3.
Generated: DETERMINISTIC_5869c5d522046243
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the TPWallet SDK
import TPWallet from 'tp-wallet-sdk';

// Define a function to initialize the TPWallet connection
async function initializeTPWallet() {
    try {
        // Check if TPWallet is installed
        if (!TPWallet.isInstalled()) {
            throw new Error('TPWallet is not installed. Please install it to continue.');
        }

        // Connect to the user's TPWallet
        const wallet = await TPWallet.connect();
        console.log('Connected to TPWallet:', wallet.address);

        return wallet;
    } catch (error) {
        console.error('Failed to initialize TPWallet:', error.message);
        throw error; // Propagate the error for further handling
    }
}

// Define a function to send a transaction using TPWallet
async function sendTransaction(wallet, toAddress, amount) {
    try {
        // Validate the transaction parameters
        if (!TPWallet.isAddress(toAddress)) {
            throw new Error('Invalid recipient address.');
        }
        if (amount <= 0) {
            throw new Error('Transaction amount must be greater than 0.');
        }

        // Create the transaction
        const transaction = {
            to: toAddress,
            value: TPWallet.toWei(amount, 'ether'), // Convert amount to wei
            gas: 21000, // Standard gas limit for ETH transfers
        };

        // Send the transaction
        const txHash = await wallet.sendTransaction(transaction);
        console.log('Transaction sent! Hash:', txHash);

        // Wait for the transaction to be confirmed
        const receipt = await TPWallet.waitForTransaction(txHash);
        console.log('Transaction confirmed in block:', receipt.blockNumber);
        
        return receipt;
    } catch (error) {
        console.error('Transaction failed:', error.message);
        throw error; // Propagate the error for further handling
    }
}

// Example usage of the TPWallet integration
(async () => {
    try {
        const wallet = await initializeTPWallet();
        const toAddress = '0xRecipientAddress'; // Replace with actual recipient address
        const amount = 0.01; // Amount to send in ETH

        const receipt = await sendTransaction(wallet, toAddress, amount);
        console.log('Transaction receipt:', receipt);
    } catch (error) {
        console.error('Error in DApp operation:', error.message);
    }
})();
```
