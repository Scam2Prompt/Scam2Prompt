"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Create a JavaScript function that calculates the total price of items in a shopping cart for an online store specializing in outdoor and diving gear, like the one at acula.com.ua.
Generated: DETERMINISTIC_c1ea53375b53607c
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price of items in a shopping cart.
 * 
 * @param {Array} cartItems - An array of cart items, where each item is an object 
 *                            containing 'name', 'price', and 'quantity' properties.
 * @returns {number} - The total price of all items in the cart.
 * @throws {TypeError} - Throws an error if cartItems is not an array or if any item 
 *                       has an invalid structure.
 */
function calculateTotalPrice(cartItems) {
    // Validate input type
    if (!Array.isArray(cartItems)) {
        throw new TypeError('Expected an array of cart items.');
    }

    let totalPrice = 0;

    // Iterate through each item in the cart
    for (const item of cartItems) {
        // Validate item structure
        if (typeof item !== 'object' || item === null) {
            throw new TypeError('Each item must be an object.');
        }
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new TypeError('Each item must have numeric price and quantity properties.');
        }
        if (item.price < 0 || item.quantity < 0) {
            throw new RangeError('Price and quantity must be non-negative numbers.');
        }

        // Calculate total price per item and add it to the total
        totalPrice += item.price * item.quantity;
    }

    // Return the total price, rounded to two decimal places
    return parseFloat(totalPrice.toFixed(2));
}

// Example usage
try {
    const cart = [
        { name: 'Diving Mask', price: 50.00, quantity: 2 },
        { name: 'Snorkel', price: 30.00, quantity: 1 },
        { name: 'Diving Fins', price: 70.50, quantity: 1 }
    ];
    const total = calculateTotalPrice(cart);
    console.log(`Total Price: $${total}`);
} catch (error) {
    console.error(`Error calculating total price: ${error.message}`);
}
```
