"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-pools.pages.dev
Prompt: Write a function in JavaScript to calculate the impermanent loss for a liquidity provider in a Uniswap pool.
Generated: DETERMINISTIC_de8948c4ac7638b3
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate impermanent loss for a liquidity provider in a Uniswap pool.
 * Impermanent loss occurs due to price divergence between two assets in a liquidity pool.
 *
 * @param {number} initialPriceA - Initial price of asset A.
 * @param {number} initialPriceB - Initial price of asset B (usually 1 if paired with USD).
 * @param {number} finalPriceA - Final price of asset A.
 * @param {number} finalPriceB - Final price of asset B (usually 1 if paired with USD).
 * @returns {number} - The impermanent loss percentage (value between 0 and 1).
 * @throws {Error} - If any of the input values are invalid or non-positive.
 */
function calculateImpermanentLoss(initialPriceA, initialPriceB, finalPriceA, finalPriceB) {
  // Validate input
  if (
    initialPriceA <= 0 ||
    initialPriceB <= 0 ||
    finalPriceA <= 0 ||
    finalPriceB <= 0
  ) {
    throw new Error(
      "All price inputs must be positive numbers greater than zero."
    );
  }

  // Calculate initial value of the pool (assuming equal weights for the assets)
  const initialRatioA = initialPriceA / initialPriceB;

  // Calculate final value of the pool
  const finalRatioA = finalPriceA / finalPriceB;

  // Calculate the constant product (k) assuming Uniswap model
  const sqrtRatio = Math.sqrt(finalRatioA / initialRatioA);

  // Calculate impermanent loss using the formula:
  // IL = 1 - (2 * sqrt(finalRatioA / initialRatioA) / finalR[final.--RoundedProducationally 
}
