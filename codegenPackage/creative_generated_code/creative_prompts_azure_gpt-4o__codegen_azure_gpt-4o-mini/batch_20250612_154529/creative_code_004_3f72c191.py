"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.trade
Prompt: Create a function in JavaScript to calculate slippage for a token swap using the Uniswap Interface.
Generated: DETERMINISTIC_3f72c191a8ff87a1
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates slippage for a token swap using the Uniswap Interface.
 * 
 * @param {number} amountIn - The amount of input tokens being swapped.
 * @param {number} amountOut - The expected amount of output tokens.
 * @param {number} amountOutMin - The minimum amount of output tokens expected to receive.
 * @returns {number} - The slippage percentage.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateSlippage(amountIn, amountOut, amountOutMin) {
    // Validate inputs
    if (amountIn <= 0 || amountOut <= 0 || amountOutMin < 0) {
        throw new Error("Invalid input values. All amounts must be greater than or equal to zero.");
    }

    // Calculate slippage
    const slippageAmount = amountOut - amountOutMin;

    // Calculate slippage percentage
    const slippagePercentage = (slippageAmount / amountOut) * 100;

    // Return the calculated slippage percentage
    return slippagePercentage;
}

// Example usage:
try {
    const amountIn = 1000; // Amount of input tokens
    const amountOut = 950; // Expected amount of output tokens
    const amountOutMin = 900; // Minimum amount of output tokens expected

    const slippage = calculateSlippage(amountIn, amountOut, amountOutMin);
    console.log(`Slippage: ${slippage.toFixed(2)}%`);
} catch (error) {
    console.error(`Error calculating slippage: ${error.message}`);
}
```
