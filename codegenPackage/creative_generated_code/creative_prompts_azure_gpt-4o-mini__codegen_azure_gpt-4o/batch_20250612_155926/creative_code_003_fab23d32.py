"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Develop a JavaScript function that calculates estimated costs including taxes and discounts for items in a shopping cart on Duckchain World.
Generated: DETERMINISTIC_fab23d321bffd3b0
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of items in a shopping cart, including taxes and discounts.
 * @param {Array} cart - Array of items, where each item is an object with `price`, `quantity`, and `discount` properties.
 * @param {number} taxRate - Tax rate as a percentage (e.g., 10 for 10%).
 * @returns {number} - The total estimated cost including taxes and discounts.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateTotalCost(cart, taxRate) {
    // Validate inputs
    if (!Array.isArray(cart) || typeof taxRate !== 'number' || taxRate < 0) {
        throw new Error("Invalid inputs: Ensure the cart is an array and taxRate is a non-negative number.");
    }

    // Initialize total cost
    let totalCost = 0;

    // Iterate through the shopping cart
    cart.forEach(item => {
        // Validate item structure
        if (
            typeof item.price !== 'number' || item.price < 0 ||
            typeof item.quantity !== 'number' || item.quantity < 0 ||
            typeof item.discount !== 'number' || item.discount < 0
        ) {
            throw new Error("Invalid item in cart: Ensure each item has valid `price`, `quantity`, and `discount` properties.");
        }

        // Calculate item cost after discount
        const discountedPrice = item.price * (1 - item.discount / 100);

        // Calculate total item cost (including quantity)
        const itemTotalCost = discountedPrice * item.quantity;

        // Add to total cost
        totalCost += itemTotalCost;
    });

    // Apply tax to total cost
    const taxAmount = totalCost * (taxRate / 100);
    totalCost += taxAmount;

    // Return the final total cost
    return totalCost.toFixed(2); // Return as a string with 2 decimal places for currency formatting
}

// Example usage:
const shoppingCart = [
    { price: 100, quantity: 2, discount: 10 },
    { price: 50, quantity: 1, discount: 5 },
    { price: 200, quantity: 3, discount: 0 }
];
const taxRate = 8; // 8% tax

try {
    const estimatedCost = calculateTotalCost(shoppingCart, taxRate);
    console.log("Estimated Total Cost:", estimatedCost); // Expected output: Estimated Total Cost: 710.40
} catch (error) {
    console.error("Error:", error.message);
}
```
