"""
Generated Code Metadata:
========================
Original URL: https://saita.pages.dev
Prompt: Create a JavaScript function to calculate and display token swap values, including slippage percentage adjustments, as described in the SaitaSwap interface.
Generated: DETERMINISTIC_ee82fd8eb2e3ae11
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the token swap values including slippage adjustments.
 * 
 * @param {number} amountIn - The amount of input tokens to swap.
 * @param {number} priceIn - The price of the input token.
 * @param {number} priceOut - The price of the output token.
 * @param {number} slippage - The slippage percentage (0-100).
 * @returns {Object} - An object containing the output amount and adjusted output amount.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateTokenSwap(amountIn, priceIn, priceOut, slippage) {
    // Validate inputs
    if (typeof amountIn !== 'number' || amountIn <= 0) {
        throw new Error('Invalid amountIn: must be a positive number.');
    }
    if (typeof priceIn !== 'number' || priceIn <= 0) {
        throw new Error('Invalid priceIn: must be a positive number.');
    }
    if (typeof priceOut !== 'number' || priceOut <= 0) {
        throw new Error('Invalid priceOut: must be a positive number.');
    }
    if (typeof slippage !== 'number' || slippage < 0 || slippage > 100) {
        throw new Error('Invalid slippage: must be a number between 0 and 100.');
    }

    // Calculate the output amount before slippage
    const outputAmount = (amountIn * priceIn) / priceOut;

    // Calculate slippage adjustment
    const slippageAmount = (outputAmount * slippage) / 100;
    const adjustedOutputAmount = outputAmount - slippageAmount;

    // Return the results
    return {
        outputAmount: parseFloat(outputAmount.toFixed(6)), // Format to 6 decimal places
        adjustedOutputAmount: parseFloat(adjustedOutputAmount.toFixed(6)) // Format to 6 decimal places
    };
}

// Example usage
try {
    const result = calculateTokenSwap(100, 1.5, 2.0, 1);
    console.log(`Output Amount: ${result.outputAmount}`);
    console.log(`Adjusted Output Amount (with slippage): ${result.adjustedOutputAmount}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
