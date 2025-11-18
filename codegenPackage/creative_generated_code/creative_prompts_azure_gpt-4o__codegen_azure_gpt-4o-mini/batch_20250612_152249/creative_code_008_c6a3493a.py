"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getretik.pages.dev
Prompt: Write a JavaScript function to pre-order Retik DeFi debit cards based on user-selected tiers (Silver, Gold, Diamond) and calculate the associated costs.
Generated: DETERMINISTIC_c6a3493ad0d0a8a0
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Pre-orders Retik DeFi debit cards based on user-selected tiers and calculates the associated costs.
 * 
 * @param {string} tier - The selected tier for the debit card. Should be one of 'Silver', 'Gold', or 'Diamond'.
 * @param {number} quantity - The number of debit cards to be pre-ordered.
 * @returns {object} - An object containing the tier, quantity, total cost, and a success message.
 * @throws {Error} - Throws an error if the tier is invalid or quantity is not a positive integer.
 */
function preOrderRetikCard(tier, quantity) {
    // Define card tier prices
    const tierPrices = {
        Silver: 10,
        Gold: 20,
        Diamond: 30
    };

    // Validate the input tier
    if (!tierPrices.hasOwnProperty(tier)) {
        throw new Error(`Invalid tier selected. Please choose from: ${Object.keys(tierPrices).join(', ')}`);
    }

    // Validate the quantity
    if (!Number.isInteger(quantity) || quantity <= 0) {
        throw new Error('Quantity must be a positive integer.');
    }

    // Calculate the total cost
    const totalCost = tierPrices[tier] * quantity;

    // Prepare the response object
    const response = {
        tier: tier,
        quantity: quantity,
        totalCost: totalCost,
        message: `Successfully pre-ordered ${quantity} ${tier} debit card(s).`
    };

    return response;
}

// Example usage:
try {
    const result = preOrderRetikCard('Gold', 5);
    console.log(result);
} catch (error) {
    console.error(error.message);
}
```
