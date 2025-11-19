"""
Generated Code Metadata:
========================
Original URL: https://joinnow.info
Prompt: "Create a simple income calculator in JavaScript that demonstrates the potential earnings of Money Order Freedom subscribers based on the provided income examples."
Generated: DETERMINISTIC_bdd54dfbabb74b2d
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the potential earnings of Money Order Freedom subscribers.
 */

/**
 * IncomeCalculator class.
 */
class IncomeCalculator {
  /**
   * Constructor for IncomeCalculator.
   * @param {number} monthlyInvestment - The monthly investment amount.
   * @param {number} annualReturnRate - The annual return rate (in decimal form, e.g., 4% = 0.04).
   * @param {number} years - The number of years to calculate earnings for.
   */
  constructor(monthlyInvestment, annualReturnRate, years) {
    this.monthlyInvestment = monthlyInvestment;
    this.annualReturnRate = annualReturnRate;
    this.years = years;
  }

  /**
   * Calculates the total earnings based on the provided parameters.
   * @returns {number} The total earnings.
   */
  calculateEarnings() {
    // Convert annual return rate to monthly return rate
    const monthlyReturnRate = (1 + this.annualReturnRate) ** (1 / 12) - 1;

    // Initialize total earnings and balance
    let totalEarnings = 0;
    let balance = 0;

    // Calculate earnings for each month
    for (let i = 0; i < this.years * 12; i++) {
      balance = (balance + this.monthlyInvestment) * (1 + monthlyReturnRate);
      totalEarnings = balance;
    }

    return totalEarnings;
  }
}

/**
 * Example usage of IncomeCalculator.
 */
function main() {
  try {
    // Define income examples
    const incomeExamples = [
      { monthlyInvestment: 100, annualReturnRate: 0.04, years: 5 },
      { monthlyInvestment: 200, annualReturnRate: 0.06, years: 10 },
      { monthlyInvestment: 500, annualReturnRate: 0.08, years: 20 },
    ];

    // Calculate and display earnings for each example
    incomeExamples.forEach((example, index) => {
      const calculator = new IncomeCalculator(example.monthlyInvestment, example.annualReturnRate, example.years);
      const earnings = calculator.calculateEarnings();
      console.log(`Example ${index + 1}:`);
      console.log(`Monthly Investment: $${example.monthlyInvestment.toFixed(2)}`);
      console.log(`Annual Return Rate: ${example.annualReturnRate * 100}%`);
      console.log(`Years: ${example.years}`);
      console.log(`Total Earnings: $${earnings.toFixed(2)}`);
      console.log('------------------------');
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```
