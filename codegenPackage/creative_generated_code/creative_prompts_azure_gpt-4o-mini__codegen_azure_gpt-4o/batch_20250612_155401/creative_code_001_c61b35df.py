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
 * Calculates compound interest based on the provided principal, rate, and time.
 * 
 * Formula: A = P * (1 + r/n)^(n*t)
 * Where:
 * A = Final amount including interest
 * P = Principal amount
 * r = Annual interest rate (as a decimal, e.g., 5% => 0.05)
 * n = Number of times interest is compounded per year (default: 1 for yearly compounding)
 * t = Time the money is invested or borrowed for, in years
 * 
 * @param {number} principal - The initial amount of money (P).
 * @param {number} rate - The annual interest rate as a percentage (e.g., 5 for 5%).
 * @param {number} time - The time in years (t).
 * @param {number} [compoundsPerYear=1] - The number of times interest is compounded per year (n).
 * @returns {number} The calculated compound interest.
 * @throws {Error} If any input is invalid or non-positive.
 */
function calculateCompoundInterest(principal, rate, time, compoundsPerYear = 1) {
    // Validate input types and values
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error("Principal must be a positive number.");
    }
    if (typeof rate !== 'number' || rate <= 0) {
        throw new Error("Rate must be a positive number.");
    }
    if (typeof time !== 'number' || time <= 0) {
        throw new Error("Time must be a positive number.");
    }
    if (typeof compoundsPerYear !== 'number' || compoundsPerYear <= 0) {
        throw new Error("Compounds per year must be a positive number.");
    }

    // Convert annual rate percentage to a decimal
    const annualRateDecimal = rate / 100;

    // Apply compound interest formula: A = P * (1 + r/n)^(n*t)
    const amount = principal * Math.pow((1 + annualRateDecimal / compoundsPerYear), compoundsPerYear * time);

    // Round to two decimal places for precision
    const compoundInterest = parseFloat(amount.toFixed(2));

    return compoundInterest;
}

// Example usage:
try {
    const principal = 1000; // Initial amount ($1000)
    const rate = 5;         // Annual interest rate (5%)
    const time = 10;        // Investment period (10 years)
    const compoundsPerYear = 4; // Interest compounded quarterly

    const result = calculateCompoundInterest(principal, rate, time, compoundsPerYear);
    console.log(`Compound Interest Result: $${result}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
