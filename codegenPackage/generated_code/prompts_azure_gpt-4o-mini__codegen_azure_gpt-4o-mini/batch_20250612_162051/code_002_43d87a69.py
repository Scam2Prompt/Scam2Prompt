"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Create a JavaScript function that calculates the estimated cost of moving services based on the type of items (e.g., small furniture, appliances) and distance within Antalya.
Generated: DETERMINISTIC_43d87a69e74b0bb0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost of moving services based on the type of items and distance.
 * 
 * @param {Array} items - An array of objects representing the items to be moved.
 * @param {number} distance - The distance in kilometers for the move.
 * @returns {number} - The estimated cost of the moving services.
 * @throws {Error} - Throws an error if the distance is negative or if items are not provided.
 */
function calculateMovingCost(items, distance) {
    // Validate input parameters
    if (!Array.isArray(items) || items.length === 0) {
        throw new Error("Items must be a non-empty array.");
    }
    if (typeof distance !== 'number' || distance < 0) {
        throw new Error("Distance must be a non-negative number.");
    }

    // Define cost per item type (in local currency)
    const costPerItem = {
        smallFurniture: 50, // Cost for small furniture
        largeFurniture: 100, // Cost for large furniture
        appliances: 150, // Cost for appliances
        boxes: 20 // Cost per box
    };

    // Initialize total cost
    let totalCost = 0;

    // Calculate total cost based on items
    for (const item of items) {
        const { type, quantity } = item;

        // Check if the item type is valid
        if (!costPerItem[type]) {
            throw new Error(`Invalid item type: ${type}`);
        }

        // Add to total cost
        totalCost += costPerItem[type] * quantity;
    }

    // Calculate distance cost (e.g., $1 per km)
    const distanceCost = distance * 1;

    // Return the total estimated cost
    return totalCost + distanceCost;
}

// Example usage
try {
    const itemsToMove = [
        { type: 'smallFurniture', quantity: 2 },
        { type: 'largeFurniture', quantity: 1 },
        { type: 'appliances', quantity: 1 },
        { type: 'boxes', quantity: 5 }
    ];
    const distanceToMove = 10; // Distance in kilometers

    const estimatedCost = calculateMovingCost(itemsToMove, distanceToMove);
    console.log(`Estimated moving cost: ${estimatedCost} currency units`);
} catch (error) {
    console.error(`Error calculating moving cost: ${error.message}`);
}
```
