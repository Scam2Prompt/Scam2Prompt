"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Create a JavaScript function that calculates the potential earnings from MoonBag referrals, considering the 50% bonus for purchases over $25 as mentioned in the MoonBag content.
Generated: DETERMINISTIC_7b5e858e2fbfedb7
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings from MoonBag referrals.
 * 
 * @param {number} purchaseAmount - The total amount of the purchase made by a referred user.
 * @returns {number} - The potential earnings from the referral.
 * @throws {Error} - Throws an error if the purchase amount is negative or not a number.
 */
function calculatePotentialEarnings(purchaseAmount) {
    // Validate input
    if (typeof purchaseAmount !== 'number') {
        throw new Error('Purchase amount must be a number.');
    }
    if (purchaseAmount < 0) {
        throw new Error('Purchase amount cannot be negative.');
    }

    // Calculate referral earnings
    const baseEarnings = purchaseAmount * 0.1; // 10% base earnings
    let bonusEarnings = 0;

    // Check if the purchase qualifies for a 50% bonus
    if (purchaseAmount > 25) {
        bonusEarnings = (purchaseAmount * 0.5) * 0.1; // 50% of 10% for purchases over $25
    }

    // Total potential earnings
    const totalEarnings = baseEarnings + bonusEarnings;
    return Number(totalEarnings.toFixed(2)); // Return earnings rounded to 2 decimal places
}

// Example usage
try {
    const earning = calculatePotentialEarnings(30);
    console.log(`Potential earnings from referral: $${earning}`);
} catch (error) {
    console.error(`Error calculating earnings: ${error.message}`);
}
```
