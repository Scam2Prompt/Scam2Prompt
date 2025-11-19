"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Create a simple investing calculator using JavaScript, inspired by the financial literacy concepts taught in Luke Belmar's Capital Club course.
Generated: DETERMINISTIC_ac38e271674279ca
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Investing Calculator
 * 
 * Calculates the future value of an investment based on the principal amount,
 * monthly contributions, interest rate, and time period.
 * 
 * Inspired by Luke Belmar's Capital Club course.
 */

// Define the InvestingCalculator class
class InvestingCalculator {
  /**
   * Constructor
   * 
   * @param {number} principal - The initial investment amount
   * @param {number} monthlyContribution - The monthly contribution amount
   * @param {number} interestRate - The annual interest rate (in decimal form, e.g., 4% = 0.04)
   * @param {number} years - The time period in years
   */
  constructor(principal, monthlyContribution, interestRate, years) {
    this.principal = principal;
    this.monthlyContribution = monthlyContribution;
    this.interestRate = interestRate / 100; // Convert to decimal form
    this.years = years;
  }

  /**
   * Calculate the future value of the investment
   * 
   * @returns {number} The future value of the investment
   */
  calculateFutureValue() {
    const monthlyInterestRate = this.interestRate / 12;
    const months = this.years * 12;
    let balance = this.principal;

    for (let i = 0; i < months; i++) {
      balance = (balance + this.monthlyContribution) * (1 + monthlyInterestRate);
    }

    return balance.toFixed(2); // Round to 2 decimal places
  }

  /**
   * Calculate the total contributions made
   * 
   * @returns {number} The total contributions made
   */
  calculateTotalContributions() {
    return (this.monthlyContribution * this.years * 12).toFixed(2);
  }

  /**
   * Calculate the interest earned
   * 
   * @returns {number} The interest earned
   */
  calculateInterestEarned() {
    const futureValue = parseFloat(this.calculateFutureValue());
    const totalContributions = parseFloat(this.calculateTotalContributions());
    const principal = this.principal;

    return (futureValue - totalContributions - principal).toFixed(2);
  }
}

// Example usage
function main() {
  try {
    const calculator = new InvestingCalculator(
      1000, // Principal
      500, // Monthly contribution
      8, // Interest rate (8%)
      10 // Time period (10 years)
    );

    console.log(`Future Value: $${calculator.calculateFutureValue()}`);
    console.log(`Total Contributions: $${calculator.calculateTotalContributions()}`);
    console.log(`Interest Earned: $${calculator.calculateInterestEarned()}`);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```
