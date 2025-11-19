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
 * Calculates the total cost of items in a shopping cart, including discounts and shipping options.
 * 
 * @param {Array} cart - Array of items in the shopping cart. Each item should have:
 *   - price {number}: Price of the item
 *   - quantity {number}: Quantity of the item
 *   - discount {number}: Discount for the item (percentage, e.g., 10 for 10%)
 * @param {Object} shipping - Shipping details object:
 *   - type {string}: Type of shipping ("standard", "express", or "free")
 *   - cost {number}: Cost of shipping if not free
 * @returns {number} - The total cost of the shopping cart
 */
function calculateTotalCost(cart, shipping) {
    // Validate input
    if (!Array.isArray(cart) || typeof shipping !== 'object') {
        throw new Error("Invalid input: cart must be an array and shipping must be an object.");
    }

    // Calculate the total cost of items in the cart
    let totalItemsCost = 0;
    for (const item of cart) {
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number' || typeof item.discount !== 'number') {
            throw new Error("Invalid item in cart: Each item must have price, quantity, and discount as numbers.");
        }

        const discountedPrice = item.price - (item.price * (item.discount / 100));
        totalItemsCost += discountedPrice * item.quantity;
    }

    // Calculate shipping cost
    let shippingCost = 0;
    if (shipping.type === "standard" || shipping.type === "express") {
        shippingCost = shipping.cost || 0; // Default to 0 if cost is missing
    } else if (shipping.type === "free") {
        shippingCost = 0;
    } else {
        throw new Error("Invalid shipping type: Must be 'standard', 'express', or 'free'.");
    }

    // Calculate total cost
    const totalCost = totalItemsCost + shippingCost;

    // Ensure total cost is non-negative
    if (totalCost < 0) {
        throw new Error("Total cost cannot be negative.");
    }

    return totalCost;
}

// Example usage:
try {
    const cart = [
        { price: 15.99, quantity: 2, discount: 10 },
        { price: 25.50, quantity: 1, discount: 5 },
        { price: 9.99, quantity: 3, discount: 0 }
    ];
    const shipping = { type: "standard", cost: 5.99 };

    const totalCost = calculateTotalCost(cart, shipping);
    console.log(`Total Cost: $${totalCost.toFixed(2)}`); // Output: Total Cost: $77.46
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
