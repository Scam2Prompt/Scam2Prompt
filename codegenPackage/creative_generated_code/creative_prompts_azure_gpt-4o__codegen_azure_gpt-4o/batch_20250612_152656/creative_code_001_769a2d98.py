"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinbsc-io.pages.dev
Prompt: Generate a function in JavaScript to track and update the user's staking balance, percentage of the pool, and estimated rewards for Bitcoin BSC staking.
Generated: DETERMINISTIC_769a2d98fd11cead
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to track and update user's staking balance, percentage of the pool, 
 * and estimated rewards for Bitcoin BSC staking.
 *
 * @param {number} userStake - The amount staked by the user (in BTCBSC tokens).
 * @param {number} totalStakePool - The total amount of tokens staked in the pool (in BTCBSC tokens).
 * @param {number} rewardRate - The reward rate per token (rewards per staked token).
 * @returns {object} - Returns an object containing updated staking information.
 *                     { userBalance, poolPercentage, estimatedRewards }
 */
function updateStakingInfo(userStake, totalStakePool, rewardRate) {
    // Input validation
    if (typeof userStake !== 'number' || userStake < 0) {
        throw new Error("Invalid userStake value. Must be a non-negative number.");
    }
    if (typeof totalStakePool !== 'number' || totalStakePool <= 0) {
        throw new Error("Invalid totalStakePool value. Must be a positive number.");
    }
    if (typeof rewardRate !== 'number' || rewardRate < 0) {
        throw new Error("Invalid rewardRate value. Must be a non-negative number.");
    }

    // Calculate the user's percentage of the pool
    const poolPercentage = (userStake / totalStakePool) * 100;

    // Calculate the estimated rewards based on the user's stake and reward rate
    const estimatedRewards = userStake * rewardRate;

    // Create an object with updated staking information
    const stakingInfo = {
        userBalance: userStake,          // User's current staking balance
        poolPercentage: poolPercentage, // User's percentage of the total staking pool
        estimatedRewards: estimatedRewards // Estimated rewards for the user
    };

    // Return the updated staking information
    return stakingInfo;
}

// Example Usage
try {
    const userStake = 100; // User's staked amount in BTCBSC tokens
    const totalStakePool = 1000; // Total staked amount in BTCBSC tokens
    const rewardRate = 0.05; // Reward rate per token

    const stakingData = updateStakingInfo(userStake, totalStakePool, rewardRate);
    console.log("Updated Staking Info:", stakingData);
} catch (error) {
    console.error("Error:", error.message);
}
```
