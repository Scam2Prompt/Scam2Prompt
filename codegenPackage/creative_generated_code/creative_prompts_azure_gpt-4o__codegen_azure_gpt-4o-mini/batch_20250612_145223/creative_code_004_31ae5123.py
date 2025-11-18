"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: Write a script in JavaScript to calculate loan repayment schedules, assuming TymeBank's loan terms and interest rates.
Generated: DETERMINISTIC_31ae512312ec0ca4
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Loan Repayment Schedule Calculator
 * This script calculates the repayment schedule for a loan based on the loan amount,
 * interest rate, and duration. It generates an amortization schedule showing monthly 
 * payments, interest, principal repayments, and remaining balance.
 */

/**
 * Function to calculate monthly payment using the formula:
 * M = P[r(1 + r)^n] / [(1 + r)^n – 1]
 * where P = principal loan amount, r = monthly interest rate, n = number of payments
 * 
 * @param {number} principal - The total amount of the loan
 * @param {number} annualInterestRate - The annual interest rate (as a percentage)
 * @param {number} numberOfPayments - The total number of monthly payments
 * @returns {number} - The monthly payment amount
 */
function calculateMonthlyPayment(principal, annualInterestRate, numberOfPayments) {
    const monthlyInterestRate = (annualInterestRate / 100) / 12;
    return (principal * monthlyInterestRate) / (1 - Math.pow(1 + monthlyInterestRate, -numberOfPayments));
}

/**
 * Function to generate the loan repayment schedule
 * 
 * @param {number} principal - The total amount of the loan
 * @param {number} annualInterestRate - The annual interest rate (as a percentage)
 * @param {number} numberOfPayments - The total number of monthly payments
 * @returns {Array} - An array of repayment schedule objects
 */
function generateLoanRepaymentSchedule(principal, annualInterestRate, numberOfPayments) {
    const monthlyPayment = calculateMonthlyPayment(principal, annualInterestRate, numberOfPayments);
    const schedule = [];
    let remainingBalance = principal;

    for (let i = 0; i < numberOfPayments; i++) {
        const interestPayment = remainingBalance * (annualInterestRate / 100) / 12;
        const principalPayment = monthlyPayment - interestPayment;
        remainingBalance -= principalPayment;

        // Ensure remaining balance does not go below zero
        if (remainingBalance < 0) {
            remainingBalance = 0;
        }

        schedule.push({
            month: i + 1,
            monthlyPayment: parseFloat(monthlyPayment.toFixed(2)),
            interestPayment: parseFloat(interestPayment.toFixed(2)),
            principalPayment: parseFloat(principalPayment.toFixed(2)),
            remainingBalance: parseFloat(remainingBalance.toFixed(2)),
        });
    }

    return schedule;
}

// Example usage:
try {
    const loanAmount = 10000; // Loan amount in currency (e.g., $10,000)
    const interestRate = 5; // Annual interest rate (e.g., 5%)
    const termInMonths = 24; // Loan term in months (e.g., 24 months)

    const repaymentSchedule = generateLoanRepaymentSchedule(loanAmount, interestRate, termInMonths);
    
    // Output the repayment schedule
    console.log("Loan Repayment Schedule:");
    console.table(repaymentSchedule);
} catch (error) {
    console.error("An error occurred while generating the loan repayment schedule:", error);
}
```
