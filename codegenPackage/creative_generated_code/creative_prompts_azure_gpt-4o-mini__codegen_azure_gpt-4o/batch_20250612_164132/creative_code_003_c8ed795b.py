"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bsc-scan.net
Prompt: Create a JavaScript function that calculates weekly and monthly profits based on the investment amount and the selected plan from BSC Scan.
Generated: DETERMINISTIC_c8ed795b49d3479e
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate weekly and monthly profits based on the investment amount 
 * and selected plan.
 * 
 * @param {number} investmentAmount - The amount of money invested.
 * @param {string} plan - The selected investment plan (e.g., "basic", "standard", "premium").
 * @returns {Object} An object containing the weekly and monthly profits.
 * @throws Will throw an error if inputs are invalid or if the plan is not recognized.
 */
function calculateProfits(investmentAmount, plan) {
    // Input validation
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Invalid investment amount. Please provide a positive number.');
    }
    
    if (typeof plan !== 'string' || plan.trim() === '') {
        throw new Error('Invalid plan. Please provide a valid plan name.');
    }

    // Define profit rates for each plan
    const profitRates = {
        basic: { weeklyRate: 0.02, monthlyRate: 0.08 },    // 2% weekly, 8% monthly
        standard: { weeklyRate: 0.035, monthlyRate: 0.14 }, // 3.5% weekly, 14% monthly
        premium: { weeklyRate: 0.05, monthlyRate: 0.2 }    // 5% weekly, 20% monthly
    };

    // Check if the plan exists in profitRates
    if (!profitRates[plan.toLowerCase()]) {
        throw new Error(`Unknown plan: ${plan}. Available plans are: basic, standard, premium.`);
    }

    // Retrieve the profit rates for the selected plan
    const { weeklyRate, monthlyRate } = profitRates[plan.toLowerCase()];

    // Calculate profits
    const weeklyProfit = investmentAmount * weeklyRate;
    const monthlyProfit = investmentAmount * monthlyRate;

    // Return the calculated profits
    return {
        weeklyProfit: parseFloat(weeklyProfit.toFixed(2)), // Round to 2 decimal places
        monthlyProfit: parseFloat(monthlyProfit.toFixed(2)) // Round to 2 decimal places
    };
}

// Example usage
try {
    const investmentAmount = 1000; // Example investment amount
    const plan = 'standard'; // Example plan

    const profits = calculateProfits(investmentAmount, plan);
    console.log(`Weekly Profit: $${profits.weeklyProfit}`);
    console.log(`Monthly Profit: $${profits.monthlyProfit}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
