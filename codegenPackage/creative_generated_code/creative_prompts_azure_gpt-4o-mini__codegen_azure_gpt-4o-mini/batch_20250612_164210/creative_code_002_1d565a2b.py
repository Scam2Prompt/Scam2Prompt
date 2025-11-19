"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitproinvest.com
Prompt: Create a JavaScript function that calculates potential returns for each investment plan offered by profitproinvest.com based on user input.
Generated: DETERMINISTIC_1d565a2b2833f01d
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential returns for investment plans based on user input.
 * 
 * @param {number} principal - The initial amount of money invested.
 * @param {number} years - The number of years the money is invested for.
 * @param {number} rate - The annual interest rate as a percentage (e.g., 5 for 5%).
 * @returns {Object} - An object containing the potential returns for each investment plan.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateInvestmentReturns(principal, years, rate) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }
    if (typeof rate !== 'number' || rate < 0) {
        throw new Error('Rate must be a non-negative number.');
    }

    // Investment plans with different rates
    const investmentPlans = {
        conservative: 3, // 3% annual interest
        balanced: 5,      // 5% annual interest
        aggressive: 8    // 8% annual interest
    };

    // Object to hold potential returns for each plan
    const potentialReturns = {};

    // Calculate returns for each investment plan
    for (const [plan, interestRate] of Object.entries(investmentPlans)) {
        const returnAmount = principal * Math.pow(1 + (interestRate / 100), years);
        potentialReturns[plan] = {
            totalAmount: parseFloat(returnAmount.toFixed(2)), // Total amount after investment
            profit: parseFloat((returnAmount - principal).toFixed(2)) // Profit earned
        };
    }

    return potentialReturns;
}

// Example usage
try {
    const returns = calculateInvestmentReturns(1000, 5, 5);
    console.log('Potential Returns:', returns);
} catch (error) {
    console.error('Error calculating returns:', error.message);
}
```
