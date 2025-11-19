"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Develop a JavaScript function that calculates estimated costs including taxes and discounts for items in a shopping cart on Duckchain World.
Generated: DETERMINISTIC_fab23d321bffd3b0
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated total cost for items in a shopping cart,
 * including taxes and discounts.
 *
 * @param {Array<Object>} cartItems - An array of objects representing items in the cart.
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.07 for 7%).
 * @param {number} discountRate - The discount rate as a decimal (e.g., 0.10 for 10%).
 * @returns {Object} - An object containing the subtotal, total discount, tax amount, and total cost.
 * @throws {Error} - Throws an error if cartItems is not an array or if any item is missing required properties.
 */
function calculateCartTotal(cartItems, taxRate = 0, discountRate = 0) {
    // Validate input types
    if (!Array.isArray(cartItems)) {
        throw new Error('cartItems must be an array.');
    }

    let subtotal = 0;

    // Calculate the subtotal
    for (const item of cartItems) {
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error('Each item must have a price and quantity as numbers.');
        }
        subtotal += item.price * item.quantity;
    }

    // Calculate total discount
    const totalDiscount = subtotal * discountRate;

    // Calculate tax amount
    const taxAmount = (subtotal - totalDiscount) * taxRate;

    // Calculate the total cost
    const totalCost = subtotal - totalDiscount + taxAmount;

    // Return a structured result
    return {
        subtotal: parseFloat(subtotal.toFixed(2)),
        totalDiscount: parseFloat(totalDiscount.toFixed(2)),
        taxAmount: parseFloat(taxAmount.toFixed(2)),
        totalCost: parseFloat(totalCost.toFixed(2)),
    };
}

// Example usage:
try {
    const cartItems = [
        { price: 29.99, quantity: 2 },
        { price: 15.00, quantity: 1 },
        { price: 5.50, quantity: 3 },
    ];
    const taxRate = 0.07;    // 7% tax
    const discountRate = 0.10; // 10% discount

    const totals = calculateCartTotal(cartItems, taxRate, discountRate);
    console.log(totals);
} catch (error) {
    console.error('Error calculating totals:', error.message);
}
```
