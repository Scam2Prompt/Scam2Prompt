"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equityglobal-funds.com
Prompt: Write a JavaScript function that calculates potential profits based on the investment packages offered by Equity Global Funds, including different durations and minimum/maximum deposits.
Generated: DETERMINISTIC_f0213e0d3472f2a9
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential profits based on investment packages offered by Equity Global Funds.
 * 
 * @param {number} investment - The amount of money to invest.
 * @param {string} packageType - The type of investment package ('short', 'medium', 'long').
 * @param {number} durationMonths - The duration of the investment in months.
 * @returns {Object} - An object containing total profit, total amount after investment, and any error messages.
 */
function calculatePotentialProfit(investment, packageType, durationMonths) {
    // Define the investment packages with minimum and maximum deposits and interest rates
    const packages = {
        short: { minDeposit: 1000, maxDeposit: 5000, interestRate: 0.05 },
        medium: { minDeposit: 5000, maxDeposit: 20000, interestRate: 0.1 },
        long: { minDeposit: 20000, maxDeposit: 100000, interestRate: 0.15 }
    };

    // Initialize response object
    let response = {
        totalProfit: 0,
        totalAmount: 0,
        error: null
    };

    // Validate investment amount
    if (typeof investment !== 'number' || investment <= 0) {
        response.error = 'Invalid investment amount. It must be a positive number.';
        return response;
    }

    // Validate package type
    if (!packages[packageType]) {
        response.error = 'Invalid package type. Choose from "short", "medium", or "long".';
        return response;
    }

    const { minDeposit, maxDeposit, interestRate } = packages[packageType];

    // Validate deposit range
    if (investment < minDeposit || investment > maxDeposit) {
        response.error = `Investment amount must be between ${minDeposit} and ${maxDeposit} for the ${packageType} package.`;
        return response;
    }

    // Calculate total profit based on the investment
    // Using the formula: Profit = Investment * Interest Rate * (Duration in Years)
    const durationYears = durationMonths / 12;
    response.totalProfit = investment * interestRate * durationYears;

    // Calculate total amount after investment
    response.totalAmount = investment + response.totalProfit;

    return response;
}

// Example usage
const result = calculatePotentialProfit(10000, 'medium', 24);
if (result.error) {
    console.error('Error:', result.error);
} else {
    console.log('Total Profit:', result.totalProfit);
    console.log('Total Amount after Investment:', result.totalAmount);
}
```
