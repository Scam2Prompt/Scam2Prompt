"""
Generated Code Metadata:
========================
Original URL: https://scotty-ai.pages.dev
Prompt: Generate a JavaScript function to display the total staked $SCOTTY tokens, the user's percentage of the staking pool, and their estimated rewards based on the provided data.
Generated: DETERMINISTIC_4a9efef0c8405789
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates and displays the total staked $SCOTTY tokens, 
 * the user's percentage of the staking pool, and their estimated rewards.
 */

/**
 * @typedef {Object} StakingData
 * @property {number} totalStaked - The total amount of $SCOTTY tokens staked.
 * @property {number} userStaked - The amount of $SCOTTY tokens staked by the user.
 * @property {number} rewardRate - The estimated reward rate as a decimal.
 */

/**
 * Calculates and displays staking information.
 * 
 * @param {StakingData} stakingData - The staking data.
 */
function displayStakingInfo(stakingData) {
    try {
        // Check if stakingData is valid
        if (!stakingData || typeof stakingData !== 'object') {
            throw new Error('Invalid staking data');
        }

        const { totalStaked, userStaked, rewardRate } = stakingData;

        // Check for valid numbers
        if (typeof totalStaked !== 'number' || typeof userStaked !== 'number' || typeof rewardRate !== 'number') {
            throw new Error('Invalid staking data values');
        }

        // Check for non-positive numbers
        if (totalStaked <= 0 || userStaked < 0 || rewardRate < 0) {
            throw new Error('Staking data values must be positive numbers');
        }

        // Calculate user's percentage of the staking pool
        const userPercentage = (userStaked / totalStaked) * 100;

        // Calculate estimated rewards
        const estimatedRewards = userStaked * rewardRate;

        // Display staking information
        console.log(`Total staked $SCOTTY tokens: ${totalStaked}`);
        console.log(`Your staked $SCOTTY tokens: ${userStaked}`);
        console.log(`Your percentage of the staking pool: ${userPercentage.toFixed(2)}%`);
        console.log(`Estimated rewards: ${estimatedRewards.toFixed(2)} $SCOTTY tokens`);
    } catch (error) {
        console.error('Error displaying staking info:', error.message);
    }
}

// Example usage:
const stakingData = {
    totalStaked: 1000000,
    userStaked: 50000,
    rewardRate: 0.05
};

displayStakingInfo(stakingData);
```
