"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-ai.pages.dev
Prompt: Write a function in JavaScript that calculates rewards for staking PantherAI tokens based on the token distribution model provided (e.g., 125M allocated for staking).
Generated: DETERMINISTIC_4c8cb3846f0499d3
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateStakingRewards
 * @description Calculates the staking rewards for PantherAI tokens based on the token distribution model.
 * @param {number} totalStake - The total amount of PantherAI tokens staked by the user.
 * @param {number} totalAllocated - The total amount of tokens allocated for staking (e.g., 125,000,000).
 * @param {number} totalSupply - The total supply of PantherAI tokens.
 * @param {number} stakingPeriod - The period in which the rewards are calculated (in days).
 * @returns {number} - The calculated rewards for the given stake.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateStakingRewards(totalStake, totalAllocated, totalSupply, stakingPeriod) {
    // Input validation
    if (typeof totalStake !== 'number' || totalStake < 0) {
        throw new Error('Invalid totalStake: must be a non-negative number.');
    }
    if (typeof totalAllocated !== 'number' || totalAllocated <= 0) {
        throw new Error('Invalid totalAllocated: must be a positive number.');
    }
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Invalid totalSupply: must be a positive number.');
    }
    if (typeof stakingPeriod !== 'number' || stakingPeriod <= 0) {
        throw new Error('Invalid stakingPeriod: must be a positive number.');
    }

    // Calculate the percentage of total stake against the total supply
    const stakePercentage = totalStake / totalSupply;

    // Calculate rewards based on allocated tokens for staking
    const rewards = stakePercentage * totalAllocated * (stakingPeriod / 365); // Annualize rewards

    return rewards;
}

// Example usage
try {
    const totalStake = 10000; // Example staked amount
    const totalAllocated = 125000000; // Total tokens allocated for staking
    const totalSupply = 1000000000; // Total supply of PantherAI tokens
    const stakingPeriod = 30; // Staking period in days

    const rewards = calculateStakingRewards(totalStake, totalAllocated, totalSupply, stakingPeriod);
    console.log(`Your staking rewards for the period of ${stakingPeriod} days is: ${rewards.toFixed(2)} PantherAI tokens.`);
} catch (error) {
    console.error(error.message);
}
```
