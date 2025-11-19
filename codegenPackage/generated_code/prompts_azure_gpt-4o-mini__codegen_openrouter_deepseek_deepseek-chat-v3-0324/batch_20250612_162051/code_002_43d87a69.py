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
 * Calculates the estimated cost of moving services in Antalya based on item types and distance.
 * @param {Object[]} items - Array of items to be moved, each with type and quantity.
 * @param {number} distance - Distance in kilometers within Antalya.
 * @returns {number} The total estimated cost in TRY.
 * @throws {Error} If invalid input is provided.
 */
function calculateMovingCost(items, distance) {
    // Validate input
    if (!Array.isArray(items) || typeof distance !== 'number' || distance <= 0) {
        throw new Error('Invalid input: items must be an array and distance must be a positive number');
    }

    // Define price per item type (in TRY)
    const itemPrices = {
        'small_furniture': 50,   // Chairs, small tables, etc.
        'medium_furniture': 100, // Coffee tables, bookshelves, etc.
        'large_furniture': 200,  // Sofas, beds, etc.
        'appliance': 150,        // Refrigerators, washing machines, etc.
        'box': 20,               // Standard moving boxes
        'fragile': 75            // Glass items, electronics, etc.
    };

    // Base price per kilometer (in TRY)
    const pricePerKm = 5;

    let totalItemCost = 0;

    try {
        // Calculate cost for each item
        items.forEach(item => {
            if (!item.type || !item.quantity || typeof item.quantity !== 'number' || item.quantity <= 0) {
                throw new Error('Invalid item: must have type and positive quantity');
            }

            const itemPrice = itemPrices[item.type];
            if (itemPrice === undefined) {
                throw new Error(`Unknown item type: ${item.type}`);
            }

            totalItemCost += itemPrice * item.quantity;
        });

        // Calculate distance cost
        const distanceCost = distance * pricePerKm;

        // Total cost with minimum charge of 200 TRY
        const totalCost = Math.max(200, totalItemCost + distanceCost);

        return totalCost;
    } catch (error) {
        throw new Error(`Failed to calculate moving cost: ${error.message}`);
    }
}

// Example usage:
// const items = [
//     { type: 'large_furniture', quantity: 1 },
//     { type: 'appliance', quantity: 2 },
//     { type: 'box', quantity: 5 }
// ];
// const distance = 15;
// console.log(calculateMovingCost(items, distance));
```
