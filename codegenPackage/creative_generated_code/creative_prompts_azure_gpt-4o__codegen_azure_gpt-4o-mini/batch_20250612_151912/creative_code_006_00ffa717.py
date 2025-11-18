"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enigmatoken.com
Prompt: Write a JavaScript function to calculate the total cost of purchasing ENIGMA tokens during a presale, given a specific token price and quantity.
Generated: DETERMINISTIC_00ffa7174378062a
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of purchasing ENIGMA tokens during a presale.
 * 
 * @param {number} tokenPrice - The price of a single ENIGMA token in the selected currency.
 * @param {number} quantity - The number of ENIGMA tokens to purchase.
 * @returns {number} - The total cost of purchasing the specified quantity of tokens.
 * @throws {Error} - Throws an error if tokenPrice or quantity is not a positive number.
 */
function calculateTotalCost(tokenPrice, quantity) {
    // Validate inputs
    if (typeof tokenPrice !== 'number' || tokenPrice <= 0) {
        throw new Error('Invalid token price. It must be a positive number.');
    }
    if (typeof quantity !== 'number' || quantity <= 0) {
        throw new Error('Invalid quantity. It must be a positive number.');
    }

    // Calculate total cost
    const totalCost = tokenPrice * quantity;

    // Return the total cost
    return totalCost;
}

// Example usage:
try {
    const pricePerToken = 10; // Price in the selected currency
    const numberOfTokens = 5; // Number of tokens to purchase
    const total = calculateTotalCost(pricePerToken, numberOfTokens);
    console.log(`Total cost for purchasing ${numberOfTokens} ENIGMA tokens: ${total}`);
} catch (error) {
    console.error(error.message);
}
```
