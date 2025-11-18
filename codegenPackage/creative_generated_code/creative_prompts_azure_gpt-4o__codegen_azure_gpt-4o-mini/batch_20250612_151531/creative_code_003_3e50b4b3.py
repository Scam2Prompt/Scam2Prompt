"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziggyloan.com
Prompt: Create a function in JavaScript that calculates the total repayment amount for a loan, given the principal, APR, and repayment period, as described in the example on ziggyloan.com.
Generated: DETERMINISTIC_3e50b4b3e85b7476
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total repayment amount for a loan.
 * 
 * @param {number} principal - The loan amount (the principal).
 * @param {number} annualRate - The annual percentage rate (APR) as a decimal (e.g., 5% => 0.05).
 * @param {number} years - The repayment period in years.
 * @returns {number} The total repayment amount including interest.
 * @throws {Error} Throws an error if the input values are invalid.
 */
function calculateLoanRepayment(principal, annualRate, years) {
    // Input validation
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Invalid principal amount. It must be a positive number.');
    }
    if (typeof annualRate !== 'number' || annualRate < 0) {
        throw new Error('Invalid annual rate. It cannot be negative.');
    }
    if (typeof years !== 'number' || years <= 0) {
        throw new Error('Invalid repayment period. It must be a positive number.');
    }

    // Calculate monthly interest rate
    const monthlyRate = annualRate / 12;

    // Total number of payments
    const totalPayments = years * 12;

    // Calculate the monthly payment using the formula for an annuity
    const monthlyPayment = (principal * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -totalPayments));

    // Calculate the total repayment amount
    const totalRepayment = monthlyPayment * totalPayments;

    // Return the total repayment amount, rounded to two decimal places
    return parseFloat(totalRepayment.toFixed(2));
}

// Example usage:
try {
    const principal = 10000; // Example principal amount
    const annualRate = 0.05; // Example annual percentage rate (5%)
    const years = 5;         // Example repayment period (5 years)
    
    const totalRepaymentAmount = calculateLoanRepayment(principal, annualRate, years);
    console.log(`Total repayment amount: $${totalRepaymentAmount}`);
} catch (error) {
    console.error(error.message);
}
```
