"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zepeapp.com
Prompt: Write a JavaScript function that calculates the nutritional values of the meal packages offered by Zepe, focusing on high-protein and detox options.
Generated: DETERMINISTIC_1c7f0d364307afbe
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @description Calculates nutritional values for meal packages offered by Zepe.
 * The function supports high-protein and detox options.
 * @param {Array<Object>} mealPackages - Array of meal package objects. Each object should contain details like name, type, and ingredients.
 * @returns {Array<Object>} - Returns an array of nutritional values for each meal package.
 */
function calculateNutritionalValues(mealPackages) {
  // Helper function to validate and extract nutritional information from ingredients
  const getNutritionalInfo = (ingredients) => {
    if (!Array.isArray(ingredients)) {
      throw new Error('Ingredients must be an array.');
    }

    return ingredients.reduce(
      (totals, ingredient) => {
        // Validate ingredient structure
        if (
          typeof ingredient.name !== 'string' ||
          typeof ingredient.protein !== 'number' ||
          typeof ingredient.carbs !== 'number' ||
          typeof ingredient.fats !== 'number' ||
          typeof ingredient.calories !== 'number'
        ) {
          throw new Error('Invalid ingredient format.');
        }

        // Aggregate nutritional values
        totals.protein += ingredient.protein;
        totals.carbs += ingredient.carbs;
        totals.fats += ingredient.fats;
        totals.calories += ingredient.calories;

        return totals;
      },
      { protein: 0, carbs: 0, fats: 0, calories: 0 }
    );
  };

  // Validate mealPackages input
  if (!Array.isArray(mealPackages)) {
    throw new Error('Meal packages must be an array.');
  }

  return mealPackages.map((package) => {
    const { name, type, ingredients } = package;

    // Validate package structure
    if (
      typeof name !== 'string' ||
      typeof type !== 'string' ||
      !Array.isArray(ingredients)
    ) {
      throw new Error('Invalid meal package format.');
    }

    const nutritionalInfo = getNutritionalInfo(ingredients);

    // Add package-specific adjustments based on type
    switch (type.toLowerCase()) {
      case 'high-protein':
        nutritionalInfo.isHighProtein = nutritionalInfo.protein > 50; // Example threshold for high-protein
        break;
      case 'detox':
        nutritionalInfo.isDetox = nutritionalInfo.calories < 300; // Example threshold for detox
        break;
      default:
        throw new Error(`Unknown package type: ${type}`);
    }

    return {
      name,
      type,
      nutritionalValues: nutritionalInfo,
    };
  });
}

// Example usage:
const mealPackages = [
  {
    name: 'Protein Power',
    type: 'high-protein',
    ingredients: [
      { name: 'Chicken Breast', protein: 43, carbs: 0, fats: 3, calories: 200 },
      { name: 'Egg Whites', protein: 12, carbs: 1, fats: 0, calories: 60 },
    ],
  },
  {
    name: 'Green Detox',
    type: 'detox',
    ingredients: [
      { name: 'Spinach', protein: 3, carbs: 4, fats: 0, calories: 30 },
      { name: 'Cucumber', protein: 1, carbs: 4, fats: 0, calories: 20 },
      { name: 'Lemon Juice', protein: 0, carbs: 2, fats: 0, calories: 10 },
    ],
  },
];

console.log(calculateNutritionalValues(mealPackages));
```
