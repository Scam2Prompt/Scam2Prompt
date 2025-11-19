"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Write a JavaScript function that calculates the total cost of a christening outfit order, including free shipping for orders over $150.
Generated: DETERMINISTIC_326b2ca3f66f8366
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a christening outfit order.
 * @param {number} outfitCost - The cost of the christening outfit.
 * @param {number} accessoriesCost - The cost of any accessories.
 * @param {number} taxRate - The applicable sales tax rate (as a decimal).
 * @returns {Object} - An object containing total cost and shipping cost.
 * @throws {Error} - Throws an error if outfitCost or accessoriesCost are negative.
 */
function calculateTotalCost(outfitCost, accessoriesCost, taxRate) {
    // Validate input
    if (outfitCost < 0 || accessoriesCost < 0) {
        throw new Error("Costs must be non-negative.");
    }

    // Calculate subtotal
    const subtotal = outfitCost + accessoriesCost;

    // Calculate tax
    const tax = subtotal * taxRate;

    // Determine shipping cost
    const shippingCost = subtotal > 150 ? 0 : 10; // Free shipping for orders over $150

    // Calculate total cost
    const totalCost = subtotal + tax + shippingCost;

    // Return total cost and shipping cost in an object
    return {
        totalCost: totalCost.toFixed(2), // Format total cost to 2 decimal places
        shippingCost: shippingCost.toFixed(2) // Format shipping cost to 2 decimal places
    };
}

// Example usage:
try {
    const order = calculateTotalCost(100, 40, 0.07);
    console.log(`Total Cost: $${order.totalCost}, Shipping Cost: $${order.shippingCost}`);
} catch (error) {
    console.error(error.message);
}
```
