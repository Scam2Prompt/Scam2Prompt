"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Create a JavaScript function that calculates the total cost of various building closures, including garage doors and gates, based on user-selected options.
Generated: DETERMINISTIC_4f853c30d3093eb9
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the total cost of building closures (garage doors and gates)
 * based on user-selected options.
 * 
 * @param {Array} closures - Array of closure objects selected by the user.
 * Each object should have the following properties:
 *   - type {string}: Type of closure ('garageDoor' or 'gate').
 *   - quantity {number}: Number of closures of this type.
 *   - unitPrice {number}: Price per unit of the closure.
 * 
 * @returns {number} - The total cost of all closures.
 * Throws an error if input is invalid.
 */
function calculateTotalCost(closures) {
    // Validate input
    if (!Array.isArray(closures)) {
        throw new Error("Invalid input: closures must be an array.");
    }

    let totalCost = 0;

    closures.forEach((closure) => {
        // Validate closure object structure
        if (
            typeof closure !== 'object' ||
            !closure.type ||
            !['garageDoor', 'gate'].includes(closure.type) ||
            typeof closure.quantity !== 'number' ||
            closure.quantity < 0 ||
            typeof closure.unitPrice !== 'number' ||
            closure.unitPrice < 0
        ) {
            throw new Error("Invalid closure object structure.");
        }

        // Calculate cost for the current closure type
        const closureCost = closure.quantity * closure.unitPrice;
        totalCost += closureCost;
    });

    return totalCost;
}

// Example usage:
try {
    const userSelectedClosures = [
        { type: 'garageDoor', quantity: 2, unitPrice: 500 },
        { type: 'gate', quantity: 1, unitPrice: 300 }
    ];
    const total = calculateTotalCost(userSelectedClosures);
    console.log(`Total cost: $${total}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
