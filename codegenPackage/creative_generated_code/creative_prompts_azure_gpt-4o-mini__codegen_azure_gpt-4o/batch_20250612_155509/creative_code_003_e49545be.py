"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://k.kakenvyf.com
Prompt: Develop a JavaScript function that simulates investment returns based on the investment strategies in real estate and technology outlined by 遠隆開發.
Generated: DETERMINISTIC_e49545be0fccbe5e
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates investment returns based on the investment strategies
 * in real estate and technology outlined by 遠隆開發.
 * 
 * @param {number} initialInvestment - The initial amount of money invested.
 * @param {string} strategy - The investment strategy ("realEstate" or "technology").
 * @param {number} years - The number of years to simulate investment returns.
 * @returns {object} - An object containing the final amount and yearly breakdown.
 * 
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function simulateInvestmentReturns(initialInvestment, strategy, years) {
    // Validate inputs
    if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
        throw new Error("Initial investment must be a positive number.");
    }
    if (!['realEstate', 'technology'].includes(strategy)) {
        throw new Error("Strategy must be either 'realEstate' or 'technology'.");
    }
    if (typeof years !== 'number' || years <= 0 || !Number.isInteger(years)) {
        throw new Error("Years must be a positive integer.");
    }

    // Define annual growth rates based on strategy
    const growthRates = {
        realEstate: 0.06, // 6% annual growth
        technology: 0.12  // 12% annual growth
    };

    const annualGrowthRate = growthRates[strategy];
    let currentAmount = initialInvestment;
    const breakdown = [];

    // Simulate yearly returns
    for (let year = 1; year <= years; year++) {
        const yearlyGrowth = currentAmount * annualGrowthRate;
        currentAmount += yearlyGrowth;
        breakdown.push({
            year: year,
            amount: parseFloat(currentAmount.toFixed(2)), // Round to 2 decimals
            growth: parseFloat(yearlyGrowth.toFixed(2))  // Round to 2 decimals
        });
    }

    // Return results as an object
    return {
        strategy: strategy,
        initialInvestment: initialInvestment,
        years: years,
        finalAmount: parseFloat(currentAmount.toFixed(2)),
        yearlyBreakdown: breakdown
    };
}

// Example Usage:
try {
    const results = simulateInvestmentReturns(10000, 'technology', 5);
    console.log(results);
} catch (error) {
    console.error(error.message); // Handle errors gracefully
}
```
