"""
Generated Code Metadata:
========================
Original URL: https://fintradeoptions.com
Prompt: "Design a simple investment calculator in JavaScript that takes into account the Fintradeoptions investment plans, including the capital back and return type for each plan."
Generated: DETERMINISTIC_848c9d18fdbb97bc
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Investment Calculator for Fintradeoptions Plans
 * 
 * This script calculates the total return on investment based on Fintradeoptions plans.
 * Each plan has a specific return type and capital back policy.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Define the investment plans
const investmentPlans = [
  {
    name: "Basic Plan",
    returnRate: 0.05, // 5% return
    capitalBack: true, // Capital is returned
  },
  {
    name: "Standard Plan",
    returnRate: 0.1, // 10% return
    capitalBack: true, // Capital is returned
  },
  {
    name: "Premium Plan",
    returnRate: 0.15, // 15% return
    capitalBack: false, // Capital is not returned
  },
];

/**
 * Calculate the total return on investment.
 * 
 * @param {number} principal - The initial investment amount.
 * @param {string} planName - The name of the investment plan.
 * @returns {number} - The total return on investment.
 * @throws {Error} - Throws an error if the plan name is invalid or principal is negative.
 */
function calculateInvestmentReturn(principal, planName) {
  // Validate input
  if (principal <= 0) {
    throw new Error("Principal amount must be greater than zero.");
  }

  const plan = investmentPlans.find((p) => p.name === planName);
  if (!plan) {
    throw new Error("Invalid investment plan name.");
  }

  // Calculate return
  const returnAmount = principal * plan.returnRate;
  const totalReturn = plan.capitalBack ? principal + returnAmount : returnAmount;

  return totalReturn;
}

/**
 * Display the investment calculation result.
 * 
 * @param {number} principal - The initial investment amount.
 * @param {string} planName - The name of the investment plan.
 */
function displayInvestmentResult(principal, planName) {
  try {
    const totalReturn = calculateInvestmentReturn(principal, planName);
    console.log(`Investment Plan: ${planName}`);
    console.log(`Principal Amount: $${principal.toFixed(2)}`);
    console.log(`Total Return: $${totalReturn.toFixed(2)}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Example usage
const principal = 1000; // Example principal amount
const planName = "Standard Plan"; // Example plan name

displayInvestmentResult(principal, planName);
```
