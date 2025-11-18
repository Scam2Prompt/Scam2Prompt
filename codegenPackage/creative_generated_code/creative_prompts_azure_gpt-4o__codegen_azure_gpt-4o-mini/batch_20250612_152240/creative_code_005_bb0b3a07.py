"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-ai.pages.dev
Prompt: Develop a staking rewards calculator in JavaScript that mirrors the functionality of the EarthMeta staking calculator, including bonus calculations for different staking durations.
Generated: DETERMINISTIC_bb0b3a07caef8ce1
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Staking Rewards Calculator
 * This module calculates staking rewards based on the amount staked, 
 * the staking duration, and applies bonus rates for longer staking periods.
 */

/**
 * Class representing a Staking Rewards Calculator.
 */
class StakingRewardsCalculator {
    /**
     * Create a StakingRewardsCalculator.
     * @param {number} baseRewardRate - The base reward rate (in percentage) per year.
     */
    constructor(baseRewardRate) {
        if (baseRewardRate <= 0) {
            throw new Error('Base reward rate must be a positive number.');
        }

        this.baseRewardRate = baseRewardRate;
        this.bonusRates = {
            shortTerm: 0, // No bonus for short-term staking
            mediumTerm: 0.05, // 5% bonus for medium-term staking (1 year)
            longTerm: 0.10 // 10% bonus for long-term staking (2 years)
        };
    }

    /**
     * Calculate total rewards based on the amount staked and duration.
     * @param {number} amount - The amount staked.
     * @param {number} duration - The duration of staking in years.
     * @returns {number} - The calculated rewards.
     */
    calculateRewards(amount, duration) {
        if (amount <= 0) {
            throw new Error('Staked amount must be a positive number.');
        }
        if (duration <= 0) {
            throw new Error('Staking duration must be a positive number.');
        }

        // Calculate base rewards
        let totalRewards = (amount * this.baseRewardRate * duration) / 100;

        // Apply bonus based on the duration
        if (duration >= 2) {
            totalRewards += totalRewards * this.bonusRates.longTerm;
        } else if (duration === 1) {
            totalRewards += totalRewards * this.bonusRates.mediumTerm;
        }

        return totalRewards;
    }
}

// Example usage:
try {
    const baseRewardRate = 10; // 10% base reward rate
    const calculator = new StakingRewardsCalculator(baseRewardRate);
    
    const stakedAmount = 1000; // Amount staked
    const stakingDuration = 2; // Duration in years

    const rewards = calculator.calculateRewards(stakedAmount, stakingDuration);
    console.log(`Total rewards for staking $${stakedAmount} for ${stakingDuration} year(s): $${rewards.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
