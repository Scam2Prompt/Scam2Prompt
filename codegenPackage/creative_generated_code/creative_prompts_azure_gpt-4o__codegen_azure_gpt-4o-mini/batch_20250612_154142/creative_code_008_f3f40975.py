"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freefinance.pages.dev
Prompt: Write a function to calculate compound interest in JavaScript, referencing concepts from freefinance.pages.dev.
Generated: DETERMINISTIC_f3f40975b3924cfa
Batch ID: 20250612_154142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the compound interest for a given principal amount, interest rate, 
 * number of times interest applied per time period, and the total number of time periods.
 *
 * @param {number} principal - The initial amount of money (the principal).
 * @param {number} rate - The annual interest rate (in decimal form, e.g., 5% = 0.05).
 * @param {number} timesCompounded - The number of times that interest is compounded per year.
 * @param {number} years - The number of years the money is invested or borrowed for.
 * @returns {number} - The amount of money accumulated after n years, including interest.
 * @throws {Error} - Throws an error if any arguments are not valid numbers or less than zero.
 */
function calculateCompoundInterest(principal, rate, timesCompounded, years) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Principal must be a non-negative number.');
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

    // Calculate compound interest using the formula
    const amount = principal * Math.pow((1 + rate / timesCompounded), timesCompounded * years);
    
    // Return the final amount
    return parseFloat(amount.toFixed(2)); // Return the amount rounded to 2 decimal places
}

// Example usage:
try {
    const principal = 1000;   // Initial investment
    const rate = 0.05;       // 5% interest rate
    const timesCompounded = 4; // Quarterly compounding
    const years = 5;         // Duration of investment in years

    const finalAmount = calculateCompoundInterest(principal, rate, timesCompounded, years);
    console.log(`Final amount after ${years} years: $${finalAmount}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
