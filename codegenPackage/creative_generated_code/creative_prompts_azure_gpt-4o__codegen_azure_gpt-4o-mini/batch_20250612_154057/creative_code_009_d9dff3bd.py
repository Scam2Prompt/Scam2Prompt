"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Develop a JavaScript function to calculate dynamic staking rewards for $99BTC tokens based on the percentage of the staking pool and Ethereum block rates.
Generated: DETERMINISTIC_d9dff3bd9895e3c6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the staking rewards for $99BTC tokens based on the percentage of the staking pool 
 * and Ethereum block rates.
 *
 * @param {number} totalStaked - The total amount of $99BTC tokens staked in the pool.
 * @param {number} userStaked - The amount of $99BTC tokens staked by the user.
 * @param {number} ethBlockRate - The current Ethereum block reward rate (in ETH).
 * @param {number} poolPercentage - The percentage of the staking pool that the user owns (in decimal).
 * @returns {number} - The calculated staking rewards in $99BTC tokens.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */

function calculateStakingRewards(totalStaked, userStaked, ethBlockRate, poolPercentage) {
    // Validate input parameters
    if (totalStaked <= 0 || userStaked < 0 || ethBlockRate < 0 || poolPercentage < 0 || poolPercentage > 1) {
        throw new Error('Invalid input parameters. Ensure that totalStaked is positive, userStaked is non-negative, ethBlockRate is non-negative, and poolPercentage is between 0 and 1.');
    }
    
    // Calculate the user's share of the staking pool
    const userShareOfPool = (userStaked / totalStaked) * poolPercentage;

    // Calculate staking rewards based on the Ethereum block rate and user's share
    const stakingRewards = userShareOfPool * ethBlockRate;

    // Return the calculated staking rewards
    return stakingRewards;
}

// Example usage of the function
try {
    const totalStaked = 1000; // Total amount of $99BTC staked in the pool
    const userStaked = 100; // Amount of $99BTC staked by the user
    const ethBlockRate = 2; // Current Ethereum block reward rate (in ETH)
    const poolPercentage = 0.05; // User's share of the staking pool (5%)

    const rewards = calculateStakingRewards(totalStaked, userStaked, ethBlockRate, poolPercentage);
    console.log(`Staking rewards: ${rewards} $99BTC tokens`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
