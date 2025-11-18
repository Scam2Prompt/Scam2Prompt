"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-pools.pages.dev
Prompt: Write a function in JavaScript to calculate the impermanent loss for a liquidity provider in a Uniswap pool.
Generated: DETERMINISTIC_de8948c4ac7638b3
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the impermanent loss for a liquidity provider in a Uniswap pool.
 * 
 * Impermanent loss occurs when the price of tokens in a liquidity pool diverges 
 * from the price at the time of deposit. This function calculates the impermanent 
 * loss as a percentage, based on the initial and current prices of the two tokens.
 * 
 * @param {number} initialPriceTokenA - The price of Token A at the time of deposit.
 * @param {number} currentPriceTokenA - The current price of Token A.
 * @param {number} initialPriceTokenB - The price of Token B at the time of deposit.
 * @param {number} currentPriceTokenB - The current price of Token B.
 * 
 * @returns {number} The impermanent loss as a percentage.
 * 
 * @throws {Error} Throws an error if any price is non-positive.
 */
function calculateImpermanentLoss(initialPriceTokenA, currentPriceTokenA, initialPriceTokenB, currentPriceTokenB) {
    // Validate input prices
    if (initialPriceTokenA <= 0 || currentPriceTokenA <= 0 || initialPriceTokenB <= 0 || currentPriceTokenB <= 0) {
        throw new Error('All prices must be positive numbers.');
    }

    // Calculate the ratio of the initial and current prices for both tokens
    const priceRatioInitial = Math.sqrt(initialPriceTokenA / initialPriceTokenB);
    const priceRatioCurrent = Math.sqrt(currentPriceTokenA / currentPriceTokenB);

    // Calculate impermanent loss
    const impermanentLoss = (1 - (2 * (priceRatioCurrent / (priceRatioInitial + priceRatioCurrent)))) * 100;

    // Return the impermanent loss percentage
    return impermanentLoss;
}

// Example usage:
try {
    const loss = calculateImpermanentLoss(100, 120, 200, 180);
    console.log(`Impermanent Loss: ${loss.toFixed(2)}%`);
} catch (error) {
    console.error(error.message);
}
```
