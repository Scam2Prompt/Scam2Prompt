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
 * Calculates the total price of items in a shopping cart.
 * 
 * @param {Array<Object>} items - An array of items where each item is an object containing:
 *                                { price: number, quantity: number }
 * @param {number} taxRate - The tax rate to apply (in decimal form, e.g. 0.05 for 5%).
 * @param {number} discountThreshold - The minimum amount to qualify for a discount.
 * @param {number} discountRate - The discount rate to apply (in decimal form, e.g. 0.10 for 10%).
 * @returns {number} - The total price after applying tax and discounts.
 * @throws {Error} - Throws an error if items array is empty or if an item has invalid properties.
 */
function calculateTotalPrice(items, taxRate = 0.05, discountThreshold = 150.00, discountRate = 0.10) {
    // Validate input
    if (!Array.isArray(items) || items.length === 0) {
        throw new Error("Invalid items array: must be a non-empty array.");
    }

    let subtotal = 0;

    // Calculate subtotal
    items.forEach(item => {
        if (typeof item.price !== 'number' || typeof item.quantity !== 'number' || item.quantity < 0) {
            throw new Error("Invalid item: each item must have a valid price (number) and quantity (non-negative number).");
        }
        subtotal += item.price * item.quantity;
    });

    // Apply discount if subtotal exceeds the discount threshold
    if (subtotal > discountThreshold) {
        subtotal -= subtotal * discountRate;
    }

    // Calculate total price with tax
    const totalPrice = subtotal + (subtotal * taxRate);

    return parseFloat(totalPrice.toFixed(2)); // Return total price rounded to 2 decimal places
}

// Example usage
try {
    const cartItems = [
        { price: 50, quantity: 2 }, // 2 items at AED 50 each
        { price: 30, quantity: 1 }   // 1 item at AED 30
    ];
    const total = calculateTotalPrice(cartItems);
    console.log(`Total Price: AED ${total}`);
} catch (error) {
    console.error(error.message);
}
```
