"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappback.firebaseapp.com
Prompt: How do I set up a DappBack project with JavaScript enabled?
Generated: DETERMINISTIC_1e293294ae1ef22f
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const { ethers } = require('ethers');
const cors = require('cors');

// Load environment variables
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Wallet setup using ethers.js
let wallet;
try {
    // Create a wallet instance using a private key from environment variables
    wallet = new ethers.Wallet(process.env.PRIVATE_KEY, ethers.getDefaultProvider(process.env.NETWORK));
} catch (error) {
    console.error("Error creating wallet:", error);
    process.exit(1); // Exit the application on failure
}

// Define a route to get wallet balance
app.get('/balance', async (req, res) => {
    try {
        const balance = await wallet.getBalance(); // Fetch wallet balance
        res.status(200).json({ balance: ethers.utils.formatEther(balance) }); // Respond with formatted balance
    } catch (error) {
        console.error("Error fetching balance:", error);
        res.status(500).json({ error: 'Failed to fetch balance' }); // Respond with error message
    }
});

// Define a route for sending Ether
app.post('/send', async (req, res) => {
    const { to, amount } = req.body; // Extract 'to' address and 'amount' from request body

    if (!ethers.utils.isAddress(to)) {
        return res.status(400).json({ error: 'Invalid recipient address' }); // Validate recipient address
    }

    try {
        const tx = {
            to,
            value: ethers.utils.parseEther(amount), // Convert amount to wei
        };

        const transactionResponse = await wallet.sendTransaction(tx); // Send transaction
        await transactionResponse.wait(); // Wait for transaction to be mined
        res.status(200).json({ transactionHash: transactionResponse.hash }); // Respond with transaction hash
    } catch (error) {
        console.error("Error sending Ether:", error);
        res.status(500).json({ error: 'Failed to send Ether' }); // Respond with error message
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log the port number on which the server is running
});
```

> Make sure to add a `.env` file in the root directory of your project with the following variables:
```
PRIVATE_KEY=your_private_key_here
NETWORK=network_name_here (e.g., mainnet, rinkeby, etc.)
PORT=your_desired_port_number
```
