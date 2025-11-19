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
 * @param {number} amountIn - The input amount of tokens being swapped
 * @param {number} reserveIn - The current reserve of input tokens in the pool
 * @param {number} reserveOut - The current reserve of output tokens in the pool
 * @param {number} feePercentage - The swap fee percentage (e.g., 0.3 for 0.3%)
 * @returns {Object} An object containing price impact details
 * @throws {Error} If input parameters are invalid
 */
function calculatePriceImpact(amountIn, reserveIn, reserveOut, feePercentage) {
    // Validate input parameters
    if (typeof amountIn !== 'number' || typeof reserveIn !== 'number' || 
        typeof reserveOut !== 'number' || typeof feePercentage !== 'number') {
        throw new Error('All parameters must be numbers');
    }

    if (amountIn <= 0 || reserveIn <= 0 || reserveOut <= 0 || feePercentage < 0) {
        throw new Error('Parameters must be positive numbers');
    }

    if (feePercentage >= 100) {
        throw new Error('Fee percentage must be less than 100');
    }

    // Calculate the fee factor (1 - feePercentage/100)
    const feeFactor = 1 - (feePercentage / 100);

    // Calculate output amount using the constant product formula (x * y = k)
    const amountInAfterFee = amountIn * feeFactor;
    const newReserveIn = reserveIn + amountInAfterFee;
    const newReserveOut = (reserveIn * reserveOut) / newReserveIn;
    const amountOut = reserveOut - newReserveOut;

    // Calculate price before swap
    const priceBefore = reserveOut / reserveIn;

    // Calculate price after swap
    const priceAfter = newReserveOut / newReserveIn;

    // Calculate price impact percentage
    const priceImpact = ((priceBefore - priceAfter) / priceBefore) * 100;

    return {
        amountOut: amountOut,
        priceBefore: priceBefore,
        priceAfter: priceAfter,
        priceImpact: priceImpact,
        newReserveIn: newReserveIn,
        newReserveOut: newReserveOut
    };
}

module.exports = calculatePriceImpact;
```
