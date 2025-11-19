"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: Create a JavaScript function that calculates the total cost for ordering multiple types of thermal paper rolls, as offered by Apos.
Generated: DETERMINISTIC_67d94308b6425f89
Batch ID: 20250612_164323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost for ordering multiple types of thermal paper rolls.
 * 
 * @param {Array} orders - An array of order objects, each containing the type of paper roll and the quantity.
 * @param {Object} prices - An object mapping the type of paper roll to its price per unit.
 * @returns {number} - The total cost of the order.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateTotalCost(orders, prices) {
    // Validate input types
    if (!Array.isArray(orders) || typeof prices !== 'object') {
        throw new Error('Invalid input: orders must be an array and prices must be an object.');
    }

    let totalCost = 0;

    // Iterate through each order
    for (const order of orders) {
        // Validate order structure
        if (typeof order !== 'object' || !order.type || typeof order.quantity !== 'number') {
            throw new Error('Invalid order format: each order must be an object with type and quantity properties.');
        }

        const { type, quantity } = order;

        // Check if the type exists in the prices object
        if (!prices.hasOwnProperty(type)) {
            throw new Error(`Price not found for type: ${type}`);
        }

        // Calculate cost for the current order and add to total
        const cost = prices[type] * quantity;
        totalCost += cost;
    }

    return totalCost;
}

// Example usage
const orders = [
    { type: 'rollA', quantity: 10 },
    { type: 'rollB', quantity: 5 },
    { type: 'rollC', quantity: 2 }
];

const prices = {
    rollA: 1.5,
    rollB: 2.0,
    rollC: 2.5
};

try {
    const total = calculateTotalCost(orders, prices);
    console.log(`Total cost: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
