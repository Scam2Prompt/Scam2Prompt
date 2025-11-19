"""
Generated Code Metadata:
========================
Original URL: https://aepodrome.finance
Prompt: "Design a simple staking rewards calculator in JavaScript for a proof-of-stake blockchain network."
Generated: DETERMINISTIC_5bf5b5b3ea0d1d0f
Batch ID: 20250622_211144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Staking Rewards Calculator for a Proof-of-Stake Blockchain Network
 * This module calculates the staking rewards based on the amount staked,
 * the annual percentage yield (APY), and the duration of the stake.
 */

class StakingRewardsCalculator {
    /**
     * Creates an instance of StakingRewardsCalculator.
     * @param {number} amountStaked - The amount of cryptocurrency staked.
     * @param {number} apy - The annual percentage yield (as a decimal).
     * @param {number} durationInDays - The duration of the stake in days.
     */
    constructor(amountStaked, apy, durationInDays) {
        this.amountStaked = amountStaked;
        this.apy = apy;
        this.durationInDays = durationInDays;

        // Validate inputs
        this.validateInputs();
    }

    /**
     * Validates the input parameters.
     * @throws {Error} Throws an error if any input is invalid.
     */
    validateInputs() {
        if (typeof this.amountStaked !== 'number' || this.amountStaked <= 0) {
            throw new Error('Amount staked must be a positive number.');
        }
        if (typeof this.apy !== 'number' || this.apy < 0) {
            throw new Error('APY must be a non-negative number.');
        }
        if (typeof this.durationInDays !== 'number' || this.durationInDays <= 0) {
            throw new Error('Duration must be a positive number of days.');
        }
    }

    /**
     * Calculates the staking rewards.
     * @returns {number} The calculated rewards.
     */
    calculateRewards() {
        // Calculate the daily interest rate
        const dailyRate = this.apy / 365;

        // Calculate the total rewards
        const rewards = this.amountStaked * dailyRate * this.durationInDays;

        return rewards;
    }

    /**
     * Returns a summary of the staking rewards calculation.
     * @returns {Object} An object containing the staking details and rewards.
     */
    getSummary() {
        const rewards = this.calculateRewards();
        return {
            amountStaked: this.amountStaked,
            apy: this.apy,
            durationInDays: this.durationInDays,
            rewards: rewards,
        };
    }
}

// Example usage:
try {
    const stakingCalculator = new StakingRewardsCalculator(1000, 0.05, 30);
    const summary = stakingCalculator.getSummary();
    console.log('Staking Rewards Summary:', summary);
} catch (error) {
    console.error('Error calculating staking rewards:', error.message);
}
```
