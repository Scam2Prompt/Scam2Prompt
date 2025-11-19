"""
Generated Code Metadata:
========================
Original URL: https://air-tonway.top
Prompt: Create a JavaScript function to calculate the total cost of a shopping cart containing track cycling products, including taxes and shipping costs.
Generated: DETERMINISTIC_ac0bddf020d6cef8
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a shopping cart containing track cycling products.
 * 
 * @param {Array} cart - An array of product objects in the shopping cart.
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.07 for 7%).
 * @param {number} shippingCost - The flat shipping cost for the order.
 * @returns {number} - The total cost including product prices, tax, and shipping.
 * @throws {Error} - Throws an error if the cart is empty or if any product has invalid price.
 */
function calculateTotalCost(cart, taxRate, shippingCost) {
    // Validate input parameters
    if (!Array.isArray(cart) || cart.length === 0) {
        throw new Error("The shopping cart is empty.");
    }
    if (typeof taxRate !== 'number' || taxRate < 0) {
        throw new Error("Invalid tax rate. It must be a non-negative number.");
    }
    if (typeof shippingCost !== 'number' || shippingCost < 0) {
        throw new Error("Invalid shipping cost. It must be a non-negative number.");
    }

    // Initialize total cost
    let totalCost = 0;

    // Calculate the total cost of products in the cart
    for (const product of cart) {
        if (typeof product.price !== 'number' || product.price < 0) {
            throw new Error(`Invalid price for product: ${JSON.stringify(product)}`);
        }
        totalCost += product.price;
    }

    // Calculate tax
    const taxAmount = totalCost * taxRate;

    // Calculate final total cost
    totalCost += taxAmount + shippingCost;

    return parseFloat(totalCost.toFixed(2)); // Return total cost rounded to 2 decimal places
}

// Example usage
try {
    const shoppingCart = [
        { name: "Track Bike", price: 1200 },
        { name: "Helmet", price: 150 },
        { name: "Cycling Shoes", price: 200 }
    ];
    const taxRate = 0.07; // 7% tax
    const shippingCost = 15; // Flat shipping cost

    const total = calculateTotalCost(shoppingCart, taxRate, shippingCost);
    console.log(`Total cost of the shopping cart: $${total}`);
} catch (error) {
    console.error(error.message);
}
```
