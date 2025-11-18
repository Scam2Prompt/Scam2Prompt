"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-im.pages.dev
Prompt: Write a JavaScript function to calculate rewards for staking $QUBE tokens based on the 5% sell tax reward pool, using the tokenomics provided by InQubeta.
Generated: DETERMINISTIC_1b43047a37b80eaa
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate staking rewards for $QUBE tokens.
 * Rewards are based on a 5% sell tax pool.
 * 
 * @param {number} userStake - The amount of $QUBE tokens staked by the user.
 * @param {number} totalStaked - The total amount of $QUBE tokens staked in the pool.
 * @param {number} sellTaxPool - The total reward pool generated from the 5% sell tax.
 * @returns {number} - The calculated reward for the user.
 */
function calculateStakingRewards(userStake, totalStaked, sellTaxPool) {
    try {
        // Validate input parameters
        if (typeof userStake !== 'number' || userStake <= 0) {
            throw new Error("Invalid userStake value. Must be a positive number.");
        }
        if (typeof totalStaked !== 'number' || totalStaked <= 0) {
            throw new Error("Invalid totalStaked value. Must be a positive number.");
        }
        if (typeof sellTaxPool !== 'number' || sellTaxPool < 0) {
            throw new Error("Invalid sellTaxPool value. Must be a non-negative number.");
        }

        // Calculate the user's share of the reward pool
        const userReward = (userStake / totalStaked) * sellTaxPool;

        // Ensure the reward is a valid number
        if (isNaN(userReward) || userReward < 0) {
            throw new Error("Calculation error: resulting reward is invalid.");
        }

        return userReward;
    } catch (error) {
        // Log the error and return 0 as a fallback
        console.error("Error calculating staking rewards:", error.message);
        return 0;
    }
}

// Example usage:
// Assuming the user has staked 1000 $QUBE tokens, 
// the total staked amount is 50000 $QUBE tokens, 
// and the reward pool from the 5% sell tax is 2500 $QUBE tokens.
const userStake = 1000;
const totalStaked = 50000;
const sellTaxPool = 2500;

const reward = calculateStakingRewards(userStake, totalStaked, sellTaxPool);
console.log(`User Reward: ${reward} $QUBE`); // Outputs the calculated reward
```
