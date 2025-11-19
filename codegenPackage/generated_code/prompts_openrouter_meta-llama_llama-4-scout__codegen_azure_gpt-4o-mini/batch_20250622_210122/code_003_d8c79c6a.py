"""
Generated Code Metadata:
========================
Original URL: https://shubaswap.com
Prompt: Create a JavaScript function to calculate daily bonuses and cashback rewards for users on a platform like MESIN128.
Generated: DETERMINISTIC_d8c79c6a9098e08e
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates daily bonuses and cashback rewards for users.
 * 
 * @param {number} totalSpent - The total amount spent by the user in a day.
 * @param {number} totalEarned - The total amount earned by the user in a day.
 * @returns {Object} An object containing the daily bonus and cashback rewards.
 * @throws {Error} Throws an error if the inputs are not valid numbers.
 */
function calculateRewards(totalSpent, totalEarned) {
    // Validate input types
    if (typeof totalSpent !== 'number' || typeof totalEarned !== 'number') {
        throw new Error('Invalid input: totalSpent and totalEarned must be numbers.');
    }

    // Validate input values
    if (totalSpent < 0 || totalEarned < 0) {
        throw new Error('Invalid input: totalSpent and totalEarned must be non-negative.');
    }

    // Define reward rates
    const bonusRate = 0.1; // 10% bonus on total earned
    const cashbackRate = 0.05; // 5% cashback on total spent

    // Calculate daily bonus and cashback
    const dailyBonus = totalEarned * bonusRate;
    const cashbackReward = totalSpent * cashbackRate;

    // Return the results as an object
    return {
        dailyBonus: parseFloat(dailyBonus.toFixed(2)), // Round to 2 decimal places
        cashbackReward: parseFloat(cashbackReward.toFixed(2)) // Round to 2 decimal places
    };
}

// Example usage
try {
    const rewards = calculateRewards(200, 150);
    console.log(`Daily Bonus: $${rewards.dailyBonus}, Cashback Reward: $${rewards.cashbackReward}`);
} catch (error) {
    console.error(error.message);
}
```
