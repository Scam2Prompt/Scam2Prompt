"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Create a JavaScript function using ethers.js to calculate staking rewards for $STARS holders based on the dynamic APY model outlined in the Crypto All-Stars platform.
Generated: DETERMINISTIC_07d174243b404302
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the ethers.js library
const { ethers } = require("ethers");

/**
 * Calculate staking rewards for $STARS holders based on a dynamic APY model.
 * 
 * @param {string} stakerAddress - The wallet address of the $STARS holder.
 * @param {number} amountStaked - The amount of $STARS tokens staked.
 * @param {number} daysStaked - The number of days the tokens have been staked.
 * @param {number} dynamicAPY - The dynamic annual percentage yield as a decimal (e.g., 0.05 for 5%).
 * @returns {Promise<number>} - The calculated staking rewards in $STARS tokens.
 * @throws {Error} - Throws an error if input values are invalid.
 */
async function calculateStakingRewards(stakerAddress, amountStaked, daysStaked, dynamicAPY) {
    // Input validation
    if (!ethers.utils.isAddress(stakerAddress)) {
        throw new Error("Invalid staker address.");
    }
    if (amountStaked <= 0) {
        throw new Error("Amount staked must be greater than zero.");
    }
    if (daysStaked < 0) {
        throw new Error("Days staked cannot be negative.");
    }
    if (dynamicAPY < 0) {
        throw new Error("APY cannot be negative.");
    }

    try {
        // Calculate the reward based on the formula: rewards = (amountStaked * dynamicAPY * daysStaked) / 365
        const rewards = (amountStaked * dynamicAPY * daysStaked) / 365;
        return rewards;
    } catch (error) {
        // Handle any unexpected errors
        console.error("Error calculating staking rewards:", error);
        throw new Error("Failed to calculate staking rewards.");
    }
}

// Example usage (uncomment to test):
// (async () => {
//     try {
//         const rewards = await calculateStakingRewards("0xYourAddressHere", 1000, 30, 0.05);
//         console.log(`Staking rewards: ${rewards} $STARS`);
//     } catch (error) {
//         console.error(error.message);
//     }
// })();
```
