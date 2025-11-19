"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Write a JavaScript function to calculate the total value of $MANIA tokens based on the current rate of 0.009003 USDT.
Generated: DETERMINISTIC_2678abe5b26b7715
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total value of $MANIA tokens in USDT.
 * 
 * @param {number} maniaTokens - The number of $MANIA tokens to convert.
 * @param {number} rate - The current rate of $MANIA tokens in USDT (default is 0.009003).
 * @returns {number} The total value of the $MANIA tokens in USDT.
 * @throws {Error} Throws an error if the input is not a valid number or is negative.
 */
function calculateManiaValue(maniaTokens, rate = 0.009003) {
    // Validate input
    if (typeof maniaTokens !== 'number' || isNaN(maniaTokens) || maniaTokens < 0) {
        throw new Error('Invalid input: maniaTokens must be a non-negative number.');
    }

    // Calculate total value
    const totalValue = maniaTokens * rate;

    return totalValue;
}

// Example usage:
try {
    const tokens = 1000; // Number of $MANIA tokens
    const totalValueInUSDT = calculateManiaValue(tokens);
    console.log(`Total value of $MANIA tokens: $${totalValueInUSDT.toFixed(6)} USDT`);
} catch (error) {
    console.error(error.message);
}
```
