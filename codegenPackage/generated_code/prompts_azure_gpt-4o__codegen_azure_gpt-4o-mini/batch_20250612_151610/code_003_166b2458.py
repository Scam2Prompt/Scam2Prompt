"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Create a function in JavaScript to calculate the cost savings of using stretch films with high elongation and low density, as detailed in the "Stretch Film 18 pulgadas" product description.
Generated: DETERMINISTIC_166b24586231408a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost savings of using stretch films with high elongation and low density.
 * 
 * @param {number} currentCostPerUnit - The current cost per unit of the existing stretch film.
 * @param {number} newCostPerUnit - The cost per unit of the new stretch film with high elongation and low density.
 * @param {number} currentUsage - The current usage in units of the existing stretch film.
 * @param {number} newUsage - The expected usage in units of the new stretch film.
 * @returns {number} - The calculated cost savings.
 * @throws {Error} - Throws an error if any input is negative or if costs are zero.
 */
function calculateCostSavings(currentCostPerUnit, newCostPerUnit, currentUsage, newUsage) {
    // Validate inputs
    if (currentCostPerUnit < 0 || newCostPerUnit < 0 || currentUsage < 0 || newUsage < 0) {
        throw new Error("Cost and usage values must be non-negative.");
    }
    if (currentCostPerUnit === 0 || newCostPerUnit === 0) {
        throw new Error("Cost per unit must be greater than zero.");
    }

    // Calculate total costs for current and new stretch films
    const currentTotalCost = currentCostPerUnit * currentUsage;
    const newTotalCost = newCostPerUnit * newUsage;

    // Calculate cost savings
    const costSavings = currentTotalCost - newTotalCost;

    // Return the cost savings, ensuring it's not negative
    return Math.max(costSavings, 0);
}

// Example usage
try {
    const savings = calculateCostSavings(100, 80, 50, 40);
    console.log(`Cost savings: $${savings}`);
} catch (error) {
    console.error(`Error calculating cost savings: ${error.message}`);
}
```
