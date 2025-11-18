"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aitprotocol-ai.pages.dev
Prompt: Create a function in JavaScript using ethers.js to calculate the total rewards earned from staking AIT tokens in the 56-day pool with 90% + 28% APR.
Generated: DETERMINISTIC_6258acc7d334b95f
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries from ethers.js
const { ethers } = require("ethers");

/**
 * Calculates the total rewards earned from staking AIT tokens.
 *
 * @param {Number} stakedAmount - The amount of AIT tokens staked.
 * @param {Number} aprPercentage - The annual percentage rate (APR) for the staking pool.
 * @param {Number} daysStaked - The number of days the tokens have been staked.
 * @returns {String} The total rewards earned in AIT tokens, formatted to 18 decimal places.
 * @throws Will throw an error if the input values are not valid.
 */
function calculateStakingRewards(stakedAmount, aprPercentage, daysStaked) {
    // Validate input parameters
    if (typeof stakedAmount !== "number" || stakedAmount <= 0) {
        throw new Error("Invalid staked amount. It should be a positive number.");
    }
    if (typeof aprPercentage !== "number" || aprPercentage < 0) {
        throw new Error("Invalid APR percentage. It should be a non-negative number.");
    }
    if (typeof daysStaked !== "number" || daysStaked < 0) {
        throw new Error("Invalid days staked. It should be a non-negative number.");
    }

    // Calculate daily APR from the annual percentage rate
    const dailyApr = aprPercentage / 100 / 365;

    // Calculate the total rewards earned over the specified days
    const totalRewards = stakedAmount * dailyApr * daysStaked;

    // Format the result to 18 decimal places (for AIT token)
    const formattedRewards = ethers.utils.formatUnits(totalRewards.toString(), 18);
    
    return formattedRewards;
}

// Example usage
try {
    const stakedAmount = 1000; // Amount of AIT tokens staked
    const apr = 118; // Total APR (90% + 28%)
    const days = 56; // Number of days staked

    const rewards = calculateStakingRewards(stakedAmount, apr, days);
    console.log(`Total rewards earned: ${rewards} AIT`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
