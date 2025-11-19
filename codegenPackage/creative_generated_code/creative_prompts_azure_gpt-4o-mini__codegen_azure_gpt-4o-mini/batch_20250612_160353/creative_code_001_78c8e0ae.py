"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Write a JavaScript function that calculates the cost of ingredients for a pastry recipe, similar to what students might learn in the Pastelería y Panificación program at Egatur.
Generated: DETERMINISTIC_78c8e0ae13e3ba5f
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of ingredients for a pastry recipe.
 * 
 * @param {Object} ingredients - An object where the keys are ingredient names 
 *                                and the values are objects containing the `quantity`
 *                                and `pricePerUnit` for each ingredient.
 * @returns {number} - The total cost of the ingredients.
 * @throws {Error} - Throws an error if the input is not valid.
 */
function calculateIngredientCost(ingredients) {
    // Validate input
    if (typeof ingredients !== 'object' || ingredients === null) {
        throw new Error('Invalid input: ingredients must be a non-null object');
    }

    let totalCost = 0;

    // Iterate through each ingredient to calculate the total cost
    for (const [ingredient, details] of Object.entries(ingredients)) {
        // Validate the structure of each ingredient's details
        if (typeof details.quantity !== 'number' || typeof details.pricePerUnit !== 'number') {
            throw new Error(`Invalid details for ingredient '${ingredient}': quantity and pricePerUnit must be numbers`);
        }
        if (details.quantity < 0 || details.pricePerUnit < 0) {
            throw new Error(`Invalid values for ingredient '${ingredient}': quantity and pricePerUnit must be non-negative`);
        }

        // Calculate the cost for the current ingredient
        const ingredientCost = details.quantity * details.pricePerUnit;
        totalCost += ingredientCost; // Accumulate the total cost
    }

    return totalCost; // Return the total cost of all ingredients
}

// Example usage:
try {
    const ingredients = {
        flour: { quantity: 2, pricePerUnit: 1.5 }, // 2 kg of flour at $1.5 per kg
        sugar: { quantity: 1, pricePerUnit: 2.0 }, // 1 kg of sugar at $2.0 per kg
        butter: { quantity: 0.5, pricePerUnit: 3.0 } // 0.5 kg of butter at $3.0 per kg
    };

    const totalCost = calculateIngredientCost(ingredients);
    console.log(`Total cost of ingredients: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message); // Handle and log errors
}
```
