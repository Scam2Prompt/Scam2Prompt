"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woopytee.com
Prompt: Write a JavaScript function to calculate the discount on a cart total based on the WoopyTee "Buy More Save More" promotion.
Generated: DETERMINISTIC_b058131f01ee27e6
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the discount based on the "Buy More Save More" promotion.
 * 
 * @param {number} cartTotal - The total amount of the cart before discount.
 * @param {number} itemCount - The total number of items in the cart.
 * @returns {number} The discount amount.
 * @throws {TypeError} Throws an error if cartTotal or itemCount is not a number.
 */
function calculateDiscount(cartTotal, itemCount) {
    // Validate inputs
    if (typeof cartTotal !== 'number' || typeof itemCount !== 'number') {
        throw new TypeError('Both cartTotal and itemCount should be numbers.');
    }

    // Initialize discount variable
    let discount = 0;

    // Define discount tiers based on item count
    if (itemCount >= 10) {
        discount = cartTotal * 0.20; // 20% off for 10 or more items
    } else if (itemCount >= 5) {
        discount = cartTotal * 0.10; // 10% off for 5 to 9 items
    } else if (itemCount >= 3) {
        discount = cartTotal * 0.05; // 5% off for 3 to 4 items
    }

    // Return the discount amount
    return discount;
}

// Example usage:
try {
    const cartTotal = 150; // total cart value
    const itemCount = 6;   // number of items in the cart
    const discount = calculateDiscount(cartTotal, itemCount);
    console.log(`Discount applied: $${discount.toFixed(2)}`); // Log the discount
} catch (error) {
    console.error(error.message); // Log any errors
}
```
