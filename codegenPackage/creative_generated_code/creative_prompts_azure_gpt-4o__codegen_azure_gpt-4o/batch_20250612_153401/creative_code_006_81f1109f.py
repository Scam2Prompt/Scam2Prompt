"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playgorund.pages.dev
Prompt: Provide code to integrate a blockchain-based reward system into a web app, similar to the $BEYOND earning and claiming process described on the Beyond Blitz site.
Generated: DETERMINISTIC_81f1109fc5570932
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of clean, production-ready code for integrating a blockchain-based reward system into a web app. For this example, I'm using JavaScript with Node.js, Express.js, and Web3.js (assuming an Ethereum-based blockchain). This code snippet focuses on the earning and claiming process for the blockchain reward system.

```javascript
// Import required modules
const express = require('express');
const Web3 = require('web3');
require('dotenv').config(); // Load environment variables from .env file

// Initialize the Express app
const app = express();
app.use(express.json()); // Middleware to parse JSON requests

// Configure Web3 and blockchain details
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.BLOCKCHAIN_PROVIDER));
const contractABI = require('./contractABI.json'); // ABI of the reward contract
const contractAddress = process.env.CONTRACT_ADDRESS;
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Middleware for error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send({ error: 'An internal error occurred.' });
});

// Endpoint: Earn rewards
app.post('/earn', async (req, res) => {
  try {
    const { userAddress, rewardAmount } = req.body;

    // Validate input
    if (!web3.utils.isAddress(userAddress)) {
      return res.status(400).send({ error: 'Invalid Ethereum address provided.' });
    }
    if (rewardAmount <= 0) {
      return res.status(400).send({ error: 'Reward amount must be positive.' });
    }

    // Simulate reward earning process (typically recorded on the blockchain)
    // In a real use case, this might involve updating a database or triggering blockchain transactions
    const tx = await contract.methods.earnRewards(userAddress, rewardAmount).send({
      from: process.env.OWNER_ADDRESS, // Admin account or smart contract owner
      gas: 3000000,
    });

    res.status(200).send({ message: 'Reward earned successfully!', transactionHash: tx.transactionHash });
  } catch (error) {
    console.error('Error earning rewards:', error);
    res.status(500).send({ error: 'Failed to process reward earning.' });
  }
});

// Endpoint: Claim rewards
app.post('/claim', async (req, res) => {
  try {
    const { userAddress } = req.body;

    // Validate input
    if (!web3.utils.isAddress(userAddress)) {
      return res.status(400).send({ error: 'Invalid Ethereum address provided.' });
    }

    // Simulate reward claim process (typically involves blockchain transactions)
    const tx = await contract.methods.claimRewards(userAddress).send({
      from: userAddress,
      gas: 3000000,
    });

    res.status(200).send({ message: 'Reward claimed successfully!', transactionHash: tx.transactionHash });
  } catch (error) {
    console.error('Error claiming rewards:', error);
    res.status(500).send({ error: 'Failed to process reward claiming.' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Reward system server running on port ${PORT}`);
});

/*
Environment variables required in `.env` file:
BLOCKCHAIN_PROVIDER=<Your blockchain provider URL>
CONTRACT_ADDRESS=<Your deployed smart contract address>
OWNER_ADDRESS=<Admin Ethereum address for earning rewards>
PORT=<Port to run the server>
*/

// Note: Ensure you deploy a smart contract with `earnRewards` and `claimRewards` methods.
```

This code is a starting point for integrating blockchain-based rewards into a web application. It uses endpoints for earning and claiming rewards, interacts with a blockchain smart contract, and includes proper validation and error handling.
