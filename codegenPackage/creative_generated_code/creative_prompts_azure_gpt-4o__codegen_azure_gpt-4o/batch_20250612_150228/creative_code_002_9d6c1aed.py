"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testopolistomarta.pages.dev
Prompt: Generate a function in JavaScript to calculate and display "Notcoin" rewards in both token amounts and USD₮ based on user activity.
Generated: DETERMINISTIC_9d6c1aed37b3afa2
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
 * Function to calculate and display Notcoin rewards in token amounts and USD₮ based on user activity.
 * @param {number} activityScore - The user's activity score (e.g., points earned from activity).
 * @param {number} tokenRate - The reward rate, i.e., tokens per activity score unit.
 * @param {number} usdRate - The value of 1 token in USD₮.
 * @returns {object} An object containing the rewards in tokens and USD₮.
 */
function calculateNotcoinRewards(activityScore, tokenRate, usdRate) {
    try {
        // Input validation
        if (typeof activityScore !== 'number' || activityScore < 0) {
            throw new Error("Invalid activityScore. It must be a non-negative number.");
        }
        if (typeof tokenRate !== 'number' || tokenRate <= 0) {
            throw new Error("Invalid tokenRate. It must be a positive number.");
        }
        if (typeof usdRate !== 'number' || usdRate <= 0) {
            throw new Error("Invalid usdRate. It must be a positive number.");
        }

        // Calculate rewards in tokens and USD₮
        const rewardsInTokens = activityScore * tokenRate;
        const rewardsInUsd = rewardsInTokens * usdRate;

        // Display rewards
        console.log(`Rewards:`);
        console.log(`- Tokens: ${rewardsInTokens.toFixed(2)}`);
        console.log(`- USD₮: ${rewardsInUsd.toFixed(2)}`);

        // Return rewards as an object
        return {
            tokens: rewardsInTokens,
            usd: rewardsInUsd,
        };
    } catch (error) {
        // Handle errors and display meaningful messages
        console.error(`Error calculating rewards: ${error.message}`);
        return null;
    }
}

// Example usage:
// Define inputs
const activityScore = 150; // Example user activity score
const tokenRate = 0.5; // Example tokens per activity score unit
const usdRate = 1.2; // Example value of 1 Notcoin token in USD₮

// Calculate and display rewards
calculateNotcoinRewards(activityScore, tokenRate, usdRate);
```
