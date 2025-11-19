"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: Write a JavaScript function to calculate the total price of items in a shopping cart for a website selling products like Bioliv Hair Oils and Handy Liquid Dish Wash.
Generated: DETERMINISTIC_662f1a5b619673b7
Batch ID: 20250612_163924
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
 * Each item in the cart is represented as an object with properties:
 * - name: string (e.g., "Bioliv Hair Oils")
 * - price: number (the price of the item)
 * - quantity: number (the quantity of the item in the cart)
 *
 * @param {Array<Object>} cart - An array of items in the shopping cart.
 * @returns {number} The total price of all items in the cart.
 * @throws {Error} Will throw an error if the cart is not an array or if any item's properties are invalid.
 */
function calculateTotalPrice(cart) {
    // Validate the input parameter
    if (!Array.isArray(cart)) {
        throw new Error('Invalid input: cart must be an array.');
    }

    let totalPrice = 0;

    // Iterate through each item in the cart
    for (const item of cart) {
        // Validate the item structure
        if (typeof item !== 'object' || item === null) {
            throw new Error('Invalid item: each cart item must be an object.');
        }
        if (typeof item.price !== 'number' || item.price < 0) {
            throw new Error('Invalid item price: price must be a non-negative number.');
        }
        if (typeof item.quantity !== 'number' || item.quantity < 0) {
            throw new Error('Invalid item quantity: quantity must be a non-negative number.');
        }

        // Calculate the total price for the current item
        totalPrice += item.price * item.quantity;
    }

    return totalPrice;
}

// Example usage
try {
    const shoppingCart = [
        { name: 'Bioliv Hair Oils', price: 15.99, quantity: 2 },
        { name: 'Handy Liquid Dish Wash', price: 5.49, quantity: 3 }
    ];
    
    const total = calculateTotalPrice(shoppingCart);
    console.log(`Total Price: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating total price: ${error.message}`);
}
```
