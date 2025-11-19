"""
Generated Code Metadata:
========================
Original URL: https://bonaeac.com
Prompt: Generate a JavaScript function to calculate earnings based on a user's membership level (Junior, Intermediate, Premium, Professional) and the amount they have booked.
Generated: DETERMINISTIC_c87bc7a6b6e4a77f
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates earnings based on the user's membership level and the amount booked.
 * 
 * @param {string} membershipLevel - The membership level of the user (Junior, Intermediate, Premium, Professional).
 * @param {number} amountBooked - The amount booked by the user.
 * @returns {number} - The calculated earnings based on the membership level.
 * @throws {Error} - Throws an error if the membership level is invalid or if the amount booked is negative.
 */
function calculateEarnings(membershipLevel, amountBooked) {
    // Define the earnings multiplier for each membership level
    const earningsMultipliers = {
        Junior: 0.1,        // 10% for Junior members
        Intermediate: 0.15, // 15% for Intermediate members
        Premium: 0.2,       // 20% for Premium members
        Professional: 0.25   // 25% for Professional members
    };

    // Validate the membership level
    if (!earningsMultipliers.hasOwnProperty(membershipLevel)) {
        throw new Error(`Invalid membership level: ${membershipLevel}. Valid options are: ${Object.keys(earningsMultipliers).join(', ')}`);
    }

    // Validate the amount booked
    if (typeof amountBooked !== 'number' || amountBooked < 0) {
        throw new Error('Amount booked must be a non-negative number.');
    }

    // Calculate earnings
    const earnings = amountBooked * earningsMultipliers[membershipLevel];

    return earnings;
}

// Example usage:
try {
    const membership = 'Premium';
    const bookedAmount = 1000; // Example amount booked
    const earnings = calculateEarnings(membership, bookedAmount);
    console.log(`Earnings for ${membership} member: $${earnings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
