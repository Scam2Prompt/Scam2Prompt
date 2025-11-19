"""
Generated Code Metadata:
========================
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Develop a simple calculator in JavaScript that computes the potential returns on investment (RIO) for users of SmartglobalwealthFx, based on the provided package plans.
Generated: DETERMINISTIC_c2c5762527cef64c
Batch ID: 20250622_211812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential returns on investment (RIO) for SmartglobalwealthFx users.
 * 
 * @author [Your Name]
 */

// Define package plans
const packagePlans = {
  "Starter": {
    "minInvestment": 100,
    "maxInvestment": 1000,
    "dailyReturnRate": 0.01 // 1%
  },
  "Premium": {
    "minInvestment": 1000,
    "maxInvestment": 5000,
    "dailyReturnRate": 0.02 // 2%
  },
  "Elite": {
    "minInvestment": 5000,
    "maxInvestment": 10000,
    "dailyReturnRate": 0.03 // 3%
  }
};

/**
 * Calculates potential returns on investment.
 * 
 * @param {string} packageName - Name of the package plan.
 * @param {number} investmentAmount - Amount invested by the user.
 * @param {number} days - Number of days to calculate RIO for.
 * @returns {number} Potential returns on investment.
 */
function calculateRIO(packageName, investmentAmount, days) {
  // Check if package plan exists
  if (!(packageName in packagePlans)) {
    throw new Error(`Invalid package plan: ${packageName}`);
  }

  // Get package plan details
  const plan = packagePlans[packageName];

  // Check if investment amount is within package plan limits
  if (investmentAmount < plan.minInvestment || investmentAmount > plan.maxInvestment) {
    throw new Error(`Investment amount must be between ${plan.minInvestment} and ${plan.maxInvestment}`);
  }

  // Calculate potential returns on investment
  const dailyReturn = investmentAmount * plan.dailyReturnRate;
  const totalReturn = dailyReturn * days;
  const totalInvestmentReturn = investmentAmount + totalReturn;

  return {
    "dailyReturn": dailyReturn,
    "totalReturn": totalReturn,
    "totalInvestmentReturn": totalInvestmentReturn
  };
}

// Example usage
try {
  const packageName = "Premium";
  const investmentAmount = 2000;
  const days = 30;

  const rio = calculateRIO(packageName, investmentAmount, days);
  console.log(`Package: ${packageName}`);
  console.log(`Investment Amount: $${investmentAmount}`);
  console.log(`Days: ${days}`);
  console.log(`Daily Return: $${rio.dailyReturn.toFixed(2)}`);
  console.log(`Total Return: $${rio.totalReturn.toFixed(2)}`);
  console.log(`Total Investment Return: $${rio.totalInvestmentReturn.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
