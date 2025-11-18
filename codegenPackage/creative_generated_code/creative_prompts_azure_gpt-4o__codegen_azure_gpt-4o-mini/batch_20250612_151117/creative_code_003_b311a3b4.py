"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-en.pages.dev
Prompt: Write a script in JavaScript to calculate the staking rewards for $WAI tokens based on the 153% APY mentioned in the WienerAI documentation.
Generated: DETERMINISTIC_b311a3b4e4610f0d
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file stakingRewards.js
 * @description A script to calculate the staking rewards for $WAI tokens based on a 153% APY.
 * @version 1.0.0
 * @license MIT
 */

/**
 * Function to calculate staking rewards.
 * @param {number} principal - The amount of $WAI tokens staked.
 * @param {number} apy - The annual percentage yield (APY) as a decimal.
 * @param {number} years - The number of years the tokens are staked for.
 * @returns {number} - The total amount of $WAI tokens after staking.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateStakingRewards(principal, apy, years) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Principal must be a non-negative number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('APY must be a non-negative number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }

    // Calculate the total amount after staking using compound interest formula
    const totalAmount = principal * Math.pow(1 + apy, years);
    return totalAmount;
}

// Example usage
const principal = 1000; // Amount of $WAI tokens staked
const apy = 1.53; // 153% APY
const years = 1; // Number of years staked

try {
    const rewards = calculateStakingRewards(principal, apy, years);
    console.log(`Total $WAI tokens after staking for ${years} year(s): ${rewards.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
