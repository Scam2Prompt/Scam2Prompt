"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Create a JavaScript function that calculates the total cost of various building closures, including garage doors and gates, based on user-selected options.
Generated: DETERMINISTIC_4f853c30d3093eb9
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of building closures based on user-selected options.
 * @param {Object[]} items - Array of selected items, where each item is an object containing type, quantity, and unit_price.
 * @returns {number} - Total cost of all selected items.
 */
function calculateTotalCost(items) {
    // Input validation: Ensure items is an array
    if (!Array.isArray(items)) {
        throw new Error("Invalid input: 'items' must be an array.");
    }

    // Initialize total cost
    let totalCost = 0;

    // Loop through each item and calculate the total cost
    for (const item of items) {
        // Validate item structure
        if (
            typeof item.type !== "string" ||
            typeof item.quantity !== "number" ||
            typeof item.unit_price !== "number"
        ) {
            throw new Error("Invalid item structure: Each item must contain 'type', 'quantity', and 'unit_price'.");
        }

        // Ensure quantity and unit_price are non-negative
        if (item.quantity < 0 || item.unit_price < 0) {
            throw new Error("Invalid values: 'quantity' and 'unit_price' must be non-negative.");
        }

        // Calculate cost for the current item and add to total cost
        totalCost += item.quantity * item.unit_price;
    }

    // Return the calculated total cost
    return totalCost;
}

// Example usage:
try {
    const selectedItems = [
        { type: 'Garage Door', quantity: 2, unit_price: 300 },
        { type: 'Gate', quantity: 1, unit_price: 500 },
    ];
    const totalCost = calculateTotalCost(selectedItems);
    console.log(`Total cost of building closures: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
