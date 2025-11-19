"""
Generated Code Metadata:
========================
Original URL: https://theasterixtrade.com
Prompt: Write a JavaScript function that calculates potential profits based on the investment plans (Easy, Professional, Executive) offered by Asterix Trade, including daily profit percentages.
Generated: DETERMINISTIC_9a282e89fb036db6
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential profits based on the investment plan selected.
 * 
 * @param {number} investmentAmount - The amount of money invested.
 * @param {string} plan - The investment plan selected. Can be 'Easy', 'Professional', or 'Executive'.
 * @param {number} days - The number of days the investment is held.
 * @returns {number} - The potential profit based on the investment plan.
 * @throws {Error} - Throws an error if the investment amount is less than or equal to zero,
 *                   if the plan is not recognized, or if days is not a positive integer.
 */
function calculatePotentialProfit(investmentAmount, plan, days) {
    // Validate input parameters
    if (investmentAmount <= 0) {
        throw new Error("Investment amount must be greater than zero.");
    }
    if (days <= 0 || !Number.isInteger(days)) {
        throw new Error("Days must be a positive integer.");
    }

    // Define daily profit percentages for each plan
    const profitPercentages = {
        Easy: 0.01,        // 1% daily profit
        Professional: 0.02, // 2% daily profit
        Executive: 0.03    // 3% daily profit
    };

    // Check if the selected plan is valid
    if (!profitPercentages.hasOwnProperty(plan)) {
        throw new Error("Invalid investment plan selected. Choose 'Easy', 'Professional', or 'Executive'.");
    }

    // Calculate potential profit
    const dailyProfitPercentage = profitPercentages[plan];
    const potentialProfit = investmentAmount * dailyProfitPercentage * days;

    return potentialProfit;
}

// Example usage:
try {
    const investment = 1000; // Example investment amount
    const plan = 'Professional'; // Example investment plan
    const duration = 30; // Example duration in days

    const profit = calculatePotentialProfit(investment, plan, duration);
    console.log(`Potential profit for ${plan} plan over ${duration} days: $${profit.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
