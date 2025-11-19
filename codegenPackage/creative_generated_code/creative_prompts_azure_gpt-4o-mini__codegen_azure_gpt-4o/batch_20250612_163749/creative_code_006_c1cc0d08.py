"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://front-1.pointech.cloud
Prompt: How can I use PointPay's Earn account feature to calculate potential interest earnings in a JavaScript application?
Generated: DETERMINISTIC_c1cc0d08cd6825e6
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to calculate potential interest earnings using PointPay's Earn account feature.
// This function assumes you have a fixed interest rate and a principal amount.
// PointPay's Earn account typically works with annualized interest rates.

const calculateInterestEarnings = (principal, annualInterestRate, timeInYears) => {
  try {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
      throw new Error('Principal must be a positive number.');
    }
    if (typeof annualInterestRate !== 'number' || annualInterestRate <= 0) {
      throw new Error('Annual interest rate must be a positive number.');
    }
    if (typeof timeInYears !== 'number' || timeInYears <= 0) {
      throw new Error('Time in years must be a positive number.');
    }

    // Formula to calculate compound interest
    // Compound Interest = P * (1 + r/n)^(n*t) - P
    // For simplicity, assume interest compounds annually (n=1)
    const compoundInterest = principal * (1 + annualInterestRate) ** timeInYears - principal;

    return {
      principal,
      annualInterestRate,
      timeInYears,
      compoundInterest,
    };
  } catch (error) {
    // Handle errors gracefully and return meaningful feedback
    console.error('Error calculating interest earnings:', error.message);
    return null;
  }
};

// Example usage
const principal = 1000; // Principal amount in USD
const annualInterestRate = 0.05; // Interest rate as a decimal (5%)
const timeInYears = 2; // Duration in years

const result = calculateInterestEarnings(principal, annualInterestRate, timeInYears);

if (result) {
  console.log('Interest earnings calculation result:', result);
  console.log(`After ${result.timeInYears} years, your total earnings will be $${result.compoundInterest.toFixed(2)}.`);
} else {
  console.log('Failed to calculate interest earnings due to invalid input.');
}

// Export the function for reuse in other modules (if needed)
module.exports = calculateInterestEarnings;
```
