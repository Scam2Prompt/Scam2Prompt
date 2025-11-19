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
 * Calculates compound interest on an investment.
 * 
 * @param {number} principal - The initial amount of money invested or loaned.
 * @param {number} rate - The annual interest rate (in decimal form, e.g., 5% as 0.05).
 * @param {number} timesCompounded - The number of times the interest is compounded per year.
 * @param {number} years - The number of years the money is invested for.
 * @returns {number} - The total amount after compound interest is applied.
 * @throws {Error} - If any parameter is invalid (e.g., negative values or non-numeric input).
 */
function calculateCompoundInterest(principal, rate, timesCompounded, years) {
  // Validate input parameters
  if (
    typeof principal !== 'number' || principal < 0 ||
    typeof rate !== 'number' || rate < 0 ||
    typeof timesCompounded !== 'number' || timesCompounded <= 0 ||
    typeof years !== 'number' || years < 0
  ) {
    throw new Error('Invalid input: All parameters must be non-negative numbers, and timesCompounded must be greater than 0.');
  }

  // Compound interest formula: A = P(1 + r/n)^(n*t)
  const compoundFactor = Math.pow(1 + rate / timesCompounded, timesCompounded * years);
  const totalAmount = principal * compoundFactor;

  return totalAmount;
}

// Example usage:
try {
  const principal = 1000; // Initial investment
  const rate = 0.05; // Annual interest rate (5%)
  const timesCompounded = 4; // Compounded quarterly
  const years = 10; // Duration of investment in years

  const result = calculateCompoundInterest(principal, rate, timesCompounded, years);
  console.log(`Total amount after ${years} years: $${result.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
