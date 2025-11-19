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
 * Calculates earnings based on a user's membership level and the amount they have booked.
 * 
 * @param {string} membershipLevel - The user's membership level (Junior, Intermediate, Premium, Professional)
 * @param {number} amountBooked - The amount the user has booked
 * @returns {number} The calculated earnings
 */
function calculateEarnings(membershipLevel, amountBooked) {
    // Define the commission rates for each membership level
    const commissionRates = {
        Junior: 0.05, // 5%
        Intermediate: 0.10, // 10%
        Premium: 0.15, // 15%
        Professional: 0.20 // 20%
    };

    // Check if the membership level is valid
    if (!(membershipLevel in commissionRates)) {
        throw new Error(`Invalid membership level: ${membershipLevel}`);
    }

    // Check if the amount booked is a positive number
    if (typeof amountBooked !== 'number' || amountBooked <= 0) {
        throw new Error('Amount booked must be a positive number');
    }

    // Calculate the earnings
    const commissionRate = commissionRates[membershipLevel];
    const earnings = amountBooked * commissionRate;

    return earnings;
}

// Example usage:
try {
    const membershipLevel = 'Premium';
    const amountBooked = 1000;
    const earnings = calculateEarnings(membershipLevel, amountBooked);
    console.log(`Earnings for ${membershipLevel} member: $${earnings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
