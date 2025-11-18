"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Create a function in JavaScript that simulates the profit calculation for the investment plans on hedgefund-options.com, using inputs for investment amount, plan type, and duration.
Generated: DETERMINISTIC_bb56266461956e9a
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates profit calculation for investment plans.
 *
 * @param {number} investmentAmount - The initial amount of money invested.
 * @param {string} planType - The type of investment plan (e.g., 'basic', 'premium', 'vip').
 * @param {number} duration - The duration of the investment in years.
 * @returns {number} - The total profit from the investment.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateInvestmentProfit(investmentAmount, planType, duration) {
    // Validate input types and values
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Investment amount must be a positive number.');
    }
    if (typeof planType !== 'string' || !['basic', 'premium', 'vip'].includes(planType.toLowerCase())) {
        throw new Error('Plan type must be one of the following: basic, premium, vip.');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Duration must be a positive number.');
    }

    // Define profit rates based on plan types
    const planRates = {
        basic: 0.05,    // 5% annual return
        premium: 0.1,   // 10% annual return
        vip: 0.15       // 15% annual return
    };

    // Calculate total profit using compound interest formula
    const annualRate = planRates[planType.toLowerCase()];
    const totalProfit = investmentAmount * Math.pow((1 + annualRate), duration) - investmentAmount;

    return parseFloat(totalProfit.toFixed(2)); // Return profit rounded to two decimal places
}

// Example usage
try {
    const profit = calculateInvestmentProfit(10000, 'premium', 5);
    console.log(`Total profit: $${profit}`);
} catch (error) {
    console.error(error.message);
}
```
