"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Develop a JavaScript-based profit calculator for Steadfast Asset Innovation's investment plans, allowing users to select a plan and input their investment amount to calculate returns.
Generated: DETERMINISTIC_d300bf8d84c9c3fb
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Steadfast Asset Innovation Profit Calculator
// This script provides a simple way to calculate investment returns based on predefined plans.

// Define the investment plans
const investmentPlans = {
  basic: {
    name: "Basic Plan",
    rate: 0.05, // 5% return
    description: "5% return on your investment."
  },
  standard: {
    name: "Standard Plan",
    rate: 0.1, // 10% return
    description: "10% return on your investment."
  },
  premium: {
    name: "Premium Plan",
    rate: 0.2, // 20% return
    description: "20% return on your investment."
  }
};

// Function to calculate the profit based on the selected plan and investment amount
function calculateProfit(planKey, investmentAmount) {
  // Input validation
  if (!investmentPlans[planKey]) {
    throw new Error("Invalid investment plan selected.");
  }
  if (isNaN(investmentAmount) || investmentAmount <= 0) {
    throw new Error("Investment amount must be a positive number.");
  }

  const plan = investmentPlans[planKey];
  const profit = investmentAmount * plan.rate; // Calculate profit
  return {
    planName: plan.name,
    investmentAmount,
    profit,
    totalReturn: investmentAmount + profit // Total return = initial amount + profit
  };
}

// Example usage (this would typically be replaced by user input in a real application)
try {
  const selectedPlan = "standard"; // User-selected plan (e.g., "basic", "standard", "premium")
  const investmentAmount = 1000; // User-provided investment amount

  // Perform profit calculation
  const result = calculateProfit(selectedPlan, investmentAmount);

  // Display the results
  console.log("Investment Plan:", result.planName);
  console.log("Investment Amount: $", result.investmentAmount.toFixed(2));
  console.log("Profit: $", result.profit.toFixed(2));
  console.log("Total Return: $", result.totalReturn.toFixed(2));
} catch (error) {
  // Handle errors gracefully
  console.error("Error:", error.message);
}

// Example function for displaying plans (optional)
// This function can be used to show available plans to the user
function displayAvailablePlans() {
  console.log("Available Investment Plans:");
  for (const key in investmentPlans) {
    const plan = investmentPlans[key];
    console.log(`- ${plan.name}: ${plan.description} (Rate: ${plan.rate * 100}%)`);
  }
}

// Uncomment the line below to display available plans
// displayAvailablePlans();
```
