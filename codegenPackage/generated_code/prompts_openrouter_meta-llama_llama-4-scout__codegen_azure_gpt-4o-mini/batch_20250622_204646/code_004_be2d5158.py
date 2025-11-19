"""
Generated Code Metadata:
========================
Original URL: https://bnbfour-meme.pages.dev
Prompt: Create a JavaScript function to calculate the buy/sell tax for a token, given that the tax rate is 0% as mentioned for $FOUR.
Generated: DETERMINISTIC_be2d5158757ca0fe
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the buy/sell tax for a given token.
 * 
 * @param {number} amount - The amount of tokens being bought or sold.
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.0 for 0%).
 * @returns {number} - The calculated tax amount.
 * @throws {Error} - Throws an error if the amount is negative or if the tax rate is not between 0 and 1.
 */
function calculateTax(amount, taxRate) {
    // Validate input parameters
    if (amount < 0) {
        throw new Error("Amount must be a non-negative number.");
    }
    if (taxRate < 0 || taxRate > 1) {
        throw new Error("Tax rate must be between 0 and 1.");
    }

    // Calculate the tax amount
    const taxAmount = amount * taxRate;

    // Return the calculated tax amount
    return taxAmount;
}

// Example usage
try {
    const amount = 1000; // Amount of tokens
    const taxRate = 0.0; // Tax rate for $FOUR
    const tax = calculateTax(amount, taxRate);
    console.log(`The tax for ${amount} tokens at a rate of ${taxRate * 100}% is: $${tax}`);
} catch (error) {
    console.error(`Error calculating tax: ${error.message}`);
}
```
