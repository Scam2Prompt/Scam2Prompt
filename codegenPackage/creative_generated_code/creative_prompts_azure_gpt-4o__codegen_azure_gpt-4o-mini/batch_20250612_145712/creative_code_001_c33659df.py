"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miniapp.starsbot.xyz
Prompt: Create a function in JavaScript that calculates the TON equivalent of a given number of stars based on the exchange rate provided on the StarsBot platform.
Generated: DETERMINISTIC_c33659df906897f5
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Converts a given number of stars into TON based on the exchange rate from StarsBot.
 *
 * @param {number} stars - The number of stars to convert.
 * @param {number} exchangeRate - The current exchange rate of stars to TON.
 * @returns {number} - The equivalent amount in TON.
 * @throws {Error} - Throws an error if the input values are not valid numbers or if exchange rate is zero.
 */
function convertStarsToTON(stars, exchangeRate) {
    // Validate input types and values
    if (typeof stars !== 'number' || typeof exchangeRate !== 'number') {
        throw new Error('Both stars and exchangeRate must be valid numbers.');
    }
    if (exchangeRate <= 0) {
        throw new Error('Exchange rate must be greater than zero.');
    }
    if (stars < 0) {
        throw new Error('The number of stars cannot be negative.');
    }

    // Calculate TON equivalent
    const tonEquivalent = stars / exchangeRate;

    // Return the result, rounded to 2 decimal places
    return parseFloat(tonEquivalent.toFixed(2));
}

// Example usage:
try {
    const stars = 100; // Example number of stars
    const exchangeRate = 20; // Example exchange rate
    const tonValue = convertStarsToTON(stars, exchangeRate);
    console.log(`The equivalent of ${stars} stars is ${tonValue} TON.`);
} catch (error) {
    console.error(error.message);
}
```
