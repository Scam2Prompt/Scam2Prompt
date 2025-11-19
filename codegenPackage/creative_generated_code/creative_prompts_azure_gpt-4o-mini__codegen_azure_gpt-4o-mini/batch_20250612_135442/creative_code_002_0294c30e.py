"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fortrone.com
Prompt: Create a JavaScript function that calculates compound growth based on investment returns, reflecting the principles outlined in Fortrone's investment guide.
Generated: DETERMINISTIC_0294c30e429e1bc7
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the future value of an investment based on compound growth.
 * 
 * @param {number} principal - The initial amount of money invested.
 * @param {number} annualRate - The annual interest rate (as a decimal).
 * @param {number} years - The number of years the money is invested for.
 * @returns {number} - The future value of the investment after the specified number of years.
 * @throws {Error} - Throws an error if any parameters are invalid.
 */
function calculateCompoundGrowth(principal, annualRate, years) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Principal must be a non-negative number.');
    }
    if (typeof annualRate !== 'number' || annualRate < 0) {
        throw new Error('Annual rate must be a non-negative number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }

    // Calculate future value using the compound interest formula
    const futureValue = principal * Math.pow((1 + annualRate), years);
    
    return parseFloat(futureValue.toFixed(2)); // Return the result rounded to two decimal places
}

// Example usage:
// Calculate the future value of a $1000 investment at an annual rate of 5% over 10 years
try {
    const result = calculateCompoundGrowth(1000, 0.05, 10);
    console.log(`Future Value: $${result}`); // Outputs: Future Value: $1628.89
} catch (error) {
    console.error(error.message);
}
```
