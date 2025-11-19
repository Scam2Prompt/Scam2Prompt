"""
Generated Code Metadata:
========================
Original URL: https://chevroletfinanciado.com.ar
Prompt: "Write a code snippet in JavaScript to create a simple calculator for determining the price of a Chevrolet car under different financing plans in Argentina."
Generated: DETERMINISTIC_8e76cf05761fa8ee
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the price of a Chevrolet car under different financing plans in Argentina.
 */

// Define a class for the Chevrolet car financing calculator
class ChevroletFinancingCalculator {
  /**
   * Constructor for the calculator.
   * @param {number} carPrice - The base price of the Chevrolet car.
   * @param {object} financingPlans - An object containing different financing plans.
   */
  constructor(carPrice, financingPlans) {
    this.carPrice = carPrice;
    this.financingPlans = financingPlans;
  }

  /**
   * Calculates the total price of the car under a specific financing plan.
   * @param {string} planName - The name of the financing plan.
   * @param {number} downPayment - The down payment amount.
   * @param {number} months - The number of months to finance the car.
   * @returns {object} An object containing the total price and monthly payment.
   */
  calculatePrice(planName, downPayment, months) {
    if (!this.financingPlans[planName]) {
      throw new Error(`Financing plan '${planName}' not found.`);
    }

    const plan = this.financingPlans[planName];
    const interestRate = plan.interestRate / 100 / 12; // Convert to monthly interest rate
    const loanAmount = this.carPrice - downPayment;
    const monthlyPayment = this.calculateMonthlyPayment(loanAmount, interestRate, months);
    const totalPrice = downPayment + loanAmount + (monthlyPayment * months * interestRate);

    return {
      totalPrice: Math.round(totalPrice * 100) / 100,
      monthlyPayment: Math.round(monthlyPayment * 100) / 100,
    };
  }

  /**
   * Calculates the monthly payment using the formula for monthly payments on a fixed-rate loan.
   * @param {number} loanAmount - The amount borrowed.
   * @param {number} interestRate - The monthly interest rate.
   * @param {number} months - The number of months to repay the loan.
   * @returns {number} The monthly payment amount.
   */
  calculateMonthlyPayment(loanAmount, interestRate, months) {
    if (interestRate === 0) {
      return loanAmount / months;
    }

    const monthlyPayment = loanAmount * interestRate * Math.pow(1 + interestRate, months) / (Math.pow(1 + interestRate, months) - 1);
    return monthlyPayment;
  }
}

// Example usage:
const financingPlans = {
  'Plan A': { interestRate: 20 },
  'Plan B': { interestRate: 25 },
  'Plan C': { interestRate: 30 },
};

const calculator = new ChevroletFinancingCalculator(500000, financingPlans);

try {
  const result = calculator.calculatePrice('Plan A', 100000, 60);
  console.log(`Total Price: $${result.totalPrice}`);
  console.log(`Monthly Payment: $${result.monthlyPayment}`);
} catch (error) {
  console.error(error.message);
}
```
