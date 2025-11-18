"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wagmidefi.pages.dev
Prompt: Write a function in JavaScript to calculate liquidity for the KAVA/WAGMI trading pair and display the percentage change in price on a DeFi platform.
Generated: DETERMINISTIC_d46b9577e2601753
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateLiquidityAndPriceChange
 * @description Calculates liquidity and percentage change in price for the KAVA/WAGMI trading pair.
 * @param {number} kavaReserve - Current reserve of KAVA tokens in the pool.
 * @param {number} wagmiReserve - Current reserve of WAGMI tokens in the pool.
 * @param {number} previousPrice - Price of KAVA/WAGMI from the previous check.
 * @returns {Object} Liquidity and percentage change in price.
 * @throws Will throw an error if invalid input is provided.
 */
function calculateLiquidityAndPriceChange(kavaReserve, wagmiReserve, previousPrice) {
    // Input validation
    if (
        typeof kavaReserve !== 'number' ||
        typeof wagmiReserve !== 'number' ||
        typeof previousPrice !== 'number' ||
        kavaReserve <= 0 ||
        wagmiReserve <= 0 ||
        previousPrice <= 0
    ) {
        throw new Error('Invalid input. All inputs must be positive numbers.');
    }

    // Calculate liquidity (product of reserves)
    const liquidity = kavaReserve * wagmiReserve;

    // Calculate current price (WAGMI per KAVA)
    const currentPrice = wagmiReserve / kavaReserve;

    // Calculate percentage change in price
    const priceChangePercentage = ((currentPrice - previousPrice) / previousPrice) * 100;

    // Return both liquidity and price change
    return {
        liquidity,
        priceChangePercentage: parseFloat(priceChangePercentage.toFixed(2)), // Round to 2 decimal places
    };
}

// Example usage
try {
    const kavaReserve = 1000; // Replace with actual reserve data
    const wagmiReserve = 5000; // Replace with actual reserve data
    const previousPrice = 5; // Replace with previous price data

    const result = calculateLiquidityAndPriceChange(kavaReserve, wagmiReserve, previousPrice);

    console.log(`Liquidity: ${result.liquidity}`);
    console.log(`Price Change Percentage: ${result.priceChangePercentage}%`);
} catch (error) {
    console.error('Error:', error.message);
}
```
