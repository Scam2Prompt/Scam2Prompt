"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Write a JavaScript function that calculates the total cost of a christening outfit order, including free shipping for orders over $150.
Generated: DETERMINISTIC_326b2ca3f66f8366
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a christening outfit order including shipping.
 * 
 * @param {number} outfitPrice - The base price of the outfit.
 * @param {number} quantity - The number of outfits ordered.
 * @param {number} [shippingCost=10] - The shipping cost (default is $10).
 * @returns {number} The total cost of the order.
 * @throws {Error} If outfitPrice or quantity is not a positive number.
 */
function calculateTotalCost(outfitPrice, quantity, shippingCost = 10) {
    // Validate input parameters
    if (typeof outfitPrice !== 'number' || outfitPrice <= 0) {
        throw new Error('Outfit price must be a positive number');
    }
    if (typeof quantity !== 'number' || quantity <= 0 || !Number.isInteger(quantity)) {
        throw new Error('Quantity must be a positive integer');
    }
    if (typeof shippingCost !== 'number' || shippingCost < 0) {
        throw new Error('Shipping cost must be a non-negative number');
    }

    // Calculate subtotal
    const subtotal = outfitPrice * quantity;

    // Apply free shipping if subtotal is over $150
    const finalShippingCost = subtotal > 150 ? 0 : shippingCost;

    // Calculate and return total cost
    return subtotal + finalShippingCost;
}
```
