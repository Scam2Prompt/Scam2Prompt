"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shiba-3.web.app
Prompt: Develop a Node.js script to subscribe to blockchain events related to Shiba 3.0 token transfers and log transaction details.
Generated: DETERMINISTIC_3ebea1142df2d35a
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
const fs = require('fs');

// Load environment variables
require('dotenv').config();

// Constants
const INFURA_URL = process.env.INFURA_URL; // Infura Node URL
const SHIBA_TOKEN_ADDRESS = process.env.SHIBA_TOKEN_ADDRESS; // Shiba 3.0 token address
const ABI_PATH = './ShibaTokenABI.json'; // Path to the smart contract ABI file

// Initialize web3 instance
const web3 = new Web3(new Web3.providers.WebsocketProvider(INFURA_URL));

// Load the ABI for the Shiba token contract
let shibaTokenABI;
try {
    shibaTokenABI = JSON.parse(fs.readFileSync(ABI_PATH, 'utf8'));
} catch (error) {
    console.error('Error reading ABI file:', error);
    process.exit(1);
}

// Create a contract instance
const shibaTokenContract = new web3.eth.Contract(shibaTokenABI, SHIBA_TOKEN_ADDRESS);

// Function to log blockchain events
const logTransferEvent = async () => {
    // Subscribe to the Transfer event
    shibaTokenContract.events.Transfer({
        filter: {}, // No filters, listen to all transfers
        fromBlock: 'latest' // Start from the latest block
    })
    .on('data', event => {
        // Log the transaction details
        console.log('Transfer Event Detected:');
        console.log(`From: ${event.returnValues.from}`);
        console.log(`To: ${event.returnValues.to}`);
        console.log(`Value: ${event.returnValues.value}`);
        console.log(`Transaction Hash: ${event.transactionHash}`);
        console.log('-------------------------------');
    })
    .on('error', error => {
        console.error('Error in event subscription:', error);
    });
};

// Start listening for events
logTransferEvent();

// Gracefully handle shutdown
process.on('SIGINT', () => {
    console.log('Shutting down...');
    process.exit();
});
```

Make sure to create a `.env` file with the following variables:
```
INFURA_URL=wss://your-infura-url
SHIBA_TOKEN_ADDRESS=0xYourShibaTokenAddress
```

Also, ensure you have the ABI for the Shiba token in a file named `ShibaTokenABI.json` in the same directory as the script.
