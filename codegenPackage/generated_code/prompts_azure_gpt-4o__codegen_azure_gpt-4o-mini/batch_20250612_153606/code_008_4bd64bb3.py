"""
Generated Code Metadata:
========================
Original URL: https://swap-dev-git-feat-wagmi-8-cowswap.vercel.app
Prompt: Generate a JavaScript script to calculate transaction costs and slippage for trades executed via CoW Swap.
Generated: DETERMINISTIC_4bd64bb3d25e18cc
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CoW Swap Transaction Cost and Slippage Calculator
 * This script calculates the transaction costs and slippage for trades executed via CoW Swap.
 * 
 * @module CoWSwapCalculator
 */

/**
 * Calculates the transaction cost based on the input parameters.
 * 
 * @param {number} amount - The amount of tokens being traded.
 * @param {number} price - The price of the token in the market.
 * @param {number} feePercentage - The transaction fee percentage (e.g., 0.01 for 1%).
 * @returns {number} - The total transaction cost.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateTransactionCost(amount, price, feePercentage) {
    if (amount <= 0 || price <= 0 || feePercentage < 0) {
        throw new Error("Invalid input values. Amount and price must be greater than 0, and fee percentage cannot be negative.");
    }

    const totalCost = amount * price;
    const fee = totalCost * feePercentage;
    return totalCost + fee;
}

/**
 * Calculates the slippage for a trade.
 * 
 * @param {number} expectedPrice - The price expected before the trade.
 * @param {number} actualPrice - The price at which the trade is executed.
 * @returns {number} - The slippage percentage.
 * @throws {Error} - Throws an error if the expected price is zero.
 */
function calculateSlippage(expectedPrice, actualPrice) {
    if (expectedPrice === 0) {
        throw new Error("Expected price cannot be zero.");
    }

    const slippage = ((actualPrice - expectedPrice) / expectedPrice) * 100;
    return slippage;
}

// Example usage
try {
    const amount = 100; // Amount of tokens to trade
    const price = 50; // Market price of the token
    const feePercentage = 0.01; // 1% transaction fee

    const transactionCost = calculateTransactionCost(amount, price, feePercentage);
    console.log(`Transaction Cost: $${transactionCost.toFixed(2)}`);

    const expectedPrice = 50; // Expected price before trade
    const actualPrice = 52; // Actual price after trade

    const slippage = calculateSlippage(expectedPrice, actualPrice);
    console.log(`Slippage: ${slippage.toFixed(2)}%`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
