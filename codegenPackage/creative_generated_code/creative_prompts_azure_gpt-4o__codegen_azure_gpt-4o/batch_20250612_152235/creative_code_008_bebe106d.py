"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-octa.pages.dev
Prompt: Generate a backend API in Node.js that validates wallet ownership and triggers the claiming process for the OctaSpace $OCTA token airdrop.
Generated: DETERMINISTIC_bebe106d830461c5
Batch ID: 20250612_152235
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
const { ethers } = require('ethers'); // For wallet validation and airdrop logic
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());

// Simulated database for wallet and airdrop data
const walletDatabase = {
  '0x1234567890123456789012345678901234567890': {
    hasClaimed: false,
  },
  // Add other wallets as needed
};

// Airdrop contract configuration (replace with actual values in production)
const AIRDROP_CONTRACT_ADDRESS = process.env.AIRDROP_CONTRACT_ADDRESS;
const AIRDROP_PRIVATE_KEY = process.env.AIRDROP_PRIVATE_KEY;

// Initialize ethers provider and signer (use Alchemy/Infura or other service provider in production)
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
const signer = new ethers.Wallet(AIRDROP_PRIVATE_KEY, provider);

// POST endpoint to validate wallet ownership and trigger $OCTA token claim
app.post('/api/claim-airdrop', async (req, res) => {
  try {
    const { walletAddress, signature } = req.body;

    // Input validation
    if (!walletAddress || !signature) {
      return res.status(400).json({ error: 'Missing walletAddress or signature.' });
    }

    // Verify wallet ownership
    const message = `Verify ownership for $OCTA airdrop`;
    const recoveredAddress = ethers.utils.verifyMessage(message, signature);

    if (recoveredAddress.toLowerCase() !== walletAddress.toLowerCase()) {
      return res.status(401).json({ error: 'Wallet ownership validation failed.' });
    }

    // Check if wallet is eligible and has not already claimed
    const walletData = walletDatabase[walletAddress.toLowerCase()];
    if (!walletData) {
      return res.status(404).json({ error: 'Wallet not found or not eligible for airdrop.' });
    }
    if (walletData.hasClaimed) {
      return res.status(400).json({ error: 'Airdrop already claimed for this wallet.' });
    }

    // Interact with the airdrop smart contract to trigger the claim
    const airdropContract = new ethers.Contract(
      AIRDROP_CONTRACT_ADDRESS,
      ['function claimTokens(address recipient) public'], // Replace with actual ABI
      signer
    );

    const tx = await airdropContract.claimTokens(walletAddress);
    await tx.wait(); // Wait for transaction to be mined

    // Update the database to mark the wallet as claimed
    walletDatabase[walletAddress.toLowerCase()].hasClaimed = true;

    return res.status(200).json({
      message: 'Airdrop successfully claimed.',
      transactionHash: tx.hash,
    });
  } catch (error) {
    console.error('Error processing airdrop claim:', error);
    return res.status(500).json({ error: 'Internal server error. Please try again later.' });
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'API is running' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Airdrop API server is running on port ${PORT}`);
});
```

**Note:** Replace placeholder values (`RPC_URL`, `AIRDROP_CONTRACT_ADDRESS`, `AIRDROP_PRIVATE_KEY`, etc.) with actual configuration values in your `.env` file for production use.
