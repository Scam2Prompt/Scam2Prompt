"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: Create a JavaScript function that simulates the process of rolling for Doge rewards on Moon5 and displays the results.
Generated: DETERMINISTIC_c141a7bd19f7529d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the process of rolling for Doge rewards on Moon5.
 * 
 * @param {number} balance - The user's current balance.
 * @param {number} rollAmount - The amount to roll for.
 * @param {number} chance - The chance of winning (between 0 and 1).
 * @returns {object} An object containing the result of the roll.
 */
function rollForDogeRewards(balance, rollAmount, chance) {
    // Check if the balance and roll amount are valid
    if (balance <= 0 || rollAmount <= 0) {
        throw new Error("Balance and roll amount must be greater than 0.");
    }

    // Check if the chance is valid
    if (chance < 0 || chance > 1) {
        throw new Error("Chance must be between 0 and 1.");
    }

    // Check if the user has sufficient balance
    if (balance < rollAmount) {
        throw new Error("Insufficient balance.");
    }

    // Simulate the roll
    const rollResult = Math.random() < chance;

    // Calculate the new balance
    let newBalance;
    if (rollResult) {
        // Generate a random reward amount
        const rewardAmount = Math.floor(Math.random() * 100) + 1;
        newBalance = balance + rewardAmount - rollAmount;
        return {
            success: true,
            rewardAmount,
            newBalance,
        };
    } else {
        newBalance = balance - rollAmount;
        return {
            success: false,
            newBalance,
        };
    }
}

// Example usage
try {
    const balance = 1000;
    const rollAmount = 10;
    const chance = 0.1; // 10% chance of winning

    const result = rollForDogeRewards(balance, rollAmount, chance);
    console.log(`Roll result: ${result.success ? "Win" : "Loss"}`);
    console.log(`New balance: ${result.newBalance}`);
    if (result.success) {
        console.log(`Reward amount: ${result.rewardAmount}`);
    }
} catch (error) {
    console.error(error.message);
}
```
