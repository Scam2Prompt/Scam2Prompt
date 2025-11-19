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
 * Calculates the nutritional values for meal packages offered by Zepe.
 * @class
 */
class MealPackage {
    /**
     * Constructs a MealPackage instance.
     * @param {string} name - The name of the meal package.
     * @param {number} protein - The amount of protein in grams.
     * @param {number} calories - The total calorie count.
     * @param {number} carbs - The amount of carbohydrates in grams.
     * @param {number} fats - The amount of fats in grams.
     */
    constructor(name, protein, calories, carbs, fats) {
        this.name = name;
        this.protein = protein;
        this.calories = calories;
        this.carbs = carbs;
        this.fats = fats;
    }

    /**
     * Returns a summary of the meal package's nutritional values.
     * @returns {string} A summary string.
     */
    getNutritionalSummary() {
        return `Meal Package: ${this.name}\n` +
               `Protein: ${this.protein}g\n` +
               `Calories: ${this.calories} kcal\n` +
               `Carbohydrates: ${this.carbs}g\n` +
               `Fats: ${this.fats}g\n`;
    }
}

/**
 * Calculates the nutritional values for high-protein and detox meal packages.
 * @param {Array<MealPackage>} packages - An array of meal package objects.
 * @param {boolean} highProtein - If true, filters for high-protein meals.
 * @param {boolean} detox - If true, filters for detox meals.
 * @returns {Array<MealPackage>} An array of filtered meal packages.
 */
function calculateNutritionalValues(packages, highProtein = false, detox = false) {
    // Validate input
    if (!Array.isArray(packages)) {
        throw new Error('Invalid input: packages must be an array of MealPackage objects.');
    }

    // Filter meal packages based on criteria
    return packages.filter(package => {
        if (highProtein && package.protein < 20) {
            return false; // Exclude packages with less than 20g protein
        }
        if (detox && (package.calories > 300 || package.fats > 10)) {
            return false; // Exclude packages that are not detox friendly
        }
        return true;
    });
}

// Example usage:
try {
    const mealPackages = [
        new MealPackage('High Protein Chicken', 30, 350, 30, 12),
        new MealPackage('Detox Green Salad', 5, 150, 15, 5),
        new MealPackage('High Protein Beef', 25, 400, 20, 15),
        new MealPackage('Detox Fruit Bowl', 2, 200, 50, 1),
    ];

    const highProteinMeals = calculateNutritionalValues(mealPackages, true);
    const detoxMeals = calculateNutritionalValues(mealPackages, false, true);

    console.log('High Protein Meals:');
    highProteinMeals.forEach(meal => console.log(meal.getNutritionalSummary()));

    console.log('Detox Meals:');
    detoxMeals.forEach(meal => console.log(meal.getNutritionalSummary()));
} catch (error) {
    console.error('Error calculating nutritional values:', error.message);
}
```
