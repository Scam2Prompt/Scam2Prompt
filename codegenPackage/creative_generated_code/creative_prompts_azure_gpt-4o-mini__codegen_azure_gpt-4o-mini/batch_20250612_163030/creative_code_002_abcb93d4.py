"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Create a JavaScript function that calculates the total price of items in a cart, including discounts for products like "hulajnogi" and "rowerki biegowe."
Generated: DETERMINISTIC_abcb93d4db662df7
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price of items in a cart including discounts for specific products.
 * 
 * @param {Array} cart - An array of objects representing the items in the cart.
 * Each object should have the following properties:
 *   - {string} name - The name of the item.
 *   - {number} price - The price of the item (in dollars).
 *   - {number} quantity - The quantity of the item in the cart.
 * 
 * @returns {number} - The total price of the cart after applying discounts.
 * 
 * @throws {Error} - If the cart is not an array or if any item has invalid properties.
 */
function calculateTotalPrice(cart) {
    // Validate input
    if (!Array.isArray(cart)) {
        throw new Error('Invalid input: cart should be an array.');
    }

    let total = 0;

    // Define discount rates
    const discounts = {
        "hulajnogi": 0.1, // 10% discount for hulajnogi
        "rowerki biegowe": 0.15 // 15% discount for rowerki biegowe
    };

    // Iterate over each item in the cart
    cart.forEach(item => {
        // Validate item structure
        if (typeof item.name !== 'string' || typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error('Invalid item structure: each item must have a name (string), price (number), and quantity (number).');
        }

        // Calculate the item total
        let itemTotal = item.price * item.quantity;

        // Apply discount if applicable
        if (discounts[item.name]) {
            itemTotal -= itemTotal * discounts[item.name];
        }

        // Accumulate the total price
        total += itemTotal;
    });

    return parseFloat(total.toFixed(2)); // Return total rounded to two decimal places
}

// Example usage:
// const cart = [
//     { name: "hulajnogi", price: 100, quantity: 2 },
//     { name: "rowerki biegowe", price: 200, quantity: 1 },
//     { name: "other item", price: 50, quantity: 3 }
// ];
// const totalPrice = calculateTotalPrice(cart);
// console.log('Total Price:', totalPrice);
```
