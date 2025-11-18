"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-modal-hedera-dapp.vercel.app
Prompt: Suggest tools or frameworks for developing a multi-modal Hedera dApp that supports staking rewards and requires JavaScript functionality.
Generated: DETERMINISTIC_110afad64fcf4aa9
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { Client, PrivateKey, AccountId, Hbar } = require("@hashgraph/sdk");
const express = require("express");
const bodyParser = require("body-parser");

// Initialize Hedera client
const client = Client.forTestnet(); // Use Client.forMainnet() for production
const operatorId = AccountId.fromString("YOUR_ACCOUNT_ID"); // Replace with your account ID
const operatorKey = PrivateKey.fromString("YOUR_PRIVATE_KEY"); // Replace with your private key
client.setOperator(operatorId, operatorKey);

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Route for staking rewards
app.post("/stake", async (req, res) => {
    const { amount, stakingAccountId } = req.body;

    // Basic input validation
    if (!amount || !stakingAccountId) {
        return res.status(400).json({ error: "Amount and stakingAccountId are required." });
    }

    try {
        // Stake HBAR
        const transaction = await new TransferTransaction()
            .addHbarTransfer(operatorId, Hbar.fromTinybars(-amount)) // Deduct from operator
            .addHbarTransfer(stakingAccountId, Hbar.fromTinybars(amount)) // Add to staking account
            .execute(client);

        // Wait for transaction receipt
        const receipt = await transaction.getReceipt(client);

        // Check if transaction was successful
        if (receipt.status !== Status.Success) {
            throw new Error(`Transaction failed: ${receipt.status}`);
        }

        res.status(200).json({ message: "Staking successful", transactionId: transaction.transactionId });
    } catch (error) {
        console.error("Error while staking:", error);
        res.status(500).json({ error: "An error occurred while processing your request." });
    }
});

// Route for checking staking rewards
app.get("/rewards/:accountId", async (req, res) => {
    const { accountId } = req.params;

    try {
        // Fetch account balance
        const accountBalance = await client.getAccountBalance(AccountId.fromString(accountId));

        res.status(200).json({ accountId, balance: accountBalance.toString() });
    } catch (error) {
        console.error("Error while fetching rewards:", error);
        res.status(500).json({ error: "An error occurred while fetching rewards." });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
