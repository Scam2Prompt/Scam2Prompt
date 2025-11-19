"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liquidlauncher.app
Prompt: Create a web3 application that incorporates elements mentioned in "Navigating the Digital Landscape: How Technology Shapes Our Lives" from LiquidLauncher.
Generated: DETERMINISTIC_c0263d6bab56dc25
Batch ID: 20250612_162913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import necessary modules
const Web3 = require('web3'); // Web3 library for interacting with Ethereum blockchain
const express = require('express'); // Express for server-side logic
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests

// Initialize the web3 instance
const web3 = new Web3("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"); // Connect to Ethereum mainnet via Infura

// Initialize the Express app
const app = express();
app.use(bodyParser.json()); // Middleware to handle JSON requests

// Environment variables (ensure these are set in production securely)
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Ethereum account private key
const PUBLIC_KEY = process.env.PUBLIC_KEY; // Ethereum account public key

// Smart contract interaction (example: ERC-20 token)
const TOKEN_ADDRESS = '0xYourTokenAddressHere'; // Replace with actual contract address
const TOKEN_ABI = [/* Provide your token's ABI here */];
const tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_ADDRESS);

// Route: Fetch account balance
app.get('/balance', async (req, res) => {
  try {
    // Fetch the balance of the user's public address
    const balance = await tokenContract.methods.balanceOf(PUBLIC_KEY).call();
    res.status(200).json({ balance });
  } catch (error) {
    console.error("Error fetching balance:", error);
    res.status(500).json({ error: "Unable to fetch balance." });
  }
});

// Route: Transfer tokens
app.post('/transfer', async (req, res) => {
  const { toAddress, amount } = req.body;

  if (!web3.utils.isAddress(toAddress)) {
    return res.status(400).json({ error: "Invalid recipient address." });
  }

  try {
    // Create transaction for token transfer
    const tx = tokenContract.methods.transfer(toAddress, web3.utils.toWei(amount.toString(), 'ether'));
    const gas = await tx.estimateGas({ from: PUBLIC_KEY });
    const gasPrice = await web3.eth.getGasPrice();
    const data = tx.encodeABI();
    const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY);

    const signedTx = await web3.eth.accounts.signTransaction(
      {
        to: TOKEN_ADDRESS,
        data,
        gas,
        gasPrice,
        nonce,
        chainId: 1, // Mainnet chain ID
      },
      PRIVATE_KEY
    );

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    res.status(200).json({ receipt });
  } catch (error) {
    console.error("Error transferring tokens:", error);
    res.status(500).json({ error: "Token transfer failed." });
  }
});

// Route: Get latest block info
app.get('/latest-block', async (req, res) => {
  try {
    const block = await web3.eth.getBlock('latest');
    res.status(200).json(block);
  } catch (error) {
    console.error("Error fetching latest block:", error);
    res.status(500).json({ error: "Unable to fetch latest block information." });
  }
});

// Health check route
app.get('/health', (req, res) => {
  res.status(200).json({ status: "Healthy" });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
Key Notes:
1. Replace `YOUR_INFURA_PROJECT_ID`, `PRIVATE_KEY`, `PUBLIC_KEY`, `0xYourTokenAddressHere`,
   and `TOKEN_ABI` with your actual credentials and contract details.
2. Ensure environment variables are securely managed in production.
3. This application provides basic web3 functions: balance check, token transfer, and block info retrieval.
4. Error handling is implemented for robustness.
5. Follow production standards, such as enabling HTTPS, rate limiting, and logging in production systems.
*/
```
