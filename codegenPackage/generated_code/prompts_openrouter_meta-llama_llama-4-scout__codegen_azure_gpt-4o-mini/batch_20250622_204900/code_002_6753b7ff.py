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
 * This function calculates the Equated Monthly Installment (EMI) for a loan.
 * 
 * @param {number} principal - The loan amount (principal).
 * @param {number} annualInterestRate - The annual interest rate (in percentage).
 * @param {number} tenureInMonths - The tenure of the loan in months.
 * @returns {number} - The calculated EMI amount.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateEMI(principal, annualInterestRate, tenureInMonths) {
    // Input validation
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Invalid principal amount. It must be a positive number.');
    }
    if (typeof annualInterestRate !== 'number' || annualInterestRate < 0) {
        throw new Error('Invalid interest rate. It must be a non-negative number.');
    }
    if (typeof tenureInMonths !== 'number' || tenureInMonths <= 0) {
        throw new Error('Invalid tenure. It must be a positive number.');
    }

    // Convert annual interest rate to monthly and decimal
    const monthlyInterestRate = (annualInterestRate / 100) / 12;

    // Calculate EMI using the formula
    const emi = (principal * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, tenureInMonths)) /
                (Math.pow(1 + monthlyInterestRate, tenureInMonths) - 1);

    return parseFloat(emi.toFixed(2)); // Return EMI rounded to 2 decimal places
}

// Example usage
try {
    const principal = 500000; // Loan amount
    const annualInterestRate = 7.5; // Annual interest rate in percentage
    const tenureInMonths = 60; // Tenure in months

    const emi = calculateEMI(principal, annualInterestRate, tenureInMonths);
    console.log(`The EMI for the loan is: ₹${emi}`);
} catch (error) {
    console.error(`Error calculating EMI: ${error.message}`);
}
```
