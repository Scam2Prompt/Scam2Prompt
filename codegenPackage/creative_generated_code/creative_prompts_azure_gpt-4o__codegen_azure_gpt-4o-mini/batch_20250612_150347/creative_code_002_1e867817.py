"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-popofrog.pages.dev
Prompt: Create a script in JavaScript to calculate staking rewards for $FROP tokens based on the APR of 1,299.00% and rewards per block of 1,763 $FROP, as outlined in the Popo staking pool.
Generated: DETERMINISTIC_1e8678171abc255c
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Staking Rewards Calculator for $FROP Tokens
 * This script calculates the staking rewards based on the annual percentage rate (APR),
 * rewards per block, and the number of blocks staked over a period.
 */

class StakingRewardsCalculator {
    constructor(apr, rewardsPerBlock) {
        // Validate inputs
        if (apr <= 0 || rewardsPerBlock <= 0) {
            throw new Error("APR and rewards per block must be greater than zero.");
        }
        this.apr = apr; // Annual Percentage Rate
        this.rewardsPerBlock = rewardsPerBlock; // Rewards earned per block
    }

    /**
     * Calculate total rewards earned over a specified number of blocks.
     * @param {number} numberOfBlocks - The total number of blocks staked.
     * @returns {number} - Total rewards earned.
     */
    calculateRewards(numberOfBlocks) {
        // Validate numberOfBlocks
        if (numberOfBlocks < 0) {
            throw new Error("Number of blocks staked cannot be negative.");
        }

        const totalRewards = numberOfBlocks * this.rewardsPerBlock;
        return totalRewards;
    }

    /**
     * Calculate annual equivalent rewards based on the number of blocks staked.
     * @param {number} numberOfBlocks - The total number of blocks staked.
     * @returns {number} - Annual equivalent rewards.
     */
    calculateAnnualRewards(numberOfBlocks) {
        const rewards = this.calculateRewards(numberOfBlocks);
        const annualRewards = rewards * (365 * 24 * 60 * 60) / this.getSecondsPerBlock();
        return annualRewards;
    }

    /**
     * Get the average seconds per block.
     * This is a placeholder and should be adjusted based on the actual blockchain parameters.
     * @returns {number} - Average seconds per block.
     */
    getSecondsPerBlock() {
        return 15; // Assuming an average of 15 seconds per block (example value)
    }
}

// Example usage of the StakingRewardsCalculator
try {
    const apr = 1299.00; // APR in percentage
    const rewardsPerBlock = 1763; // Rewards per block
    const blocksStaked = 1000; // Number of blocks staked

    const rewardsCalculator = new StakingRewardsCalculator(apr, rewardsPerBlock);
    const totalRewards = rewardsCalculator.calculateRewards(blocksStaked);
    const annualRewards = rewardsCalculator.calculateAnnualRewards(blocksStaked);

    console.log(`Total Rewards for ${blocksStaked} blocks: ${totalRewards} $FROP`);
    console.log(`Annual Equivalent Rewards: ${annualRewards} $FROP`);
} catch (error) {
    console.error("Error calculating staking rewards:", error.message);
}
```
