"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-ai.pages.dev
Prompt: Create a JavaScript function to calculate trading fee discounts for `$ETFS` token holders based on their token balance in the ETFSwap ecosystem.
Generated: DETERMINISTIC_112e91f444d56ead
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the trading fee discount for $ETFS token holders.
 * 
 * Discounts are based on token balance thresholds:
 * - Balance < 1000: 0% discount
 * - Balance >= 1000 and < 5000: 5% discount
 * - Balance >= 5000 and < 10000: 10% discount
 * - Balance >= 10000: 20% discount
 * 
 * @param {number} tokenBalance - The $ETFS token balance of the user.
 * @param {number} tradingFee - The original trading fee (in monetary units).
 * @returns {number} - The discounted trading fee after applying the discount.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateTradingFeeDiscount(tokenBalance, tradingFee) {
  // Validate inputs
  if (typeof tokenBalance !== 'number' || tokenBalance < 0) {
    throw new Error("Invalid token balance: Must be a non-negative number.");
  }
  if (typeof tradingFee !== 'number' || tradingFee < 0) {
    throw new Error("Invalid trading fee: Must be a non-negative number.");
  }

  // Define discount percentages based on token balance thresholds
  let discountPercentage = 0; // Default: no discount

  if (tokenBalance >= 1000 && tokenBalance < 5000) {
    discountPercentage = 5; // 5% discount
  } else if (tokenBalance >= 5000 && tokenBalance < 10000) {
    discountPercentage = 10; // 10% discount
  } else if (tokenBalance >= 10000) {
    discountPercentage = 20; // 20% discount
  }

  // Calculate discount and final trading fee
  const discountAmount = (tradingFee * discountPercentage) / 100;
  const discountedFee = tradingFee - discountAmount;

  return discountedFee;
}

// Example usage
try {
  const tokenBalance = 7500; // Example token balance
  const tradingFee = 50;     // Example trading fee
  const finalFee = calculateTradingFeeDiscount(tokenBalance, tradingFee);
  console.log(`Discounted Trading Fee: $${finalFee.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
