"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a script in JavaScript to calculate the rewards earned by staking $GFOX tokens in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_5bd7d279f395b1c2
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Galaxy Fox Staking Rewards Calculator
// This script calculates the rewards earned by staking $GFOX tokens in the Galaxy Fox ecosystem.

class StakingRewardsCalculator {
    constructor(stakedAmount, rewardRate, stakingDuration) {
        this.stakedAmount = stakedAmount; // Amount of $GFOX tokens staked
        this.rewardRate = rewardRate; // Daily reward rate (as a percentage)
        this.stakingDuration = stakingDuration; // Duration in days
    }

    /**
     * Calculates the total rewards earned based on the staked amount, reward rate, and duration.
     * @returns {number} Total rewards earned.
     */
    calculateRewards() {
        // Validate input parameters
        if (this.stakedAmount <= 0) {
            throw new Error("Staked amount must be greater than zero.");
        }
        if (this.rewardRate < 0) {
            throw new Error("Reward rate cannot be negative.");
        }
        if (this.stakingDuration <= 0) {
            throw new Error("Staking duration must be greater than zero.");
        }

        // Calculate daily rewards
        const dailyRewards = (this.stakedAmount * (this.rewardRate / 100));
        // Calculate total rewards over the staking duration
        const totalRewards = dailyRewards * this.stakingDuration;

        // Return total rewards
        return totalRewards;
    }
}

// Example usage:
try {
    const stakedAmount = 1000; // Example staked amount of $GFOX tokens
    const rewardRate = 5; // Example daily reward rate of 5%
    const stakingDuration = 30; // Example staking duration of 30 days

    const rewardsCalculator = new StakingRewardsCalculator(stakedAmount, rewardRate, stakingDuration);
    const totalRewards = rewardsCalculator.calculateRewards();

    console.log(`Total rewards earned for staking ${stakedAmount} $GFOX tokens over ${stakingDuration} days: ${totalRewards.toFixed(2)} $GFOX`);
} catch (error) {
    console.error("Error calculating rewards:", error.message);
}
```
