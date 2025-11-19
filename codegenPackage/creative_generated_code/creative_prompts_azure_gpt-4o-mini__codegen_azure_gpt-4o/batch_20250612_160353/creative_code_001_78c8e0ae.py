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
 * Function to calculate the total cost of ingredients for a pastry recipe.
 * 
 * @param {Array} ingredients - An array of ingredient objects. Each object should have:
 *                              - `name` (string): Name of the ingredient.
 *                              - `quantity` (number): Quantity required in grams.
 *                              - `costPerGram` (number): Cost of the ingredient per gram.
 * @returns {number} - The total cost of the ingredients, rounded to two decimal places.
 * 
 * Example:
 * const ingredients = [
 *   { name: 'Flour', quantity: 500, costPerGram: 0.02 },
 *   { name: 'Sugar', quantity: 200, costPerGram: 0.03 },
 *   { name: 'Butter', quantity: 250, costPerGram: 0.05 }
 * ];
 * const totalCost = calculateRecipeCost(ingredients);
 * console.log(totalCost); // Output: 22.50
 */
function calculateRecipeCost(ingredients) {
  // Validate the input
  if (!Array.isArray(ingredients)) {
    throw new Error('Invalid input: ingredients must be an array.');
  }

  // Initialize the total cost
  let totalCost = 0;

  // Iterate through the ingredients to calculate the total cost
  for (const ingredient of ingredients) {
    // Validate the structure of each ingredient object
    if (
      typeof ingredient.name !== 'string' ||
      typeof ingredient.quantity !== 'number' ||
      typeof ingredient.costPerGram !== 'number'
    ) {
      throw new Error(`Invalid ingredient object: ${JSON.stringify(ingredient)}`);
    }

    // Calculate the cost for the current ingredient
    const ingredientCost = ingredient.quantity * ingredient.costPerGram;

    // Add the ingredient's cost to the total cost
    totalCost += ingredientCost;
  }

  // Return the total cost rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
const ingredients = [
  { name: 'Flour', quantity: 500, costPerGram: 0.02 },
  { name: 'Sugar', quantity: 200, costPerGram: 0.03 },
  { name: 'Butter', quantity: 250, costPerGram: 0.05 }
];

try {
  const totalCost = calculateRecipeCost(ingredients);
  console.log(`Total cost of ingredients: $${totalCost}`);
} catch (error) {
  console.error(`Error calculating recipe cost: ${error.message}`);
}
```
