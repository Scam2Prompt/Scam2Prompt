"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Create a JavaScript function that calculates the total cost of items in a shopping cart, inspired by the pricing structure seen on Curaheridas.
Generated: DETERMINISTIC_fce5ed6fecf2ffb6
Batch ID: 20250612_155432
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
 * The function considers a pricing structure with potential discounts.
 * 
 * @param {Array} cart - An array of objects representing items in the cart.
 * Each object should have the following properties:
 *   - {number} price - The price of the item.
 *   - {number} quantity - The quantity of the item.
 *   - {number} [discount=0] - The discount on the item (optional), expressed as a percentage (0-100).
 * 
 * @returns {number} - The total cost of items in the cart, including discounts.
 * @throws {Error} - Throws an error if any item has invalid price or quantity.
 */
function calculateTotalCost(cart) {
    // Initialize total cost
    let totalCost = 0;

    // Validate cart input
    if (!Array.isArray(cart)) {
        throw new Error('Invalid cart: Expected an array of items.');
    }

    // Iterate over each item in the cart
    cart.forEach(item => {
        // Destructure properties for clarity
        const { price, quantity, discount = 0 } = item;

        // Validate item properties
        if (typeof price !== 'number' || price < 0) {
            throw new Error(`Invalid price for item: ${price}. Price must be a non-negative number.`);
        }
        if (typeof quantity !== 'number' || quantity < 1) {
            throw new Error(`Invalid quantity for item: ${quantity}. Quantity must be a positive integer.`);
        }
        if (typeof discount !== 'number' || discount < 0 || discount > 100) {
            throw new Error(`Invalid discount for item: ${discount}. Discount must be between 0 and 100.`);
        }

        // Calculate item total cost after discount
        const discountAmount = (price * discount) / 100;
        const finalPrice = price - discountAmount;
        totalCost += finalPrice * quantity; // Add to total cost
    });

    // Return the total cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage
try {
    const shoppingCart = [
        { price: 20.00, quantity: 2, discount: 10 },
        { price: 5.00, quantity: 1 },
        { price: 15.00, quantity: 3, discount: 5 }
    ];
    
    const total = calculateTotalCost(shoppingCart);
    console.log(`Total cost: $${total}`); // Total cost output
} catch (error) {
    console.error(error.message); // Handle errors gracefully
}
```
