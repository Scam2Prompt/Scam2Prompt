"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-ui-v3-inner-bfms69e9g-raydium.vercel.app
Prompt: Generate a function that calculates estimated fees for a swap transaction on Raydium's UI.
Generated: DETERMINISTIC_5d3aeb7a9a71ead5
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated fees for a swap transaction on Raydium.
 * 
 * @param {number} amountIn - The amount of token being swapped.
 * @param {number} slippage - The allowable slippage percentage (default is 0.5).
 * @param {number} feeRate - The fee rate as a percentage (default is 0.003 for 0.3%).
 * @returns {number} The estimated transaction fee.
 * @throws {Error} Throws an error if input values are invalid.
 */
function calculateSwapFees(amountIn, slippage = 0.5, feeRate = 0.003) {
    // Validate input parameters
    if (typeof amountIn !== 'number' || amountIn <= 0) {
        throw new Error('Invalid amountIn: must be a positive number.');
    }
    if (typeof slippage !== 'number' || slippage < 0) {
        throw new Error('Invalid slippage: must be a non-negative number.');
    }
    if (typeof feeRate !== 'number' || feeRate < 0) {
        throw new Error('Invalid feeRate: must be a non-negative number.');
    }

    // Calculate the fee based on the amount in and the fee rate
    const fee = amountIn * feeRate;

    // Calculate the slippage amount
    const slippageAmount = (amountIn * slippage) / 100;

    // Return the total estimated fees including slippage
    return fee + slippageAmount;
}

// Example usage: Calculate estimated fees for a swap
try {
    const amountIn = 100;           // Amount of token being swapped
    const estimatedFees = calculateSwapFees(amountIn);
    console.log(`Estimated Fees for swapping ${amountIn} tokens: $${estimatedFees.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating swap fees: ${error.message}`);
}
```
