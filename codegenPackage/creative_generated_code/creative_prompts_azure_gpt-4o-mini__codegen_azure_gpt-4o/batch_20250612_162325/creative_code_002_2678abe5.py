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
 * Calculates the total value of $MANIA tokens in USDT.
 * 
 * @param {number} maniaTokens - The number of $MANIA tokens owned.
 * @returns {number|string} The total value in USDT or an error message if input is invalid.
 */
function calculateManiaValue(maniaTokens) {
    // Constant rate: 1 $MANIA = 0.009003 USDT
    const MANIA_TO_USDT_RATE = 0.009003;

    try {
        // Validate input: maniaTokens should be a positive number
        if (typeof maniaTokens !== 'number' || maniaTokens < 0) {
            throw new Error('Invalid input: maniaTokens must be a positive number.');
        }

        // Calculate the total value
        const totalValue = maniaTokens * MANIA_TO_USDT_RATE;

        // Return the result rounded to 4 decimal places for precision
        return parseFloat(totalValue.toFixed(4));
    } catch (error) {
        // Return error message in case of invalid input or other issues
        return `Error: ${error.message}`;
    }
}

// Example usage
const maniaTokensOwned = 120; // Replace with actual value
const totalValueInUSDT = calculateManiaValue(maniaTokensOwned);
console.log(`Total value of $MANIA tokens: ${totalValueInUSDT} USDT`);
```
