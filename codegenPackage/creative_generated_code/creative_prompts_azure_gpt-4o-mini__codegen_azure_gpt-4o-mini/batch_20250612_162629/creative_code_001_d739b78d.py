"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Write a function in JavaScript that calculates the compound interest on an investment over a specified number of years.
Generated: DETERMINISTIC_d739b78d380f8126
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the compound interest on an investment.
 *
 * @param {number} principal - The initial amount of money invested.
 * @param {number} rate - The annual interest rate (in decimal).
 * @param {number} timesCompounded - The number of times that interest is compounded per year.
 * @param {number} years - The number of years the money is invested or borrowed for.
 * @returns {number} The total amount after interest.
 * @throws {Error} If any parameter is invalid (non-positive or non-numeric).
 */
function calculateCompoundInterest(principal, rate, timesCompounded, years) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof rate !== 'number' || rate < 0) {
        throw new Error('Rate must be a non-negative number.');
    }
    if (typeof timesCompounded !== 'number' || timesCompounded <= 0) {
        throw new Error('Times compounded must be a positive integer.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }

    // Calculate compound interest
    const amount = principal * Math.pow((1 + rate / timesCompounded), (timesCompounded * years));
    
    // Return the total amount after interest
    return amount;
}

// Example usage:
// const totalAmount = calculateCompoundInterest(1000, 0.05, 4, 5);
// console.log(`Total amount after interest: $${totalAmount.toFixed(2)}`);
```
