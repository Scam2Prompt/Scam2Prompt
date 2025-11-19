"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Write a JavaScript function that simulates the investment process on CoineeHub, allowing users to input their investment amount and calculate expected profits based on the specified plans.
Generated: DETERMINISTIC_22a3e566aa245c48
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * InvestmentSimulator class provides functionality to simulate investments
 * on CoineeHub.
 */
class InvestmentSimulator {
    constructor() {
        // Define the investment plans with their respective profit percentages
        this.plans = {
            basic: { min: 100, max: 999, profitPercent: 5 },
            advanced: { min: 1000, max: 4999, profitPercent: 10 },
            premium: { min: 5000, max: 10000, profitPercent: 15 }
        };
    }

    /**
     * Calculate expected profits based on the investment amount and selected plan
     * @param {number} amount - The investment amount provided by the user
     * @param {string} plan - The investment plan selected by the user
     * @returns {object} - An object containing the investment amount, profit, and total return
     * @throws {Error} - Throws an error if the input is invalid
     */
    calculateProfit(amount, plan) {
        // Validate input parameters
        if (typeof amount !== 'number' || amount <= 0) {
            throw new Error('Investment amount must be a positive number.');
        }
        if (!this.plans[plan]) {
            throw new Error('Invalid investment plan selected.');
        }

        const selectedPlan = this.plans[plan];

        // Validate that the amount falls within the selected plan's range
        if (amount < selectedPlan.min || amount > selectedPlan.max) {
            throw new Error(`Investment amount must be between ${selectedPlan.min} and ${selectedPlan.max} for the ${plan} plan.`);
        }

        // Calculate profit and total return
        const profit = (amount * selectedPlan.profitPercent) / 100;
        const totalReturn = amount + profit;

        return {
            investment: amount,
            profit: profit,
            totalReturn: totalReturn
        };
    }
}

// Example usage:
try {
    const simulator = new InvestmentSimulator();
    const result = simulator.calculateProfit(1500, 'advanced');
    console.log(result);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
