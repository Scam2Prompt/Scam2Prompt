"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinstantmining.com
Prompt: Write a code snippet in JavaScript that calculates potential profits based on the investment plans offered by Globalinstantmining, such as the Silver, Gold, and Premium accounts.
Generated: DETERMINISTIC_227a0ac78d8a0b65
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Investment plans offered by Globalinstantmining
 * Silver: Minimum investment $500, profit rate 5%
 * Gold: Minimum investment $1000, profit rate 10%
 * Premium: Minimum investment $5000, profit rate 20%
 */

/**
 * Function to calculate potential profit based on the investment plan
 * @param {string} plan - The investment plan (Silver, Gold, Premium)
 * @param {number} amount - The investment amount
 * @returns {object} - Object containing valid status and profit information
 */
function calculateProfit(plan, amount) {
  // Define investment plans and their respective profit rates
  const investmentPlans = {
    Silver: { minInvestment: 500, profitRate: 0.05 },
    Gold: { minInvestment: 1000, profitRate: 0.10 },
    Premium: { minInvestment: 5000, profitRate: 0.20 },
  };

  // Validate input parameters
  if (typeof plan !== 'string' || typeof amount !== 'number' || amount <= 0) {
    return {
      valid: false,
      message: "Invalid input. Plan must be a string and amount must be a positive number.",
      profit: null,
    };
  }

  // Check if the plan exists in the predefined investment plans
  const selectedPlan = investmentPlans[plan];
  if (!selectedPlan) {
    return {
      valid: false,
      message: "Invalid plan. Choose from Silver, Gold, or Premium.",
      profit: null,
    };
  }

  // Ensure the investment meets the minimum requirement for the selected plan
  if (amount < selectedPlan.minInvestment) {
    return {
      valid: false,
      message: `Insufficient investment amount for the ${plan} plan. Minimum required is $${selectedPlan.minInvestment}.`,
      profit: null,
    };
  }

  // Calculate the profit based on the profit rate of the selected plan
  const profit = amount * selectedPlan.profitRate;

  return {
    valid: true,
    message: `Profit calculated successfully for the ${plan} plan.`,
    profit: profit,
  };
}

// Example usage
try {
  const investmentPlan = "Gold"; // Can be "Silver", "Gold", or "Premium"
  const investmentAmount = 1500;

  const result = calculateProfit(investmentPlan, investmentAmount);
  if (result.valid) {
    console.log(`Success: ${result.message}`);
    console.log(`Potential Profit: $${result.profit.toFixed(2)}`);
  } else {
    console.log(`Error: ${result.message}`);
  }
} catch (error) {
  console.error("Unexpected error occurred:", error.message);
}
```
