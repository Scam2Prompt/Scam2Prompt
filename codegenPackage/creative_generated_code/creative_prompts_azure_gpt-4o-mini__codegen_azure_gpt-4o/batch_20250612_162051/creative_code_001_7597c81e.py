"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Generate a JavaScript function that calculates the total price of items in a ShopeeWise shopping cart, including taxes and discounts for orders above AED 150.00.
Generated: DETERMINISTIC_7597c81e1470020c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total price of items in a ShopeeWise shopping cart.
 * Applies a discount for orders above AED 150.00 and includes a tax rate.
 * 
 * @param {Array} cartItems - Array of objects representing items in the cart.
 * Each object should have the following properties:
 *   - price: {number} Price of the item.
 *   - quantity: {number} Quantity of the item.
 * @param {number} taxRate - Tax rate as a percentage (e.g., 5 for 5% tax).
 * @param {number} discountThreshold - Order minimum for discount eligibility.
 * @param {number} discountRate - Discount rate as a percentage (e.g., 10 for 10% discount).
 * @returns {number} - The total price after applying taxes and discounts.
 */
function calculateTotalPrice(cartItems, taxRate, discountThreshold, discountRate) {
    try {
        // Validate inputs
        if (!Array.isArray(cartItems)) {
            throw new Error("cartItems must be an array.");
        }
        if (typeof taxRate !== "number" || taxRate < 0) {
            throw new Error("taxRate must be a non-negative number.");
        }
        if (typeof discountThreshold !== "number" || discountThreshold < 0) {
            throw new Error("discountThreshold must be a non-negative number.");
        }
        if (typeof discountRate !== "number" || discountRate < 0) {
            throw new Error("discountRate must be a non-negative number.");
        }

        // Calculate subtotal
        let subtotal = 0;
        for (const item of cartItems) {
            if (typeof item.price !== "number" || item.price < 0 || typeof item.quantity !== "number" || item.quantity < 0) {
                throw new Error("Each item must have a non-negative price and quantity.");
            }
            subtotal += item.price * item.quantity;
        }

        // Apply discount if the subtotal exceeds the discount threshold
        let discount = 0;
        if (subtotal > discountThreshold) {
            discount = (subtotal * discountRate) / 100;
        }

        // Calculate tax
        const tax = ((subtotal - discount) * taxRate) / 100;

        // Calculate total price
        const total = subtotal - discount + tax;

        return parseFloat(total.toFixed(2)); // Return the total rounded to 2 decimal places
    } catch (error) {
        console.error("Error calculating total price:", error.message);
        throw error; // Re-throw error for further handling if necessary
    }
}

// Example usage
const cartItems = [
    { price: 50.0, quantity: 2 },
    { price: 25.0, quantity: 1 },
    { price: 100.0, quantity: 1 },
];
const taxRate = 5; // 5% tax
const discountThreshold = 150.0; // AED 150.00 threshold for discount
const discountRate = 10; // 10% discount

try {
    const totalPrice = calculateTotalPrice(cartItems, taxRate, discountThreshold, discountRate);
    console.log("Total Price (including tax and discount): AED", totalPrice);
} catch (error) {
    console.error("Failed to calculate total price:", error.message);
}
```
