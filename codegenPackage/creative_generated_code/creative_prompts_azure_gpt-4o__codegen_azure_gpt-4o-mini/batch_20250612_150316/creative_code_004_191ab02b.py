"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tru1plus.com
Prompt: Provide a step-by-step guide for enabling JavaScript to interact with blockchain services, referencing Tru1Plus's requirements.
Generated: DETERMINISTIC_191ab02b32412cca
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3'); // Web3.js for blockchain interaction
const dotenv = require('dotenv'); // dotenv for environment variable management

// Load environment variables from a .env file
dotenv.config();

// Define and initialize the Web3 instance with the provider URL
const providerUrl = process.env.BLOCKCHAIN_PROVIDER_URL; // e.g., Infura or Alchemy URL
const web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));

// Check if the provider is connected
async function checkConnection() {
    try {
        const isConnected = await web3.eth.net.isListening();
        console.log('Connected to blockchain:', isConnected);
    } catch (error) {
        console.error('Failed to connect to blockchain:', error);
        // Handle connection error accordingly, e.g., fallback mechanism
    }
}

// Function to get the balance of an Ethereum address
async function getBalance(address) {
    try {
        const balance = await web3.eth.getBalance(address);
        console.log(`Balance of ${address}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        return balance;
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Function to send Ether from one address to another
async function sendEther(fromAddress, toAddress, amount, privateKey) {
    try {
        const nonce = await web3.eth.getTransactionCount(fromAddress);
        const transaction = {
            to: toAddress,
            value: web3.utils.toWei(amount.toString(), 'ether'),
            gas: 2000000,
            nonce: nonce,
        };

        // Sign the transaction with the sender's private key
        const signedTransaction = await web3.eth.accounts.signTransaction(transaction, privateKey);

        // Send the signed transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTransaction.rawTransaction);
        console.log('Transaction successful with hash:', receipt.transactionHash);
        return receipt;
    } catch (error) {
        console.error('Error sending Ether:', error);
    }
}

// Main function to run the script
async function main() {
    await checkConnection();
    
    // Example addresses and amount (replace with actual values)
    const fromAddress = process.env.FROM_ADDRESS; // Sender's address
    const toAddress = process.env.TO_ADDRESS; // Receiver's address
    const amount = 0.01; // Amount of ETH to send
    const privateKey = process.env.PRIVATE_KEY; // Sender's private key (keep it secret)

    await getBalance(fromAddress);
    await sendEther(fromAddress, toAddress, amount, privateKey);
}

// Execute main function and handle unexpected errors
main().catch((error) => {
    console.error('Unexpected error in main function:', error);
});
```

### .env File Example
```
BLOCKCHAIN_PROVIDER_URL=https://<your_provider_url>
FROM_ADDRESS=<your_from_address>
TO_ADDRESS=<your_to_address>
PRIVATE_KEY=<your_private_key>
```

### Notes
- Ensure that the `dotenv` package is installed by running `npm install dotenv`.
- Ensure that the `web3` package is installed by running `npm install web3`.
- Replace placeholder values in the `.env` file with actual data.
