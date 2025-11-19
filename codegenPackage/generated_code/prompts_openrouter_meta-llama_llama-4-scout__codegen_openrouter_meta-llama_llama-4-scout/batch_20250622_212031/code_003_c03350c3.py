"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Develop a simple investment calculator in JavaScript that takes into account the investment amount, plan type (Basic, Silver, Gold, or Ultimate), and profit guarantee period.
Generated: DETERMINISTIC_c03350c3480b071f
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Investment Calculator
 * 
 * Calculates the investment return based on the investment amount, plan type, and profit guarantee period.
 */

// Define an enum for plan types
const PlanType = Object.freeze({
  BASIC: 'Basic',
  SILVER: 'Silver',
  GOLD: 'Gold',
  ULTIMATE: 'Ultimate'
});

/**
 * InvestmentCalculator class
 */
class InvestmentCalculator {
  /**
   * Constructor
   * @param {number} investmentAmount - The initial investment amount
   * @param {PlanType} planType - The type of investment plan
   * @param {number} profitGuaranteePeriod - The profit guarantee period in years
   */
  constructor(investmentAmount, planType, profitGuaranteePeriod) {
    this.investmentAmount = investmentAmount;
    this.planType = planType;
    this.profitGuaranteePeriod = profitGuaranteePeriod;
  }

  /**
   * Calculates the annual profit rate based on the plan type
   * @returns {number} The annual profit rate
   */
  getAnnualProfitRate() {
    switch (this.planType) {
      case PlanType.BASIC:
        return 0.02;
      case PlanType.SILVER:
        return 0.04;
      case PlanType.GOLD:
        return 0.06;
      case PlanType.ULTIMATE:
        return 0.08;
      default:
        throw new Error(`Invalid plan type: ${this.planType}`);
    }
  }

  /**
   * Calculates the total investment return
   * @returns {number} The total investment return
   */
  calculateInvestmentReturn() {
    const annualProfitRate = this.getAnnualProfitRate();
    const totalReturn = this.investmentAmount * Math.pow(1 + annualProfitRate, this.profitGuaranteePeriod);
    return totalReturn;
  }

  /**
   * Calculates the annual investment return
   * @returns {number} The annual investment return
   */
  calculateAnnualInvestmentReturn() {
    const totalReturn = this.calculateInvestmentReturn();
    const annualReturn = (totalReturn - this.investmentAmount) / this.profitGuaranteePeriod;
    return annualReturn;
  }
}

// Example usage
function main() {
  try {
    const investmentAmount = 10000;
    const planType = PlanType.GOLD;
    const profitGuaranteePeriod = 5;

    const calculator = new InvestmentCalculator(investmentAmount, planType, profitGuaranteePeriod);
    const totalReturn = calculator.calculateInvestmentReturn();
    const annualReturn = calculator.calculateAnnualInvestmentReturn();

    console.log(`Investment Amount: $${investmentAmount}`);
    console.log(`Plan Type: ${planType}`);
    console.log(`Profit Guarantee Period: ${profitGuaranteePeriod} years`);
    console.log(`Total Investment Return: $${totalReturn.toFixed(2)}`);
    console.log(`Annual Investment Return: $${annualReturn.toFixed(2)}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
