"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-etuktuk-io.pages.dev
Prompt: Generate code for a Node.js backend service to facilitate presale participation of $TUK tokens, including wallet connection and transaction validation.
Generated: DETERMINISTIC_b089ec25466b3650
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const Web3 = require('web3');
const dotenv = require('dotenv');

// Load environment variables from a .env file
dotenv.config();

// Initialize app and middleware
const app = express();
app.use(bodyParser.json());

// Set up Web3 instance with an Ethereum provider
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.ETH_PROVIDER));

// Define presale contract details
const presaleContractAddress = process.env.PRESALE_CONTRACT_ADDRESS;
const presaleABI = JSON.parse(process.env.PRESALE_CONTRACT_ABI);
const presaleContract = new web3.eth.Contract(presaleABI, presaleContractAddress);

// Endpoint: Connect wallet
app.post('/connect-wallet', async (req, res) => {
  try {
    const { walletAddress } = req.body;

    // Validate wallet address format
    if (!web3.utils.isAddress(walletAddress)) {
      return res.status(400).json({ error: 'Invalid wallet address' });
    }

    // Return success response
    res.status(200).json({ message: 'Wallet connected successfully', walletAddress });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error connecting wallet:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint: Participate in presale
app.post('/participate', async (req, res) => {
  try {
    const { walletAddress, amount } = req.body;

    // Validate wallet address format
    if (!web3.utils.isAddress(walletAddress)) {
      return res.status(400).json({ error: 'Invalid wallet address' });
    }

    // Validate token amount
    if (!Number(amount) || amount <= 0) {
      return res.status(400).json({ error: 'Invalid token amount' });
    }

    // Check if wallet has enough ETH for the transaction
    const balance = await web3.eth.getBalance(walletAddress);
    if (web3.utils.toBN(balance).lt(web3.utils.toBN(web3.utils.toWei(amount.toString(), 'ether')))) {
      return res.status(400).json({ error: 'Insufficient balance' });
    }

    // Simulate a transaction to validate its execution (replace with actual transaction logic)
    const gasEstimate = await presaleContract.methods
      .participate(walletAddress, web3.utils.toWei(amount.toString(), 'ether'))
      .estimateGas({ from: walletAddress });

    res.status(200).json({
      message: 'Transaction validated successfully',
      gasEstimate,
    });
  } catch (error) {
    // Handle errors (e.g., smart contract call failures)
    console.error('Error participating in presale:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// 404 fallback for undefined routes
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Notes:
- Install dependencies: `npm install express body-parser web3 dotenv`
- Create a `.env` file with the following keys: `ETH_PROVIDER`, `PRESALE_CONTRACT_ADDRESS`, `PRESALE_CONTRACT_ABI`, and `PORT`.
