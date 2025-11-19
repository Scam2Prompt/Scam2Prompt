"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Write a JavaScript function that calculates the cost of ingredients for a pastry recipe, similar to what students might learn in the Pastelería y Panificación program at Egatur.
Generated: DETERMINISTIC_78c8e0ae13e3ba5f
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of ingredients for a pastry recipe.
 * @param {Object} ingredients - An object where keys are ingredient names and values are objects with 'quantity' and 'unitPrice' properties.
 * @param {number} servings - Number of servings the recipe yields.
 * @param {number} desiredServings - Desired number of servings to calculate for.
 * @returns {Object} An object containing the total cost and detailed cost breakdown.
 * @throws {Error} If inputs are invalid or missing required properties.
 */
function calculatePastryCost(ingredients, servings, desiredServings) {
    // Validate inputs
    if (!ingredients || typeof ingredients !== 'object' || Object.keys(ingredients).length === 0) {
        throw new Error('Ingredients must be a non-empty object');
    }
    if (typeof servings !== 'number' || servings <= 0) {
        throw new Error('Servings must be a positive number');
    }
    if (typeof desiredServings !== 'number' || desiredServings <= 0) {
        throw new Error('Desired servings must be a positive number');
    }

    // Calculate scaling factor
    const scalingFactor = desiredServings / servings;

    // Calculate costs
    let totalCost = 0;
    const costBreakdown = {};

    for (const [ingredient, details] of Object.entries(ingredients)) {
        // Validate ingredient details
        if (typeof details !== 'object' || 
            typeof details.quantity !== 'number' || 
            typeof details.unitPrice !== 'number') {
            throw new Error(`Invalid details for ingredient: ${ingredient}`);
        }

        if (details.quantity < 0 || details.unitPrice < 0) {
            throw new Error(`Quantity and unit price must be non-negative for ingredient: ${ingredient}`);
        }

        // Calculate scaled quantity and cost
        const scaledQuantity = details.quantity * scalingFactor;
        const ingredientCost = scaledQuantity * details.unitPrice;
        
        // Add to totals
        totalCost += ingredientCost;
        costBreakdown[ingredient] = {
            quantity: scaledQuantity,
            unitPrice: details.unitPrice,
            cost: parseFloat(ingredientCost.toFixed(2))
        };
    }

    return {
        totalCost: parseFloat(totalCost.toFixed(2)),
        costBreakdown,
        scalingFactor,
        originalServings: servings,
        desiredServings
    };
}

// Example usage:
/*
const ingredients = {
    flour: { quantity: 500, unitPrice: 0.02 }, // 500g at $0.02 per gram
    sugar: { quantity: 200, unitPrice: 0.03 },
    eggs: { quantity: 4, unitPrice: 0.25 },
    butter: { quantity: 250, unitPrice: 0.05 }
};

const result = calculatePastryCost(ingredients, 12, 24);
console.log(result);
*/
```
