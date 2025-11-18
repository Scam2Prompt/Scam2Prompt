"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degentip-9l3.pages.dev
Prompt: Write a JavaScript function using ethers.js to calculate impermanent loss for liquidity provided in the Uniswap V3 DEGEN/WETH pool.
Generated: DETERMINISTIC_ed90421bc97c8fc2
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates impermanent loss for liquidity provided in a Uniswap V3 pool.
 *
 * @param {number} initialRatio - The initial price ratio of the two assets (DEGEN/WETH).
 * @param {number} finalRatio - The final price ratio of the two assets (DEGEN/WETH).
 * @returns {number} - The impermanent loss as a percentage.
 *
 * Note: This function assumes the liquidity provider holds equal value of both assets initially.
 */

function calculateImpermanentLoss(initialRatio, finalRatio) {
  if (initialRatio <= 0 || finalRatio <= 0) {
    throw new Error("Initial and final ratios must be positive numbers.");
  }

  // Calculate square root of price ratio (used for AMM calculations).
  const sqrtInitialRatio = Math.sqrt(initialRatio);
  const sqrtFinalRatio = Math.sqrt(finalRatio);

  // Calculate the value of assets held after price change.
  const valueAfterChange =
    (2 * sqrtInitialRatio * sqrtFinalRatio) / (sqrtInitialRatio + sqrtFinalRatio);

  // Calculate impermanent loss percentage.
  const impermanentLoss = ((valueAfterChange / 2) - 1) * 100;

  return Math.abs(impermanentLoss); // Return the absolute value as a percentage.
}

// Example usage:
try {
  const initialRatio = 1.25; // Example initial ratio of DEGEN to WETH.
  const finalRatio = 1.75;   // Example final ratio of DEGEN to WETH.

  const impermanentLoss = calculateImpermanentLoss(initialRatio, finalRatio);
  console.log(`Impermanent Loss: ${impermanentLoss.toFixed(2)}%`);
} catch (error) {
  console.error(`Error calculating impermanent loss: ${error.message}`);
}
```
