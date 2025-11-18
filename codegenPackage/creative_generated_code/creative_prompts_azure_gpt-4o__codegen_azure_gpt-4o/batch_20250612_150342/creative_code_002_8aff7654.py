"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-app-9i4.pages.dev
Prompt: Create a JavaScript function that calculates compound interest for a financial app like Tianguis Finance.
Generated: DETERMINISTIC_8aff7654a4d87b9e
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates compound interest.
 * 
 * Formula: A = P * (1 + r / n)^(n * t)
 * Where:
 *   A = the future value of the investment/loan, including interest
 *   P = the principal investment amount (initial deposit or loan amount)
 *   r = annual interest rate (in decimal form, e.g., 5% -> 0.05)
 *   n = number of times that interest is compounded per year
 *   t = time the money is invested/borrowed for in years
 * 
 * @param {number} principal - The initial amount of money (P).
 * @param {number} rate - The annual interest rate in percentage (e.g., 5 for 5%).
 * @param {number} timesCompounded - Number of times interest is compounded per year (n).
 * @param {number} years - Time in years the money is invested/borrowed (t).
 * @returns {number} - The future value of the investment/loan (A).
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateCompoundInterest(principal, rate, timesCompounded, years) {
  // Input validation
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error('Principal must be a positive number.');
  }
  if (typeof rate !== 'number' || rate < 0) {
    throw new Error('Rate must be a non-negative number.');
  }
  if (typeof timesCompounded !== 'number' || timesCompounded <= 0) {
    throw new Error('Times compounded must be a positive number.');
  }
  if (typeof years !== 'number' || years < 0) {
    throw new Error('Years must be a non-negative number.');
  }

  // Convert percentage rate to decimal
  const rateDecimal = rate / 100;

  // Compound interest formula implementation
  const amount = principal * Math.pow(1 + rateDecimal / timesCompounded, timesCompounded * years);

  // Round to two decimal places for financial calculations
  return Math.round(amount * 100) / 100;
}

// Example usage:
try {
  const result = calculateCompoundInterest(1000, 5, 12, 10); // $1000 principal, 5% annual rate, compounded monthly (12 times a year), for 10 years
  console.log(`Future Value: $${result}`);
} catch (error) {
  console.error('Error:', error.message);
}
```
