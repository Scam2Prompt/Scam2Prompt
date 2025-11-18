"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hmhgbg.pages.dev
Prompt: Generate code to integrate Nakamigos-CLOAKS assets into a decentralized application (dApp) with support for worldwide gaming rights.
Generated: DETERMINISTIC_faf82929370ef5e2
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and dependencies
const express = require('express'); // Server framework
const Web3 = require('web3'); // Ethereum Web3 library
const bodyParser = require('body-parser'); // For parsing JSON requests
const dotenv = require('dotenv'); // For environment variable management
const fs = require('fs'); // For file system interactions

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(bodyParser.json()); // Middleware to parse JSON requests

// Initialize Web3 with the provider from the environment variables
const web3 = new Web3(process.env.BLOCKCHAIN_PROVIDER);

// Load ABI and contract details for Nakamigos-CLOAKS
const CONTRACT_ABI = JSON.parse(fs.readFileSync('./NakamigosCloaksABI.json', 'utf-8'));
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;

// Create a contract instance
const cloaksContract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

// Middleware to validate incoming requests
function validateRequest(req, res, next) {
  if (!req.body.walletAddress) {
    return res.status(400).json({ error: 'Missing walletAddress in request body' });
  }
  next();
}

// Route: Get asset details for a given wallet address
app.post('/getAssets', validateRequest, async (req, res) => {
  try {
    const { walletAddress } = req.body;

    // Validate wallet address
    if (!web3.utils.isAddress(walletAddress)) {
      return res.status(400).json({ error: 'Invalid wallet address' });
    }

    // Interact with the smart contract to fetch owned assets
    const ownedAssets = await cloaksContract.methods.getOwnedAssets(walletAddress).call();
    res.status(200).json({ walletAddress, ownedAssets });
  } catch (error) {
    console.error('Error fetching assets:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Set worldwide gaming rights for an asset
app.post('/setGamingRights', validateRequest, async (req, res) => {
  try {
    const { walletAddress, assetId, enableGamingRights } = req.body;

    // Validate input
    if (!assetId || typeof enableGamingRights !== 'boolean') {
      return res.status(400).json({ error: 'Missing or invalid assetId or enableGamingRights' });
    }

    // Execute transaction to enable/disable gaming rights
    const tx = cloaksContract.methods.setGamingRights(assetId, enableGamingRights);
    const gas = await tx.estimateGas({ from: walletAddress });
    const txData = tx.encodeABI();

    const signedTx = await web3.eth.accounts.signTransaction(
      {
        to: CONTRACT_ADDRESS,
        data: txData,
        gas,
      },
      process.env.PRIVATE_KEY
    );

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    res.status(200).json({ message: 'Gaming rights updated successfully', receipt });
  } catch (error) {
    console.error('Error updating gaming rights:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Notes:
// 1. Ensure that `NakamigosCloaksABI.json` and `.env` files are present in the project root.
// 2. The `.env` file should contain BLOCKCHAIN_PROVIDER, CONTRACT_ADDRESS, PRIVATE_KEY, and optionally PORT.
```
