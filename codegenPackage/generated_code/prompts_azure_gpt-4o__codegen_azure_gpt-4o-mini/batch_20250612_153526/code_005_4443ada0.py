"""
Generated Code Metadata:
========================
Original URL: https://dodgecoiin20.pages.dev
Prompt: Develop a returns calculator in JavaScript that takes the amount of DOGE20 purchased and the token price as inputs, and calculates the potential value of the tokens.
Generated: DETERMINISTIC_4443ada041c77217
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Returns Calculator for DOGE20 Tokens
 * This function calculates the potential value of DOGE20 tokens based on the amount purchased and the current token price.
 * 
 * @param {number} amountPurchased - The amount of DOGE20 tokens purchased.
 * @param {number} tokenPrice - The current price of a single DOGE20 token.
 * @returns {number} - The potential value of the tokens.
 * @throws {Error} - Throws an error if the inputs are not valid numbers or if they are negative.
 */
function calculatePotentialValue(amountPurchased, tokenPrice) {
    // Validate inputs
    if (typeof amountPurchased !== 'number' || typeof tokenPrice !== 'number') {
        throw new Error('Both amountPurchased and tokenPrice must be numbers.');
    }
    if (amountPurchased < 0 || tokenPrice < 0) {
        throw new Error('Both amountPurchased and tokenPrice must be non-negative.');
    }

    // Calculate potential value
    const potentialValue = amountPurchased * tokenPrice;

    return potentialValue;
}

// Example usage
try {
    const amountPurchased = 100; // Example amount of DOGE20 purchased
    const tokenPrice = 0.5; // Example current price of DOGE20 token

    const value = calculatePotentialValue(amountPurchased, tokenPrice);
    console.log(`The potential value of your DOGE20 tokens is: $${value.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
