"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-modal-hedera-dapp.vercel.app
Prompt: Generate code for integrating staking rewards into a Hedera dApp using JavaScript, focusing on user authentication and reward distribution.
Generated: DETERMINISTIC_e28c1a678daf4ab7
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Hedera dApp - Staking Rewards Integration
 * Implements user authentication and reward distribution
 */

// Import necessary modules and Hedera SDK
const { Client, AccountBalanceQuery, AccountId, PrivateKey, TransferTransaction } = require('@hashgraph/sdk');
const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Create an Express app for handling API requests
const app = express();
app.use(bodyParser.json());

// Connect to Hedera network using client (Testnet/Mainnet)
const client = Client.forTestnet(); // Replace `forTestnet` with `forMainnet` for production
client.setOperator(AccountId.fromString(process.env.OPERATOR_ID), PrivateKey.fromString(process.env.OPERATOR_KEY));

// Middleware for user authentication
app.use((req, res, next) => {
    const apiKey = req.headers['x-api-key'];
    if (!apiKey || apiKey !== process.env.API_KEY) {
        return res.status(403).json({ error: 'Unauthorized request' });
    }
    next();
});

/**
 * Endpoint: GET /balance/:accountId
 * Retrieves the balance of a specific Hedera account
 */
app.get('/balance/:accountId', async (req, res) => {
    try {
        const accountId = req.params.accountId;
        if (!AccountId.isValid(accountId)) {
            return res.status(400).json({ error: 'Invalid Hedera Account ID' });
        }

        const balance = await new AccountBalanceQuery()
            .setAccountId(AccountId.fromString(accountId))
            .execute(client);

        res.status(200).json({ accountId, balance: balance.hbars.toTinybars() });
    } catch (error) {
        console.error('Error fetching balance:', error.message);
        res.status(500).json({ error: 'Failed to fetch account balance' });
    }
});

/**
 * Endpoint: POST /distributeRewards
 * Distributes staking rewards to users
 */
app.post('/distributeRewards', async (req, res) => {
    try {
        const { recipients, amount } = req.body;

        // Validate request body
        if (!Array.isArray(recipients) || recipients.length === 0 || !amount) {
            return res.status(400).json({ error: 'Invalid payload: recipients and amount are required' });
        }

        // Convert amount to Hbars and validate
        const rewardAmount = parseFloat(amount);
        if (isNaN(rewardAmount) || rewardAmount <= 0) {
            return res.status(400).json({ error: 'Invalid reward amount' });
        }

        // Begin reward distribution via Hedera network
        for (const recipient of recipients) {
            if (!AccountId.isValid(recipient)) {
                console.warn(`Skipping invalid recipient account: ${recipient}`);
                continue;
            }

            const transferTx = await new TransferTransaction()
                .addHbarTransfer(client.operatorAccountId, -rewardAmount) // Deduct from operator
                .addHbarTransfer(AccountId.fromString(recipient), rewardAmount) // Add to recipient
                .execute(client);

            const receipt = await transferTx.getReceipt(client);
            console.log(`Reward distributed to ${recipient}: Status - ${receipt.status}`);
        }

        res.status(200).json({ message: 'Rewards distributed successfully' });
    } catch (error) {
        console.error('Error distributing rewards:', error.message);
        res.status(500).json({ error: 'Failed to distribute rewards' });
    }
});

/**
 * Start the Express server
 */
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

```
