"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crryptiowalltiei.godaddysites.com
Prompt: Write code to integrate a Ledger hardware wallet with the Phantom Extension using JavaScript or a relevant API.
Generated: DETERMINISTIC_fc476c6679b2d695
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { LedgerSigner } from '@ethersproject/hardware-wallets';
import { ethers } from 'ethers';
import { PhantomConnector } from '@solana/wallet-adapter-phantom';

// Initialize Phantom Connector
const phantom = new PhantomConnector();

// Function to connect Ledger hardware wallet
async function connectLedger() {
    try {
        // Request account access
        const accounts = await phantom.connect();

        if (!accounts.length) {
            throw new Error('No accounts found');
        }

        console.log('Connected to Phantom wallet:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Connection failed:', error.message);
        throw error; // Rethrow error for further handling if necessary
    }
}

// Function to sign a transaction using Ledger
async function signTransaction(transaction) {
    try {
        // Create a Ledger signer instance
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const ledgerSigner = new LedgerSigner(provider);

        // Sign the transaction
        const signedTransaction = await ledgerSigner.signTransaction(transaction);

        console.log('Transaction signed:', signedTransaction);
        return signedTransaction;
    } catch (error) {
        console.error('Transaction signing failed:', error.message);
        throw error; // Rethrow error for further handling if necessary
    }
}

// Main function to initialize connection and sign transaction
async function main() {
    try {
        const userAddress = await connectLedger();

        // Placeholder for a transaction object
        const transaction = {
            to: '0xrecipientAddress', // Replace with actual recipient address
            value: ethers.utils.parseEther('0.01'), // Amount to send
            gasLimit: 21000, // Gas limit
            nonce: await ethers.provider.getTransactionCount(userAddress), // Fetch nonce
        };

        const signedTransaction = await signTransaction(transaction);
        console.log('Final signed transaction:', signedTransaction);
        
        // Here you would send the signed transaction to the network
        // const txResponse = await provider.sendTransaction(signedTransaction);
        // console.log('Transaction response:', txResponse);
        
    } catch (error) {
        console.error('Error in main execution:', error.message);
    }
}

// Execute the main function
main();
```

### Notes:
- Replace `'0xrecipientAddress'` with the actual address you want to send the transaction to.
- Ensure that you have installed the required dependencies: `@ethersproject/hardware-wallets`, `ethers`, and `@solana/wallet-adapter-phantom`.
- The commented-out section for sending the signed transaction can be activated based on your needs.
