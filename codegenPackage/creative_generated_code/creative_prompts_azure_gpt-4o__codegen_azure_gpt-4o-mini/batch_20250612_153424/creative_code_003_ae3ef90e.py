"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-frax-finance.github.io
Prompt: Create a JavaScript function to calculate token prices in a Frax Finance liquidity pool using the AMM algorithm based on token ratios.
Generated: DETERMINISTIC_ae3ef90ec1d7837e
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the price of a token in a Frax Finance liquidity pool using the AMM algorithm.
 * 
 * @param {number} tokenAmountA - The amount of token A in the liquidity pool.
 * @param {number} tokenAmountB - The amount of token B in the liquidity pool.
 * @param {number} inputAmount - The amount of token A being swapped.
 * @returns {number} The price of token B in terms of token A.
 * @throws {Error} Will throw an error if any input is less than or equal to zero.
 */
function calculateTokenPrice(tokenAmountA, tokenAmountB, inputAmount) {
    // Input validation
    if (tokenAmountA <= 0 || tokenAmountB <= 0 || inputAmount <= 0) {
        throw new Error('All token amounts must be greater than zero.');
    }

    // Calculate the new amount of token A after the swap
    const newAmountA = tokenAmountA + inputAmount;

    // Calculate the new amount of token B using the AMM formula
    const newAmountB = (tokenAmountA * tokenAmountB) / newAmountA;

    // Calculate the price of token B in terms of token A
    const priceOfTokenB = (tokenAmountB - newAmountB) / inputAmount;

    // Return the calculated price
    return priceOfTokenB;
}

// Example usage
try {
    const tokenAmountA = 1000; // Example amount of token A
    const tokenAmountB = 2000; // Example amount of token B
    const inputAmount = 100;    // Amount of token A to swap

    const price = calculateTokenPrice(tokenAmountA, tokenAmountB, inputAmount);
    console.log(`The price of token B in terms of token A is: ${price}`);
} catch (error) {
    console.error(error.message);
}
```
