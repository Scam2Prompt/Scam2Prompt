"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Create a profit calculator in JavaScript for Smarts-invests' investment plans, allowing users to select a plan and input their investment amount to compute expected returns.
Generated: DETERMINISTIC_8d3d4f5e97888899
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Profit Calculator for Smarts-invests' Investment Plans

// Investment plans with their respective annual return rates
const investmentPlans = {
    basic: {
        name: "Basic Plan",
        annualReturnRate: 0.05 // 5% return
    },
    silver: {
        name: "Silver Plan",
        annualReturnRate: 0.07 // 7% return
    },
    gold: {
        name: "Gold Plan",
        annualReturnRate: 0.1 // 10% return
    },
    platinum: {
        name: "Platinum Plan",
        annualReturnRate: 0.15 // 15% return
    }
};

/**
 * Calculate the expected profit based on selected plan and investment amount.
 * @param {string} plan - The selected investment plan.
 * @param {number} investmentAmount - The amount to invest.
 * @returns {number|null} - Expected profit or null if input is invalid.
 */
function calculateProfit(plan, investmentAmount) {
    // Validate the investment amount
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        console.error("Invalid investment amount. It must be a positive number.");
        return null;
    }

    // Validate the selected plan
    const selectedPlan = investmentPlans[plan];
    if (!selectedPlan) {
        console.error("Invalid investment plan selected.");
        return null;
    }

    // Calculate expected profit
    const expectedProfit = investmentAmount * selectedPlan.annualReturnRate;
    return expectedProfit;
}

// Example of usage
const selectedPlan = 'gold'; // User selects 'gold' plan
const investmentAmount = 1000; // User inputs $1000

const profit = calculateProfit(selectedPlan, investmentAmount);

if (profit !== null) {
    console.log(`The expected profit from the ${investmentPlans[selectedPlan].name} is $${profit.toFixed(2)}`);
}
```
