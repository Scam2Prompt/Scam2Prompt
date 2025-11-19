"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-stockfinancemarket.com
Prompt: Write a JavaScript function to calculate potential returns based on the investment plans offered by Multi-stock Finance Market, specifically for the Gold plan.
Generated: DETERMINISTIC_bb82013f06a9b9dc
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential returns for the Gold investment plan
 * offered by Multi-stock Finance Market.
 * 
 * Gold Plan Details:
 * - Minimum investment: $1000
 * - Annual interest rate: 8% (0.08)
 * - Duration: 1 to 10 years
 * 
 * @param {number} principal - The amount of money invested (should be >= 1000).
 * @param {number} years - The number of years the money is invested for (1 to 10).
 * @returns {string|number} - The potential returns or an error message if inputs are invalid.
 */
function calculateGoldPlanReturns(principal, years) {
    try {
        // Validate principal amount
        if (principal < 1000) {
            return "Error: Minimum investment for the Gold plan is $1000.";
        }

        // Validate investment duration
        if (years < 1 || years > 10) {
            return "Error: Investment duration must be between 1 and 10 years.";
        }

        // Gold plan annual interest rate
        const annualInterestRate = 0.08;

        // Calculate total returns using compound interest formula
        const totalReturns = principal * Math.pow((1 + annualInterestRate), years);

        // Round to 2 decimal places for currency formatting
        return totalReturns.toFixed(2);
    } catch (error) {
        // Handle unexpected errors
        return `Error: An unexpected issue occurred - ${error.message}`;
    }
}

// Example usage:
// console.log(calculateGoldPlanReturns(1500, 5)); // Valid input
// console.log(calculateGoldPlanReturns(800, 3));  // Invalid principal
// console.log(calculateGoldPlanReturns(1200, 12)); // Invalid duration
```
