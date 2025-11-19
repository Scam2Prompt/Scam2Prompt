"""
Generated Code Metadata:
========================
Original URL: https://nft-minting-app-main.pages.dev
Prompt: Suggest tools and frameworks for creating a JavaScript-based NFT minting app that requires JavaScript to function, as described on the ALPACADABRAZ NFT site.
Generated: DETERMINISTIC_275b374765d75658
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const Web3 = require('web3');
const { ethers } = require('ethers');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

/**
 * NFT Minting App
 * 
 * This application provides a simple interface for minting NFTs.
 */

// Set up Express app
const app = express();
app.use(express.json());

// Set up Web3 provider
const web3 = new Web3(process.env.INFURA_URL);

// Set up Ethereum provider
const provider = new ethers.providers.JsonRpcProvider(process.env.INFURA_URL);

// Set up contract ABI and address
const contractAbi = require('./contractAbi.json');
const contractAddress = process.env.CONTRACT_ADDRESS;

// Create contract instance
const contract = new ethers.Contract(contractAddress, contractAbi, provider);

/**
 * Mint NFT
 * 
 * @param {string} owner - The address of the NFT owner
 * @param {string} tokenUri - The URI of the NFT token
 * 
 * @returns {Promise<string>} The transaction hash
 */
async function mintNft(owner, tokenUri) {
    try {
        // Get the latest nonce
        const nonce = await provider.getTransactionCount(owner);

        // Create transaction
        const tx = contract.connect(provider).mint(owner, tokenUri, {
            nonce,
            gasLimit: '500000',
            gasPrice: ethers.utils.parseUnits('20', 'gwei'),
        });

        // Send transaction
        const txHash = await tx.hash;

        return txHash;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

// API endpoint to mint NFT
app.post('/mint', async (req, res) => {
    try {
        const { owner, tokenUri } = req.body;

        if (!owner || !tokenUri) {
            res.status(400).send({ error: 'Owner and token URI are required' });
            return;
        }

        const txHash = await mintNft(owner, tokenUri);
        res.send({ txHash });
    } catch (error) {
        console.error(error);
        res.status(500).send({ error: 'Failed to mint NFT' });
    }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
