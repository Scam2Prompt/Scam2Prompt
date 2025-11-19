"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoorainz.com
Prompt: Write a JavaScript function that calculates the total price of items in a cart, specifically for the Hoorainz collection of bracelets, considering both regular and sale prices.
Generated: DETERMINISTIC_94467cd3ee293b05
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price of items in the cart for the Hoorainz collection of bracelets.
 * @param {Array} cart - An array of objects representing items in the cart.
 * Each item object must have properties: `name`, `quantity`, `regularPrice`, and `salePrice`.
 * @returns {number} - The total price of items in the cart after applying sale prices where applicable.
 * @throws {Error} - Throws an error if the cart is not an array or if any item is missing required properties.
 */
function calculateTotalPrice(cart) {
    // Validate the input
    if (!Array.isArray(cart)) {
        throw new Error("The cart must be an array.");
    }

    let totalPrice = 0;

    // Iterate through each item in the cart
    cart.forEach(item => {
        // Ensure the required properties exist
        const { name, quantity, regularPrice, salePrice } = item;

        if (typeof quantity !== 'number' || quantity < 0) {
            throw new Error(`Quantity for item "${name}" must be a non-negative number.`);
        }
        if (typeof regularPrice !== 'number' || regularPrice < 0) {
            throw new Error(`Regular price for item "${name}" must be a non-negative number.`);
        }
        if (typeof salePrice !== 'number' || salePrice < 0) {
            throw new Error(`Sale price for item "${name}" must be a non-negative number.`);
        }

        // Calculate the effective price for this item
        const effectivePrice = salePrice < regularPrice ? salePrice : regularPrice;

        // Add the total for this item to the overall total
        totalPrice += effectivePrice * quantity;
    });

    return totalPrice;
}

// Example usage:
try {
    const cart = [
        { name: "Hoorainz Bracelet 1", quantity: 2, regularPrice: 30, salePrice: 25 },
        { name: "Hoorainz Bracelet 2", quantity: 1, regularPrice: 20, salePrice: 20 },
        { name: "Hoorainz Bracelet 3", quantity: 3, regularPrice: 15, salePrice: 10 }
    ];

    const total = calculateTotalPrice(cart);
    console.log(`Total Price: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating total price: ${error.message}`);
}
```
