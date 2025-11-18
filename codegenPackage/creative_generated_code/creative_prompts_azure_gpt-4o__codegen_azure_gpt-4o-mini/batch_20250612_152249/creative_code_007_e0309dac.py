"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: Write a tutorial-style script for building a web3 gaming dapp on Linea, leveraging its rapid transaction capabilities and low gas fees.
Generated: DETERMINISTIC_e0309dacb96e50e7
Batch ID: 20250612_152249
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://linea.endpoint.url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
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
// Import necessary libraries and frameworks
const express = require('express'); // Web framework for Node.js
const { ethers } = require('ethers'); // Ethereum library for interacting with the Ethereum blockchain
const cors = require('cors'); // Middleware for enabling CORS
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// Setup provider for Linea network
const LINEA_RPC_URL = 'https://linea.endpoint.url'; // Replace with actual Linea RPC URL
const provider = new ethers.providers.JsonRpcProvider(LINEA_RPC_URL);

// Smart contract ABI and address
const contractABI = [ /* Your Contract ABI Here */ ];
const contractAddress = '0xYourContractAddressHere'; // Replace with actual contract address
const contract = new ethers.Contract(contractAddress, contractABI, provider);

// Endpoint to retrieve game data
app.get('/api/game-data', async (req, res) => {
    try {
        const gameData = await contract.getGameData(); // Replace with actual function call
        res.status(200).json(gameData);
    } catch (error) {
        console.error('Error fetching game data:', error);
        res.status(500).json({ error: 'Failed to fetch game data' });
    }
});

// Endpoint for user actions (e.g., make a move in the game)
app.post('/api/user-action', async (req, res) => {
    const { userAction } = req.body; // Expecting action data in the request body

    // Basic validation
    if (!userAction) {
        return res.status(400).json({ error: 'User action is required' });
    }

    try {
        // Create a wallet instance (replace with user's wallet later)
        const wallet = ethers.Wallet.fromMnemonic('your mnemonic here'); // Use secure storage for production
        const connectedContract = contract.connect(wallet);

        // Send user action to the smart contract
        const tx = await connectedContract.performAction(userAction); // Replace with actual function
        await tx.wait(); // Wait for transaction confirmation

        res.status(200).json({ message: 'Action performed successfully', transactionHash: tx.hash });
    } catch (error) {
        console.error('Error performing user action:', error);
        res.status(500).json({ error: 'Failed to perform user action' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Export the app for testing (if needed)
module.exports = app;
```

In this script, ensure to replace placeholders with actual Linea RPC URL, contract ABI, and contract address. Update wallet management according to your application's authentication strategy.
