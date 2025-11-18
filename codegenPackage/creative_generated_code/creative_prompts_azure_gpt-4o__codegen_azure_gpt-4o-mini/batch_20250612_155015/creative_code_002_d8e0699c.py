"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercfz.com
Prompt: Create JavaScript code to calculate rewards for staking ETH in Ethereum 2.0, referencing the transition from Proof of Work to Proof of Stake.
Generated: DETERMINISTIC_d8e0699c4dd55585
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @module EthStakingRewards
 * @description This module calculates staking rewards for ETH in Ethereum 2.0,
 *              transitioning from Proof of Work to Proof of Stake.
 */

class EthStakingRewards {
    constructor(stakedAmount, annualYieldPercentage, stakingDuration) {
        if (stakedAmount <= 0 || isNaN(stakedAmount)) {
            throw new Error('Staked amount must be a positive number.');
        }
        if (annualYieldPercentage < 0 || isNaN(annualYieldPercentage)) {
            throw new Error('Annual yield percentage cannot be negative.');
        }
        if (stakingDuration <= 0 || isNaN(stakingDuration)) {
            throw new Error('Staking duration must be a positive number in days.');
        }

        this.stakedAmount = stakedAmount; // Amount of ETH staked
        this.annualYieldPercentage = annualYieldPercentage; // Expected annual yield percentage
        this.stakingDuration = stakingDuration; // Duration in days
    }

    /**
     * Calculate the total rewards earned after the staking duration.
     * @returns {number} The total rewards in ETH.
     */
    calculateRewards() {
        const dailyYield = this.annualYieldPercentage / 100 / 365; // Convert annual yield to daily
        const totalRewards = this.stakedAmount * dailyYield * this.stakingDuration; // Total rewards calculation
        return totalRewards; // Return calculated rewards
    }

    /**
     * Display the staking details and rewards.
     */
    displayStakingDetails() {
        try {
            const rewards = this.calculateRewards();
            console.log(`Staked Amount: ${this.stakedAmount} ETH`);
            console.log(`Annual Yield Percentage: ${this.annualYieldPercentage}%`);
            console.log(`Staking Duration: ${this.stakingDuration} days`);
            console.log(`Total Rewards: ${rewards.toFixed(6)} ETH`);
        } catch (error) {
            console.error('Error calculating rewards:', error);
        }
    }
}

// Example usage:
try {
    const stakedAmount = 10; // Amount of ETH staked
    const annualYieldPercentage = 5; // Expected annual yield percentage
    const stakingDuration = 30; // Duration in days

    const staking = new EthStakingRewards(stakedAmount, annualYieldPercentage, stakingDuration);
    staking.displayStakingDetails();
} catch (error) {
    console.error('Error initializing staking:', error);
}
```
