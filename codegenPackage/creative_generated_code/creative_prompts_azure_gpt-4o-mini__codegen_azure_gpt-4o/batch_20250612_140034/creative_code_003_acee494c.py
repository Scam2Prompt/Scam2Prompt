"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buildstock-finance.com
Prompt: Write a JavaScript function that calculates potential profits based on the investment plans offered by Buildstock-Finance Investment, such as the Deluxe Plan and Exclusive Plan.
Generated: DETERMINISTIC_acee494cd8bc61ac
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential profits based on investment plans.
 * 
 * Buildstock-Finance Investment offers two plans:
 * - Deluxe Plan: 5% daily profit for a specified number of days.
 * - Exclusive Plan: 8% daily profit for a specified number of days.
 * 
 * @param {string} plan - The investment plan ('Deluxe' or 'Exclusive').
 * @param {number} principal - The initial investment amount (must be a positive number).
 * @param {number} days - The number of days the investment will last (must be a positive integer).
 * @returns {number} - The total potential profit after the investment period.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculatePotentialProfit(plan, principal, days) {
    // Validate inputs
    if (typeof plan !== 'string' || (plan !== 'Deluxe' && plan !== 'Exclusive')) {
        throw new Error("Invalid plan. Please choose 'Deluxe' or 'Exclusive'.");
    }
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error("Invalid principal amount. Must be a positive number.");
    }
    if (!Number.isInteger(days) || days <= 0) {
        throw new Error("Invalid number of days. Must be a positive integer.");
    }

    // Set the daily profit rate based on the plan
    let dailyRate;
    if (plan === 'Deluxe') {
        dailyRate = 0.05; // 5% daily profit
    } else if (plan === 'Exclusive') {
        dailyRate = 0.08; // 8% daily profit
    }

    // Calculate total profit
    const totalProfit = principal * dailyRate * days;

    // Round to two decimal places for financial calculations
    return parseFloat(totalProfit.toFixed(2));
}

// Example Usage:
// Uncomment the lines below to test the function

// try {
//     console.log(calculatePotentialProfit('Deluxe', 1000, 30)); // Expected output: 1500.00
//     console.log(calculatePotentialProfit('Exclusive', 1000, 30)); // Expected output: 2400.00
// } catch (error) {
//     console.error(error.message);
// }
```
