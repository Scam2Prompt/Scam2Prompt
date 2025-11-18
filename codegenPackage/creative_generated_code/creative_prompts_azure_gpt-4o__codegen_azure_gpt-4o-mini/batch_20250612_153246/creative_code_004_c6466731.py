"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Write a function in JavaScript to calculate cashback or discounts (e.g., 100% cashback) for slot game deposits based on promotional offers.
Generated: DETERMINISTIC_c646673183898546
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cashback or discount for a slot game deposit based on promotional offers.
 * 
 * @param {number} depositAmount - The amount deposited by the player.
 * @param {number} cashbackPercentage - The percentage of cashback to be applied (0-100).
 * @param {number} maxCashback - The maximum cashback amount that can be applied.
 * @returns {number} - The calculated cashback amount.
 * @throws {Error} - Throws an error if depositAmount is negative, cashbackPercentage is out of range, 
 *                   or maxCashback is negative.
 */
function calculateCashback(depositAmount, cashbackPercentage, maxCashback) {
    // Validate input parameters
    if (depositAmount < 0) {
        throw new Error('Deposit amount must be a non-negative number.');
    }
    if (cashbackPercentage < 0 || cashbackPercentage > 100) {
        throw new Error('Cashback percentage must be between 0 and 100.');
    }
    if (maxCashback < 0) {
        throw new Error('Maximum cashback must be a non-negative number.');
    }

    // Calculate the potential cashback based on the deposit amount and cashback percentage
    const potentialCashback = (depositAmount * (cashbackPercentage / 100));

    // Return the lesser of the potential cashback or the maximum cashback allowed
    return Math.min(potentialCashback, maxCashback);
}

// Example usage:
try {
    const deposit = 100; // Amount deposited
    const cashbackRate = 100; // 100% cashback
    const maxCashbackAllowed = 50; // Maximum cashback allowed

    const cashback = calculateCashback(deposit, cashbackRate, maxCashbackAllowed);
    console.log(`Calculated cashback: $${cashback.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating cashback: ${error.message}`);
}
```
