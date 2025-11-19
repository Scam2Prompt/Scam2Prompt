"""
Generated Code Metadata:
========================
Original URL: https://curaheridas.com
Prompt: Create a JavaScript function that calculates the total cost of items in a shopping cart, inspired by the pricing structure seen on Curaheridas.
Generated: DETERMINISTIC_fce5ed6fecf2ffb6
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of items in a shopping cart.
 * 
 * @param {Object[]} cart - The shopping cart contents.
 * @param {string} cart[].name - The name of the item.
 * @param {number} cart[].price - The price of the item.
 * @param {number} cart[].quantity - The quantity of the item.
 * @param {Object} [discounts={}] - Optional discounts object.
 * @param {number} [discounts.percentage=0] - Percentage discount.
 * @param {number} [discounts.fixed=0] - Fixed amount discount.
 * @returns {number} The total cost of the items in the cart.
 */
function calculateTotalCost(cart, discounts = {}) {
    // Initialize total cost to zero
    let totalCost = 0;

    // Validate cart contents
    if (!Array.isArray(cart)) {
        throw new Error('Cart must be an array');
    }

    // Iterate over each item in the cart
    cart.forEach(item => {
        // Validate item properties
        if (typeof item.name !== 'string' || typeof item.price !== 'number' || typeof item.quantity !== 'number') {
            throw new Error('Invalid item properties');
        }

        // Calculate item subtotal
        const itemSubtotal = item.price * item.quantity;

        // Add item subtotal to total cost
        totalCost += itemSubtotal;
    });

    // Apply discounts
    if (discounts.percentage) {
        // Calculate percentage discount amount
        const percentageDiscount = totalCost * (discounts.percentage / 100);

        // Subtract percentage discount from total cost
        totalCost -= percentageDiscount;
    }

    if (discounts.fixed) {
        // Subtract fixed discount from total cost
        totalCost -= discounts.fixed;
    }

    // Ensure total cost is not negative
    totalCost = Math.max(totalCost, 0);

    // Return total cost rounded to two decimal places
    return Number(totalCost.toFixed(2));
}

// Example usage:
const cart = [
    { name: 'Item 1', price: 10.99, quantity: 2 },
    { name: 'Item 2', price: 5.49, quantity: 3 },
];

const discounts = {
    percentage: 10,
    fixed: 2.00,
};

try {
    const totalCost = calculateTotalCost(cart, discounts);
    console.log(`Total cost: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
