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
 * Calculates the total cost of a frozen yogurt order.
 * 
 * @param {number} weight - The weight of the frozen yogurt in ounces.
 * @param {Array<string>} toppings - An array of selected toppings.
 * @returns {number} - The total cost of the order.
 * @throws {Error} - Throws an error if weight is not a positive number or if toppings is not an array.
 */
function calculateFrozenYogurtCost(weight, toppings) {
    // Define the cost per ounce and the cost per topping
    const costPerOunce = 0.50; // Cost per ounce of frozen yogurt
    const costPerTopping = 0.75; // Cost per topping

    // Validate the weight input
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Weight must be a positive number.');
    }

    // Validate the toppings input
    if (!Array.isArray(toppings)) {
        throw new Error('Toppings must be an array.');
    }

    // Calculate the total cost
    const yogurtCost = weight * costPerOunce;
    const toppingsCost = toppings.length * costPerTopping;

    // Return the total cost
    return yogurtCost + toppingsCost;
}

// Example usage:
try {
    const totalCost = calculateFrozenYogurtCost(10, ['sprinkles', 'chocolate chips', 'nuts']);
    console.log(`Total cost of the frozen yogurt order: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
