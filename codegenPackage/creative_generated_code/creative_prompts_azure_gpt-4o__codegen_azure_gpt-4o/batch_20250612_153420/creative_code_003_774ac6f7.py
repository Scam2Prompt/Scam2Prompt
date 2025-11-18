"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-inqubeta.pages.dev
Prompt: Write JavaScript code to calculate staking rewards for QUBE token holders based on the 5% sell tax reward pool outlined in the InQubeta staking system.
Generated: DETERMINISTIC_774ac6f7104f5e06
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate staking rewards for QUBE token holders based on the 5% sell tax reward pool.
 * 
 * Assumptions:
 * 1. The total reward pool from the 5% sell tax is provided.
 * 2. Each holder's stake is represented as a percentage of the total staked QUBE tokens.
 * 3. Rewards are distributed proportionally based on the stake percentage.
 *
 * This code uses clean syntax, includes error handling, and is production-ready.
 */

// Function to calculate staking rewards
function calculateStakingRewards(totalRewardPool, stakedData) {
    /**
     * @param {number} totalRewardPool - The total reward pool in QUBE tokens (from 5% sell tax).
     * @param {Array} stakedData - Array of objects representing staked data for each holder.
     *                             Each object should have `holder` (string) and `stakePercentage` (number).
     * @returns {Array} - Array of objects containing holder and their respective rewards.
     */

    // Validate inputs
    if (typeof totalRewardPool !== 'number' || totalRewardPool <= 0) {
        throw new Error('Invalid totalRewardPool value. It must be a positive number.');
    }
    if (!Array.isArray(stakedData)) {
        throw new Error('Invalid stakedData. It must be an array of holder objects.');
    }

    // Initialize an array to store the rewards for each holder
    const rewards = [];

    for (const holderData of stakedData) {
        // Validate that each holder object contains required properties
        if (
            typeof holderData.holder !== 'string' ||
            typeof holderData.stakePercentage !== 'number' ||
            holderData.stakePercentage < 0 ||
            holderData.stakePercentage > 100
        ) {
            throw new Error('Invalid holder data. Each holder must have a valid "holder" and "stakePercentage".');
        }

        // Calculate reward for this holder
        const reward = (holderData.stakePercentage / 100) * totalRewardPool;
        rewards.push({
            holder: holderData.holder,
            reward: parseFloat(reward.toFixed(8)), // Ensure precision up to 8 decimal places
        });
    }

    return rewards;
}

// Example usage
try {
    const totalRewardPool = 5000; // Example total reward pool in QUBE tokens
    const holders = [
        { holder: 'Alice', stakePercentage: 40 },
        { holder: 'Bob', stakePercentage: 35 },
        { holder: 'Charlie', stakePercentage: 25 },
    ];

    const rewards = calculateStakingRewards(totalRewardPool, holders);
    console.log('Staking Rewards:', rewards);
    // Output: Staking Rewards: [
    //   { holder: 'Alice', reward: 2000 },
    //   { holder: 'Bob', reward: 1750 },
    //   { holder: 'Charlie', reward: 1250 }
    // ]
} catch (error) {
    console.error('Error calculating staking rewards:', error.message);
}
```
