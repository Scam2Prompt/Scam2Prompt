"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landx.pages.dev
Prompt: Write a JavaScript function that calculates the conversion of cTokens to USDC based on the current market price as described on LandX.
Generated: DETERMINISTIC_09310e8b30d6f663
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the conversion of cTokens to USDC based on the current market price.
 * 
 * @param {number} cTokenAmount - The amount of cTokens to convert.
 * @param {number} exchangeRate - The current exchange rate for cTokens to the underlying asset (scaled by 1e18).
 * @param {number} usdcDecimals - The USDC decimal places (typically 6).
 * @returns {number} - The equivalent amount in USDC.
 * @throws Will throw an error if the inputs are invalid.
 */
function convertCTokensToUSDC(cTokenAmount, exchangeRate, usdcDecimals = 6) {
    try {
        // Validate inputs
        if (typeof cTokenAmount !== 'number' || cTokenAmount <= 0) {
            throw new Error('Invalid cToken amount. Must be a positive number.');
        }

        if (typeof exchangeRate !== 'number' || exchangeRate <= 0) {
            throw new Error('Invalid exchange rate. Must be a positive number.');
        }

        if (typeof usdcDecimals !== 'number' || usdcDecimals <= 0 || !Number.isInteger(usdcDecimals)) {
            throw new Error('Invalid USDC decimals. Must be a positive integer.');
        }

        // Calculate the conversion (cTokens * exchangeRate / scaling factor, adjusted for USDC decimals)
        const scalingFactor = Math.pow(10, 18); // Exchange rate scaling factor (1e18)
        const rawUSDCValue = (cTokenAmount * exchangeRate) / scalingFactor;

        // Adjust for USDC decimal places
        const usdcValue = parseFloat(rawUSDCValue.toFixed(usdcDecimals));

        return usdcValue;
    } catch (error) {
        console.error('Error in conversion:', error.message);
        throw error; // Re-throw error to be handled by the caller
    }
}

// Example usage:
try {
    const cTokenAmount = 100; // Amount of cTokens
    const exchangeRate = 200000000000000000; // Example exchange rate (scaled by 1e18)
    const usdcValue = convertCTokensToUSDC(cTokenAmount, exchangeRate);
    console.log(`USDC Value: ${usdcValue}`);
} catch (error) {
    console.error('Failed to calculate USDC value:', error.message);
}
```
