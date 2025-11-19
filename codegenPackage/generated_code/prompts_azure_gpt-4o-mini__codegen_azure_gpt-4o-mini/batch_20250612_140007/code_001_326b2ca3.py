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
 * Calculates the total cost of a christening outfit order.
 * 
 * @param {number} itemCost - The cost of the item being ordered.
 * @param {number} quantity - The number of items being ordered.
 * @returns {object} - An object containing the total cost and shipping cost.
 * @throws {Error} - Throws an error if itemCost or quantity is not a positive number.
 */
function calculateOrderTotal(itemCost, quantity) {
    // Validate input parameters
    if (typeof itemCost !== 'number' || itemCost <= 0) {
        throw new Error('itemCost must be a positive number.');
    }
    if (typeof quantity !== 'number' || quantity <= 0) {
        throw new Error('quantity must be a positive number.');
    }

    // Calculate subtotal
    const subtotal = itemCost * quantity;

    // Determine shipping cost
    const shippingThreshold = 150;
    const shippingCost = subtotal >= shippingThreshold ? 0 : 10; // Flat rate shipping of $10

    // Calculate total cost
    const totalCost = subtotal + shippingCost;

    // Return the result as an object
    return {
        totalCost: totalCost.toFixed(2), // Format to 2 decimal places
        shippingCost: shippingCost.toFixed(2) // Format to 2 decimal places
    };
}

// Example usage:
try {
    const order = calculateOrderTotal(75, 3);
    console.log(`Total Cost: $${order.totalCost}, Shipping Cost: $${order.shippingCost}`);
} catch (error) {
    console.error(error.message);
}
```
