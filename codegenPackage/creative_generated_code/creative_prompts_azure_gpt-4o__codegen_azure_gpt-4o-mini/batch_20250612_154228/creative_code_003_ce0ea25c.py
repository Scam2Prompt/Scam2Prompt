"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockappsnode.com
Prompt: Provide a code example for building a decentralized application with multichain support and self-custodial features, based on the tools discussed on BlockAppsNode.com.
Generated: DETERMINISTIC_ce0ea25cb8f84f31
Batch ID: 20250612_154228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`": {
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
const Web3 = require('web3'); // Web3 library for Ethereum interactions
const { ethers } = require('ethers'); // Ethers.js for Ethereum, optimized for performance
const express = require('express'); // Express for creating a web server
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests

// Define constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura Project ID
const PORT = process.env.PORT || 3000; // Server port

// Initialize Web3 and Ethers
const web3 = new Web3(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`);
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Create Express application
const app = express();
app.use(bodyParser.json()); // Parse JSON request bodies

// Middleware to handle errors
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Endpoint to get account balance for a given address
app.post('/balance', async (req, res) => {
    const { address } = req.body; // Extract address from request body

    try {
        // Validate Ethereum address
        if (!web3.utils.isAddress(address)) {
            return res.status(400).send('Invalid Ethereum address');
        }

        // Fetch balance from the blockchain
        const balance = await provider.getBalance(address);
        // Convert balance from Wei to Ether
        const etherBalance = ethers.utils.formatEther(balance);

        res.json({ address, balance: etherBalance }); // Send response with balance
    } catch (error) {
        console.error('Error fetching balance:', error);
        res.status(500).send('Unable to fetch balance');
    }
});

// Endpoint to send Ether from one address to another
app.post('/send', async (req, res) => {
    const { from, to, amount, privateKey } = req.body; // Extract required fields

    try {
        // Validate Ethereum addresses
        if (!web3.utils.isAddress(from) || !web3.utils.isAddress(to)) {
            return res.status(400).send('Invalid Ethereum address');
        }

        // Validate amount
        if (isNaN(amount) || amount <= 0) {
            return res.status(400).send('Invalid amount');
        }

        // Create a wallet instance using the private key
        const wallet = new ethers.Wallet(privateKey, provider);

        // Create the transaction
        const tx = {
            to: to,
            value: ethers.utils.parseEther(amount.toString()), // Convert amount to Wei
            gasLimit: 21000, // Standard gas limit for a transfer
        };

        // Send the transaction
        const transactionResponse = await wallet.sendTransaction(tx);
        await transactionResponse.wait(); // Wait for transaction to be mined

        res.json({ txHash: transactionResponse.hash }); // Send response with transaction hash
    } catch (error) {
        console.error('Error sending transaction:', error);
        res.status(500).send('Transaction failed');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
