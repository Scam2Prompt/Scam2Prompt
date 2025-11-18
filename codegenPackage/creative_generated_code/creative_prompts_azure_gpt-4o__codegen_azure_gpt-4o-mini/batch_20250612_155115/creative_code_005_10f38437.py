"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artistichive.io
Prompt: Provide a guide for integrating Ethereum-based payment processing into a digital art platform, including code examples for handling transactions securely, as seen on ArtisticHive.io.
Generated: DETERMINISTIC_10f38437aad7a017
Batch ID: 20250612_155115
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
// Ethereum Payment Processing Integration for Digital Art Platform

// Import required libraries
const Web3 = require('web3');
const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Initialize Web3 instance using Infura or another Ethereum node provider
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Wallet address and private key for your Ethereum account
const walletAddress = process.env.WALLET_ADDRESS;
const privateKey = process.env.PRIVATE_KEY;

// Check for valid Ethereum address
if (!web3.utils.isAddress(walletAddress)) {
    throw new Error('Invalid Ethereum wallet address');
}

// Function to create a transaction
async function createTransaction(toAddress, amountInEther) {
    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

        // Create a transaction object
        const txObject = {
            to: toAddress,
            value: amountInWei,
            gas: 2000000,
            gasPrice: await web3.eth.getGasPrice(),
            nonce: await web3.eth.getTransactionCount(walletAddress),
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(txObject, privateKey);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        return receipt;
    } catch (error) {
        console.error('Transaction error:', error);
        throw new Error('Transaction failed');
    }
}

// Endpoint to handle payment requests
app.post('/api/payment', async (req, res) => {
    const { toAddress, amount } = req.body;

    // Validate input
    if (!toAddress || !amount) {
        return res.status(400).json({ error: 'Invalid input' });
    }
    
    // Check if the recipient address is valid
    if (!web3.utils.isAddress(toAddress)) {
        return res.status(400).json({ error: 'Invalid recipient address' });
    }

    try {
        // Create and send the transaction
        const receipt = await createTransaction(toAddress, amount);
        return res.status(200).json({ success: true, receipt });
    } catch (error) {
        return res.status(500).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

```plaintext
// .env file example
INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
WALLET_ADDRESS=YOUR_WALLET_ADDRESS
PRIVATE_KEY=YOUR_PRIVATE_KEY
PORT=3000
```

### Note:
- Ensure you have the `web3`, `express`, `dotenv`, and `body-parser` packages installed. You can install them using:
  ```bash
  npm install web3 express dotenv body-parser
  ```
- Replace placeholders in the `.env` file with actual values before running the application.
