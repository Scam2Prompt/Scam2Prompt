"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Write a JavaScript function that calculates potential ROI based on MINE BNB's tariff plans, specifically for the Exclusive plan with a 15% daily rate.
Generated: DETERMINISTIC_a925ac3bd6d82d0b
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential Return on Investment (ROI) for the Exclusive plan
 * based on MINE BNB's daily rate of 15%.
 *
 * @param {number} investment - The initial investment amount in BNB.
 * @param {number} days - The number of days the investment will be held.
 * @returns {number} - The total amount after the specified number of days.
 * @throws {Error} - Throws an error if the investment or days are negative.
 */
function calculateROI(investment, days) {
    // Validate the input parameters
    if (typeof investment !== 'number' || investment < 0) {
        throw new Error('Investment must be a non-negative number.');
    }
    if (typeof days !== 'number' || days < 0) {
        throw new Error('Days must be a non-negative number.');
    }

    // Daily rate for the Exclusive plan
    const dailyRate = 0.15;

    // Calculate the total amount after the specified number of days
    const totalAmount = investment * Math.pow((1 + dailyRate), days);
    
    return totalAmount;
}

// Example usage
try {
    const initialInvestment = 1; // Example investment in BNB
    const investmentDuration = 30; // Example duration in days

    const potentialReturn = calculateROI(initialInvestment, investmentDuration);
    console.log(`Potential Return after ${investmentDuration} days: ${potentialReturn.toFixed(2)} BNB`);
} catch (error) {
    console.error('Error calculating ROI:', error.message);
}
```
