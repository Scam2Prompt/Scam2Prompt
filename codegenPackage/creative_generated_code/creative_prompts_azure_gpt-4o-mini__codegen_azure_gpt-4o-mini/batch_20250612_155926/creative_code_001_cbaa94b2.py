"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Write a JavaScript function that calculates the total cost of an order from EcoSwap, including taxes and shipping based on user input.
Generated: DETERMINISTIC_cbaa94b2aa66c310
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
 * Calculates the total cost of an order including item cost, tax, and shipping.
 * 
 * @param {number} itemCost - The cost of the items in the order.
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.07 for 7%).
 * @param {number} shippingCost - The cost of shipping.
 * @returns {number} The total cost of the order.
 * @throws {Error} Throws an error if any of the parameters are negative or not numbers.
 */
function calculateTotalCost(itemCost, taxRate, shippingCost) {
    // Validate input parameters
    if (typeof itemCost !== 'number' || typeof taxRate !== 'number' || typeof shippingCost !== 'number') {
        throw new Error('All parameters must be numbers.');
    }
    if (itemCost < 0 || taxRate < 0 || shippingCost < 0) {
        throw new Error('Parameters must not be negative.');
    }

    // Calculate tax amount
    const taxAmount = itemCost * taxRate;

    // Calculate total cost
    const totalCost = itemCost + taxAmount + shippingCost;

    // Return the total cost, rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
    const orderTotal = calculateTotalCost(100, 0.07, 5);
    console.log(`Total order cost: $${orderTotal}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
