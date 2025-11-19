"""
Generated Code Metadata:
========================
Original URL: https://financeforcetd.com
Prompt: "Generate a JavaScript function to simulate the earnings of an investor with a $5000 deposit in the Flexible Plan, with a 6% daily return and a 10% referral bonus."
Generated: DETERMINISTIC_22c95aafe4d1ccd5
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the earnings of an investor in a Flexible Plan.
 * 
 * @param {number} initialDeposit - The initial amount deposited by the investor.
 * @param {number} dailyReturnRate - The daily return rate as a decimal.
 * @param {number} referralBonusRate - The referral bonus rate as a decimal.
 * @param {number} days - The number of days to simulate earnings for.
 * @returns {object} - An object containing total earnings and total amount after the specified days.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function simulateEarnings(initialDeposit, dailyReturnRate, referralBonusRate, days) {
    // Validate inputs
    if (typeof initialDeposit !== 'number' || initialDeposit <= 0) {
        throw new Error('Initial deposit must be a positive number.');
    }
    if (typeof dailyReturnRate !== 'number' || dailyReturnRate < 0) {
        throw new Error('Daily return rate must be a non-negative number.');
    }
    if (typeof referralBonusRate !== 'number' || referralBonusRate < 0) {
        throw new Error('Referral bonus rate must be a non-negative number.');
    }
    if (typeof days !== 'number' || days < 0) {
        throw new Error('Days must be a non-negative integer.');
    }

    // Initialize variables
    let totalEarnings = 0;
    let totalAmount = initialDeposit;

    // Simulate earnings over the specified number of days
    for (let day = 1; day <= days; day++) {
        // Calculate daily earnings
        const dailyEarnings = totalAmount * dailyReturnRate;
        totalEarnings += dailyEarnings;
        totalAmount += dailyEarnings;

        // Apply referral bonus (for demonstration, we assume a referral bonus is applied every day)
        const referralBonus = totalAmount * referralBonusRate;
        totalEarnings += referralBonus;
        totalAmount += referralBonus;
    }

    // Return the results
    return {
        totalEarnings: totalEarnings.toFixed(2), // Format to 2 decimal places
        totalAmount: totalAmount.toFixed(2) // Format to 2 decimal places
    };
}

// Example usage
try {
    const initialDeposit = 5000; // Initial deposit amount
    const dailyReturnRate = 0.06; // 6% daily return
    const referralBonusRate = 0.10; // 10% referral bonus
    const days = 30; // Simulate for 30 days

    const result = simulateEarnings(initialDeposit, dailyReturnRate, referralBonusRate, days);
    console.log(`Total Earnings: $${result.totalEarnings}`);
    console.log(`Total Amount after ${days} days: $${result.totalAmount}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
