"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Generate a JavaScript function to display the total staked $SCOTTY tokens, the user's percentage of the staking pool, and their estimated rewards based on the provided data.
Generated: DETERMINISTIC_4a9efef0c8405789
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate and display staking details for $SCOTTY tokens.
 * @param {number} userStake - The amount of $SCOTTY tokens staked by the user.
 * @param {number} totalStakePool - The total amount of $SCOTTY tokens in the staking pool.
 * @param {number} totalRewards - The total rewards distributed for the staking pool.
 * @returns {Object} Returns an object with the user's staking details.
 */
function getStakingDetails(userStake, totalStakePool, totalRewards) {
    try {
        // Validate inputs
        if (typeof userStake !== 'number' || userStake < 0) {
            throw new Error("Invalid user stake. Must be a positive number.");
        }
        if (typeof totalStakePool !== 'number' || totalStakePool <= 0) {
            throw new Error("Invalid total stake pool. Must be a positive number.");
        }
        if (typeof totalRewards !== 'number' || totalRewards < 0) {
            throw new Error("Invalid total rewards. Must be a positive number.");
        }

        // Calculate user's percentage of the staking pool
        const userPercentage = (userStake / totalStakePool) * 100;

        // Calculate user's estimated rewards based on their percentage
        const estimatedRewards = (userPercentage / 100) * totalRewards;

        // Display results (you can customize this as needed for a UI)
        console.log("=== Staking Details ===");
        console.log(`Total Staked: ${totalStakePool.toFixed(2)} $SCOTTY`);
        console.log(`Your Stake: ${userStake.toFixed(2)} $SCOTTY`);
        console.log(`Your Percentage of Pool: ${userPercentage.toFixed(2)}%`);
        console.log(`Your Estimated Rewards: ${estimatedRewards.toFixed(2)} $SCOTTY`);

        // Return results for further use
        return {
            totalStaked: totalStakePool.toFixed(2),
            userStake: userStake.toFixed(2),
            userPercentage: userPercentage.toFixed(2),
            estimatedRewards: estimatedRewards.toFixed(2),
        };
    } catch (error) {
        // Handle errors gracefully
        console.error("Error calculating staking details:", error.message);
        return null;
    }
}

// Example usage:
const userStake = 500; // User's staked $SCOTTY tokens
const totalStakePool = 10000; // Total staked $SCOTTY tokens in the pool
const totalRewards = 2000; // Total rewards distributed for the staking pool

getStakingDetails(userStake, totalStakePool, totalRewards);
```
