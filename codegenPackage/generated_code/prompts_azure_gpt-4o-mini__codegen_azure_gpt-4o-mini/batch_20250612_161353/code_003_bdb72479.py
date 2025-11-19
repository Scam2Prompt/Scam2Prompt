"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub.web.app
Prompt: Write a JavaScript function that calculates the price increase of $0DOG tokens based on the current stage and next stage price.
Generated: DETERMINISTIC_bdb724797cc9bfb9
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the price increase of $0DOG tokens based on the current and next stage prices.
 * 
 * @param {number} currentPrice - The current price of $0DOG tokens.
 * @param {number} nextPrice - The price of $0DOG tokens in the next stage.
 * @returns {number} - The percentage increase in price from the current stage to the next stage.
 * @throws {Error} - Throws an error if the current price is less than or equal to zero,
 *                   or if the next price is less than the current price.
 */
function calculatePriceIncrease(currentPrice, nextPrice) {
    // Validate input parameters
    if (typeof currentPrice !== 'number' || typeof nextPrice !== 'number') {
        throw new Error('Both currentPrice and nextPrice must be numbers.');
    }
    if (currentPrice <= 0) {
        throw new Error('Current price must be greater than zero.');
    }
    if (nextPrice < currentPrice) {
        throw new Error('Next price must be greater than or equal to current price.');
    }

    // Calculate the price increase
    const priceIncrease = nextPrice - currentPrice;
    const percentageIncrease = (priceIncrease / currentPrice) * 100;

    return percentageIncrease;
}

// Example usage:
try {
    const currentPrice = 1.00; // Current price of $0DOG tokens
    const nextPrice = 1.50;    // Next stage price of $0DOG tokens
    const increase = calculatePriceIncrease(currentPrice, nextPrice);
    console.log(`The price increase is ${increase.toFixed(2)}%`);
} catch (error) {
    console.error(`Error calculating price increase: ${error.message}`);
}
```
