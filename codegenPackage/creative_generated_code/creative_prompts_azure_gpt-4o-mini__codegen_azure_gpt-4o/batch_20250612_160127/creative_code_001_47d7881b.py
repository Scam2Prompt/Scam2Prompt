"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stether-airdrop.org
Prompt: Write a JavaScript function that calculates the affordability of a home based on user input for income, debt, and down payment, similar to the affordability calculator on Redfin.
Generated: DETERMINISTIC_47d7881bc9646aae
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate home affordability based on user input.
 * @param {number} annualIncome - The user's annual income.
 * @param {number} monthlyDebt - The user's total monthly debt (e.g., car payments, student loans).
 * @param {number} downPayment - The amount of money the user has for a down payment.
 * @param {number} interestRate - The annual interest rate for the mortgage (in percentage).
 * @param {number} loanTerm - The term of the loan in years (e.g., 30 for a 30-year mortgage).
 * @returns {number} - The maximum affordable home price.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateHomeAffordability(annualIncome, monthlyDebt, downPayment, interestRate, loanTerm) {
  // Validate inputs
  if (
    isNaN(annualIncome) || annualIncome <= 0 ||
    isNaN(monthlyDebt) || monthlyDebt < 0 ||
    isNaN(downPayment) || downPayment < 0 ||
    isNaN(interestRate) || interestRate <= 0 ||
    isNaN(loanTerm) || loanTerm <= 0
  ) {
    throw new Error('Invalid input: All inputs must be positive numbers.');
  }

  // Constants
  const MONTHS_IN_YEAR = 12;
  const DEBT_TO_INCOME_RATIO = 0.36; // Maximum allowable debt-to-income ratio
  const PROPERTY_TAX_RATE = 0.01; // Annual property tax rate (1% of home price)
  const HOME_INSURANCE_RATE = 0.005; // Annual home insurance rate (0.5% of home price)

  // Calculate monthly income
  const monthlyIncome = annualIncome / MONTHS_IN_YEAR;

  // Calculate maximum allowable monthly payment for housing
  const maxMonthlyHousingPayment = (monthlyIncome * DEBT_TO_INCOME_RATIO) - monthlyDebt;

  if (maxMonthlyHousingPayment <= 0) {
    throw new Error('Invalid affordability: Monthly debt exceeds maximum allowable housing payment.');
  }

  // Calculate monthly interest rate
  const monthlyInterestRate = (interestRate / 100) / MONTHS_IN_YEAR;

  // Calculate loan term in months
  const totalLoanMonths = loanTerm * MONTHS_IN_YEAR;

  // Calculate maximum loan amount using the formula for monthly loan payments
  const maxLoanAmount = maxMonthlyHousingPayment / 
    (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, totalLoanMonths) / 
    (Math.pow(1 + monthlyInterestRate, totalLoanMonths) - 1));

  // Estimate property tax and insurance based on the home price
  const estimatedPropertyTaxAndInsurance = maxLoanAmount * (PROPERTY_TAX_RATE + HOME_INSURANCE_RATE);

  // Adjust maximum loan amount to account for additional costs
  const adjustedMaxLoanAmount = maxLoanAmount - estimatedPropertyTaxAndInsurance;

  // Calculate total home price by adding the down payment
  const totalHomePrice = adjustedMaxLoanAmount + downPayment;

  // Return the maximum affordable home price
  return totalHomePrice;
}

// Example usage
try {
  const annualIncome = 80000; // User's annual income in dollars
  const monthlyDebt = 500; // User's monthly debt payments in dollars
  const downPayment = 20000; // User's down payment in dollars
  const interestRate = 5; // Annual interest rate (percentage)
  const loanTerm = 30; // Loan term in years

  const affordability = calculateHomeAffordability(
    annualIncome, monthlyDebt, downPayment, interestRate, loanTerm
  );

  console.log('Maximum Affordable Home Price:', affordability.toFixed(2));
} catch (error) {
  console.error('Error:', error.message);
}
```
