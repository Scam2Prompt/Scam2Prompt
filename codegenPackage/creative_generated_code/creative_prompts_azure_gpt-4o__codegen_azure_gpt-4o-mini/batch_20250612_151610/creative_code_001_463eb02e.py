"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Create a function in JavaScript that calculates daily earnings and total ROI for the "Exclusive" tariff plan on MineBNB, given a deposit amount.
Generated: DETERMINISTIC_463eb02efd49d5fe
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates daily earnings and total ROI for the "Exclusive" tariff plan on MineBNB.
 * 
 * @param {number} depositAmount - The amount deposited in the "Exclusive" tariff plan.
 * @returns {Object} An object containing daily earnings and total ROI.
 * @throws {Error} Throws an error if depositAmount is not a positive number.
 */
function calculateExclusiveTariff(depositAmount) {
    // Validate input
    if (typeof depositAmount !== 'number' || depositAmount <= 0) {
        throw new Error('Deposit amount must be a positive number.');
    }

    // Constants for the "Exclusive" tariff plan
    const DAILY_INTEREST_RATE = 0.05; // 5% daily earnings
    const TOTAL_DAYS = 30; // Total duration for ROI calculation

    // Calculate daily earnings
    const dailyEarnings = depositAmount * DAILY_INTEREST_RATE;

    // Calculate total ROI after the specified duration
    const totalROI = depositAmount + (dailyEarnings * TOTAL_DAYS);

    // Return the results in an object
    return {
        dailyEarnings: dailyEarnings,
        totalROI: totalROI
    };
}

// Example usage
try {
    const deposit = 1000; // Example deposit amount
    const result = calculateExclusiveTariff(deposit);
    console.log(`Daily Earnings: $${result.dailyEarnings.toFixed(2)}`);
    console.log(`Total ROI: $${result.totalROI.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
