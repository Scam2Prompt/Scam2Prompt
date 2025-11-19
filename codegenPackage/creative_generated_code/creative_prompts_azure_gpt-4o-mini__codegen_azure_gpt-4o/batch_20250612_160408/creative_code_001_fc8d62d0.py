"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoprohashings.vip
Prompt: Write a JavaScript function that calculates potential profits based on the investment plans offered by CryptoProHashings, specifically for the Silver, Gold, and Premium accounts.
Generated: DETERMINISTIC_fc8d62d0e2ffdaf4
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential profits based on CryptoProHashings investment plans.
 * 
 * Investment plans:
 * - Silver: 5% profit per month
 * - Gold: 10% profit per month
 * - Premium: 20% profit per month
 * 
 * @param {string} plan - The investment plan ('Silver', 'Gold', or 'Premium').
 * @param {number} principal - The initial investment amount.
 * @param {number} months - The duration of the investment in months.
 * @returns {object} An object containing the potential profit and total amount.
 * @throws {Error} If input values are invalid or plan is unrecognized.
 */
function calculateCryptoProfits(plan, principal, months) {
    // Validate input values
    if (typeof plan !== 'string') {
        throw new Error("Invalid plan type. Expected a string ('Silver', 'Gold', 'Premium').");
    }
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error("Invalid principal. Expected a positive number.");
    }
    if (typeof months !== 'number' || months <= 0) {
        throw new Error("Invalid months. Expected a positive number.");
    }

    // Define profit rates for each plan
    const profitRates = {
        Silver: 0.05,  // 5% per month
        Gold: 0.10,    // 10% per month
        Premium: 0.20  // 20% per month
    };

    // Check if the plan is valid
    if (!profitRates.hasOwnProperty(plan)) {
        throw new Error("Unrecognized plan. Available plans are 'Silver', 'Gold', and 'Premium'.");
    }

    // Calculate potential profits
    const rate = profitRates[plan];
    const profit = principal * rate * months; // Total profit for the given months
    const totalAmount = principal + profit;  // Total amount after adding the profit

    // Return the result as an object
    return {
        profit: parseFloat(profit.toFixed(2)),     // Round to 2 decimal places
        totalAmount: parseFloat(totalAmount.toFixed(2)) // Round to 2 decimal places
    };
}

// Example usage:
try {
    const result = calculateCryptoProfits('Gold', 1000, 6);
    console.log(result); // Outputs: { profit: 600, totalAmount: 1600 }
} catch (error) {
    console.error(error.message);
}
```
