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
 * Calculates compound growth based on investment returns.
 * 
 * Formula: A = P * (1 + r/n)^(n*t)
 * Where:
 * A = Future Value of Investment
 * P = Principal Investment (Initial amount)
 * r = Annual Interest Rate (in decimal form)
 * n = Number of compounding periods per year
 * t = Time (in years)
 * 
 * @param {number} principal - Initial amount of investment (P).
 * @param {number} annualRate - Annual interest rate (r) in decimal (e.g., 0.05 for 5%).
 * @param {number} compoundingPeriods - Number of times interest is compounded per year (n).
 * @param {number} timeYears - Duration of the investment in years (t).
 * @returns {number} - Future Value of Investment (A).
 * @throws {Error} - If any parameter is invalid (e.g., negative numbers or non-numeric values).
 */
function calculateCompoundGrowth(principal, annualRate, compoundingPeriods, timeYears) {
  // Input validation
  if (
    typeof principal !== 'number' || principal <= 0 ||
    typeof annualRate !== 'number' || annualRate <= 0 ||
    typeof compoundingPeriods !== 'number' || compoundingPeriods <= 0 ||
    typeof timeYears !== 'number' || timeYears <= 0
  ) {
    throw new Error('Invalid input: All parameters must be positive numbers.');
  }

  // Calculate compound growth
  const futureValue = principal * Math.pow(1 + annualRate / compoundingPeriods, compoundingPeriods * timeYears);

  // Ensure the calculation doesn't produce NaN or Infinity
  if (!isFinite(futureValue)) {
    throw new Error('Calculation error: Invalid result for compound growth.');
  }

  // Return the result rounded to two decimal places for financial accuracy
  return parseFloat(futureValue.toFixed(2));
}

// Example usage:
try {
  const principal = 10000; // Initial investment amount
  const annualRate = 0.05; // Annual interest rate (5%)
  const compoundingPeriods = 12; // Monthly compounding (12 periods per year)
  const timeYears = 10; // Investment duration in years

  const result = calculateCompoundGrowth(principal, annualRate, compoundingPeriods, timeYears);
  console.log(`Future value of investment: $${result}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
