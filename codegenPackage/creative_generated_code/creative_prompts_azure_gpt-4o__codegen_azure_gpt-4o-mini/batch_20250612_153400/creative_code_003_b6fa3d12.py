"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: Create a JavaScript function to calculate the value of DOGE20 tokens using the returns calculator formula provided on the website. Include input parameters for token price and purchase amount.
Generated: DETERMINISTIC_b6fa3d12e47b5c98
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the value of DOGE20 tokens using the given price and purchase amount.
 * 
 * @param {number} tokenPrice - The current price of a DOGE20 token.
 * @param {number} purchaseAmount - The amount of DOGE20 tokens purchased.
 * @returns {number} The total value of the DOGE20 tokens purchased.
 * @throws {Error} Throws an error if tokenPrice or purchaseAmount is not a positive number.
 */
function calculateDoge20Value(tokenPrice, purchaseAmount) {
    // Validate input parameters
    if (typeof tokenPrice !== 'number' || tokenPrice <= 0) {
        throw new Error('Invalid tokenPrice: must be a positive number.');
    }
    if (typeof purchaseAmount !== 'number' || purchaseAmount <= 0) {
        throw new Error('Invalid purchaseAmount: must be a positive number.');
    }

    // Calculate the total value of DOGE20 tokens
    const totalValue = tokenPrice * purchaseAmount;

    // Return the total value
    return totalValue;
}

// Example usage:
// try {
//     const price = 0.5; // Example token price
//     const amount = 100; // Example purchase amount
//     const value = calculateDoge20Value(price, amount);
//     console.log(`Total value of DOGE20 tokens: $${value.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
