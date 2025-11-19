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
 * Calculates token swap values with slippage adjustment.
 * 
 * @param {number} inputAmount - The amount of input token to swap.
 * @param {number} exchangeRate - The current exchange rate (output per input token).
 * @param {number} slippage - The slippage percentage (0-100).
 * @returns {Object} An object containing swap details.
 * @throws {Error} If input parameters are invalid.
 */
function calculateTokenSwap(inputAmount, exchangeRate, slippage) {
    // Validate input parameters
    if (typeof inputAmount !== 'number' || inputAmount <= 0) {
        throw new Error('Input amount must be a positive number');
    }
    if (typeof exchangeRate !== 'number' || exchangeRate <= 0) {
        throw new Error('Exchange rate must be a positive number');
    }
    if (typeof slippage !== 'number' || slippage < 0 || slippage > 100) {
        throw new Error('Slippage must be a number between 0 and 100');
    }

    // Calculate expected output without slippage
    const expectedOutput = inputAmount * exchangeRate;

    // Calculate minimum output after slippage
    const slippageFactor = 1 - (slippage / 100);
    const minOutput = expectedOutput * slippageFactor;

    return {
        inputAmount,
        exchangeRate,
        slippage,
        expectedOutput,
        minOutput,
        priceImpact: 0, // Placeholder for future implementation
        exchangeRateAfterSlippage: exchangeRate * slippageFactor
    };
}

/**
 * Formats and displays swap details in a user-friendly way.
 * 
 * @param {Object} swapDetails - The swap details object from calculateTokenSwap.
 * @returns {string} Formatted display string.
 */
function displaySwapDetails(swapDetails) {
    return `
    Swap Details:
    - Input Amount: ${swapDetails.inputAmount.toFixed(6)}
    - Exchange Rate: 1 = ${swapDetails.exchangeRate.toFixed(6)}
    - Slippage Tolerance: ${swapDetails.slippage}%
    - Expected Output: ${swapDetails.expectedOutput.toFixed(6)}
    - Minimum Received: ${swapDetails.minOutput.toFixed(6)}
    - Exchange Rate After Slippage: 1 = ${swapDetails.exchangeRateAfterSlippage.toFixed(6)}
    `;
}

// Example usage:
try {
    const swap = calculateTokenSwap(100, 0.5, 1); // 100 tokens at 0.5 rate with 1% slippage
    console.log(displaySwapDetails(swap));
} catch (error) {
    console.error('Error calculating swap:', error.message);
}
```
