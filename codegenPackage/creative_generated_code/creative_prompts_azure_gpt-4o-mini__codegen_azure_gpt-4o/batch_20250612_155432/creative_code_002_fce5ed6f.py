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
 * 
 * Each item in the shopping cart contains:
 * - `name`: Name of the product
 * - `price`: The per-unit price of the product
 * - `quantity`: The number of units of the product being purchased
 * - `discount`: (Optional) Percentage discount applied to the total cost of this item
 * 
 * @param {Array} cart - Array of objects representing the shopping cart items.
 * @returns {number} - Total cost of all items in the shopping cart (after discounts).
 * @throws {Error} - If the input is invalid.
 */
function calculateTotalCost(cart) {
    // Validate input
    if (!Array.isArray(cart)) {
        throw new Error("Invalid input: cart must be an array.");
    }

    let totalCost = 0;

    for (const item of cart) {
        try {
            // Validate item structure
            if (
                typeof item.name !== "string" ||
                typeof item.price !== "number" ||
                typeof item.quantity !== "number" ||
                (item.discount !== undefined && typeof item.discount !== "number")
            ) {
                throw new Error(
                    `Invalid item structure: ${JSON.stringify(item)}`
                );
            }

            // Calculate cost for this item
            let itemCost = item.price * item.quantity;

            // Apply discount if present
            if (item.discount) {
                if (item.discount < 0 || item.discount > 100) {
                    throw new Error(
                        `Invalid discount value for item: ${item.name}`
                    );
                }
                itemCost -= (itemCost * item.discount) / 100;
            }

            // Add item cost to the total cost
            totalCost += itemCost;
        } catch (error) {
            console.error(
                `Error processing item "${item.name || "unknown"}":`,
                error.message
            );
            // Optionally, continue processing other items in the cart
        }
    }

    // Return the rounded total cost
    return Math.round(totalCost * 100) / 100; // Rounded to 2 decimal places
}

// Example usage:
const shoppingCart = [
    { name: "Item A", price: 10.99, quantity: 2 },
    { name: "Item B", price: 5.49, quantity: 4, discount: 10 },
    { name: "Item C", price: 20.0, quantity: 1, discount: 5 },
];

try {
    const total = calculateTotalCost(shoppingCart);
    console.log(`Total cost: $${total}`);
} catch (error) {
    console.error("Failed to calculate total cost:", error.message);
}
```
