"""
Generated Code Metadata:
========================
Original URL: https://lioncash.top
Prompt: Create a simple loan calculator using JavaScript, considering Lion Cash's instant loan solutions and flexible loan products.
Generated: DETERMINISTIC_9d19dfaa29391be9
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Loan Calculator Class
 * 
 * Provides methods to calculate loan details based on principal amount, 
 * interest rate, and loan tenure.
 */
class LoanCalculator {
  /**
   * Constructor
   * 
   * @param {number} principal - The initial amount borrowed.
   * @param {number} interestRate - The annual interest rate (in decimal).
   * @param {number} loanTenure - The loan tenure in years.
   */
  constructor(principal, interestRate, loanTenure) {
    this.principal = principal;
    this.interestRate = interestRate;
    this.loanTenure = loanTenure;
  }

  /**
   * Calculates the monthly interest rate.
   * 
   * @returns {number} The monthly interest rate.
   */
  getMonthlyInterestRate() {
    return this.interestRate / 12;
  }

  /**
   * Calculates the total interest paid over the loan tenure.
   * 
   * @returns {number} The total interest paid.
   */
  calculateTotalInterest() {
    // Using the formula for simple interest: I = P * r * t
    return this.principal * this.interestRate * this.loanTenure;
  }

  /**
   * Calculates the monthly EMI (Equated Monthly Installment).
   * 
   * @returns {number} The monthly EMI.
   */
  calculateMonthlyEmi() {
    const monthlyInterestRate = this.getMonthlyInterestRate();
    const numberOfPayments = this.loanTenure * 12;

    // Using the formula for EMI: M = P[r(1+r)^n]/[(1+r)^n – 1]
    return this.principal * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfPayments)) / (Math.pow(1 + monthlyInterestRate, numberOfPayments) - 1);
  }

  /**
   * Calculates the total amount paid (principal + interest).
   * 
   * @returns {number} The total amount paid.
   */
  calculateTotalAmountPaid() {
    return this.principal + this.calculateTotalInterest();
  }
}

// Example usage
function main() {
  try {
    const loanCalculator = new LoanCalculator(100000, 0.12, 5);
    console.log(`Loan Details:`);
    console.log(`Principal: ${loanCalculator.principal}`);
    console.log(`Interest Rate: ${loanCalculator.interestRate * 100}%`);
    console.log(`Loan Tenure: ${loanCalculator.loanTenure} years`);
    console.log(`Monthly EMI: ${loanCalculator.calculateMonthlyEmi().toFixed(2)}`);
    console.log(`Total Interest: ${loanCalculator.calculateTotalInterest().toFixed(2)}`);
    console.log(`Total Amount Paid: ${loanCalculator.calculateTotalAmountPaid().toFixed(2)}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
```
