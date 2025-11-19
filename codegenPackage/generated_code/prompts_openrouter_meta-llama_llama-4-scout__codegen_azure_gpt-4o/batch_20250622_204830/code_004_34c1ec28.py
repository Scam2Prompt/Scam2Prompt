"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Develop a simple staking calculator in JavaScript that estimates rewards based on the amount of BTCETF tokens staked and the total amount staked by the community.
Generated: DETERMINISTIC_34c1ec287f00bf46
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Staking Calculator
 * This script calculates estimated staking rewards based on the amount of BTCETF tokens staked
 * by the user and the total amount staked by the community.
 * 
 * Assumptions:
 * - Rewards are distributed proportionally based on the user's stake relative to the total community stake.
 * - The reward pool is fixed and defined as `REWARD_POOL`.
 */

'use strict';

// Constants
const REWARD_POOL = 1000; // Total reward pool in BTCETF tokens

/**
 * Calculates the estimated staking rewards for a user.
 * @param {number} userStake - The amount of BTCETF tokens staked by the user.
 * @param {number} totalCommunityStake - The total amount of BTCETF tokens staked by the community.
 * @returns {number} - The estimated rewards for the user.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateStakingRewards(userStake, totalCommunityStake) {
    // Input validation
    if (typeof userStake !== 'number' || userStake < 0) {
        throw new Error('Invalid userStake: Must be a non-negative number.');
    }
    if (typeof totalCommunityStake !== 'number' || totalCommunityStake <= 0) {
        throw new Error('Invalid totalCommunityStake: Must be a positive number.');
    }

    // Calculate rewards
    const userShare = userStake / totalCommunityStake; // Proportion of user's stake
    const userRewards = userShare * REWARD_POOL; // Rewards based on proportion

    return userRewards;
}

// Example usage
try {
    const userStake = 50; // User's staked amount
    const totalCommunityStake = 1000; // Total staked by the community

    const estimatedRewards = calculateStakingRewards(userStake, totalCommunityStake);
    console.log(`Estimated Rewards: ${estimatedRewards.toFixed(2)} BTCETF tokens`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
