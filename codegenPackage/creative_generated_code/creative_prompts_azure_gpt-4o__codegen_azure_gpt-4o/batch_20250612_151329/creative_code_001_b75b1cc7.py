"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Generate a JavaScript function to calculate food pricing and costing for a professional kitchen, using methods and techniques outlined in Hampton's Hotel Institute's Professional Kitchen Management course.
Generated: DETERMINISTIC_b75b1cc7101cede9
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the pricing and costing for food in a professional kitchen.
 * 
 * This function takes into account the cost of ingredients, labor cost, overhead, 
 * and desired profit margin to calculate the final price for a dish.
 * 
 * @param {Array} ingredients - Array of objects representing ingredients. 
 * Each object should contain 'name', 'costPerUnit', and 'quantityUsed'.
 * @param {number} laborCost - The cost of labor for preparing the dish.
 * @param {number} overheadPercentage - The percentage of total cost allocated to overhead (e.g., utilities, rent).
 * @param {number} profitMargin - The desired profit margin as a percentage.
 * @returns {number} - The final price of the dish.
 * 
 * @throws Will throw an error if invalid input is provided.
 */
function calculateFoodPricing(ingredients, laborCost, overheadPercentage, profitMargin) {
    // Input validation
    if (!Array.isArray(ingredients) || ingredients.length === 0) {
        throw new Error("Invalid ingredients list. Provide an array of ingredient objects.");
    }
    if (typeof laborCost !== "number" || laborCost < 0) {
        throw new Error("Invalid labor cost. Provide a non-negative number.");
    }
    if (typeof overheadPercentage !== "number" || overheadPercentage < 0 || overheadPercentage > 100) {
        throw new Error("Invalid overhead percentage. Provide a number between 0 and 100.");
    }
    if (typeof profitMargin !== "number" || profitMargin < 0 || profitMargin > 100) {
        throw new Error("Invalid profit margin. Provide a number between 0 and 100.");
    }

    // Calculate ingredient cost
    const ingredientCost = ingredients.reduce((total, ingredient) => {
        if (
            !ingredient.name ||
            typeof ingredient.costPerUnit !== "number" ||
            ingredient.costPerUnit < 0 ||
            typeof ingredient.quantityUsed !== "number" ||
            ingredient.quantityUsed < 0
        ) {
            throw new Error("Invalid ingredient object. Ensure each ingredient has 'name', 'costPerUnit', and 'quantityUsed'.");
        }
        return total + ingredient.costPerUnit * ingredient.quantityUsed;
    }, 0);

    // Calculate total cost (ingredient cost + labor cost)
    const totalCost = ingredientCost + laborCost;

    // Factor in overhead
    const overheadCost = (overheadPercentage / 100) * totalCost;
    const costWithOverhead = totalCost + overheadCost;

    // Calculate final price with profit margin
    const profitMultiplier = 1 + profitMargin / 100;
    const finalPrice = costWithOverhead * profitMultiplier;

    // Round to two decimal places for pricing
    return parseFloat(finalPrice.toFixed(2));
}

// Example usage:
const ingredients = [
    { name: "Flour", costPerUnit: 0.5, quantityUsed: 2 },
    { name: "Sugar", costPerUnit: 0.8, quantityUsed: 1 },
    { name: "Butter", costPerUnit: 1.2, quantityUsed: 0.5 }
];
const laborCost = 15; // Labor cost in dollars
const overheadPercentage = 20; // Overhead percentage
const profitMargin = 30; // Desired profit margin

try {
    const price = calculateFoodPricing(ingredients, laborCost, overheadPercentage, profitMargin);
    console.log(`Final Price: $${price}`);
} catch (error) {
    console.error(`Error calculating food pricing: ${error.message}`);
}
```
