"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-ten.vercel.app
Prompt: Provide an example of how to integrate Linea's zk rollup infrastructure into a gaming dapp to enable on-chain in-game commerce while maintaining high speed and user experience.
Generated: DETERMINISTIC_e57ade77fd29490e
Batch ID: 20250612_154913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.linea.network": {
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
import { ethers } from "ethers";
import { zkRollupClient } from "linea-zk-rollup"; // Hypothetical zk rollup client
import express from 'express';
import bodyParser from 'body-parser';

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Configuration for the zk rollup client
const zkRollupConfig = {
    rpcUrl: "https://rpc.linea.network", // RPC URL for Linea zk rollup
    contractAddress: "0xYourContractAddress", // Replace with your contract address
};

// Initialize the zk rollup client
const client = new zkRollupClient(zkRollupConfig);

// Function to handle in-game purchases
async function handleInGamePurchase(userAddress, itemId, amount) {
    try {
        // Validate input
        if (!ethers.utils.isAddress(userAddress)) {
            throw new Error("Invalid user address");
        }
        if (amount <= 0) {
            throw new Error("Amount must be greater than 0");
        }

        // Create transaction for the purchase
        const transaction = await client.createTransaction({
            from: userAddress,
            to: zkRollupConfig.contractAddress,
            data: client.encodePurchaseData(itemId, amount),
            value: ethers.utils.parseEther("0.01"), // Example value for gas fees
        });

        // Send the transaction
        const receipt = await client.sendTransaction(transaction);

        // Wait for transaction confirmation
        await client.waitForConfirmation(receipt.transactionHash);

        return {
            success: true,
            transactionHash: receipt.transactionHash,
            message: "Purchase successful",
        };
    } catch (error) {
        console.error("Error handling in-game purchase:", error);
        return {
            success: false,
            message: error.message,
        };
    }
}

// API endpoint for in-game purchases
app.post('/api/purchase', async (req, res) => {
    const { userAddress, itemId, amount } = req.body;

    // Call the purchase handler
    const result = await handleInGamePurchase(userAddress, itemId, amount);

    // Send response back to client
    res.status(result.success ? 200 : 400).json(result);
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- This code is a simplified example of how to integrate Linea's zk rollup infrastructure into a gaming DApp for in-game commerce.
- Ensure you have the necessary libraries installed and replace placeholders like `0xYourContractAddress` and the RPC URL with real values as necessary.
- Additional security measures and validation checks may be needed based on the specific requirements of your application.
