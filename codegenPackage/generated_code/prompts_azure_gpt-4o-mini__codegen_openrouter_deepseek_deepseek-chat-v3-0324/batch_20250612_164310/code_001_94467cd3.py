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
 * Calculates the total price of items in a cart for the Hoorainz bracelet collection.
 * Considers both regular and sale prices, and applies proper error handling.
 * 
 * @param {Array} cartItems - Array of cart items with product details
 * @returns {Object} An object containing the total price and any errors encountered
 */
function calculateCartTotal(cartItems) {
    if (!Array.isArray(cartItems)) {
        return {
            total: 0,
            errors: ['Invalid cart items format. Expected an array.']
        };
    }

    let total = 0;
    const errors = [];

    cartItems.forEach((item, index) => {
        try {
            // Validate required fields
            if (!item || typeof item !== 'object') {
                errors.push(`Item at position ${index} is invalid.`);
                return;
            }

            if (item.quantity === undefined || item.quantity === null) {
                errors.push(`Item at position ${index} has no quantity specified.`);
                return;
            }

            const quantity = Number(item.quantity);
            if (isNaN(quantity) || quantity < 0) {
                errors.push(`Invalid quantity for item at position ${index}.`);
                return;
            }

            // Determine which price to use (sale price takes precedence)
            let price = 0;
            if (item.salePrice !== undefined && item.salePrice !== null) {
                price = Number(item.salePrice);
            } else if (item.regularPrice !== undefined && item.regularPrice !== null) {
                price = Number(item.regularPrice);
            } else {
                errors.push(`No valid price found for item at position ${index}.`);
                return;
            }

            if (isNaN(price) || price < 0) {
                errors.push(`Invalid price for item at position ${index}.`);
                return;
            }

            // Calculate item subtotal and add to total
            total += price * quantity;
        } catch (error) {
            errors.push(`Error processing item at position ${index}: ${error.message}`);
        }
    });

    return {
        total: parseFloat(total.toFixed(2)), // Ensure proper currency formatting
        errors: errors.length > 0 ? errors : null
    };
}

// Example usage:
// const cart = [
//     { id: 1, name: 'Bracelet 1', regularPrice: 29.99, salePrice: 24.99, quantity: 2 },
//     { id: 2, name: 'Bracelet 2', regularPrice: 39.99, quantity: 1 },
//     { id: 3, name: 'Bracelet 3', salePrice: 19.99, quantity: 3 }
// ];
// const result = calculateCartTotal(cart);
// console.log(result);
```
