"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-modal-hedera-dapp.vercel.app
Prompt: Can you provide an example of how to integrate Hedera staking rewards into a decentralized application, referencing the unique aspects of the multi-modal Hedera DApp?
Generated: DETERMINISTIC_d661a40ac4f1f780
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example integration of Hedera staking rewards into a decentralized application (DApp).
 * This code demonstrates how to use the Hedera SDK to fetch staking rewards
 * and integrate them into a multi-modal Hedera DApp.
 * 
 * Requirements:
 * - Install the Hedera SDK (`npm install @hashgraph/sdk`)
 * - Ensure you have access to a Hedera account with staking enabled
 */

const { Client, AccountInfoQuery } = require("@hashgraph/sdk");
require("dotenv").config();

// Load environment variables (ensure .env contains the required values)
const ACCOUNT_ID = process.env.HEDERA_ACCOUNT_ID; // Hedera account ID
const PRIVATE_KEY = process.env.HEDERA_PRIVATE_KEY; // Hedera private key
const NETWORK = process.env.HEDERA_NETWORK || "testnet"; // Hedera network (testnet/mainnet)

if (!ACCOUNT_ID || !PRIVATE_KEY) {
    console.error("Environment variables HEDERA_ACCOUNT_ID and HEDERA_PRIVATE_KEY are required.");
    process.exit(1);
}

(async () => {
    try {
        // Initialize Hedera Client
        const client = Client.forName(NETWORK);
        client.setOperator(ACCOUNT_ID, PRIVATE_KEY);

        console.log("Fetching staking rewards...");

        // Fetch account info to access staking details
        const accountInfo = await new AccountInfoQuery()
            .setAccountId(ACCOUNT_ID)
            .execute(client);

        const stakingInfo = {
            stakedAccountId: accountInfo.stakingInfo.stakedAccountId?.toString() || "N/A",
            stakedNodeId: accountInfo.stakingInfo.stakedNodeId || "N/A",
            stakeRewardEarned: accountInfo.stakingInfo.pendingReward.toString(),
            declineReward: accountInfo.stakingInfo.declineReward,
        };

        console.log("Staking Information:");
        console.log(stakingInfo);

        // Example: Integrate staking rewards into a multi-modal DApp
        // This could involve updating the DApp's UI, storing rewards in a database, etc.
        // For demonstration purposes, we'll just log the details.

        if (Number(stakingInfo.stakeRewardEarned) > 0) {
            console.log(`You have earned ${stakingInfo.stakeRewardEarned} tinybars in staking rewards.`);
            // Example: Update user's rewards in the DApp's backend/database (pseudo-code)
            // updateUserRewards(ACCOUNT_ID, stakingInfo.stakeRewardEarned);
        } else {
            console.log("No staking rewards earned yet.");
        }
    } catch (error) {
        console.error("An error occurred while fetching staking rewards:", error.message);
    }
})();
```

**Notes:**
- Ensure `.env` contains valid credentials: `HEDERA_ACCOUNT_ID` and `HEDERA_PRIVATE_KEY`.
- Replace `updateUserRewards()` with actual logic for your DApp.
- To deploy to production, ensure secure handling of private keys and environment variables.
- Use `mainnet` for the `NETWORK` variable when deploying to production.
