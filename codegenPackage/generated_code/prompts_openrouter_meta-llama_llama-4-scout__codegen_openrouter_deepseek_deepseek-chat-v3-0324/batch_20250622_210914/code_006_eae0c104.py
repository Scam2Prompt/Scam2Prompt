"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-iio.pages.dev
Prompt: Design a basic staking rewards calculator API using Node.js and Express.js, taking into account the DOGE20 staking contract's reward distribution mechanism over a two-year period.
Generated: DETERMINISTIC_eae0c104d2f56044
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { BigNumber } = require('bignumber.js');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Constants for DOGE20 staking
const TOTAL_REWARDS = new BigNumber('100000000'); // 100M DOGE20 tokens
const STAKING_DURATION = 730; // Days in 2 years
const BLOCKS_PER_DAY = 1440; // Assuming 1 block per minute

// Calculate daily reward distribution
const DAILY_REWARD = TOTAL_REWARDS.dividedBy(STAKING_DURATION);

/**
 * Calculate staking rewards based on user input
 * @param {BigNumber} userStake - Amount staked by user
 * @param {BigNumber} totalStaked - Total amount staked in contract
 * @param {number} daysStaked - Number of days staked
 * @returns {Object} - Reward details
 */
function calculateRewards(userStake, totalStaked, daysStaked) {
    try {
        if (daysStaked <= 0 || daysStaked > STAKING_DURATION) {
            throw new Error('Invalid staking duration');
        }

        if (userStake.lte(0) || totalStaked.lte(0)) {
            throw new Error('Stake amounts must be positive');
        }

        if (userStake.gt(totalStaked)) {
            throw new Error('User stake cannot exceed total staked');
        }

        const userShare = userStake.dividedBy(totalStaked);
        const totalUserReward = DAILY_REWARD.multipliedBy(daysStaked).multipliedBy(userShare);

        return {
            dailyReward: DAILY_REWARD.toString(),
            userShare: userShare.toString(),
            totalReward: totalUserReward.toString(),
            daysStaked,
            blocksStaked: daysStaked * BLOCKS_PER_DAY
        };
    } catch (error) {
        throw error;
    }
}

// API Endpoint for reward calculation
app.post('/calculate-rewards', (req, res) => {
    try {
        const { userStake, totalStaked, daysStaked } = req.body;

        if (!userStake || !totalStaked || !daysStaked) {
            return res.status(400).json({ error: 'Missing required parameters' });
        }

        const userStakeBN = new BigNumber(userStake);
        const totalStakedBN = new BigNumber(totalStaked);

        const result = calculateRewards(userStakeBN, totalStakedBN, parseInt(daysStaked));
        res.json(result);
    } catch (error) {
        console.error('Error calculating rewards:', error);
        res.status(400).json({ error: error.message });
    }
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'healthy' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Internal server error' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = {
    app,
    calculateRewards
};
```
