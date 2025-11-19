"""
Generated Code Metadata:
========================
Original URL: https://enosysglobal.net
Prompt: "Write a function in Node.js to calculate the price impact of a large swap on Ēnosys DEX, considering the current liquidity and swap fees."
Generated: DETERMINISTIC_a6823349e100d0aa
Batch ID: 20250622_205154
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the price impact of a large swap on Ēnosys DEX.
 * 
 * @param {number} inputAmount - The amount of tokens being swapped.
 * @param {number} reserveIn - The current reserve of the input token in the liquidity pool.
 * @param {number} reserveOut - The current reserve of the output token in the liquidity pool.
 * @param {number} swapFee - The swap fee percentage (e.g., 0.003 for 0.3%).
 * @returns {number} - The price impact as a percentage.
 * 
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculatePriceImpact(inputAmount, reserveIn, reserveOut, swapFee) {
    // Validate input parameters
    if (inputAmount <= 0 || reserveIn <= 0 || reserveOut <= 0 || swapFee < 0 || swapFee >= 1) {
        throw new Error('Invalid input parameters. Ensure all values are positive and swapFee is between 0 and 1.');
    }

    // Calculate the effective input amount after swap fee deduction
    const effectiveInputAmount = inputAmount * (1 - swapFee);

    // Calculate the new reserves after the swap
    const newReserveIn = reserveIn + effectiveInputAmount;
    const newReserveOut = reserveOut - (reserveOut * effectiveInputAmount) / (reserveIn + effectiveInputAmount);

    // Calculate the price before and after the swap
    const priceBeforeSwap = reserveOut / reserveIn;
    const priceAfterSwap = newReserveOut / newReserveIn;

    // Calculate the price impact as a percentage
    const priceImpact = ((priceBeforeSwap - priceAfterSwap) / priceBeforeSwap) * 100;

    return priceImpact;
}

// Example usage:
try {
    const inputAmount = 1000; // Amount of tokens being swapped
    const reserveIn = 50000; // Current reserve of input token
    const reserveOut = 100000; // Current reserve of output token
    const swapFee = 0.003; // Swap fee (0.3%)

    const priceImpact = calculatePriceImpact(inputAmount, reserveIn, reserveOut, swapFee);
    console.log(`Price Impact: ${priceImpact.toFixed(2)}%`);
} catch (error) {
    console.error(`Error calculating price impact: ${error.message}`);
}
```
