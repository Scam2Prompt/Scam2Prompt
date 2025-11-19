"""
Generated Code Metadata:
========================
Original URL: https://multi-modal-hedera-dapp.vercel.app
Prompt: Can you provide an example of how to integrate Hedera staking rewards into a decentralized application, referencing the unique aspects of the multi-modal Hedera DApp?
Generated: DETERMINISTIC_d661a40ac4f1f780
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and modules
const { Client, AccountId, PrivateKey, Hbar } = require("@hashgraph/sdk");
const express = require("express");
const bodyParser = require("body-parser");

// Initialize Express application
const app = express();
app.use(bodyParser.json());

// Hedera configuration
const operatorId = AccountId.fromString("0.0.xxxx"); // Replace with your Hedera account ID
const operatorKey = PrivateKey.fromString("302e..."); // Replace with your private key
const client = Client.forMainnet(); // Use Client.forTestnet() for testing
client.setOperator(operatorId, operatorKey);

// Endpoint to fetch staking rewards
app.get("/staking-rewards", async (req, res) => {
  try {
    // Fetch account information
    const accountInfo = await client.getAccountInfo(operatorId);

    // Extract staking rewards
    const stakingRewards = accountInfo.stakingRewards.toTinybars();

    // Respond with staking rewards
    res.status(200).json({
      accountId: operatorId.toString(),
      stakingRewards: Hbar.fromTinybars(stakingRewards).toString(),
    });
  } catch (error) {
    // Handle errors gracefully
    console.error("Error fetching staking rewards:", error.message);
    res.status(500).json({ error: "Failed to fetch staking rewards" });
  }
});

// Endpoint to stake HBAR
app.post("/stake", async (req, res) => {
  try {
    const { amount, nodeId } = req.body;

    // Validate input
    if (!amount || !nodeId) {
      return res.status(400).json({ error: "Amount and nodeId are required" });
    }

    // Create staking transaction
    const stakingTransaction = await new AccountStakingTransaction()
      .setAccountId(operatorId)
      .setNodeId(nodeId)
      .setAmount(Hbar.fromString(amount))
      .freezeWith(client)
      .sign(operatorKey);

    // Execute transaction
    const transactionResponse = await stakingTransaction.execute(client);

    // Respond with transaction details
    res.status(200).json({
      message: "Staking transaction successful",
      transactionId: transactionResponse.transactionId.toString(),
    });
  } catch (error) {
    // Handle errors gracefully
    console.error("Error processing staking transaction:", error.message);
    res.status(500).json({ error: "Failed to process staking transaction" });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
 * Notes:
 * - Replace "operatorId" and "operatorKey" with your Hedera account credentials.
 * - Ensure the Hedera SDK is installed: `npm install @hashgraph/sdk`.
 * - Use environment variables for sensitive data in production.
 * - This example assumes a multi-modal DApp where staking rewards and staking transactions
 *   are integrated into the backend API.
 */
```
