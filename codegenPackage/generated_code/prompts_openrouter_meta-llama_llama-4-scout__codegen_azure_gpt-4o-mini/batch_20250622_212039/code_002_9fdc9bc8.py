"""
Generated Code Metadata:
========================
Original URL: https://bits-capitalearn.com
Prompt: "Write a JavaScript function to simulate the hourly interest earnings for a GOLD PLAN investor on bits-capitalearn.com, assuming a 15% interest rate after 30 hours."
Generated: DETERMINISTIC_9fdc9bc80c9071e9
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the hourly interest earnings for a GOLD PLAN investor on bits-capitalearn.com.
 * 
 * @param {number} principal - The initial amount of investment.
 * @param {number} hours - The number of hours the investment is held.
 * @returns {number} - The total amount after interest is applied.
 * @throws {Error} - Throws an error if the principal is not a positive number or if hours is not a positive integer.
 */
function calculateGoldPlanEarnings(principal, hours) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof hours !== 'number' || hours <= 0 || !Number.isInteger(hours)) {
        throw new Error('Hours must be a positive integer.');
    }

    const interestRate = 0.15; // 15% interest rate
    const totalInterest = (principal * interestRate); // Total interest after 30 hours
    const totalAmount = principal + totalInterest; // Total amount after interest

    return totalAmount; // Return the total amount after interest
}

// Example usage
try {
    const initialInvestment = 1000; // Example principal amount
    const investmentHours = 30; // Example hours
    const earnings = calculateGoldPlanEarnings(initialInvestment, investmentHours);
    console.log(`Total amount after ${investmentHours} hours: $${earnings.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
