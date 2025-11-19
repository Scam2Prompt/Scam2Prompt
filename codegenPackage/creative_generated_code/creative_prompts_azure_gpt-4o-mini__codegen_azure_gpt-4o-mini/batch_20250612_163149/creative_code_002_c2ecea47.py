"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Create a JavaScript function that calculates the potential earnings from the BTFD referral program based on the number of referrals and their purchases.
Generated: DETERMINISTIC_c2ecea47f3cc81df
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings from the BTFD referral program.
 * 
 * @param {number} referrals - The number of referrals made.
 * @param {number} avgPurchase - The average purchase amount made by each referral.
 * @param {number} commissionRate - The commission rate as a decimal (e.g., 0.1 for 10%).
 * @returns {number} The total potential earnings from the referrals.
 * @throws {Error} Throws an error if any input is invalid (negative numbers or non-numbers).
 */
function calculatePotentialEarnings(referrals, avgPurchase, commissionRate) {
    // Validate input types and values
    if (typeof referrals !== 'number' || typeof avgPurchase !== 'number' || typeof commissionRate !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    if (referrals < 0 || avgPurchase < 0 || commissionRate < 0) {
        throw new Error('Inputs must not be negative.');
    }

    // Calculate potential earnings
    const totalEarnings = referrals * avgPurchase * commissionRate;

    // Return the calculated total earnings
    return totalEarnings;
}

// Example usage:
try {
    const earnings = calculatePotentialEarnings(10, 100, 0.1);
    console.log(`Potential earnings from referrals: $${earnings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
