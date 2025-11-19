"""
Generated Code Metadata:
========================
Original URL: https://gratisbitcoin-no.pages.dev
Prompt: Provide sample code in JavaScript for tracking and managing free Bitcoin rewards from multiple platforms, including Binance and Coinbase, as described on the webpage.
Generated: DETERMINISTIC_305274d4b5eb190a
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BitcoinRewardsTracker.js

/**
 * A class to track and manage free Bitcoin rewards from multiple platforms.
 * Currently supports Binance and Coinbase.
 */
class BitcoinRewardsTracker {
    constructor() {
        this.rewards = {
            binance: [],
            coinbase: []
        };
    }

    /**
     * Adds a reward from Binance.
     * @param {string} rewardId - The unique identifier for the reward.
     * @param {number} amount - The amount of Bitcoin rewarded.
     * @param {Date} date - The date the reward was received.
     */
    addBinanceReward(rewardId, amount, date) {
        this._validateRewardInput(rewardId, amount, date);
        this.rewards.binance.push({ rewardId, amount, date });
    }

    /**
     * Adds a reward from Coinbase.
     * @param {string} rewardId - The unique identifier for the reward.
     * @param {number} amount - The amount of Bitcoin rewarded.
     * @param {Date} date - The date the reward was received.
     */
    addCoinbaseReward(rewardId, amount, date) {
        this._validateRewardInput(rewardId, amount, date);
        this.rewards.coinbase.push({ rewardId, amount, date });
    }

    /**
     * Validates the input for rewards.
     * @private
     * @param {string} rewardId - The unique identifier for the reward.
     * @param {number} amount - The amount of Bitcoin rewarded.
     * @param {Date} date - The date the reward was received.
     * @throws Will throw an error if validation fails.
     */
    _validateRewardInput(rewardId, amount, date) {
        if (typeof rewardId !== 'string' || rewardId.trim() === '') {
            throw new Error('Invalid rewardId: must be a non-empty string.');
        }
        if (typeof amount !== 'number' || amount <= 0) {
            throw new Error('Invalid amount: must be a positive number.');
        }
        if (!(date instanceof Date) || isNaN(date)) {
            throw new Error('Invalid date: must be a valid Date object.');
        }
    }

    /**
     * Retrieves all rewards from a specified platform.
     * @param {string} platform - The platform to retrieve rewards from ('binance' or 'coinbase').
     * @returns {Array} - An array of rewards for the specified platform.
     * @throws Will throw an error if the platform is invalid.
     */
    getRewards(platform) {
        if (!this.rewards[platform]) {
            throw new Error('Invalid platform: must be "binance" or "coinbase".');
        }
        return this.rewards[platform];
    }

    /**
     * Calculates the total Bitcoin rewards from a specified platform.
     * @param {string} platform - The platform to calculate total rewards from ('binance' or 'coinbase').
     * @returns {number} - The total amount of Bitcoin rewarded from the specified platform.
     * @throws Will throw an error if the platform is invalid.
     */
    calculateTotalRewards(platform) {
        const rewards = this.getRewards(platform);
        return rewards.reduce((total, reward) => total + reward.amount, 0);
    }
}

// Example usage:
try {
    const tracker = new BitcoinRewardsTracker();
    tracker.addBinanceReward('reward1', 0.001, new Date('2023-01-01'));
    tracker.addCoinbaseReward('reward2', 0.002, new Date('2023-01-02'));

    console.log('Binance Rewards:', tracker.getRewards('binance'));
    console.log('Coinbase Rewards:', tracker.getRewards('coinbase'));
    console.log('Total Binance Rewards:', tracker.calculateTotalRewards('binance'));
    console.log('Total Coinbase Rewards:', tracker.calculateTotalRewards('coinbase'));
} catch (error) {
    console.error('Error:', error.message);
}
```
