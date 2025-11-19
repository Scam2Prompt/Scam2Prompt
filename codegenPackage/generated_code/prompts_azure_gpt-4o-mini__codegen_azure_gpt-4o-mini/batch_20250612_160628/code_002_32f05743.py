"""
Generated Code Metadata:
========================
Original URL: https://bricohogar.com
Prompt: Create a JavaScript function that calculates the total cost of items in a shopping cart, including a free shipping threshold like the one mentioned on Bricohogar (free shipping over 35€).
Generated: DETERMINISTIC_32f0574310c51b7e
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of items in a shopping cart.
 * 
 * @param {Array<Object>} cart - An array of items in the shopping cart.
 * @param {number} cart[].price - The price of the item.
 * @param {number} cart[].quantity - The quantity of the item.
 * @param {number} freeShippingThreshold - The threshold for free shipping.
 * @returns {Object} - An object containing the total cost and shipping cost.
 * @throws {Error} - Throws an error if the cart is not an array or if any item has invalid properties.
 */
function calculateTotalCost(cart, freeShippingThreshold = 35) {
    // Validate input
    if (!Array.isArray(cart)) {
        throw new Error('The cart must be an array.');
    }

    let totalCost = 0;

    // Iterate through each item in the cart
    for (const item of cart) {
        // Validate item properties
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error('Each item must have a numeric price and quantity.');
        }
        if (item.price < 0 || item.quantity < 0) {
            throw new Error('Price and quantity must be non-negative.');
        }

        // Calculate total cost for the item
        totalCost += item.price * item.quantity;
    }

    // Determine shipping cost
    const shippingCost = totalCost >= freeShippingThreshold ? 0 : 5; // Assuming a flat shipping fee of 5€

    // Return the total cost and shipping cost
    return {
        totalCost: totalCost.toFixed(2), // Format to 2 decimal places
        shippingCost: shippingCost.toFixed(2) // Format to 2 decimal places
    };
}

// Example usage:
try {
    const cart = [
        { price: 10, quantity: 2 },
        { price: 5, quantity: 1 },
        { price: 20, quantity: 1 }
    ];
    
    const result = calculateTotalCost(cart);
    console.log(`Total Cost: €${result.totalCost}, Shipping Cost: €${result.shippingCost}`);
} catch (error) {
    console.error(error.message);
}
```
