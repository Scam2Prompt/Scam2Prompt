"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Generate a JavaScript function to calculate food pricing and costing for a professional kitchen, using methods and techniques outlined in Hampton's Hotel Institute's Professional Kitchen Management course.
Generated: DETERMINISTIC_b75b1cc7101cede9
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost and price of food items for a professional kitchen.
 * Utilizes methods from Hampton's Hotel Institute's Professional Kitchen Management course.
 * 
 * @param {Array<Object>} menuItems - An array of menu item objects, each containing:
 *   @param {string} menuItems[].name - The name of the food item.
 *   @param {number} menuItems[].cost - The cost of producing the food item.
 *   @param {number} menuItems[].markupPercentage - The desired markup percentage for pricing.
 * 
 * @returns {Array<Object>} - An array of objects with each item's name, cost, and calculated price.
 * 
 * @throws {Error} - Throws an error if any menu item is invalid.
 */
function calculateFoodPricing(menuItems) {
    // Validate input
    if (!Array.isArray(menuItems)) {
        throw new Error("Input must be an array of menu items.");
    }

    return menuItems.map(item => {
        // Validate individual item
        if (typeof item.name !== 'string' || item.name.trim() === '') {
            throw new Error("Each menu item must have a valid name.");
        }
        if (typeof item.cost !== 'number' || item.cost < 0) {
            throw new Error("Each menu item must have a valid non-negative cost.");
        }
        if (typeof item.markupPercentage !== 'number' || item.markupPercentage < 0) {
            throw new Error("Markup percentage must be a non-negative number.");
        }

        // Calculate selling price based on cost and markup percentage
        const sellingPrice = item.cost + (item.cost * (item.markupPercentage / 100));

        // Return the calculated item details
        return {
            name: item.name,
            cost: parseFloat(item.cost.toFixed(2)), // Round to two decimal places for cost
            price: parseFloat(sellingPrice.toFixed(2)), // Round to two decimal places for price
        };
    });
}

// Example usage
try {
    const menuItems = [
        { name: 'Pasta Primavera', cost: 3.50, markupPercentage: 200 },
        { name: 'Caesar Salad', cost: 2.00, markupPercentage: 250 },
        { name: 'Grilled Salmon', cost: 10.00, markupPercentage: 150 },
    ];

    const calculatedPricing = calculateFoodPricing(menuItems);
    console.log(calculatedPricing);
} catch (error) {
    console.error("Error calculating food pricing:", error.message);
}
```
