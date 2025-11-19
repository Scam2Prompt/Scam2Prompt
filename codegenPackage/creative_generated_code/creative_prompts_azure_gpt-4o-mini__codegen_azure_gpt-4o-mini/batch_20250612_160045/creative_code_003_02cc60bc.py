"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Develop a JavaScript function to calculate cashback rewards based on user losses in a betting platform like BaxBet.
Generated: DETERMINISTIC_02cc60bc94ab9d6e
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates cashback rewards based on user losses.
 * @param {number} totalLosses - The total losses incurred by the user.
 * @param {number} cashbackRate - The cashback rate as a percentage (0-100).
 * @returns {number} - The calculated cashback amount.
 * @throws {Error} - Throws an error if totalLosses or cashbackRate is invalid.
 */
function calculateCashback(totalLosses, cashbackRate) {
    // Validate input parameters
    if (typeof totalLosses !== 'number' || typeof cashbackRate !== 'number') {
        throw new Error('Both totalLosses and cashbackRate must be numbers.');
    }
    if (totalLosses < 0) {
        throw new Error('Total losses cannot be negative.');
    }
    if (cashbackRate < 0 || cashbackRate > 100) {
        throw new Error('Cashback rate must be between 0 and 100.');
    }

    // Calculate the cashback amount
    const cashbackAmount = (totalLosses * (cashbackRate / 100));

    // Return the calculated cashback amount rounded to two decimal places
    return parseFloat(cashbackAmount.toFixed(2));
}

// Example usage
try {
    const userLosses = 250; // Example total losses
    const userCashbackRate = 10; // Example cashback rate
    const cashback = calculateCashback(userLosses, userCashbackRate);
    console.log(`Cashback earned: $${cashback}`);
} catch (error) {
    console.error(`Error calculating cashback: ${error.message}`);
}
```
