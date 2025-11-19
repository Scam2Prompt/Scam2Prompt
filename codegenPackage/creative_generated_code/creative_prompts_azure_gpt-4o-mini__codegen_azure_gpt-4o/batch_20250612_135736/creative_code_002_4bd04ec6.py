"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soulart.hu
Prompt: Write a function in JavaScript that calculates the nutritional value of a Mediterranean meal based on the guidelines provided in the Soulart Blog.
Generated: DETERMINISTIC_4bd04ec65609626d
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the nutritional value of a Mediterranean meal.
 * @param {Object} ingredients - An array of objects representing the ingredients.
 * Each ingredient should have the following properties:
 * - name {string}: Name of the ingredient.
 * - weight {number}: Weight of the ingredient in grams.
 * - nutrients {Object}: Nutritional values per 100 grams of ingredient.
 *    - calories {number}: Calories (kcal).
 *    - protein {number}: Protein (g).
 *    - carbs {number}: Carbohydrates (g).
 *    - fats {number}: Fats (g).
 * @returns {Object} An object containing the total nutritional values of the meal:
 * - totalCalories {number}: Total calories (kcal).
 * - totalProtein {number}: Total protein (g).
 * - totalCarbs {number}: Total carbohydrates (g).
 * - totalFats {number}: Total fats (g).
 */
function calculateMealNutrition(ingredients) {
  // Validate input
  if (!Array.isArray(ingredients)) {
    throw new Error('Invalid input: ingredients must be an array of objects.');
  }

  // Initialize totals
  let totalCalories = 0;
  let totalProtein = 0;
  let totalCarbs = 0;
  let totalFats = 0;

  // Iterate over each ingredient
  for (const ingredient of ingredients) {
    // Validate ingredient properties
    if (
      !ingredient.name ||
      typeof ingredient.weight !== 'number' ||
      !ingredient.nutrients ||
      typeof ingredient.nutrients.calories !== 'number' ||
      typeof ingredient.nutrients.protein !== 'number' ||
      typeof ingredient.nutrients.carbs !== 'number' ||
      typeof ingredient.nutrients.fats !== 'number'
    ) {
      throw new Error(
        `Invalid ingredient: each ingredient must have a valid name, weight, and nutrients object.`
      );
    }

    // Calculate nutritional values based on weight
    const weightFactor = ingredient.weight / 100;
    totalCalories += ingredient.nutrients.calories * weightFactor;
    totalProtein += ingredient.nutrients.protein * weightFactor;
    totalCarbs += ingredient.nutrients.carbs * weightFactor;
    totalFats += ingredient.nutrients.fats * weightFactor;
  }

  // Return the total nutritional values rounded to two decimal places
  return {
    totalCalories: parseFloat(totalCalories.toFixed(2)),
    totalProtein: parseFloat(totalProtein.toFixed(2)),
    totalCarbs: parseFloat(totalCarbs.toFixed(2)),
    totalFats: parseFloat(totalFats.toFixed(2)),
  };
}

// Example usage:
const mediterraneanMeal = [
  {
    name: 'Olive Oil',
    weight: 20,
    nutrients: {
      calories: 884,
      protein: 0,
      carbs: 0,
      fats: 100,
    },
  },
  {
    name: 'Tomatoes',
    weight: 150,
    nutrients: {
      calories: 18,
      protein: 0.9,
      carbs: 3.9,
      fats: 0.2,
    },
  },
  {
    name: 'Grilled Chicken',
    weight: 200,
    nutrients: {
      calories: 165,
      protein: 31,
      carbs: 0,
      fats: 3.6,
    },
  },
];

try {
  const nutritionalValues = calculateMealNutrition(mediterraneanMeal);
  console.log('Nutritional Values:', nutritionalValues);
} catch (error) {
  console.error('Error:', error.message);
}
```
