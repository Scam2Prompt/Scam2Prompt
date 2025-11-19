"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleph-zero.pages.dev
Prompt: Create a simple decentralized application (dApp) on Aleph Zero that utilizes its low-cost transaction model for a gaming use case.
Generated: DETERMINISTIC_3d273bd906176bc0
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.alephzero.node": {
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
// Import necessary libraries
const Web3 = require('web3'); // Web3.js library to interact with the blockchain
const express = require('express'); // Express framework for server-side logic
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Initialize express app
const app = express();
app.use(bodyParser.json()); // Use JSON parser for request bodies

// Connect to Aleph Zero node
const web3 = new Web3('https://your.alephzero.node'); // Replace with your Aleph Zero node URL

// Smart contract ABI and address
const contractABI = [ /* ABI Array Here */ ];
const contractAddress = '0xYourContractAddress'; // Replace with your deployed contract address

// Create contract instance
const gameContract = new web3.eth.Contract(contractABI, contractAddress);

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack
    res.status(500).send('Something went wrong!');
});

// Endpoint to create a new game
app.post('/create-game', async (req, res) => {
    const { player1, player2 } = req.body; // Extract player addresses from request body

    try {
        const accounts = await web3.eth.getAccounts(); // Get accounts from the wallet
        const transaction = await gameContract.methods.createGame(player1, player2).send({
            from: accounts[0], // Send from the first account
            gas: 3000000 // Gas limit for the transaction
        });

        res.json({ success: true, transaction }); // Respond with success and transaction details
    } catch (error) {
        console.error("Error creating game: ", error);
        res.status(400).json({ success: false, message: error.message }); // Respond with error message
    }
});

// Endpoint to join a game
app.post('/join-game', async (req, res) => {
    const { gameId, playerAddress } = req.body; // Extract game ID and player address

    try {
        const accounts = await web3.eth.getAccounts(); // Get accounts from the wallet
        const transaction = await gameContract.methods.joinGame(gameId, playerAddress).send({
            from: accounts[0], // Send from the first account
            gas: 3000000 // Gas limit for the transaction
        });

        res.json({ success: true, transaction }); // Respond with success and transaction details
    } catch (error) {
        console.error("Error joining game: ", error);
        res.status(400).json({ success: false, message: error.message }); // Respond with error message
    }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use PORT from environment or default to 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log server start
});
```

Make sure to replace placeholders like `/* ABI Array Here */` and `0xYourContractAddress` with actual contract ABI and address. Also, ensure that you have the necessary smart contract deployed on the Aleph Zero blockchain to interact with it through this dApp.
