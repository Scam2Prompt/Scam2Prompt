"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: Write a JavaScript function that calculates the total price of items in a cart, specifically for the Hoorainz collection of bracelets, considering both regular and sale prices.
Generated: DETERMINISTIC_94467cd3ee293b05
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total price of items in a cart for the Hoorainz collection of bracelets.
 * 
 * @param {Array} cart - A list of cart items. Each item is an object with properties 'price' and 'salePrice' and 'quantity'.
 * @param {Boolean} useSalePrice - Whether to use the sale price or the regular price for calculation.
 * @returns {Number} The total price of items in the cart.
 */
function calculateCartTotal(cart, useSalePrice) {
    // Check if cart is an array and useSalePrice is a boolean
    if (!Array.isArray(cart) || typeof useSalePrice !== 'boolean') {
        throw new Error('Invalid input type');
    }

    // Initialize total price to 0
    let totalPrice = 0;

    // Iterate over each item in the cart
    cart.forEach(item => {
        // Check if item has required properties
        if (!('price' in item) || !('quantity' in item)) {
            throw new Error('Invalid cart item');
        }

        // Get the price to use (sale price or regular price)
        const price = useSalePrice && 'salePrice' in item ? item.salePrice : item.price;

        // Check if price and quantity are numbers
        if (typeof price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error('Invalid price or quantity');
        }

        // Add item price to total price
        totalPrice += price * item.quantity;
    });

    // Return the total price
    return totalPrice;
}

// Example usage:
const cart = [
    { price: 100, salePrice: 80, quantity: 2 },
    { price: 50, quantity: 1 },
    { price: 200, salePrice: 150, quantity: 3 }
];

try {
    const totalPriceUsingRegularPrice = calculateCartTotal(cart, false);
    console.log(`Total price using regular price: $${totalPriceUsingRegularPrice.toFixed(2)}`);

    const totalPriceUsingSalePrice = calculateCartTotal(cart, true);
    console.log(`Total price using sale price: $${totalPriceUsingSalePrice.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
