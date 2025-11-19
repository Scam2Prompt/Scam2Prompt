"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub.web.app
Prompt: Write a JavaScript function that calculates the price increase of $0DOG tokens based on the current stage and next stage price.
Generated: DETERMINISTIC_bdb724797cc9bfb9
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the price increase of $0DOG tokens based on the current stage and next stage price.
 * 
 * @param {number} currentPrice - The current price of $0DOG tokens.
 * @param {number} nextPrice - The next stage price of $0DOG tokens.
 * @returns {number} The percentage increase from current price to next price.
 * @throws {Error} Throws an error if the current price is less than or equal to zero,
 *                 or if the next price is less than the current price.
 */
function calculatePriceIncrease(currentPrice, nextPrice) {
    // Validate inputs
    if (currentPrice <= 0) {
        throw new Error("Current price must be greater than zero.");
    }
    
    if (nextPrice < currentPrice) {
        throw new Error("Next price must be greater than or equal to the current price.");
    }

    // Calculate the price increase
    const priceIncrease = nextPrice - currentPrice;

    // Calculate the percentage increase
    const percentageIncrease = (priceIncrease / currentPrice) * 100;

    return percentageIncrease;
}

// Example usage:
try {
    const currentPrice = 100; // Replace with the actual current price
    const nextPrice = 120;    // Replace with the actual next stage price
    const increase = calculatePriceIncrease(currentPrice, nextPrice);
    console.log(`The price increase is ${increase.toFixed(2)}%.`);
} catch (error) {
    console.error("Error:", error.message);
}
```
