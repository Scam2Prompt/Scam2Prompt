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
 * 
 * @param {Object} ingredients - An object where keys are ingredient names and values are objects containing 'quantity' and 'pricePerUnit'.
 * @returns {number} - The total cost of the ingredients.
 * @throws {Error} - Throws an error if the input is not valid.
 */
function calculateIngredientCost(ingredients) {
    // Validate input
    if (typeof ingredients !== 'object' || ingredients === null) {
        throw new Error('Invalid input: ingredients must be an object.');
    }

    let totalCost = 0;

    // Iterate over each ingredient to calculate total cost
    for (const [ingredient, details] of Object.entries(ingredients)) {
        // Validate ingredient details
        if (typeof details !== 'object' || details === null) {
            throw new Error(`Invalid details for ingredient "${ingredient}": must be an object.`);
        }
        const { quantity, pricePerUnit } = details;

        // Validate quantity and pricePerUnit
        if (typeof quantity !== 'number' || quantity < 0) {
            throw new Error(`Invalid quantity for ingredient "${ingredient}": must be a non-negative number.`);
        }
        if (typeof pricePerUnit !== 'number' || pricePerUnit < 0) {
            throw new Error(`Invalid price per unit for ingredient "${ingredient}": must be a non-negative number.`);
        }

        // Calculate cost for the current ingredient
        totalCost += quantity * pricePerUnit;
    }

    return totalCost;
}

// Example usage:
try {
    const ingredients = {
        flour: { quantity: 2, pricePerUnit: 1.5 },
        sugar: { quantity: 1, pricePerUnit: 0.8 },
        butter: { quantity: 0.5, pricePerUnit: 3.0 }
    };

    const totalCost = calculateIngredientCost(ingredients);
    console.log(`Total cost of ingredients: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
