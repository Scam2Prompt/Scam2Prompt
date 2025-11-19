"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradecurvemarket-en.pages.dev
Prompt: Write a JavaScript function to calculate potential trading fees and rewards when using the Tradecurve platform with TCRV tokens.
Generated: DETERMINISTIC_3e5ed1a361b58ea3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate trading fees and rewards on the Tradecurve platform
 * using TCRV tokens.
 *
 * @param {number} tradeAmount - The amount being traded in USD.
 * @param {number} feeRate - The fee rate as a percentage (e.g., 0.1 for 0.1%).
 * @param {number} rewardRate - The reward rate as a percentage (e.g., 0.5 for 0.5%).
 * @returns {Object} An object containing the calculated trading fee and reward in USD.
 */
function calculateTradecurveFeesAndRewards(tradeAmount, feeRate, rewardRate) {
  // Input validation
  if (typeof tradeAmount !== 'number' || tradeAmount <= 0) {
    throw new Error("Invalid trade amount. Must be a positive number.");
  }
  if (typeof feeRate !== 'number' || feeRate < 0) {
    throw new Error("Invalid fee rate. Must be a non-negative number.");
  }
  if (typeof rewardRate !== 'number' || rewardRate < 0) {
    throw new Error("Invalid reward rate. Must be a non-negative number.");
  }

  // Calculate the trading fee
  const tradingFee = tradeAmount * (feeRate / 100);

  // Calculate the rewards
  const reward = tradeAmount * (rewardRate / 100);

  // Return the results as an object
  return {
    tradingFee: parseFloat(tradingFee.toFixed(2)), // Round to 2 decimal places
    reward: parseFloat(reward.toFixed(2)) // Round to 2 decimal places
  };
}

// Example usage:
try {
  const tradeAmount = 1000;  // Amount being traded in USD
  const feeRate = 0.1;       // Fee rate as a percentage (e.g., 0.1 for 0.1%)
  const rewardRate = 0.5;    // Reward rate as a percentage (e.g., 0.5 for 0.5%)

  const result = calculateTradecurveFeesAndRewards(tradeAmount, feeRate, rewardRate);
  console.log("Trading Fee:", result.tradingFee, "USD");
  console.log("Rewards:", result.reward, "USD");
} catch (error) {
  console.error("Error:", error.message);
}
```
