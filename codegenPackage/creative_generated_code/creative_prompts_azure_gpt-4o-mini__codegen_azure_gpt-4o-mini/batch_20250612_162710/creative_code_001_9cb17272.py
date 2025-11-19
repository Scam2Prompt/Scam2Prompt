"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lattechocolate.com.ar
Prompt: Write a JavaScript function that calculates the total cost of items in a shopping cart on the Latte Chocolate website, including handling discounts and shipping options.
Generated: DETERMINISTIC_9cb1727247ca3429
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of items in a shopping cart, including discounts and shipping costs.
 * 
 * @param {Array} cart - An array of items in the shopping cart, each item should be an object with 
 *                       properties: price (number), quantity (number), and discount (number).
 * @param {string} shippingOption - The shipping option selected by the user ("standard" or "express").
 * @returns {number} - The total cost of items in the cart after applying discounts and adding shipping fees.
 * @throws {Error} - Throws an error if cart items are invalid or if an unsupported shipping option is provided.
 */
function calculateTotalCost(cart, shippingOption) {
    // Validate input
    if (!Array.isArray(cart)) {
        throw new Error("Invalid cart: must be an array of items.");
    }

    const shippingCosts = {
        standard: 5.00,
        express: 10.00
    };

    // Validate shipping option
    if (!(shippingOption in shippingCosts)) {
        throw new Error("Invalid shipping option: must be 'standard' or 'express'.");
    }

    let totalCost = 0;

    // Iterate over each item in the cart to calculate costs
    cart.forEach(item => {
        // Validate item structure
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number' || typeof item.discount !== 'number') {
            throw new Error("Invalid item: each item must have price, quantity, and discount as numbers.");
        }
        
        // Calculate the cost for the current item
        const itemCost = item.price * item.quantity;
        const discountAmount = itemCost * (item.discount / 100);
        const finalItemCost = itemCost - discountAmount;

        // Accumulate total cost
        totalCost += finalItemCost;
    });

    // Add shipping cost
    totalCost += shippingCosts[shippingOption];

    // Return the final total cost
    return parseFloat(totalCost.toFixed(2)); // Return the total cost rounded to two decimal places
}

// Example usage:
const cart = [
    { price: 20.00, quantity: 2, discount: 10 },
    { price: 15.00, quantity: 1, discount: 5 }
];

try {
    const total = calculateTotalCost(cart, "express");
    console.log(`Total cost: $${total}`);
} catch (error) {
    console.error(error.message);
}
```
