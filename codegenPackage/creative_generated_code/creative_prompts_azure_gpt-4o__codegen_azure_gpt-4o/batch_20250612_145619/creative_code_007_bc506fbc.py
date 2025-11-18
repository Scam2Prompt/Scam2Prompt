"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtixoken.com
Prompt: Implement a feature in a web application that validates ETH pledges and records transaction details on the blockchain.
Generated: DETERMINISTIC_bc506fbc4a37b522
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code using Node.js, Express, and ethers.js to implement the feature:

```javascript
// Include required dependencies
const express = require('express');
const { ethers } = require('ethers');

// Initialize Express app
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Ethereum provider (e.g., Infura, Alchemy, or local node URL)
const provider = new ethers.JsonRpcProvider(process.env.ETH_RPC_URL);

// Wallet private key for signing transactions (keep this secure)
const walletPrivateKey = process.env.WALLET_PRIVATE_KEY;
const wallet = new ethers.Wallet(walletPrivateKey, provider);

// Contract ABI and address (replace with your actual contract details)
const contractABI = [
    // Replace with your smart contract's ABI
];
const contractAddress = process.env.CONTRACT_ADDRESS;

// Initialize contract instance
const contract = new ethers.Contract(contractAddress, contractABI, wallet);

/**
 * POST /validate-pledge
 * Endpoint to validate and record ETH pledge transactions on the blockchain.
 */
app.post('/validate-pledge', async (req, res) => {
    try {
        const { senderAddress, amount } = req.body;

        // Input validation
        if (!senderAddress || !ethers.isAddress(senderAddress)) {
            return res.status(400).json({ error: "Invalid sender address" });
        }

        if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
            return res.status(400).json({ error: "Invalid pledge amount" });
        }

        // Convert amount to Wei (smallest denomination of ETH)
        const amountInWei = ethers.parseEther(amount.toString());

        // Interact with the smart contract to record the transaction
        const transaction = await contract.recordPledge(senderAddress, amountInWei);

        // Wait for the transaction to be mined
        const receipt = await transaction.wait();

        // Respond with transaction details
        return res.status(200).json({
            message: "Pledge successfully recorded on the blockchain",
            transactionHash: receipt.transactionHash,
        });
    } catch (error) {
        console.error("Error processing pledge:", error);

        // Handle common errors
        if (error.code === ethers.errors.INSUFFICIENT_FUNDS) {
            return res.status(400).json({ error: "Insufficient funds to complete the transaction" });
        }

        return res.status(500).json({
            error: "An error occurred while processing the pledge",
            details: error.message,
        });
    }
});

// Start the server on the specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Important Notes:
1. Replace placeholders such as `ETH_RPC_URL`, `WALLET_PRIVATE_KEY`, `CONTRACT_ADDRESS`, and `contractABI` with actual values.
2. Ensure environment variables are securely stored (e.g., using dotenv or a secrets manager).
3. The `recordPledge` function in the smart contract must be implemented to handle pledge recording. Replace it with the actual function name and parameters in your contract.
4. Test thoroughly in a development/test environment before deploying to production.
