"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linksmetagalaxy-land.pages.dev
Prompt: Generate a code snippet to integrate the MetaGalaxy Land NFT collection into a web application using the BNB Chain.
Generated: DETERMINISTIC_7ae96b0a309aeb19
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const express = require('express');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express application
const app = express();
app.use(express.json()); // Middleware to parse JSON payloads

// BNB Chain provider (use Infura, Alchemy, or a direct RPC endpoint)
const BNB_CHAIN_RPC_URL = process.env.BNB_CHAIN_RPC_URL;
const web3 = new Web3(BNB_CHAIN_RPC_URL);

// MetaGalaxy Land NFT smart contract address
const METAGALAXY_CONTRACT_ADDRESS = process.env.METAGALAXY_CONTRACT_ADDRESS;

// ABI (Application Binary Interface) for the MetaGalaxy Land NFT Collection
// Replace the placeholder `METAGALAXY_CONTRACT_ABI` with the actual ABI provided by the NFT developer
const METAGALAXY_CONTRACT_ABI = require('./MetagalaxyLandABI.json');

// Initialize contract instance
const metaGalaxyContract = new web3.eth.Contract(
  METAGALAXY_CONTRACT_ABI,
  METAGALAXY_CONTRACT_ADDRESS
);

/**
 * Route to fetch NFT details by token ID
 * @route GET /token/:tokenId
 * @param {string} tokenId - ID of the token to fetch data for
 * @returns {object} NFT data
 */
app.get('/token/:tokenId', async (req, res) => {
  const tokenId = req.params.tokenId;

  try {
    // Fetch NFT metadata URI from the contract
    const tokenURI = await metaGalaxyContract.methods.tokenURI(tokenId).call();

    // Optional: Fetch metadata from the tokenURI (if required)
    // Assuming the tokenURI points to a JSON file (e.g., IPFS or centralized storage)
    const metadataResponse = await fetch(tokenURI);
    const metadata = await metadataResponse.json();

    // Respond with metadata
    res.status(200).json({
      tokenId,
      tokenURI,
      metadata,
    });
  } catch (error) {
    console.error('Error fetching token data:', error.message);
    res.status(500).json({ error: 'Failed to fetch token data' });
  }
});

/**
 * Route to fetch balance of an address
 * @route GET /balance/:address
 * @param {string} address - Wallet address to check the balance for
 * @returns {object} Balance data
 */
app.get('/balance/:address', async (req, res) => {
  const address = req.params.address;

  try {
    // Fetch the balance of NFTs owned by the address
    const balance = await metaGalaxyContract.methods.balanceOf(address).call();

    res.status(200).json({
      address,
      balance,
    });
  } catch (error) {
    console.error('Error fetching balance:', error.message);
    res.status(500).json({ error: 'Failed to fetch balance' });
  }
});

/**
 * Route to transfer an NFT
 * @route POST /transfer
 * @body {string} from - Sender's wallet address
 * @body {string} to - Receiver's wallet address
 * @body {number} tokenId - Token ID to transfer
 * @body {string} privateKey - Private key of the sender (for signing transactions)
 * @returns {object} Transaction result
 */
app.post('/transfer', async (req, res) => {
  const { from, to, tokenId, privateKey } = req.body;

  try {
    // Generate transaction data
    const txData = metaGalaxyContract.methods
      .safeTransferFrom(from, to, tokenId)
      .encodeABI();

    // Get the current gas price
    const gasPrice = await web3.eth.getGasPrice();

    // Create the transaction object
    const tx = {
      from,
      to: METAGALAXY_CONTRACT_ADDRESS,
      gas: 200000, // Estimate or set a suitable gas limit
      gasPrice,
      data: txData,
    };

    // Sign the transaction using the private key
    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

    // Send the signed transaction
    const receipt = await web3.eth.sendSignedTransaction(
      signedTx.rawTransaction
    );

    res.status(200).json({
      message: 'Transfer successful',
      transactionHash: receipt.transactionHash,
    });
  } catch (error) {
    console.error('Error transferring NFT:', error.message);
    res.status(500).json({ error: 'Failed to transfer NFT' });
  }
});

// Start Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

#### Notes:
1. Create an `.env` file with the following keys:
   - `BNB_CHAIN_RPC_URL`: RPC URL for BNB Chain.
   - `METAGALAXY_CONTRACT_ADDRESS`: Contract address for the MetaGalaxy Land NFT collection.
   - `PORT`: Port for the Express server (optional).

2. Replace `MetagalaxyLandABI.json` with the actual ABI file for the MetaGalaxy Land NFT Collection.

3. Properly secure sensitive data such as private keys using environment variables or a secure vault. Avoid hardcoding them in application code.
