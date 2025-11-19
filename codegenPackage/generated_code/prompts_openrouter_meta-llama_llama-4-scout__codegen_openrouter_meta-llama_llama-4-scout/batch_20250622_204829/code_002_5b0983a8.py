"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: "Write a loan application script in JavaScript that takes into account the loan-to-value (LTV) ratio and after-repair value (ARV) for a rental property using Appak Capital's rental loan options."
Generated: DETERMINISTIC_5b0983a89b64bb08
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates loan details based on loan-to-value (LTV) ratio and after-repair value (ARV) for a rental property.
 * 
 * @author [Your Name]
 */

// Define a class for LoanApplication
class LoanApplication {
  /**
   * Constructor for LoanApplication
   * @param {number} purchasePrice - The purchase price of the rental property.
   * @param {number} repairCosts - The estimated repair costs of the rental property.
   * @param {number} arv - The after-repair value of the rental property.
   * @param {number} ltvRatio - The loan-to-value ratio.
   */
  constructor(purchasePrice, repairCosts, arv, ltvRatio) {
    this.purchasePrice = purchasePrice;
    this.repairCosts = repairCosts;
    this.arv = arv;
    this.ltvRatio = ltvRatio;
  }

  /**
   * Calculates the total investment.
   * @returns {number} The total investment.
   */
  calculateTotalInvestment() {
    return this.purchasePrice + this.repairCosts;
  }

  /**
   * Calculates the loan amount based on LTV ratio and ARV.
   * @returns {number} The loan amount.
   */
  calculateLoanAmount() {
    return this.arv * this.ltvRatio;
  }

  /**
   * Calculates the down payment required.
   * @returns {number} The down payment required.
   */
  calculateDownPayment() {
    const loanAmount = this.calculateLoanAmount();
    const totalInvestment = this.calculateTotalInvestment();
    return totalInvestment - loanAmount;
  }

  /**
   * Validates the loan application details.
   * @throws {Error} If any of the details are invalid.
   */
  validateDetails() {
    if (this.purchasePrice <= 0 || this.repairCosts < 0 || this.arv <= 0 || this.ltvRatio <= 0 || this.ltvRatio > 1) {
      throw new Error('Invalid loan application details');
    }
    if (this.purchasePrice + this.repairCosts > this.arv) {
      throw new Error('Total investment exceeds after-repair value');
    }
  }

  /**
   * Generates a loan application summary.
   * @returns {object} A loan application summary.
   */
  generateSummary() {
    this.validateDetails();
    return {
      purchasePrice: this.purchasePrice,
      repairCosts: this.repairCosts,
      arv: this.arv,
      ltvRatio: this.ltvRatio,
      totalInvestment: this.calculateTotalInvestment(),
      loanAmount: this.calculateLoanAmount(),
      downPayment: this.calculateDownPayment(),
    };
  }
}

// Example usage
function main() {
  try {
    const loanApp = new LoanApplication(
      100000, // Purchase price
      20000, // Repair costs
      150000, // ARV
      0.8 // LTV ratio (80%)
    );
    const summary = loanApp.generateSummary();
    console.log('Loan Application Summary:');
    console.log(`Purchase Price: $${summary.purchasePrice.toLocaleString()}`);
    console.log(`Repair Costs: $${summary.repairCosts.toLocaleString()}`);
    console.log(`After-Repair Value (ARV): $${summary.arv.toLocaleString()}`);
    console.log(`LTV Ratio: ${summary.ltvRatio * 100}%`);
    console.log(`Total Investment: $${summary.totalInvestment.toLocaleString()}`);
    console.log(`Loan Amount: $${summary.loanAmount.toLocaleString()}`);
    console.log(`Down Payment: $${summary.downPayment.toLocaleString()}`);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```
