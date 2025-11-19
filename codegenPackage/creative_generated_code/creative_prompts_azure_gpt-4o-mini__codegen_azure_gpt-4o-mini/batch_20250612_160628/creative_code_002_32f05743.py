"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bricohogar.com
Prompt: Create a JavaScript function that calculates the total cost of items in a shopping cart, including a free shipping threshold like the one mentioned on Bricohogar (free shipping over 35€).
Generated: DETERMINISTIC_32f0574310c51b7e
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of items in a shopping cart.
 * Includes shipping costs based on a free shipping threshold.
 *
 * @param {Array<Object>} cart - Array of items in the shopping cart.
 * @param {number} cart[].price - The price of the item.
 * @param {number} cart[].quantity - The quantity of the item.
 * @param {number} shippingThreshold - The threshold for free shipping.
 * @param {number} shippingCost - The cost of shipping if the threshold is not met.
 * @returns {Object} - An object containing total cost and shipping cost.
 * @throws {Error} - Throws an error if the cart is not an array or if items are invalid.
 */
function calculateTotalCost(cart, shippingThreshold = 35, shippingCost = 5) {
    // Validate input
    if (!Array.isArray(cart)) {
        throw new Error('The cart must be an array of items.');
    }

    let totalCost = 0;

    // Iterate over each item in the cart
    cart.forEach(item => {
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error('Each item must have a valid price and quantity.');
        }
        totalCost += item.price * item.quantity;
    });

    // Determine shipping cost
    const totalShippingCost = totalCost >= shippingThreshold ? 0 : shippingCost;

    // Return the total cost and shipping cost
    return {
        totalCost: totalCost + totalShippingCost,
        shippingCost: totalShippingCost
    };
}

// Example usage:
const shoppingCart = [
    { price: 10, quantity: 2 }, // €20
    { price: 5, quantity: 3 },  // €15
    { price: 15, quantity: 1 }   // €15
];

try {
    const result = calculateTotalCost(shoppingCart);
    console.log(`Total Cost: €${result.totalCost}, Shipping Cost: €${result.shippingCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
