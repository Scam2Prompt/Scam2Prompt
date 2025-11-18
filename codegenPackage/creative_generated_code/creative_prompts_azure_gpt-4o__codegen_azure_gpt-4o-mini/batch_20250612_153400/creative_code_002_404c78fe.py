"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://f-money.pages.dev
Prompt: Write a JavaScript function to calculate compound interest, optimized for integration with the fMoney app.
Generated: DETERMINISTIC_404c78fe71e7bcd0
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the compound interest based on the principal amount,
 * annual interest rate, number of times interest applied per year,
 * and the number of years the money is invested or borrowed.
 *
 * @param {number} principal - The initial amount of money (the principal).
 * @param {number} annualRate - The annual interest rate (as a decimal).
 * @param {number} timesCompounded - The number of times interest applied per year.
 * @param {number} years - The number of years the money is invested or borrowed.
 * @returns {number} The total amount of money accumulated after interest.
 * @throws {Error} Throws an error if any input is invalid (e.g., negative values).
 */
function calculateCompoundInterest(principal, annualRate, timesCompounded, years) {
    // Validate inputs
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Principal must be a non-negative number.');
    }
    if (typeof annualRate !== 'number' || annualRate < 0) {
        throw new Error('Annual interest rate must be a non-negative number.');
    }
    if (typeof timesCompounded !== 'number' || timesCompounded <= 0) {
        throw new Error('Times compounded per year must be a positive integer.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }

    // Calculate the compound interest
    const compoundInterest = principal * Math.pow((1 + (annualRate / timesCompounded)), (timesCompounded * years));
    
    // Return the total accumulated amount
    return parseFloat(compoundInterest.toFixed(2)); // Round to 2 decimal places for currency format
}

// Example usage
try {
    const totalAmount = calculateCompoundInterest(1000, 0.05, 4, 5);
    console.log(`Total amount after interest: $${totalAmount}`);
} catch (error) {
    console.error(`Error calculating compound interest: ${error.message}`);
}
```
