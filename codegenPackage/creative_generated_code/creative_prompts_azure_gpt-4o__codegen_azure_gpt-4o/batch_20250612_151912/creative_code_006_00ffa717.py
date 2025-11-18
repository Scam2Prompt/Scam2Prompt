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
 * Function to calculate the total cost of purchasing ENIGMA tokens during a presale.
 * 
 * @param {number} tokenPrice - The price of a single ENIGMA token (in USD or other currency).
 * @param {number} tokenQuantity - The quantity of tokens the user wants to purchase.
 * @returns {number} - The total cost of purchasing the tokens.
 * 
 * @throws {Error} - Throws an error if the input parameters are invalid (e.g., negative numbers, non-numeric values).
 */
function calculateTotalCost(tokenPrice, tokenQuantity) {
    // Validate inputs
    if (typeof tokenPrice !== 'number' || typeof tokenQuantity !== 'number') {
        throw new Error("Both tokenPrice and tokenQuantity must be numbers.");
    }

    if (tokenPrice <= 0) {
        throw new Error("Token price must be greater than zero.");
    }

    if (tokenQuantity <= 0) {
        throw new Error("Token quantity must be greater than zero.");
    }

    // Calculate total cost
    const totalCost = tokenPrice * tokenQuantity;

    // Ensure the calculation did not produce an invalid result (e.g., Infinity, NaN)
    if (!isFinite(totalCost)) {
        throw new Error("Total cost calculation resulted in an invalid number.");
    }

    return totalCost;
}

// Example usage:
try {
    const tokenPrice = 2.5; // Price per token
    const tokenQuantity = 100; // Number of tokens to purchase
    const totalCost = calculateTotalCost(tokenPrice, tokenQuantity);
    console.log(`Total cost for purchasing ${tokenQuantity} ENIGMA tokens: $${totalCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
