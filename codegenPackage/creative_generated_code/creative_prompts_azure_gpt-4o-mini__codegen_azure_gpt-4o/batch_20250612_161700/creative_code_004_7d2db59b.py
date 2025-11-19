"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Draft a sample API endpoint in Node.js that allows users to check their SHROOM token balance after participating in the presale.
Generated: DETERMINISTIC_7d2db59b6ea9ed3a
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const Web3 = require('web3');

// Create an instance of express
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Environment variables (ensure you set these securely in your environment)
const INFURA_URL = process.env.INFURA_URL; // Infura or any Ethereum RPC URL
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS; // SHROOM token smart contract
const ABI = JSON.parse(process.env.CONTRACT_ABI); // ABI of the SHROOM token smart contract

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Create an instance of the token contract
const tokenContract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

/**
 * GET /api/v1/balance/:address
 * Endpoint to check SHROOM token balance for a given Ethereum address
 *
 * Path Params:
 * - address: Ethereum wallet address of the user
 *
 * Response:
 * - 200: { balance: "1000" }
 * - 400: { error: "Invalid Ethereum address provided." }
 * - 500: { error: "An error occurred while fetching the balance." }
 */
app.get('/api/v1/balance/:address', async (req, res) => {
  const userAddress = req.params.address;

  try {
    // Validate Ethereum address
    if (!web3.utils.isAddress(userAddress)) {
      return res.status(400).json({ error: 'Invalid Ethereum address provided.' });
    }

    // Fetch token balance
    const balance = await tokenContract.methods.balanceOf(userAddress).call();

    // Return balance as a response
    return res.status(200).json({ balance });
  } catch (error) {
    console.error('Error fetching token balance:', error.message);
    return res.status(500).json({ error: 'An error occurred while fetching the balance.' });
  }
});

// Start the server on the specified port (default to 3000)
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Note: To run this code, make sure you have the required environment variables set up:
// - INFURA_URL: The URL for your Ethereum node or Infura endpoint.
// - CONTRACT_ADDRESS: The deployed SHROOM token's smart contract address.
// - CONTRACT_ABI: The ABI of the SHROOM token contract.
// - PORT: (Optional) The port number to run the server.
```
