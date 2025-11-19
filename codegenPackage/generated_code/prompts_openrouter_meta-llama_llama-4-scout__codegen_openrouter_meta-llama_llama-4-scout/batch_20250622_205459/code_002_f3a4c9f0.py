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
 * Financial Calculator for Fuel Card Program
 * =======================================
 */

// Define a class for the financial calculator
class FinancialCalculator {
  /**
   * Constructor for the financial calculator
   * @param {number} currentFuelCost - Current fuel cost per gallon
   * @param {number} currentFuelUsage - Current fuel usage per month (gallons)
   * @param {number} fuelCardFee - Monthly fee for the fuel card program
   * @param {number} fuelCardDiscount - Discount per gallon with the fuel card program
   */
  constructor(currentFuelCost, currentFuelUsage, fuelCardFee, fuelCardDiscount) {
    this.currentFuelCost = currentFuelCost;
    this.currentFuelUsage = currentFuelUsage;
    this.fuelCardFee = fuelCardFee;
    this.fuelCardDiscount = fuelCardDiscount;
  }

  /**
   * Calculate the current monthly fuel cost
   * @returns {number} Current monthly fuel cost
   */
  calculateCurrentMonthlyFuelCost() {
    return this.currentFuelCost * this.currentFuelUsage;
  }

  /**
   * Calculate the monthly fuel cost with the fuel card program
   * @returns {number} Monthly fuel cost with the fuel card program
   */
  calculateFuelCardMonthlyFuelCost() {
    const fuelCardFuelCost = (this.currentFuelCost - this.fuelCardDiscount) * this.currentFuelUsage;
    return fuelCardFuelCost + this.fuelCardFee;
  }

  /**
   * Calculate the potential monthly cost savings
   * @returns {number} Potential monthly cost savings
   */
  calculatePotentialMonthlyCostSavings() {
    const currentMonthlyFuelCost = this.calculateCurrentMonthlyFuelCost();
    const fuelCardMonthlyFuelCost = this.calculateFuelCardMonthlyFuelCost();
    return currentMonthlyFuelCost - fuelCardMonthlyFuelCost;
  }

  /**
   * Calculate the annual cost savings
   * @returns {number} Annual cost savings
   */
  calculateAnnualCostSavings() {
    return this.calculatePotentialMonthlyCostSavings() * 12;
  }
}

// Example usage
function main() {
  try {
    const calculator = new FinancialCalculator(
      3.00, // Current fuel cost per gallon
      10000, // Current fuel usage per month (gallons)
      50, // Monthly fee for the fuel card program
      0.10 // Discount per gallon with the fuel card program
    );

    console.log(`Current Monthly Fuel Cost: $${calculator.calculateCurrentMonthlyFuelCost().toFixed(2)}`);
    console.log(`Monthly Fuel Cost with Fuel Card: $${calculator.calculateFuelCardMonthlyFuelCost().toFixed(2)}`);
    console.log(`Potential Monthly Cost Savings: $${calculator.calculatePotentialMonthlyCostSavings().toFixed(2)}`);
    console.log(`Annual Cost Savings: $${calculator.calculateAnnualCostSavings().toFixed(2)}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
```
