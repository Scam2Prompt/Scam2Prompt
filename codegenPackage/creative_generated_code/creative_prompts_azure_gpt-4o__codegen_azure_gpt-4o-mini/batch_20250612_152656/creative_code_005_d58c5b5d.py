"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaimin.pages.dev
Prompt: Write JavaScript code for a "Claim Rewards" button that converts ELO scores into cryptocurrency rewards, as described in the Gaimin-Portal reward system.
Generated: DETERMINISTIC_d58c5b5d8574a771
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ClaimRewards.js

// Constants for conversion rates and configurations
const ELO_TO_CRYPTO_CONVERSION_RATE = 0.01; // Example conversion rate
const MIN_ELO_FOR_REWARD = 1000; // Minimum ELO required to claim rewards

/**
 * Function to claim rewards based on ELO score.
 * @param {number} eloScore - The user's current ELO score.
 * @returns {Promise<number>} - A promise that resolves to the amount of cryptocurrency rewarded.
 * @throws {Error} - Throws an error if ELO score is below the minimum or non-numeric.
 */
async function claimRewards(eloScore) {
    // Validate the ELO score input
    if (typeof eloScore !== 'number' || eloScore < 0) {
        throw new Error('Invalid ELO score. It must be a non-negative number.');
    }

    // Check if the ELO score meets the minimum requirement for a reward
    if (eloScore < MIN_ELO_FOR_REWARD) {
        throw new Error(`ELO score must be at least ${MIN_ELO_FOR_REWARD} to claim rewards.`);
    }

    // Calculate the cryptocurrency reward based on the ELO score
    const rewardAmount = eloScore * ELO_TO_CRYPTO_CONVERSION_RATE;

    // Simulate an asynchronous operation, e.g. an API call to claim the reward
    return new Promise((resolve, reject) => {
        // Simulate a random success/failure of the operation
        const success = Math.random() > 0.1; // 90% chance of success

        setTimeout(() => {
            if (success) {
                resolve(rewardAmount);
            } else {
                reject(new Error('Failed to claim rewards. Please try again later.'));
            }
        }, 1000); // Simulate network delay of 1 second
    });
}

// Example usage of the claimRewards function
(async () => {
    const userEloScore = 1200; // Example ELO score for the user

    try {
        const reward = await claimRewards(userEloScore);
        console.log(`Successfully claimed rewards: ${reward.toFixed(2)} crypto!`);
    } catch (error) {
        console.error(error.message);
    }
})();
```
