"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guiweb.worldlibertyfonancial.com
Prompt: "Write a JavaScript function that calculates compound interest based on user input for principal, rate, and time."
Generated: DETERMINISTIC_c61b35dff94be255
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates compound interest based on user input.
 * 
 * @param {number} principal - The initial amount of money (the principal).
 * @param {number} rate - The annual interest rate (in percentage).
 * @param {number} time - The time the money is invested or borrowed for (in years).
 * @returns {number} - The total amount after interest is applied.
 * @throws {Error} - Throws an error if any of the parameters are invalid.
 */
function calculateCompoundInterest(principal, rate, time) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Invalid principal amount. It must be a positive number.');
    }
    if (typeof rate !== 'number' || rate < 0) {
        throw new Error('Invalid interest rate. It cannot be negative.');
    }
    if (typeof time !== 'number' || time < 0) {
        throw new Error('Invalid time period. It cannot be negative.');
    }

    // Convert rate from percentage to a decimal
    const decimalRate = rate / 100;

    // Calculate compound interest using the formula A = P(1 + r)^t
    const amount = principal * Math.pow((1 + decimalRate), time);

    // Return the total amount after interest
    return amount;
}

// Example usage:
try {
    const principal = 1000;  // Initial amount
    const rate = 5;          // Annual interest rate in percentage
    const time = 10;         // Time in years

    const totalAmount = calculateCompoundInterest(principal, rate, time);
    console.log(`Total amount after ${time} years is: $${totalAmount.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating compound interest: ${error.message}`);
}
```
