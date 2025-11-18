"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://justrew.pages.dev
Prompt: Generate a JavaScript function to calculate the optimal swap route among Raydium pools for a given SPL token pair, leveraging the "Best Price Swaps" feature.
Generated: DETERMINISTIC_e1522af8dc555568
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function findOptimalSwapRoute
 * @description Calculates the optimal swap route among Raydium pools for a given SPL token pair.
 * Utilizes the "Best Price Swaps" feature to determine the best route with the highest efficiency.
 *
 * @param {Object} poolsData - Array of Raydium pool data containing liquidity and pricing details.
 * @param {string} tokenA - The source SPL token (e.g., USDC).
 * @param {string} tokenB - The target SPL token (e.g., SOL).
 * @param {number} amountIn - The amount of tokenA to swap.
 * @returns {Object} Optimal route information including pool ID, token pair, and expected output.
 *
 * @throws {Error} If invalid data is provided or no route is found.
 */
async function findOptimalSwapRoute(poolsData, tokenA, tokenB, amountIn) {
  if (!Array.isArray(poolsData) || !tokenA || !tokenB || amountIn <= 0) {
    throw new Error("Invalid input parameters.");
  }

  let optimalRoute = null;
  let maxOutput = 0;

  try {
    for (const pool of poolsData) {
      const { poolId, tokenPair, liquidity, fees } = pool;

      // Ensure the pool supports the requested token pair
      if (!tokenPair.includes(tokenA) || !tokenPair.includes(tokenB)) {
        continue;
      }

      const swapOutput = calculateSwapOutput(liquidity, fees, tokenA, tokenB, amountIn);

      // Update the optimal route if the swap output is higher
      if (swapOutput > maxOutput) {
        maxOutput = swapOutput;
        optimalRoute = {
          poolId,
          tokenPair,
          amountIn,
          amountOut: swapOutput,
        };
      }
    }

    if (!optimalRoute) {
      throw new Error(`No valid swap route found for ${tokenA} -> ${tokenB}.`);
    }

    return optimalRoute;
  } catch (error) {
    console.error("Error finding optimal swap route:", error.message);
    throw error;
  }
}

/**
 * @function calculateSwapOutput
 * @description Calculates the expected output of a swap based on pool liquidity, fees, and input amount.
 *
 * @param {Object} liquidity - Liquidity details of the pool (amounts of tokenA and tokenB).
 * @param {number} fees - The swap fee percentage for the pool.
 * @param {string} tokenA - The source SPL token.
 * @param {string} tokenB - The target SPL token.
 * @param {number} amountIn - The amount of tokenA to swap.
 * @returns {number} Expected output amount of tokenB.
 */
function calculateSwapOutput(liquidity, fees, tokenA, tokenB, amountIn) {
  const reserveA = liquidity[tokenA];
  const reserveB = liquidity[tokenB];

  if (!reserveA || !reserveB) {
    throw new Error(`Liquidity data missing for ${tokenA} or ${tokenB}.`);
  }

  const feeRate = 1 - fees; // Apply fee deduction
  const amountInWithFee = amountIn * feeRate;

  // Constant product formula: x * y = k
  const amountOut =
    (amountInWithFee * reserveB) / (reserveA + amountInWithFee);

  return amountOut;
}
```
