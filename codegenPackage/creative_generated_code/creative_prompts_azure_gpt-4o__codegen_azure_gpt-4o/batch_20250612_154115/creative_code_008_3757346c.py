"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Provide an example of how to use MetaMask to sign a transaction and broadcast it to the Ethereum blockchain programmatically.
Generated: DETERMINISTIC_3757346c79cbd2a7
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
// Install dependencies: `npm install web3 @metamask/detect-provider`
const Web3 = require('web3');
const detectProvider = require('@metamask/detect-provider');

// Function to sign and broadcast a transaction using MetaMask
async function signAndSendTransaction() {
    try {
        // Detect MetaMask provider
        const provider = await detectProvider();

        // Ensure MetaMask is installed
        if (!provider) {
            throw new Error('MetaMask is not installed. Please install MetaMask and try again.');
        }

        // Initialize Web3 with the MetaMask provider
        const web3 = new Web3(provider);

        // Request the user to connect their MetaMask account
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        const sender = accounts[0]; // Use the first connected account

        // Define the transaction parameters
        const transaction = {
            from: sender, // Sender's address (retrieved from MetaMask)
            to: '0xRecipientAddressHere', // Replace with the recipient address
            value: web3.utils.toWei('0.01', 'ether'), // Amount to send (in wei)
            gas: 21000, // Gas limit (basic transfer requires 21000 gas)
        };

        // Ask MetaMask to sign the transaction
        const signedTransaction = await provider.request({
            method: 'eth_sendTransaction',
            params: [transaction],
        });

        console.log('Transaction broadcasted successfully!');
        console.log(`Transaction hash: ${signedTransaction}`);
        console.log('You can view the transaction on the Ethereum blockchain explorer.');
    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while signing or broadcasting the transaction:', error.message);
    }
}

// Execute the function
signAndSendTransaction();
```

*Note: Replace `'0xRecipientAddressHere'` with the actual recipient Ethereum address.*
