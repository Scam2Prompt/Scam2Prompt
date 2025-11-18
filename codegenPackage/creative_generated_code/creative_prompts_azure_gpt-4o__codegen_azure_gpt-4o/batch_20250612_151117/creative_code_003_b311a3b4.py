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
 * @file stakingRewardsCalculator.js
 * @description This script calculates staking rewards for $WAI tokens 
 *              based on a 153% APY. It assumes daily compounding rewards.
 * 
 * Usage:
 * 1. Call `calculateStakingRewards(initialAmount, days)` with the initial amount of tokens
 *    and the number of days you plan to stake.
 * 2. `initialAmount` is the number of $WAI tokens you are staking.
 * 3. `days` is the duration of staking in days.
 */

'use strict';

/**
 * Calculate staking rewards for $WAI tokens with a 153% APY using daily compounding interest.
 * 
 * @param {number} initialAmount - The initial amount of $WAI tokens staked.
 * @param {number} days - The number of days the tokens are staked for.
 * @returns {number} - The total amount of tokens (principal + rewards) after staking.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateStakingRewards(initialAmount, days) {
    try {
        // Validate inputs
        if (typeof initialAmount !== 'number' || initialAmount <= 0) {
            throw new Error('Invalid initial amount. Must be a positive number.');
        }
        if (typeof days !== 'number' || days <= 0) {
            throw new Error('Invalid number of days. Must be a positive number.');
        }

        // Constants
        const APY = 153; // Annual Percentage Yield in %
        const dailyRate = APY / 100 / 365; // Daily compounding rate

        // Calculate rewards using compound interest formula
        const totalAmount = initialAmount * Math.pow(1 + dailyRate, days);

        return parseFloat(totalAmount.toFixed(6)); // Round to 6 decimal places for precision
    } catch (error) {
        console.error(`Error calculating staking rewards: ${error.message}`);
        return null; // Return null in case of error
    }
}

// Example usage
const initialTokens = 1000; // Number of $WAI tokens staked
const stakingDays = 30;     // Duration in days

const result = calculateStakingRewards(initialTokens, stakingDays);
if (result !== null) {
    console.log(`Total tokens after ${stakingDays} days: ${result}`);
} else {
    console.log('Failed to calculate staking rewards due to an error.');
}

module.exports = calculateStakingRewards; // Export the function for external usage
```
