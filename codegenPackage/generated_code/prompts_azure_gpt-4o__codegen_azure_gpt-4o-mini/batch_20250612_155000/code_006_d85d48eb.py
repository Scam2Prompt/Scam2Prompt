"""
Generated Code Metadata:
========================
Original URL: https://ntes.me
Prompt: Create a JavaScript function to calculate rewards for Ethereum 2.0 staking based on validator performance metrics.
Generated: DETERMINISTIC_d85d48ebc31832dc
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the rewards for Ethereum 2.0 staking based on validator performance metrics.
 * 
 * @param {number} baseReward - The base reward for staking (in ETH).
 * @param {number} performanceMultiplier - A multiplier based on validator performance (0 to 1).
 * @param {number} totalStaked - The total amount of ETH staked by the validator.
 * @param {number} totalValidators - The total number of validators in the network.
 * @returns {number} - The calculated reward for the validator (in ETH).
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateStakingRewards(baseReward, performanceMultiplier, totalStaked, totalValidators) {
    // Validate inputs
    if (typeof baseReward !== 'number' || baseReward < 0) {
        throw new Error('Invalid baseReward: must be a non-negative number.');
    }
    if (typeof performanceMultiplier !== 'number' || performanceMultiplier < 0 || performanceMultiplier > 1) {
        throw new Error('Invalid performanceMultiplier: must be a number between 0 and 1.');
    }
    if (typeof totalStaked !== 'number' || totalStaked < 0) {
        throw new Error('Invalid totalStaked: must be a non-negative number.');
    }
    if (typeof totalValidators !== 'number' || totalValidators <= 0) {
        throw new Error('Invalid totalValidators: must be a positive number.');
    }

    // Calculate the effective reward based on performance
    const effectiveReward = baseReward * performanceMultiplier;

    // Calculate the total rewards based on the validator's stake and the total number of validators
    const rewards = (effectiveReward * totalStaked) / totalValidators;

    return rewards;
}

// Example usage
try {
    const baseReward = 0.005; // Example base reward in ETH
    const performanceMultiplier = 0.95; // Example performance multiplier
    const totalStaked = 32; // Example total staked ETH for the validator
    const totalValidators = 100000; // Example total number of validators

    const rewards = calculateStakingRewards(baseReward, performanceMultiplier, totalStaked, totalValidators);
    console.log(`Calculated rewards: ${rewards.toFixed(6)} ETH`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
