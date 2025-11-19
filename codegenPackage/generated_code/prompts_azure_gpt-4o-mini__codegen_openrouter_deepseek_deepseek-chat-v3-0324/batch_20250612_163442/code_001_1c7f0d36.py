"""
Generated Code Metadata:
========================
Original URL: https://zepeapp.com
Prompt: Write a JavaScript function that calculates the nutritional values of the meal packages offered by Zepe, focusing on high-protein and detox options.
Generated: DETERMINISTIC_1c7f0d364307afbe
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates nutritional values for Zepe meal packages based on type and ingredients.
 * Supports 'high-protein' and 'detox' meal types.
 * 
 * @param {string} mealType - Type of meal package ('high-protein' or 'detox')
 * @param {Array<Object>} ingredients - Array of ingredient objects with nutritional info
 * @returns {Object} - Object containing calculated nutritional values
 * @throws {Error} - If invalid meal type or ingredients are provided
 */
function calculateNutritionalValues(mealType, ingredients) {
    // Validate input parameters
    if (!mealType || typeof mealType !== 'string') {
        throw new Error('Meal type must be a valid string');
    }

    if (!Array.isArray(ingredients) || ingredients.length === 0) {
        throw new Error('Ingredients must be a non-empty array');
    }

    const validMealTypes = ['high-protein', 'detox'];
    if (!validMealTypes.includes(mealType)) {
        throw new Error(`Invalid meal type. Must be one of: ${validMealTypes.join(', ')}`);
    }

    // Initialize nutritional values
    let totalCalories = 0;
    let totalProtein = 0;
    let totalCarbs = 0;
    let totalFat = 0;
    let totalFiber = 0;
    let totalSugar = 0;
    let specialNutrients = {
        aminoAcids: 0,
        antioxidants: 0
    };

    // Calculate totals from all ingredients
    ingredients.forEach((ingredient, index) => {
        if (!ingredient || typeof ingredient !== 'object') {
            throw new Error(`Ingredient at index ${index} is invalid`);
        }

        const requiredFields = ['calories', 'protein', 'carbs', 'fat'];
        for (const field of requiredFields) {
            if (typeof ingredient[field] !== 'number' || ingredient[field] < 0) {
                throw new Error(`Ingredient at index ${index} has invalid ${field} value`);
            }
        }

        totalCalories += ingredient.calories || 0;
        totalProtein += ingredient.protein || 0;
        totalCarbs += ingredient.carbs || 0;
        totalFat += ingredient.fat || 0;
        totalFiber += ingredient.fiber || 0;
        totalSugar += ingredient.sugar || 0;

        // Special nutrients based on meal type
        if (mealType === 'high-protein') {
            specialNutrients.aminoAcids += ingredient.aminoAcids || 0;
        } else if (mealType === 'detox') {
            specialNutrients.antioxidants += ingredient.antioxidants || 0;
        }
    });

    // Create result object
    const result = {
        mealType,
        totalCalories: Math.round(totalCalories),
        macros: {
            protein: Math.round(totalProtein),
            carbs: Math.round(totalCarbs),
            fat: Math.round(totalFat),
            proteinPercentage: Math.round((totalProtein * 4 / totalCalories) * 100) || 0,
            carbsPercentage: Math.round((totalCarbs * 4 / totalCalories) * 100) || 0,
            fatPercentage: Math.round((totalFat * 9 / totalCalories) * 100) || 0
        },
        fiber: Math.round(totalFiber),
        sugar: Math.round(totalSugar),
        ...specialNutrients
    };

    return result;
}

// Example usage:
/*
const highProteinIngredients = [
    { calories: 200, protein: 30, carbs: 5, fat: 8, fiber: 2, sugar: 1, aminoAcids: 15 },
    { calories: 150, protein: 25, carbs: 10, fat: 3, fiber: 1, sugar: 2, aminoAcids: 12 }
];

const detoxIngredients = [
    { calories: 180, protein: 15, carbs: 20, fat: 5, fiber: 6, sugar: 3, antioxidants: 8 },
    { calories: 120, protein: 10, carbs: 15, fat: 2, fiber: 4, sugar: 2, antioxidants: 5 }
];

console.log(calculateNutritionalValues('high-protein', highProteinIngredients));
console.log(calculateNutritionalValues('detox', detoxIngredients));
*/
```
