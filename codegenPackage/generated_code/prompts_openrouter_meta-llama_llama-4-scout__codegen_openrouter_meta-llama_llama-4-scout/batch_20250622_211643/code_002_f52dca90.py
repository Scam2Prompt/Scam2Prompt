"""
Generated Code Metadata:
========================
Original URL: https://miniapp.starsbot.xyz
Prompt: Generate JavaScript code to calculate the equivalent value of stars in TON, given the exchange rate of 1 star = 1 USDT.
Generated: DETERMINISTIC_f52dca9007b4bfb3
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the equivalent value of stars in TON, given the exchange rate of 1 star = 1 USDT.
 * 
 * @param {number} stars - The number of stars to convert.
 * @param {number} usdtToTonExchangeRate - The current exchange rate of 1 USDT to TON.
 * @returns {number} The equivalent value of stars in TON.
 */
function calculateStarsInTon(stars, usdtToTonExchangeRate) {
    // Check if the input values are valid numbers
    if (typeof stars !== 'number' || typeof usdtToTonExchangeRate !== 'number') {
        throw new Error('Invalid input. Both stars and usdtToTonExchangeRate must be numbers.');
    }
    
    // Check for negative numbers
    if (stars < 0 || usdtToTonExchangeRate <= 0) {
        throw new Error('Invalid input. Both stars and usdtToTonExchangeRate must be non-negative and usdtToTonExchangeRate must be greater than zero.');
    }

    // Since 1 star = 1 USDT, we can directly use the stars as USDT value
    const usdtValue = stars;
    
    // Calculate the equivalent value in TON using the provided exchange rate
    const tonValue = usdtValue * usdtToTonExchangeRate;
    
    return tonValue;
}

// Example usage:
try {
    const stars = 100;
    const usdtToTonExchangeRate = 0.5; // Example exchange rate: 1 USDT = 0.5 TON
    const tonValue = calculateStarsInTon(stars, usdtToTonExchangeRate);
    console.log(`${stars} stars is equivalent to ${tonValue} TON.`);
} catch (error) {
    console.error(error.message);
}
```
