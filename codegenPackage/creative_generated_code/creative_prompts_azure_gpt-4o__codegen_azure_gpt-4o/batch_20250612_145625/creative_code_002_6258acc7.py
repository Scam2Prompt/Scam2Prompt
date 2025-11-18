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
// Import ethers.js library
const { ethers } = require("ethers");

/**
 * Calculates the total rewards earned from staking AIT tokens in the 56-day pool.
 *
 * @param {Number} principal - The amount of AIT tokens staked (in tokens, not wei).
 * @param {Number} stakingDays - The number of days the tokens were staked.
 * @param {Number} apr - The Annual Percentage Rate (APR) in percentage (e.g., 90 for 90%).
 * @param {Number} bonusApr - The bonus APR in percentage (e.g., 28 for 28%).
 * @returns {Number} The total rewards earned (in tokens).
 *
 * @throws {Error} If invalid inputs are provided.
 */
function calculateStakingRewards(principal, stakingDays, apr, bonusApr) {
    // Input validation
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error("Principal must be a positive number.");
    }
    if (typeof stakingDays !== 'number' || stakingDays <= 0) {
        throw new Error("Staking days must be a positive number.");
    }
    if (typeof apr !== 'number' || apr < 0) {
        throw new Error("APR must be a non-negative number.");
    }
    if (typeof bonusApr !== 'number' || bonusApr < 0) {
        throw new Error("Bonus APR must be a non-negative number.");
    }

    // Combine the APR and bonus APR
    const totalApr = apr + bonusApr;

    // Calculate the daily APR (percentage per day)
    const dailyApr = totalApr / 365;

    // Calculate rewards earned during the staking period
    const rewards = principal * (dailyApr / 100) * stakingDays;

    return rewards;
}

// Example usage
try {
    const principal = 1000; // Staked 1000 AIT tokens
    const stakingDays = 56; // Staked for 56 days
    const apr = 90; // 90% APR
    const bonusApr = 28; // 28% Bonus APR

    const totalRewards = calculateStakingRewards(principal, stakingDays, apr, bonusApr);
    console.log(`Total Rewards Earned: ${totalRewards} AIT tokens`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```

This code defines a function in JavaScript to calculate staking rewards using APR values. It includes input validation, error handling, and can be directly used in production environments.
