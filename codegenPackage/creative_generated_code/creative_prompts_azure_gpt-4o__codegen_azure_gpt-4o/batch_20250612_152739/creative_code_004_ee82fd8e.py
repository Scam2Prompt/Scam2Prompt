"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saita.pages.dev
Prompt: Create a JavaScript function to calculate and display token swap values, including slippage percentage adjustments, as described in the SaitaSwap interface.
Generated: DETERMINISTIC_ee82fd8eb2e3ae11
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates and displays token swap values including slippage percentage adjustments.
 * 
 * @param {number} inputAmount - The amount of tokens being swapped.
 * @param {number} exchangeRate - The rate at which tokens are exchanged (e.g., 1 TokenA = X TokenB).
 * @param {number} slippagePercentage - The slippage percentage tolerance (e.g., 2 for 2%).
 * 
 * @returns {object} - An object containing the calculated `minReceived` and `maxReceived` token values.
 */
function calculateTokenSwap(inputAmount, exchangeRate, slippagePercentage) {
  try {
    // Input validation
    if (isNaN(inputAmount) || inputAmount <= 0) {
      throw new Error("Invalid input amount. Must be a positive number.");
    }
    if (isNaN(exchangeRate) || exchangeRate <= 0) {
      throw new Error("Invalid exchange rate. Must be a positive number.");
    }
    if (isNaN(slippagePercentage) || slippagePercentage < 0) {
      throw new Error("Invalid slippage percentage. Must be a non-negative number.");
    }

    // Calculate the raw swap value (without slippage)
    const rawSwapValue = inputAmount * exchangeRate;

    // Calculate slippage adjustments
    const slippageAdjustment = (slippagePercentage / 100) * rawSwapValue;
    const minReceived = rawSwapValue - slippageAdjustment; // Minimum tokens received after slippage
    const maxReceived = rawSwapValue + slippageAdjustment; // Maximum tokens received after slippage

    // Return the results
    return {
      minReceived: parseFloat(minReceived.toFixed(6)),  // Rounded to 6 decimal places for precision
      maxReceived: parseFloat(maxReceived.toFixed(6)),  // Rounded to 6 decimal places for precision
    };
  } catch (error) {
    // Error handling
    console.error("Error calculating token swap values:", error.message);
    return null;
  }
}

// Example usage
const inputAmount = 100; // Input token amount
const exchangeRate = 1.5; // Exchange rate (e.g., 1 TokenA = 1.5 TokenB)
const slippagePercentage = 2; // Slippage tolerance (e.g., 2%)

const result = calculateTokenSwap(inputAmount, exchangeRate, slippagePercentage);
if (result) {
  console.log("Minimum tokens received:", result.minReceived);
  console.log("Maximum tokens received:", result.maxReceived);
}
```
