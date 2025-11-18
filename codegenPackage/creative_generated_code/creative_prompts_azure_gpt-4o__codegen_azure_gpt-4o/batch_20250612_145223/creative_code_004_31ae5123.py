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
 * This script calculates the repayment schedule for a loan based on principal amount, 
 * annual interest rate, loan term, and number of payments per year.
 * Assumes TymeBank's loan terms and fixed interest rates.
 * 
 * Author: [Your Name]
 * Date: [Date]
 */

/**
 * Calculates the monthly payment based on loan details.
 * 
 * @param {number} principal - The loan amount (in monetary units).
 * @param {number} annualRate - The annual interest rate (as a percentage, e.g., 5 for 5%).
 * @param {number} termYears - The loan term in years.
 * @param {number} paymentsPerYear - Number of payments per year (e.g., 12 for monthly payments).
 * @returns {number} - The monthly payment amount.
 */
function calculateMonthlyPayment(principal, annualRate, termYears, paymentsPerYear) {
    const monthlyRate = (annualRate / 100) / paymentsPerYear; // Convert annual rate to a fraction per payment period
    const totalPayments = termYears * paymentsPerYear;

    // Formula for fixed-rate loan: M = P[r(1+r)^n] / [(1+r)^n - 1]
    if (monthlyRate === 0) {
        // If interest rate is 0, simply divide principal by total payments
        return principal / totalPayments;
    }

    const numerator = monthlyRate * Math.pow(1 + monthlyRate, totalPayments);
    const denominator = Math.pow(1 + monthlyRate, totalPayments) - 1;
    return principal * (numerator / denominator);
}

/**
 * Generates a loan repayment schedule.
 * 
 * @param {number} principal - The loan amount.
 * @param {number} annualRate - The annual interest rate (as a percentage).
 * @param {number} termYears - The loan term in years.
 * @param {number} paymentsPerYear - Number of payments per year (e.g., 12 for monthly).
 * @returns {Array} - An array of repayment objects, each representing a payment.
 */
function generateRepaymentSchedule(principal, annualRate, termYears, paymentsPerYear) {
    const monthlyPayment = calculateMonthlyPayment(principal, annualRate, termYears, paymentsPerYear);
    const totalPayments = termYears * paymentsPerYear;
    const monthlyRate = (annualRate / 100) / paymentsPerYear;

    let remainingBalance = principal;
    const schedule = [];

    for (let i = 1; i <= totalPayments; i++) {
        const interestPayment = remainingBalance * monthlyRate;
        const principalPayment = monthlyPayment - interestPayment;
        remainingBalance -= principalPayment;

        // Prevent negative balance due to rounding issues
        if (remainingBalance < 0) remainingBalance = 0;

        schedule.push({
            paymentNumber: i,
            monthlyPayment: monthlyPayment.toFixed(2),
            principalPayment: principalPayment.toFixed(2),
            interestPayment: interestPayment.toFixed(2),
            remainingBalance: remainingBalance.toFixed(2),
        });
    }

    return schedule;
}

/**
 * Main function to demonstrate the loan repayment schedule calculator.
 */
function main() {
    try {
        // Example input: Adjust as per TymeBank's terms and rates
        const principal = 100000; // Loan amount in monetary units
        const annualRate = 5; // Annual interest rate in percentage
        const termYears = 15; // Loan term in years
        const paymentsPerYear = 12; // Monthly payments

        // Generate repayment schedule
        const schedule = generateRepaymentSchedule(principal, annualRate, termYears, paymentsPerYear);

        // Display results
        console.log("Loan Repayment Schedule:");
        console.log("--------------------------------");
        schedule.forEach(payment => {
            console.log(`Payment #${payment.paymentNumber}:`);
            console.log(`  Monthly Payment: $${payment.monthlyPayment}`);
            console.log(`  Principal Payment: $${payment.principalPayment}`);
            console.log(`  Interest Payment: $${payment.interestPayment}`);
            console.log(`  Remaining Balance: $${payment.remainingBalance}`);
            console.log("--------------------------------");
        });
    } catch (error) {
        console.error("An error occurred while calculating the loan repayment schedule:", error.message);
    }
}

// Run the main function
main();
```
