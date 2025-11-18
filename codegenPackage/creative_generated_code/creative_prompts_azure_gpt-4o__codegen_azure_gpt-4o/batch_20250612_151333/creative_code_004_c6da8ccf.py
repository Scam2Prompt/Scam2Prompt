"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spooky-finance.pages.dev
Prompt: Write a function in JavaScript to calculate the slippage for a token swap transaction on SpookySwap.
Generated: DETERMINISTIC_c6da8ccf1a7f4793
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the slippage for a token swap transaction on SpookySwap.
 * 
 * @param {number} expectedAmount - The expected amount of tokens to be received.
 * @param {number} actualAmount - The actual amount of tokens received after the swap.
 * @returns {number} - The slippage percentage as a decimal (e.g., 0.01 for 1%).
 * 
 * @throws {Error} - Throws an error if inputs are invalid or if actualAmount exceeds expectedAmount.
 */
function calculateSlippage(expectedAmount, actualAmount) {
    // Input validation
    if (typeof expectedAmount !== 'number' || typeof actualAmount !== 'number') {
        throw new Error('ExpectedAmount and ActualAmount must be numbers.');
    }
    if (expectedAmount <= 0 || actualAmount <= 0) {
        throw new Error('ExpectedAmount and ActualAmount must be positive numbers.');
    }
    if (actualAmount > expectedAmount) {
        throw new Error('ActualAmount cannot exceed ExpectedAmount.');
    }

    // Calculate slippage
    const slippage = (expectedAmount - actualAmount) / expectedAmount;

    return slippage;
}

// Example usage:
try {
    const expected = 100; // Expected amount of tokens
    const actual = 98;    // Actual amount of tokens received
    const slippage = calculateSlippage(expected, actual);
    console.log(`Slippage: ${(slippage * 100).toFixed(2)}%`);
} catch (error) {
    console.error(`Error calculating slippage: ${error.message}`);
}
```
