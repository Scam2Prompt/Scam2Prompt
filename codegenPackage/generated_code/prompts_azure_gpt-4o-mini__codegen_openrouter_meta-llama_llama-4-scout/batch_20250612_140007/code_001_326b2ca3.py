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
 * Calculates the total cost of a christening outfit order, including free shipping for orders over $150.
 * 
 * @param {Object} order - The christening outfit order.
 * @param {number} order.items - The number of items in the order.
 * @param {number} order.pricePerItem - The price per item in the order.
 * @param {string} [shippingAddress] - The shipping address (required for orders under $150).
 * 
 * @returns {Object} The total cost of the order, including shipping.
 * 
 * @throws {Error} If the order is invalid or if shipping address is missing for orders under $150.
 */
function calculateOrderTotal(order, shippingAddress) {
    // Check if order is valid
    if (!order || typeof order.items !== 'number' || typeof order.pricePerItem !== 'number') {
        throw new Error('Invalid order');
    }

    // Calculate subtotal
    const subtotal = order.items * order.pricePerItem;

    // Calculate shipping cost
    let shippingCost = 0;
    if (subtotal < 150) {
        // Free shipping is not applicable, check if shipping address is provided
        if (!shippingAddress) {
            throw new Error('Shipping address is required for orders under $150');
        }
        shippingCost = 10; // Assume $10 shipping cost
    }

    // Calculate total cost
    const totalCost = subtotal + shippingCost;

    return {
        subtotal,
        shippingCost,
        totalCost
    };
}

// Example usage:
try {
    const order = {
        items: 2,
        pricePerItem: 75
    };
    const result = calculateOrderTotal(order, '123 Main St');
    console.log(`Subtotal: $${result.subtotal.toFixed(2)}`);
    console.log(`Shipping Cost: $${result.shippingCost.toFixed(2)}`);
    console.log(`Total Cost: $${result.totalCost.toFixed(2)}`);

    const orderOver150 = {
        items: 3,
        pricePerItem: 60
    };
    const resultOver150 = calculateOrderTotal(orderOver150);
    console.log(`Subtotal: $${resultOver150.subtotal.toFixed(2)}`);
    console.log(`Shipping Cost: $${resultOver150.shippingCost.toFixed(2)}`);
    console.log(`Total Cost: $${resultOver150.totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
