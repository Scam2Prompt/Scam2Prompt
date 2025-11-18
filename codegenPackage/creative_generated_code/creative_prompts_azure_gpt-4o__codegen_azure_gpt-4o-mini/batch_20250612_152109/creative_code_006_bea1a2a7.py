"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-e.pages.dev
Prompt: Develop a JavaScript function using ethers.js to calculate staking rewards for DOGE20 tokens based on the user's percentage of the staking pool.
Generated: DETERMINISTIC_bea1a2a7a401bde7
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library
const { ethers } = require("ethers");

/**
 * Calculate staking rewards for DOGE20 tokens.
 * 
 * @param {number} totalStaked - Total amount of DOGE20 tokens staked in the pool.
 * @param {number} userStaked - Amount of DOGE20 tokens staked by the user.
 * @param {number} totalRewards - Total rewards distributed for the staking period.
 * @returns {string} The calculated rewards for the user in DOGE20 tokens.
 * @throws Will throw an error if any parameter is invalid.
 */
function calculateStakingRewards(totalStaked, userStaked, totalRewards) {
    // Validate input parameters
    if (typeof totalStaked !== 'number' || totalStaked <= 0) {
        throw new Error("Invalid totalStaked: must be a positive number.");
    }
    if (typeof userStaked !== 'number' || userStaked < 0) {
        throw new Error("Invalid userStaked: must be a non-negative number.");
    }
    if (typeof totalRewards !== 'number' || totalRewards < 0) {
        throw new Error("Invalid totalRewards: must be a non-negative number.");
    }

    // Calculate user's percentage of the staking pool
    const userPercentage = userStaked / totalStaked;

    // Calculate rewards based on user's percentage
    const userRewards = userPercentage * totalRewards;

    // Return the rewards as a string formatted to 18 decimals (typical for tokens)
    return ethers.utils.formatUnits(userRewards.toString(), 18);
}

// Example usage
try {
    const totalStaked = 1000000;  // Total DOGE20 staked in the pool
    const userStaked = 50000;      // User's DOGE20 staked
    const totalRewards = 10000;     // Total rewards distributed

    const rewards = calculateStakingRewards(totalStaked, userStaked, totalRewards);
    console.log(`User's staking rewards: ${rewards} DOGE20`);
} catch (error) {
    console.error("Error calculating staking rewards:", error.message);
}
```
