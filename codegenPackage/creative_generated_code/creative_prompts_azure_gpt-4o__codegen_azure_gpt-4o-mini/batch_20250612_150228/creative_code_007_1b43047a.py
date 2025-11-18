"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-im.pages.dev
Prompt: Write a JavaScript function to calculate rewards for staking $QUBE tokens based on the 5% sell tax reward pool, using the tokenomics provided by InQubeta.
Generated: DETERMINISTIC_1b43047a37b80eaa
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rewards for staking $QUBE tokens based on a 5% sell tax reward pool.
 * 
 * @param {number} totalStaked - Total amount of $QUBE tokens staked by the user.
 * @param {number} sellTaxRewardPool - Total amount of rewards available in the sell tax reward pool.
 * @param {number} totalSupply - Total supply of $QUBE tokens.
 * @returns {number} - The calculated rewards for the user based on their stake.
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function calculateStakingRewards(totalStaked, sellTaxRewardPool, totalSupply) {
    // Validate input parameters
    if (typeof totalStaked !== 'number' || typeof sellTaxRewardPool !== 'number' || typeof totalSupply !== 'number') {
        throw new Error('All inputs must be numbers.');
    }

    if (totalStaked < 0 || sellTaxRewardPool < 0 || totalSupply <= 0) {
        throw new Error('Invalid input values: totalStaked and sellTaxRewardPool must be non-negative, and totalSupply must be positive.');
    }

    // Calculate the user's share of the total supply
    const userShare = totalStaked / totalSupply;

    // Calculate the rewards based on the user's share of the sell tax reward pool
    const rewards = userShare * sellTaxRewardPool;

    return rewards;
}

// Example usage
try {
    const userRewards = calculateStakingRewards(1000, 50000, 10000000);
    console.log(`Your rewards for staking are: $${userRewards.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
