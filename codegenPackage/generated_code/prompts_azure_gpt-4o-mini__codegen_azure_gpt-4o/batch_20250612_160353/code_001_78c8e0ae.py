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
 * Function to calculate the total cost of ingredients for a pastry recipe.
 * 
 * @param {Array} ingredients - An array of ingredient objects. Each object should have:
 *   - name {string}: The name of the ingredient.
 *   - quantity {number}: The quantity of the ingredient required (in grams, liters, etc.).
 *   - unitCost {number}: The cost per unit (e.g., per gram, per liter, etc.).
 * @returns {number} - The total cost of all ingredients.
 * 
 * Example usage:
 * const ingredients = [
 *   { name: "Flour", quantity: 500, unitCost: 0.02 },
 *   { name: "Sugar", quantity: 200, unitCost: 0.03 },
 *   { name: "Butter", quantity: 250, unitCost: 0.05 }
 * ];
 * const totalCost = calculateIngredientCost(ingredients);
 * console.log(`Total cost: $${totalCost.toFixed(2)}`);
 */

function calculateIngredientCost(ingredients) {
  // Validate input
  if (!Array.isArray(ingredients)) {
    throw new Error("Invalid input: ingredients must be an array.");
  }

  let totalCost = 0;

  for (const ingredient of ingredients) {
    // Validate each ingredient object
    if (
      typeof ingredient.name !== "string" ||
      typeof ingredient.quantity !== "number" ||
      typeof ingredient.unitCost !== "number"
    ) {
      throw new Error(
        `Invalid ingredient format: ${JSON.stringify(ingredient)}`
      );
    }

    // Calculate cost for the current ingredient
    const ingredientCost = ingredient.quantity * ingredient.unitCost;

    // Add to total cost
    totalCost += ingredientCost;
  }

  return totalCost;
}

// Example usage
const ingredients = [
  { name: "Flour", quantity: 500, unitCost: 0.02 },
  { name: "Sugar", quantity: 200, unitCost: 0.03 },
  { name: "Butter", quantity: 250, unitCost: 0.05 }
];

try {
  const totalCost = calculateIngredientCost(ingredients);
  console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error(`Error calculating ingredient cost: ${error.message}`);
}
```
