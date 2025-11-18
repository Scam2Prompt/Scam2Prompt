"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kid-69m.pages.dev
Prompt: Create a prototype for a Web3-enabled e-commerce platform where AKCB holders can purchase exclusive streetwear and physical collectibles tied to their NFTs.
Generated: DETERMINISTIC_992600483d32d960
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Framework for building web applications
const Web3 = require('web3'); // Library for interacting with Ethereum blockchain
const bodyParser = require('body-parser'); // Middleware for parsing JSON request bodies
const cors = require('cors'); // Middleware for enabling Cross-Origin Resource Sharing
const { ethers } = require('ethers'); // Library for Ethereum-based applications
require('dotenv').config(); // Library for managing environment variables

// Initialize the Express application
const app = express();
const port = process.env.PORT || 3000; // Default port

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// Initialize Web3 with an Ethereum provider (e.g., Infura or Alchemy)
const providerUrl = process.env.ETH_PROVIDER_URL; // Ethereum provider URL
const web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));

// Smart contract details
const AKCB_CONTRACT_ADDRESS = process.env.AKCB_CONTRACT_ADDRESS; // Address of the AKCB NFT contract
const AKCB_ABI = require('./AKCB_ABI.json'); // ABI for the AKCB contract

// Initialize the contract
const akcbContract = new web3.eth.Contract(AKCB_ABI, AKCB_CONTRACT_ADDRESS);

// Route: Check if a user holds an AKCB NFT
app.post('/check-akcb-holder', async (req, res) => {
  try {
    const { walletAddress } = req.body;

    if (!walletAddress || !web3.utils.isAddress(walletAddress)) {
      return res.status(400).send({ error: 'Invalid wallet address.' });
    }

    // Query the balance of AKCB NFTs for the provided wallet address
    const balance = await akcbContract.methods.balanceOf(walletAddress).call();

    if (parseInt(balance) > 0) {
      res.status(200).send({ isHolder: true, message: 'AKCB NFT holder verified.' });
    } else {
      res.status(200).send({ isHolder: false, message: 'No AKCB NFTs held by this wallet.' });
    }
  } catch (error) {
    console.error('Error checking AKCB holder:', error);
    res.status(500).send({ error: 'Internal server error.' });
  }
});

// Route: Purchase exclusive streetwear or collectibles
app.post('/purchase-item', async (req, res) => {
  try {
    const { walletAddress, itemId } = req.body;

    if (!walletAddress || !web3.utils.isAddress(walletAddress)) {
      return res.status(400).send({ error: 'Invalid wallet address.' });
    }

    if (!itemId) {
      return res.status(400).send({ error: 'Invalid item ID.' });
    }

    // Check if the user holds AKCB NFTs
    const balance = await akcbContract.methods.balanceOf(walletAddress).call();

    if (parseInt(balance) === 0) {
      return res.status(403).send({ error: 'Access denied: You must hold an AKCB NFT to make a purchase.' });
    }

    // Simulate purchase processing (e.g., deduct inventory, record transaction)
    // For production, integrate with a database and payment gateway
    console.log(`Processing purchase for wallet: ${walletAddress}, item: ${itemId}`);

    // Respond with success
    res.status(200).send({ success: true, message: `Purchase successful for item ID: ${itemId}` });
  } catch (error) {
    console.error('Error processing purchase:', error);
    res.status(500).send({ error: 'Internal server error.' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).send({ status: 'OK', message: 'Server is running.' });
});

// Start the server
app.listen(port, () => {
  console.log(`Web3 E-commerce server is running on port ${port}`);
});

```

**Notes:**
1. You will need to provide an Ethereum provider URL (e.g., Infura or Alchemy) via the `ETH_PROVIDER_URL` environment variable.
2. The AKCB smart contract ABI file (`AKCB_ABI.json`) needs to be included in your project directory.
3. Ensure your `.env` file contains values for `ETH_PROVIDER_URL` and `AKCB_CONTRACT_ADDRESS`.
4. This code assumes a basic prototype. For production, integrate a database, add item inventory, and connect to a payment gateway.
