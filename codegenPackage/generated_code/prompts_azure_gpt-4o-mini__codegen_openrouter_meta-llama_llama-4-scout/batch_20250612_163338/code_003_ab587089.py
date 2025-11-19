"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Develop a JavaScript function to calculate the total cost of a floral order, including discounts for bulk purchases, based on the products listed on a floral website.
Generated: DETERMINISTIC_ab587089b7792a37
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a floral order, including discounts for bulk purchases.
 * 
 * @param {Object[]} products - Array of products in the order, each with properties: id, name, quantity, price
 * @param {Object} discounts - Object with bulk purchase discounts, where each key is a product ID and each value is an object with properties: quantity, discount
 * @returns {number} The total cost of the order
 */
function calculateOrderTotal(products, discounts) {
    // Initialize total cost to zero
    let totalCost = 0;

    // Iterate over each product in the order
    products.forEach(product => {
        // Check if product has required properties
        if (!product.id || !product.name || !product.quantity || !product.price) {
            throw new Error(`Invalid product: ${JSON.stringify(product)}`);
        }

        // Calculate subtotal for this product
        let subtotal = product.quantity * product.price;

        // Check if there are discounts for this product
        if (discounts[product.id]) {
            // Get discount for this product
            const discount = discounts[product.id];

            // Check if discount has required properties
            if (!discount.quantity || !discount.discount) {
                throw new Error(`Invalid discount: ${JSON.stringify(discount)}`);
            }

            // Apply discount if quantity meets the requirement
            if (product.quantity >= discount.quantity) {
                subtotal *= (1 - discount.discount / 100);
            }
        }

        // Add subtotal to total cost
        totalCost += subtotal;
    });

    // Return total cost, rounded to two decimal places
    return Math.round(totalCost * 100) / 100;
}

// Example usage:
const products = [
    { id: 1, name: 'Roses', quantity: 10, price: 5.99 },
    { id: 2, name: 'Lilies', quantity: 20, price: 3.99 },
    { id: 3, name: 'Carnations', quantity: 5, price: 2.99 }
];

const discounts = {
    1: { quantity: 12, discount: 10 }, // 10% off 12+ roses
    2: { quantity: 24, discount: 15 } // 15% off 24+ lilies
};

try {
    const totalCost = calculateOrderTotal(products, discounts);
    console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
