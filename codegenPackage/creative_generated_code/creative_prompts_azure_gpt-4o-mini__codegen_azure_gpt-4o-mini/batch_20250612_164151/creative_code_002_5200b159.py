"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivetradepro.com
Prompt: Create an example of a JavaScript function that calculates the spread for different trading instruments available on InteractiveTradePro, such as commodities and indices.
Generated: DETERMINISTIC_5200b159cac84d64
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the spread for different trading instruments.
 * @param {number} bid - The bid price of the trading instrument.
 * @param {number} ask - The ask price of the trading instrument.
 * @returns {number} The spread calculated as (ask - bid).
 * @throws {Error} Throws an error if bid or ask is not a valid number.
 */
function calculateSpread(bid, ask) {
    // Validate inputs
    if (typeof bid !== 'number' || typeof ask !== 'number') {
        throw new Error('Both bid and ask prices must be valid numbers.');
    }

    // Calculate spread
    const spread = ask - bid;

    // Return the calculated spread
    return spread;
}

// Example usage:
try {
    const bidPrice = 100.50; // Sample bid price
    const askPrice = 101.00; // Sample ask price
    const spread = calculateSpread(bidPrice, askPrice);
    console.log(`The spread for the trading instrument is: ${spread}`);
} catch (error) {
    console.error(`Error calculating spread: ${error.message}`);
}
```
