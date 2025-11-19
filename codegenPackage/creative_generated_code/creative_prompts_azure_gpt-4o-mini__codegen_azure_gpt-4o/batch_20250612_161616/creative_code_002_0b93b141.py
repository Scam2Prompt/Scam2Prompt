"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushipanda.es
Prompt: Create a JavaScript function that calculates the total cost of a sushi combo order from SushiPanda, including 2x1 offers.
Generated: DETERMINISTIC_0b93b141aa246c8c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a sushi combo order from SushiPanda, including 2x1 offers.
 * 
 * @param {Array<Object>} order - Array of sushi combo objects, each containing:
 *   - name {string}: Name of the sushi combo
 *   - price {number}: Price of the sushi combo
 *   - quantity {number}: Quantity of the sushi combo ordered
 * @returns {number} - Total cost of the order factoring in 2x1 offers
 * @throws {Error} - Throws an error if the input is invalid
 */
function calculateSushiOrderTotal(order) {
    // Validate input
    if (!Array.isArray(order)) {
        throw new Error("Invalid input: Expected an array of order objects");
    }

    let totalCost = 0;

    for (const item of order) {
        // Validate each item
        if (
            typeof item.name !== 'string' ||
            typeof item.price !== 'number' ||
            typeof item.quantity !== 'number' ||
            item.price < 0 || item.quantity < 0
        ) {
            throw new Error("Invalid order item: Ensure each item has a valid name, price, and quantity");
        }

        // Apply 2x1 offer: Only charge for half the quantity (round down if odd)
        const chargeableQuantity = Math.floor(item.quantity / 2) + (item.quantity % 2);

        // Calculate total for this item
        totalCost += chargeableQuantity * item.price;
    }

    return totalCost;
}

// Example usage:
// const order = [
//     { name: "Salmon Roll Combo", price: 12.99, quantity: 3 },
//     { name: "Tuna Roll Combo", price: 14.49, quantity: 2 },
//     { name: "Vegetarian Roll Combo", price: 10.99, quantity: 5 }
// ];
// console.log(calculateSushiOrderTotal(order)); // Output: Total cost factoring in 2x1 offers
```
