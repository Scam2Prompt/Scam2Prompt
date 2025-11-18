"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapsaver.net
Prompt: Create a JavaScript function that calculates the estimated slippage for a token swap on SunSwap using TRON blockchain data.
Generated: DETERMINISTIC_6d21eca4121b6029
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate estimated slippage for a token swap on SunSwap using TRON blockchain data.
 * 
 * Slippage occurs when the price changes between the time a trade is initiated and executed.
 * This function estimates the slippage percentage based on the liquidity pool data.
 * 
 * @param {number} amountIn - The amount of tokens being swapped (input).
 * @param {number} reserveIn - The reserve of input tokens in the liquidity pool.
 * @param {number} reserveOut - The reserve of output tokens in the liquidity pool.
 * @returns {number} Estimated slippage percentage.
 * @throws {Error} If input values are invalid.
 */
function calculateSlippage(amountIn, reserveIn, reserveOut) {
    try {
        // Validate input parameters
        if (amountIn <= 0 || reserveIn <= 0 || reserveOut <= 0) {
            throw new Error("Input values must be positive numbers.");
        }

        // Constants for SunSwap calculations
        const FEE_NUMERATOR = 997; // SunSwap charges a 0.3% fee (1000 - 997)
        const FEE_DENOMINATOR = 1000;

        // Calculate amountOut using the constant product formula: (reserveIn * reserveOut = k)
        const amountInWithFee = amountIn * FEE_NUMERATOR;
        const numerator = amountInWithFee * reserveOut;
        const denominator = reserveIn * FEE_DENOMINATOR + amountInWithFee;
        const amountOut = numerator / denominator;

        // Calculate price impact (slippage)
        const idealAmountOut = (reserveOut / reserveIn) * amountIn; // Ideal without slippage
        const slippage = ((idealAmountOut - amountOut) / idealAmountOut) * 100;

        return slippage; // Return slippage percentage
    } catch (error) {
        console.error("Error calculating slippage:", error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Example usage
try {
    const amountIn = 1000; // Example input tokens
    const reserveIn = 50000; // Example liquidity pool reserve for input tokens
    const reserveOut = 25000; // Example liquidity pool reserve for output tokens

    const slippage = calculateSlippage(amountIn, reserveIn, reserveOut);
    console.log(`Estimated slippage: ${slippage.toFixed(2)}%`);
} catch (error) {
    console.error("Failed to calculate slippage:", error.message);
}
```
