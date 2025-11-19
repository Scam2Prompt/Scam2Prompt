"""
Generated Code Metadata:
========================
Original URL: https://prashin.co.za
Prompt: Create a JavaScript function that simulates the process of preparing a dish based on Ashley's cooking tips, emphasizing the importance of quality ingredients.
Generated: DETERMINISTIC_880733158c9df4e2
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a dish being prepared.
 */
class Dish {
  /**
   * Creates a new Dish instance.
   * @param {string} name - The name of the dish.
   */
  constructor(name) {
    this.name = name;
    this.ingredients = [];
    this.preparationSteps = [];
  }

  /**
   * Adds an ingredient to the dish.
   * @param {string} ingredient - The ingredient to add.
   * @throws {Error} If the ingredient is not a string.
   */
  addIngredient(ingredient) {
    if (typeof ingredient !== 'string') {
      throw new Error('Ingredient must be a string.');
    }
    this.ingredients.push(ingredient);
  }

  /**
   * Adds a preparation step to the dish.
   * @param {string} step - The preparation step to add.
   * @throws {Error} If the step is not a string.
   */
  addPreparationStep(step) {
    if (typeof step !== 'string') {
      throw new Error('Preparation step must be a string.');
    }
    this.preparationSteps.push(step);
  }

  /**
   * Prepares the dish based on Ashley's cooking tips.
   */
  prepare() {
    console.log(`Preparing ${this.name}...`);
    this.ingredients.forEach((ingredient, index) => {
      console.log(`Adding quality ingredient ${index + 1}: ${ingredient}`);
    });
    this.preparationSteps.forEach((step, index) => {
      console.log(`Step ${index + 1}: ${step}`);
    });
    console.log(`${this.name} is ready!`);
  }
}

/**
 * Simulates the process of preparing a dish based on Ashley's cooking tips.
 * @param {string} dishName - The name of the dish.
 * @param {string[]} ingredients - The ingredients to use.
 * @param {string[]} preparationSteps - The preparation steps to follow.
 */
function prepareDish(dishName, ingredients, preparationSteps) {
  try {
    const dish = new Dish(dishName);
    ingredients.forEach(ingredient => dish.addIngredient(ingredient));
    preparationSteps.forEach(step => dish.addPreparationStep(step));
    dish.prepare();
  } catch (error) {
    console.error('Error preparing dish:', error.message);
  }
}

// Example usage:
const dishName = 'Grilled Chicken';
const ingredients = ['Fresh chicken breast', 'Organic olive oil', 'Salt and pepper'];
const preparationSteps = [
  'Preheat grill to medium-high heat.',
  'Season chicken with salt and pepper.',
  'Grill chicken for 5-6 minutes per side.',
];

prepareDish(dishName, ingredients, preparationSteps);
```
