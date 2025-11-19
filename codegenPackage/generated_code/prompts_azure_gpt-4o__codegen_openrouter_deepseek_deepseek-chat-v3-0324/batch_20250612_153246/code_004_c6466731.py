"""
Generated Code Metadata:
========================
Original URL: https://diskonin.id
Prompt: Write a function in JavaScript to calculate cashback or discounts (e.g., 100% cashback) for slot game deposits based on promotional offers.
Generated: DETERMINISTIC_c646673183898546
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates cashback or discounts for slot game deposits based on promotional offers.
 * @param {number} depositAmount - The original deposit amount.
 * @param {number} cashbackPercentage - The cashback percentage (e.g., 100 for 100% cashback).
 * @param {number} [maxCashback] - Optional maximum cashback amount.
 * @returns {number} The calculated cashback amount.
 * @throws {Error} If depositAmount or cashbackPercentage is invalid.
 */
function calculateCashback(depositAmount, cashbackPercentage, maxCashback) {
    // Validate input parameters
    if (typeof depositAmount !== 'number' || depositAmount <= 0) {
        throw new Error('Invalid deposit amount. Must be a positive number.');
    }
    if (typeof cashbackPercentage !== 'number' || cashbackPercentage < 0) {
        throw new Error('Invalid cashback percentage. Must be a non-negative number.');
    }
    if (maxCashback !== undefined && (typeof maxCashback !== 'number' || maxCashback < 0)) {
        throw new Error('Invalid max cashback. Must be a non-negative number if provided.');
    }

    // Calculate cashback
    let cashback = depositAmount * (cashbackPercentage / 100);

    // Apply max cashback limit if provided
    if (maxCashback !== undefined && cashback > maxCashback) {
        cashback = maxCashback;
    }

    // Round to 2 decimal places for currency
    return parseFloat(cashback.toFixed(2));
}

// Example usage:
// try {
//     const cashback = calculateCashback(100, 50, 30); // 50% cashback, max $30
//     console.log(`Cashback amount: $${cashback}`);
// } catch (error) {
//     console.error(`Error calculating cashback: ${error.message}`);
// }
```
