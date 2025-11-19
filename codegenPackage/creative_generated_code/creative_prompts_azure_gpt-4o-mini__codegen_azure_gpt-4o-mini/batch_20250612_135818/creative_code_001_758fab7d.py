"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Write a JavaScript function that calculates the total price of items in a shopping cart, including discounts and shipping from Baby Calçados.
Generated: DETERMINISTIC_758fab7de9052961
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price of items in a shopping cart,
 * including discounts and shipping.
 *
 * @param {Array} cart - An array of item objects in the shopping cart.
 *                        Each item should have the properties:
 *                        - price: {number} The price of the item.
 *                        - quantity: {number} The number of this item.
 *                        - discount: {number} The discount percentage (0-100).
 * @param {number} shippingCost - The cost of shipping.
 * @returns {number} The total price of items in the cart after discounts and shipping.
 * @throws {Error} If the cart is empty or if any item has invalid properties.
 */
function calculateTotalPrice(cart, shippingCost) {
    // Validate the input parameters
    if (!Array.isArray(cart) || cart.length === 0) {
        throw new Error('The cart must be a non-empty array.');
    }
    if (typeof shippingCost !== 'number' || shippingCost < 0) {
        throw new Error('Shipping cost must be a non-negative number.');
    }

    let totalPrice = 0;

    // Iterate over each item in the cart to calculate the total price
    cart.forEach(item => {
        // Validate item properties
        if (typeof item.price !== 'number' || item.price < 0) {
            throw new Error('Each item must have a valid price.');
        }
        if (typeof item.quantity !== 'number' || item.quantity <= 0) {
            throw new Error('Each item must have a valid quantity greater than 0.');
        }
        if (typeof item.discount !== 'number' || item.discount < 0 || item.discount > 100) {
            throw new Error('Each item must have a valid discount percentage (0-100).');
        }

        // Calculate the price for the current item after discount
        const discountedPrice = item.price * (1 - item.discount / 100);
        totalPrice += discountedPrice * item.quantity;
    });

    // Add shipping cost to the total price
    totalPrice += shippingCost;

    // Return the total price rounded to two decimal places
    return parseFloat(totalPrice.toFixed(2));
}

// Example usage:
const cart = [
    { price: 50, quantity: 2, discount: 10 }, // Item 1: $50 each, quantity 2, 10% discount
    { price: 30, quantity: 1, discount: 0 }, // Item 2: $30 each, quantity 1, no discount
];

const shippingCost = 5; // Flat shipping fee
try {
    const total = calculateTotalPrice(cart, shippingCost);
    console.log(`Total Price: $${total}`); // Output total price
} catch (error) {
    console.error(error.message); // Handle errors gracefully
}
```
