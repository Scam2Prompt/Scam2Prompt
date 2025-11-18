"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opterisglobal.com
Prompt: Create a function in JavaScript to calculate scalable profits for a cryptocurrency investment plan, using the parameters from Opteris Global's investment plans.
Generated: DETERMINISTIC_709a4493f532ed3e
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate scalable profits for a cryptocurrency investment plan.
 * 
 * @param {number} initialInvestment - The initial amount of money invested.
 * @param {number} profitPercentage - The expected profit percentage per investment cycle.
 * @param {number} cycles - The number of investment cycles.
 * @returns {number} - The total profit after the specified number of cycles.
 * @throws Will throw an error if any of the parameters are invalid.
 */
function calculateScalableProfits(initialInvestment, profitPercentage, cycles) {
    // Validate input parameters
    if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
        throw new Error('Initial investment must be a positive number.');
    }
    if (typeof profitPercentage !== 'number' || profitPercentage < 0) {
        throw new Error('Profit percentage must be a non-negative number.');
    }
    if (typeof cycles !== 'number' || cycles < 0 || !Number.isInteger(cycles)) {
        throw new Error('Cycles must be a non-negative integer.');
    }

    let totalProfit = initialInvestment;

    // Calculate profits for each cycle
    for (let i = 0; i < cycles; i++) {
        totalProfit += totalProfit * (profitPercentage / 100);
    }

    // Return the total profit
    return totalProfit;
}

// Example usage:
try {
    const initialInvestment = 1000; // $1000 investment
    const profitPercentage = 10; // 10% profit per cycle
    const cycles = 5; // 5 investment cycles

    const totalProfit = calculateScalableProfits(initialInvestment, profitPercentage, cycles);
    console.log(`Total Profit after ${cycles} cycles: $${totalProfit.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
