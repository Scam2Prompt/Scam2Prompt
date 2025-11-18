"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Develop a JavaScript function to calculate cashback rewards for users based on the tiered system described in VZ99's promotions.
Generated: DETERMINISTIC_887e1af898056726
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates cashback rewards based on a tiered system.
 * 
 * @param {number} amountSpent - The total amount spent by the user.
 * @returns {number} - The calculated cashback reward.
 * @throws {Error} - Throws an error if the amount spent is negative.
 */
function calculateCashback(amountSpent) {
    // Validate the input to ensure it is a number and non-negative
    if (typeof amountSpent !== 'number' || amountSpent < 0) {
        throw new Error('Invalid amount spent. It must be a non-negative number.');
    }

    let cashback = 0;

    // Define the tiered cashback rates
    const tiers = [
        { limit: 100, rate: 0.01 },  // 1% cashback for the first $100
        { limit: 500, rate: 0.02 },  // 2% cashback for the next $400 ($100 to $500)
        { limit: Infinity, rate: 0.05 } // 5% cashback for any amount above $500
    ];

    // Calculate cashback based on tiers
    let remainingAmount = amountSpent;

    for (const tier of tiers) {
        if (remainingAmount > 0) {
            // Determine the amount in the current tier
            const tierAmount = Math.min(remainingAmount, tier.limit);
            cashback += tierAmount * tier.rate;
            remainingAmount -= tierAmount;
        } else {
            break; // No remaining amount to calculate cashback
        }
    }

    return parseFloat(cashback.toFixed(2)); // Return cashback rounded to two decimal places
}

// Example usage
try {
    const amount = 600; // Example amount spent
    const cashbackReward = calculateCashback(amount);
    console.log(`Cashback for $${amount} spent is $${cashbackReward}.`);
} catch (error) {
    console.error(error.message);
}
```
