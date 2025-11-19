"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon5.org
Prompt: Create a JavaScript function that simulates the process of rolling for Doge rewards on Moon5 and displays the results.
Generated: DETERMINISTIC_c141a7bd19f7529d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the process of rolling for Doge rewards on Moon5.
 * This function randomly generates a reward amount based on specified probabilities.
 * 
 * @returns {object} An object containing the roll result and the reward amount.
 * @throws {Error} Throws an error if the random number generation fails.
 */
function rollForDogeRewards() {
    try {
        // Define reward tiers and their corresponding probabilities
        const rewards = [
            { amount: 0, probability: 0.5 },  // 50% chance for no reward
            { amount: 10, probability: 0.3 }, // 30% chance for 10 Doge
            { amount: 50, probability: 0.15 }, // 15% chance for 50 Doge
            { amount: 100, probability: 0.04 }, // 4% chance for 100 Doge
            { amount: 500, probability: 0.01 }  // 1% chance for 500 Doge
        ];

        // Generate a random number between 0 and 1
        const randomNumber = Math.random();
        let cumulativeProbability = 0;

        // Iterate through the reward tiers to determine the reward amount
        for (const reward of rewards) {
            cumulativeProbability += reward.probability;

            // If the random number falls within the cumulative probability range, return the reward
            if (randomNumber <= cumulativeProbability) {
                return {
                    rollResult: randomNumber,
                    rewardAmount: reward.amount
                };
            }
        }
        
        // If no reward is found, throw an error (should not occur)
        throw new Error('Reward not found, something went wrong with the probabilities.');

    } catch (error) {
        console.error('Error during the roll for Doge rewards:', error.message);
        throw error; // Re-throw the error after logging it
    }
}

// Example usage:
try {
    const result = rollForDogeRewards();
    console.log(`Roll Result: ${result.rollResult}, Reward Amount: ${result.rewardAmount} Doge`);
} catch (error) {
    console.error('Failed to roll for Doge rewards:', error);
}
```
