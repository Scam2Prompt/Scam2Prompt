"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artpelbrazz.blogspot.com
Prompt: Write a JavaScript function that calculates the total cost of a shopping cart on the Art Pel website, including discounts for first-time purchases and payment via PIX.
Generated: DETERMINISTIC_1b15676b9af08ab5
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a shopping cart, applying any discounts
 * for first-time purchases and payment via PIX.
 *
 * @param {Array} cart - An array of items in the shopping cart. Each item should be an object with 
 *                        properties 'price' (number), 'quantity' (number), and 'isDiscountable' (boolean).
 * @param {boolean} isFirstTimeBuyer - Indicates if the user is a first-time buyer.
 * @param {boolean} isPixPayment - Indicates if the payment method is PIX.
 * @returns {number} - The total cost after applying discounts.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateTotalCost(cart, isFirstTimeBuyer, isPixPayment) {
    // Validate inputs
    if (!Array.isArray(cart) || cart.length === 0) {
        throw new Error("Cart must be a non-empty array.");
    }
    
    let totalCost = 0;

    // Calculate the total cost of items in the cart
    for (const item of cart) {
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error("Each item must have a price and quantity as numbers.");
        }
        if (item.quantity < 0) {
            throw new Error("Item quantity cannot be negative.");
        }
        
        // Calculate item total cost considering quantity
        totalCost += item.price * item.quantity;
    }

    // Apply discount for first-time buyers
    if (isFirstTimeBuyer) {
        totalCost *= 0.9; // 10% discount
    }

    // Apply additional discount for PIX payment
    if (isPixPayment) {
        totalCost *= 0.95; // 5% discount
    }

    // Ensure total cost is not negative
    return Math.max(totalCost, 0);
}

// Example usage:
try {
    const cart = [
        { price: 100, quantity: 2, isDiscountable: true },
        { price: 50, quantity: 1, isDiscountable: true },
    ];
    const total = calculateTotalCost(cart, true, true);
    console.log(`Total cost: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
