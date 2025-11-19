"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Create a JavaScript function that calculates the estimated cost of moving services based on the type of items (e.g., small furniture, appliances) and distance within Antalya.
Generated: DETERMINISTIC_43d87a69e74b0bb0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Estimates the cost of moving services based on the type of items and distance.
 * 
 * @param {Array<Object>} items - An array of items to be moved, where each item has a type and quantity.
 * @param {number} distance - The distance in kilometers for the move.
 * @returns {number} The estimated total cost of moving services.
 * @throws {Error} Throws an error if inputs are invalid.
 */
function calculateMovingCost(items, distance) {
    // Validate the input parameters
    if (!Array.isArray(items) || items.length === 0) {
        throw new Error("Items must be a non-empty array.");
    }
    if (typeof distance !== 'number' || distance <= 0) {
        throw new Error("Distance must be a positive number.");
    }

    // Cost per item type in Antalya (example rates)
    const costPerItem = {
        smallFurniture: 50,  // Cost per small furniture item
        largeFurniture: 100,  // Cost per large furniture item
        appliances: 150,      // Cost per appliances
    };

    let totalCost = 0;

    // Calculate the cost based on the items provided
    for (const item of items) {
        if (!item.type || !item.quantity || typeof item.quantity !== 'number' || item.quantity <= 0) {
            throw new Error("Each item must have a type and a positive quantity.");
        }

        const itemCost = costPerItem[item.type];
        if (itemCost === undefined) {
            throw new Error(`Unknown item type: ${item.type}`);
        }

        totalCost += itemCost * item.quantity;
    }

    // Calculate distance cost (e.g., 10% of the total item cost per kilometer)
    const distanceCost = totalCost * 0.1 * distance;

    // Final estimated cost
    const estimatedTotalCost = totalCost + distanceCost;

    return estimatedTotalCost;
}

// Example usage
try {
    const itemsToMove = [
        { type: 'smallFurniture', quantity: 2 },
        { type: 'largeFurniture', quantity: 1 },
        { type: 'appliances', quantity: 3 },
    ];
    const movingDistance = 10; // Distance in kilometers
    const estimatedCost = calculateMovingCost(itemsToMove, movingDistance);
    console.log(`Estimated moving cost: ${estimatedCost} TRY`);
} catch (error) {
    console.error(`Error calculating moving cost: ${error.message}`);
}
```
