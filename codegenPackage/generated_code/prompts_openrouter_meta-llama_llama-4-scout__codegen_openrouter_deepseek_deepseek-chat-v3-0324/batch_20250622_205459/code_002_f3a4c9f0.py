"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Develop a simple financial calculator in JavaScript to determine the potential cost savings of using a fuel card program for a small trucking company.
Generated: DETERMINISTIC_f3a4c9f09ae7d59a
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
 * Financial Calculator for Fuel Card Savings
 * Calculates potential cost savings for a small trucking company using a fuel card program.
 */

class FuelCardCalculator {
  /**
   * Initialize calculator with default values
   * @param {Object} config - Configuration object
   * @param {number} config.gallonsPerMonth - Average gallons purchased per month
   * @param {number} config.currentPricePerGallon - Current fuel price per gallon
   * @param {number} config.discountRate - Discount rate from fuel card (as decimal)
   * @param {number} config.annualFee - Annual fee for fuel card program
   */
  constructor(config = {}) {
    this.gallonsPerMonth = config.gallonsPerMonth || 0;
    this.currentPricePerGallon = config.currentPricePerGallon || 0;
    this.discountRate = config.discountRate || 0;
    this.annualFee = config.annualFee || 0;
  }

  /**
   * Validate input values
   * @throws {Error} If any input is invalid
   */
  validateInputs() {
    if (this.gallonsPerMonth <= 0) {
      throw new Error('Gallons per month must be greater than 0');
    }
    if (this.currentPricePerGallon <= 0) {
      throw new Error('Current price per gallon must be greater than 0');
    }
    if (this.discountRate < 0 || this.discountRate >= 1) {
      throw new Error('Discount rate must be between 0 and 1');
    }
    if (this.annualFee < 0) {
      throw new Error('Annual fee cannot be negative');
    }
  }

  /**
   * Calculate monthly savings from fuel card program
   * @returns {number} Monthly savings amount
   */
  calculateMonthlySavings() {
    this.validateInputs();
    const monthlyDiscount = this.gallonsPerMonth * this.currentPricePerGallon * this.discountRate;
    const monthlyFee = this.annualFee / 12;
    return monthlyDiscount - monthlyFee;
  }

  /**
   * Calculate annual savings from fuel card program
   * @returns {number} Annual savings amount
   */
  calculateAnnualSavings() {
    return this.calculateMonthlySavings() * 12;
  }

  /**
   * Calculate percentage savings compared to current spending
   * @returns {number} Percentage savings (0-100)
   */
  calculatePercentageSavings() {
    this.validateInputs();
    const currentMonthlySpend = this.gallonsPerMonth * this.currentPricePerGallon;
    const monthlySavings = this.calculateMonthlySavings();
    return (monthlySavings / currentMonthlySpend) * 100;
  }

  /**
   * Generate a comprehensive savings report
   * @returns {Object} Report containing all savings calculations
   */
  generateSavingsReport() {
    try {
      const monthlySavings = this.calculateMonthlySavings();
      const annualSavings = this.calculateAnnualSavings();
      const percentageSavings = this.calculatePercentageSavings();

      return {
        monthlySavings: parseFloat(monthlySavings.toFixed(2)),
        annualSavings: parseFloat(annualSavings.toFixed(2)),
        percentageSavings: parseFloat(percentageSavings.toFixed(2)),
        currentMonthlySpend: parseFloat((this.gallonsPerMonth * this.currentPricePerGallon).toFixed(2)),
        discountedMonthlySpend: parseFloat((this.gallonsPerMonth * this.currentPricePerGallon * (1 - this.discountRate) + (this.annualFee / 12)).toFixed(2))
      };
    } catch (error) {
      console.error('Error generating savings report:', error.message);
      return {
        error: error.message
      };
    }
  }
}

// Example usage:
/*
const calculator = new FuelCardCalculator({
  gallonsPerMonth: 3000,
  currentPricePerGallon: 3.50,
  discountRate: 0.05,
  annualFee: 500
});

const report = calculator.generateSavingsReport();
console.log(report);
*/
```
