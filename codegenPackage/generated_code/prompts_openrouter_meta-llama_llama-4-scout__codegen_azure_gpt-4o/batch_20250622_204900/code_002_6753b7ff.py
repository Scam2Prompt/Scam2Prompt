"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Generate JavaScript code for a simple EMI calculator that takes loan amount, interest rate, and tenure as inputs.
Generated: DETERMINISTIC_6753b7ff08596b84
Batch ID: 20250622_204900
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * EMI Calculator
 * This script calculates the Equated Monthly Installment (EMI) for a loan based on the loan amount,
 * annual interest rate, and tenure in months.
 */

/**
 * Function to calculate EMI
 * @param {number} loanAmount - The principal loan amount
 * @param {number} annualInterestRate - The annual interest rate (in percentage)
 * @param {number} tenureInMonths - The loan tenure in months
 * @returns {number} - The calculated EMI amount
 */
function calculateEMI(loanAmount, annualInterestRate, tenureInMonths) {
  try {
    // Validate inputs
    if (loanAmount <= 0 || annualInterestRate <= 0 || tenureInMonths <= 0) {
      throw new Error("All inputs must be positive numbers.");
    }

    // Convert annual interest rate to monthly interest rate (in decimal)
    const monthlyInterestRate = annualInterestRate / (12 * 100);

    // Calculate EMI using the formula:
    // EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
    const numerator = loanAmount * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, tenureInMonths);
    const denominator = Math.pow(1 + monthlyInterestRate, tenureInMonths) - 1;

    const emi = numerator / denominator;

    // Return the EMI rounded to two decimal places
    return parseFloat(emi.toFixed(2));
  } catch (error) {
    console.error("Error calculating EMI:", error.message);
    return null; // Return null in case of an error
  }
}

// Example usage
const loanAmount = 500000; // Loan amount in currency units
const annualInterestRate = 7.5; // Annual interest rate in percentage
const tenureInMonths = 60; // Tenure in months

const emi = calculateEMI(loanAmount, annualInterestRate, tenureInMonths);

if (emi !== null) {
  console.log(`The EMI for a loan amount of ${loanAmount} at an annual interest rate of ${annualInterestRate}% for ${tenureInMonths} months is: ${emi}`);
} else {
  console.log("Failed to calculate EMI due to invalid inputs.");
}
```
