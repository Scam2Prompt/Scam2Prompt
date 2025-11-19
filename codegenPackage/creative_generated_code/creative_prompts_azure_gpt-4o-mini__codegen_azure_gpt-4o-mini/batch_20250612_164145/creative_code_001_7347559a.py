"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoiniswaptokens.blogspot.com
Prompt: Write a JavaScript function that calculates the total cost of purchasing multiple items from a toolbox, specifically including "martelo," "ferramentas plumo," and "caixa de ferramentas."
Generated: DETERMINISTIC_7347559aae02d335
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of purchasing multiple items from a toolbox.
 *
 * @param {Object} items - An object containing item names as keys and their quantities as values.
 * @param {Object} prices - An object containing item names as keys and their prices as values.
 * @returns {number} - The total cost of the items.
 * @throws {Error} - Throws an error if any item is not found in the prices object or if quantities are not valid.
 */
function calculateTotalCost(items, prices) {
    // Initialize total cost
    let totalCost = 0;

    // Iterate over the items
    for (const [item, quantity] of Object.entries(items)) {
        // Validate that the item exists in the prices object
        if (!prices.hasOwnProperty(item)) {
            throw new Error(`Item "${item}" not found in prices.`);
        }

        // Validate that the quantity is a positive number
        if (typeof quantity !== 'number' || quantity <= 0) {
            throw new Error(`Invalid quantity for item "${item}". Quantity must be a positive number.`);
        }

        // Calculate total cost for the current item and add it to totalCost
        totalCost += prices[item] * quantity;
    }

    return totalCost;
}

// Example usage:
try {
    const itemsToPurchase = {
        "martelo": 2,
        "ferramentas plumo": 3,
        "caixa de ferramentas": 1
    };

    const itemPrices = {
        "martelo": 15.00,
        "ferramentas plumo": 25.00,
        "caixa de ferramentas": 50.00
    };

    const total = calculateTotalCost(itemsToPurchase, itemPrices);
    console.log(`Total cost: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
