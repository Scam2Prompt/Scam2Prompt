"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Create a JavaScript function that calculates the total cost for ordering multiple types of thermal paper rolls, as offered by Apos.
Generated: DETERMINISTIC_67d94308b6425f89
Batch ID: 20250612_164323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of ordering multiple types of thermal paper rolls.
 * 
 * @param {Array<Object>} orders - An array of order objects, each containing:
 *    - {string} type - The type of thermal paper.
 *    - {number} quantity - The quantity ordered.
 *    - {number} pricePerRoll - The price per roll of the specified type.
 * @returns {number} - The total cost of the order.
 * @throws {Error} - Throws an error if any order is invalid (e.g., negative quantities or prices).
 */
function calculateTotalCost(orders) {
    // Validate input
    if (!Array.isArray(orders)) {
        throw new Error("Orders must be an array.");
    }
    
    let totalCost = 0;

    // Iterate through each order to calculate total cost
    orders.forEach(order => {
        // Validate each order object
        if (typeof order.type !== 'string' || order.type.trim() === '') {
            throw new Error("Order type must be a non-empty string.");
        }

        if (typeof order.quantity !== 'number' || order.quantity < 0) {
            throw new Error("Order quantity must be a non-negative number.");
        }

        if (typeof order.pricePerRoll !== 'number' || order.pricePerRoll < 0) {
            throw new Error("Price per roll must be a non-negative number.");
        }

        // Calculate cost for the current order and add to total
        totalCost += order.quantity * order.pricePerRoll;
    });

    return totalCost;
}

// Example usage:
const orders = [
    { type: '50mm Roll', quantity: 10, pricePerRoll: 2.5 },
    { type: '80mm Roll', quantity: 5, pricePerRoll: 3.0 }
];

try {
    const total = calculateTotalCost(orders);
    console.log(`Total cost: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
