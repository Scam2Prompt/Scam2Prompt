"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Create a JavaScript function to calculate nutritional information for dishes offered by Perfect Food Corner, ensuring freshness and quality of ingredients.
Generated: DETERMINISTIC_2db2e285f1917240
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates nutritional information for dishes offered by Perfect Food Corner.
 * 
 * @param {Object} ingredients - Object containing ingredients with their quantities and units.
 * @param {Object} nutritionData - Object containing nutritional data for each ingredient per unit.
 * @returns {Object} - Object containing calculated nutritional information for the dish.
 */
function calculateNutrition(ingredients, nutritionData) {
    // Initialize object to store total nutritional information
    let totalNutrition = {
        calories: 0,
        protein: 0,
        fat: 0,
        carbohydrates: 0,
    };

    // Iterate over each ingredient
    for (let ingredient in ingredients) {
        if (ingredients.hasOwnProperty(ingredient)) {
            let quantity = ingredients[ingredient].quantity;
            let unit = ingredients[ingredient].unit;

            // Check if ingredient exists in nutrition data
            if (nutritionData[ingredient] && nutritionData[ingredient][unit]) {
                let nutritionInfo = nutritionData[ingredient][unit];

                // Calculate total nutritional information
                totalNutrition.calories += nutritionInfo.calories * quantity;
                totalNutrition.protein += nutritionInfo.protein * quantity;
                totalNutrition.fat += nutritionInfo.fat * quantity;
                totalNutrition.carbohydrates += nutritionInfo.carbohydrates * quantity;
            } else {
                // Throw error if ingredient or unit not found in nutrition data
                throw new Error(`Nutrition data not found for ${ingredient} (${unit})`);
            }
        }
    }

    return totalNutrition;
}

// Example usage:
let ingredients = {
    chicken: { quantity: 2, unit: 'kg' },
    rice: { quantity: 1, unit: 'cup' },
    vegetables: { quantity: 3, unit: 'cup' },
};

let nutritionData = {
    chicken: {
        'kg': { calories: 1650, protein: 200, fat: 30, carbohydrates: 0 },
    },
    rice: {
        'cup': { calories: 200, protein: 4, fat: 2, carbohydrates: 45 },
    },
    vegetables: {
        'cup': { calories: 50, protein: 2, fat: 0, carbohydrates: 10 },
    },
};

try {
    let nutritionInfo = calculateNutrition(ingredients, nutritionData);
    console.log('Nutritional Information:');
    console.log(`Calories: ${nutritionInfo.calories} kcal`);
    console.log(`Protein: ${nutritionInfo.protein} g`);
    console.log(`Fat: ${nutritionInfo.fat} g`);
    console.log(`Carbohydrates: ${nutritionInfo.carbohydrates} g`);
} catch (error) {
    console.error(error.message);
}
```
