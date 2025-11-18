"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftshark.cc
Prompt: Create a step-by-step guide for implementing NFTpay in a blockchain-based marketplace to allow credit card purchases of NFTs. Include details on transferring purchased NFTs to MetaMask.
Generated: DETERMINISTIC_aca8be5e1812d863
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const express = require('express');
const bodyParser = require('body-parser');
const Web3 = require('web3');
const NFTpay = require('nftpay'); // Assuming a hypothetical NFTpay SDK
const { ethers } = require('ethers');

// Create an instance of the express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Define your NFT contract address and ABI (Application Binary Interface)
const nftContractAddress = 'YOUR_NFT_CONTRACT_ADDRESS';
const nftContractABI = [ /* ABI Array */ ];

// Initialize Web3 and ethers provider
const web3 = new Web3(new Web3.providers.HttpProvider('YOUR_INFURA_OR_ALCHEMY_URL'));
const provider = new ethers.providers.JsonRpcProvider('YOUR_INFURA_OR_ALCHEMY_URL');

// Create a wallet instance for signing transactions
const privateKey = 'YOUR_PRIVATE_KEY'; // Use environment variables in production
const wallet = new ethers.Wallet(privateKey, provider);

// Endpoint to handle NFT purchases
app.post('/purchase-nft', async (req, res) => {
    const { tokenId, creditCardInfo, buyerAddress } = req.body;

    try {
        // Validate input
        if (!tokenId || !creditCardInfo || !buyerAddress) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        // Process credit card payment via NFTpay
        const paymentResponse = await NFTpay.processPayment(creditCardInfo);
        
        if (!paymentResponse.success) {
            throw new Error('Payment processing failed');
        }

        // Transfer NFT once payment is confirmed
        const nftContract = new web3.eth.Contract(nftContractABI, nftContractAddress);
        const tx = await nftContract.methods.transferFrom(wallet.address, buyerAddress, tokenId).send({ from: wallet.address });

        // Confirm transaction success
        res.status(200).json({ success: true, transactionHash: tx.transactionHash });
        
    } catch (error) {
        // Handle errors gracefully
        console.error('Error processing purchase:', error);
        res.status(500).json({ error: 'Internal server error', details: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
