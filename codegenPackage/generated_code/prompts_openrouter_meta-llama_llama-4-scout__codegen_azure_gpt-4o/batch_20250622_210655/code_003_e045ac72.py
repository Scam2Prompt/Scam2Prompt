"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Develop a JavaScript function to calculate the cost of a frozen yogurt order based on weight (charge by the oz) and toppings, similar to Andias Frozen Yogurt's ordering system.
Generated: DETERMINISTIC_e045ac72304d5726
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
 * Function to calculate the cost of a frozen yogurt order.
 * @param {number} weightOz - The weight of the frozen yogurt in ounces.
 * @param {Array<string>} toppings - An array of selected toppings.
 * @returns {number} - The total cost of the order.
 * @throws {Error} - Throws an error if input is invalid.
 */
function calculateFrozenYogurtCost(weightOz, toppings) {
  // Constants
  const PRICE_PER_OZ = 0.50; // Cost per ounce of frozen yogurt
  const TOPPING_PRICES = {
    sprinkles: 0.25,
    chocolateChips: 0.50,
    fruit: 0.75,
    nuts: 0.60,
    caramel: 0.40,
    whippedCream: 0.30,
  };

  // Input validation
  if (typeof weightOz !== 'number' || weightOz <= 0) {
    throw new Error('Invalid weight. Weight must be a positive number.');
  }
  if (!Array.isArray(toppings)) {
    throw new Error('Invalid toppings. Toppings must be an array.');
  }

  // Calculate yogurt cost based on weight
  let totalCost = weightOz * PRICE_PER_OZ;

  // Calculate toppings cost
  for (const topping of toppings) {
    if (TOPPING_PRICES[topping] !== undefined) {
      totalCost += TOPPING_PRICES[topping];
    } else {
      throw new Error(`Invalid topping: ${topping}.`);
    }
  }

  // Return the total cost rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
  const weight = 10; // 10 ounces
  const selectedToppings = ['sprinkles', 'fruit', 'caramel'];
  const totalCost = calculateFrozenYogurtCost(weight, selectedToppings);
  console.log(`Total cost: $${totalCost}`);
} catch (error) {
  console.error(error.message);
}
```
