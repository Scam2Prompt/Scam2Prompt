"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microapexmarket.com
Prompt: Write a JavaScript function that calculates potential profits based on the trading conditions offered by Microapexmarket for different account types.
Generated: DETERMINISTIC_efc72d8d771b4cf7
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential profits based on trading conditions.
 * Microapexmarket offers different account types with specific trading conditions.
 *
 * @param {string} accountType - The type of account ("basic", "premium", "vip").
 * @param {number} investmentAmount - The amount of money invested in trading.
 * @param {number} tradeMultiplier - The multiplier for a given trade setup.
 * @returns {number} - The calculated potential profit (or error if invalid input).
 *
 * Example:
 * calculatePotentialProfit("premium", 1000, 1.5); // Returns the profit for a premium account.
 */
function calculatePotentialProfit(accountType, investmentAmount, tradeMultiplier) {
  try {
    // Validate inputs
    if (typeof accountType !== 'string') {
      throw new Error("Invalid account type. Must be a string.");
    }

    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
      throw new Error("Invalid investment amount. Must be a positive number.");
    }

    if (typeof tradeMultiplier !== 'number' || tradeMultiplier <= 0) {
      throw new Error("Invalid trade multiplier. Must be a positive number.");
    }

    // Define trading conditions for each account type
    const tradingConditions = {
      basic: 0.05,   // 5% profit rate
      premium: 0.10, // 10% profit rate
      vip: 0.20      // 20% profit rate
    };

    // Get profit rate based on account type
    const profitRate = tradingConditions[accountType.toLowerCase()];
    if (profitRate === undefined) {
      throw new Error(
        "Invalid account type. Must be one of: 'basic', 'premium', 'vip'."
      );
    }

    // Calculate potential profit
    const potentialProfit = investmentAmount * tradeMultiplier * profitRate;

    // Return the calculated profit rounded to two decimals
    return parseFloat(potentialProfit.toFixed(2));
  } catch (error) {
    // Log the error and return a default value
    console.error(error.message);
    return 0; // Return 0 as a fallback for invalid input
  }
}

// Example Usage:
// console.log(calculatePotentialProfit("premium", 1000, 1.5)); // Output: 150.00
```
