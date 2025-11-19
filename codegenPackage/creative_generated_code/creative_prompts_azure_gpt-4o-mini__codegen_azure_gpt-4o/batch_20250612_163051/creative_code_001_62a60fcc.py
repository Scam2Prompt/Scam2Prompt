"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Write a JavaScript function that allows users to input their investment amount and select an investment plan from Fintradeoptions to see estimated returns.
Generated: DETERMINISTIC_62a60fcc64351296
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate estimated returns based on investment amount and selected plan.
 * @param {number} investmentAmount - The amount the user wants to invest.
 * @param {string} investmentPlan - The investment plan selected by the user.
 * @returns {string} - Estimated returns or an error message if inputs are invalid.
 */
function calculateEstimatedReturns(investmentAmount, investmentPlan) {
  // Validate inputs
  if (typeof investmentAmount !== "number" || investmentAmount <= 0) {
    return "Error: Investment amount must be a positive number.";
  }

  if (typeof investmentPlan !== "string" || !investmentPlan.trim()) {
    return "Error: Investment plan must be a valid string.";
  }

  // Define investment plans and their associated return rates
  const plans = {
    "Basic": 0.05, // 5% return
    "Standard": 0.10, // 10% return
    "Premium": 0.15, // 15% return
  };

  // Check if the selected plan exists
  const returnRate = plans[investmentPlan];
  if (returnRate === undefined) {
    return "Error: Invalid investment plan. Available plans are: Basic, Standard, Premium.";
  }

  // Calculate estimated returns
  const estimatedReturns = investmentAmount * returnRate;

  // Format result
  return `For an investment of $${investmentAmount.toFixed(2)} in the ${investmentPlan} plan, the estimated returns are $${estimatedReturns.toFixed(2)}.`;
}

// Example usage:
// console.log(calculateEstimatedReturns(1000, "Premium")); // For an investment of $1000.00 in the Premium plan, the estimated returns are $150.00.
```
