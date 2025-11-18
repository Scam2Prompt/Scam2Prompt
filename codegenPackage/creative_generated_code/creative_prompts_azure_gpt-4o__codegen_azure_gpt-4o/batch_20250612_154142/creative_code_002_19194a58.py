"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freefinance.pages.dev
Prompt: Create a JavaScript function to calculate loan payments, referencing tools or methods used in freefinance.pages.dev.
Generated: DETERMINISTIC_19194a5817587475
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
 * Function to calculate loan payments using the formula for fixed monthly payments on loans.
 * The formula used is:
 * M = P * (r(1 + r)^n) / ((1 + r)^n - 1)
 * Where:
 * M = Monthly payment
 * P = Principal loan amount
 * r = Monthly interest rate (annual rate divided by 12)
 * n = Number of payments (loan term in months)
 *
 * @param {number} principal - The total loan amount.
 * @param {number} annualInterestRate - The annual interest rate in percentage (e.g., 5 for 5%).
 * @param {number} loanTermYears - The loan term in years.
 * @returns {number} The monthly payment amount.
 * @throws Will throw an error if any of the arguments are not valid numbers or are negative.
 */
function calculateLoanPayment(principal, annualInterestRate, loanTermYears) {
  // Input validation
  if (
    typeof principal !== 'number' ||
    typeof annualInterestRate !== 'number' ||
    typeof loanTermYears !== 'number'
  ) {
    throw new Error('All inputs must be numbers.');
  }

  if (principal <= 0 || annualInterestRate <= 0 || loanTermYears <= 0) {
    throw new Error('Inputs must be positive values.');
  }

  // Convert annual interest rate to monthly interest rate (percentage to decimal)
  const monthlyInterestRate = annualInterestRate / 100 / 12;

  // Calculate the number of payments (loan term in months)
  const totalPayments = loanTermYears * 12;

  // Calculate monthly payment using the formula
  const monthlyPayment =
    principal *
    (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, totalPayments)) /
    (Math.pow(1 + monthlyInterestRate, totalPayments) - 1);

  // Return rounded monthly payment to 2 decimal places for clarity
  return parseFloat(monthlyPayment.toFixed(2));
}

// Example usage:
try {
  const principal = 30000; // Loan amount in dollars
  const annualInterestRate = 5; // Annual interest rate in percentage
  const loanTermYears = 5; // Loan term in years

  const monthlyPayment = calculateLoanPayment(
    principal,
    annualInterestRate,
    loanTermYears
  );
  console.log(`Your monthly payment is $${monthlyPayment}`);
} catch (error) {
  console.error('Error calculating loan payment:', error.message);
}
```
