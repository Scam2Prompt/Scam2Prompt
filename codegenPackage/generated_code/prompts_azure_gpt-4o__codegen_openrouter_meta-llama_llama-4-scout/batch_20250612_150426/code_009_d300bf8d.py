"""
Generated Code Metadata:
========================
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Develop a JavaScript-based profit calculator for Steadfast Asset Innovation's investment plans, allowing users to select a plan and input their investment amount to calculate returns.
Generated: DETERMINISTIC_d300bf8d84c9c3fb
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// InvestmentPlan.js

/**
 * Represents an investment plan with its properties and methods.
 */
class InvestmentPlan {
  /**
   * Creates a new InvestmentPlan instance.
   * @param {string} name - The name of the investment plan.
   * @param {number} rate - The interest rate of the investment plan.
   */
  constructor(name, rate) {
    this.name = name;
    this.rate = rate;
  }

  /**
   * Calculates the return on investment based on the principal amount.
   * @param {number} principal - The initial investment amount.
   * @returns {number} The calculated return on investment.
   */
  calculateReturn(principal) {
    if (principal <= 0) {
      throw new Error("Principal amount must be greater than zero.");
    }
    return principal * (1 + this.rate / 100);
  }
}

// ProfitCalculator.js

/**
 * Represents a profit calculator for Steadfast Asset Innovation's investment plans.
 */
class ProfitCalculator {
  /**
   * Creates a new ProfitCalculator instance.
   */
  constructor() {
    this.plans = [
      new InvestmentPlan("Conservative", 4),
      new InvestmentPlan("Moderate", 7),
      new InvestmentPlan("Aggressive", 10),
    ];
  }

  /**
   * Displays the available investment plans.
   */
  displayPlans() {
    console.log("Available Investment Plans:");
    this.plans.forEach((plan, index) => {
      console.log(`${index + 1}. ${plan.name} - ${plan.rate}% interest rate`);
    });
  }

  /**
   * Calculates the profit based on the selected plan and investment amount.
   * @param {number} planIndex - The index of the selected plan.
   * @param {number} investmentAmount - The amount invested.
   * @returns {object} An object containing the plan name, investment amount, and calculated return.
   */
  calculateProfit(planIndex, investmentAmount) {
    if (planIndex < 0 || planIndex >= this.plans.length) {
      throw new Error("Invalid plan index.");
    }

    const plan = this.plans[planIndex];
    const returnOnInvestment = plan.calculateReturn(investmentAmount);

    return {
      planName: plan.name,
      investmentAmount,
      returnOnInvestment,
      profit: returnOnInvestment - investmentAmount,
    };
  }
}

// main.js

const profitCalculator = new ProfitCalculator();

function main() {
  profitCalculator.displayPlans();

  const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  readline.question("Enter the number of your preferred plan: ", (planIndex) => {
    readline.question("Enter your investment amount: ", (investmentAmount) => {
      try {
        const result = profitCalculator.calculateProfit(
          parseInt(planIndex) - 1,
          parseFloat(investmentAmount)
        );

        console.log("\nProfit Calculation Result:");
        console.log(`Plan: ${result.planName}`);
        console.log(`Investment Amount: $${result.investmentAmount.toFixed(2)}`);
        console.log(`Return on Investment: $${result.returnOnInvestment.toFixed(2)}`);
        console.log(`Profit: $${result.profit.toFixed(2)}`);

        readline.close();
      } catch (error) {
        console.error("Error:", error.message);
        readline.close();
      }
    });
  });
}

main();
```
