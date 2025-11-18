"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Create a function in JavaScript to calculate the cost savings of using stretch films with high elongation and low density, as detailed in the "Stretch Film 18 pulgadas" product description.
Generated: DETERMINISTIC_166b24586231408a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cost savings of using stretch films with high elongation and low density.
 * 
 * @param {number} currentCost - The current cost of the stretch film per unit.
 * @param {number} newCost - The cost of the new stretch film per unit.
 * @param {number} currentUsage - The current usage of the stretch film in units.
 * @param {number} newUsage - The expected new usage of the stretch film in units.
 * @returns {number} - The calculated cost savings.
 * @throws {Error} - Throws an error if any input is negative or zero.
 */
function calculateCostSavings(currentCost, newCost, currentUsage, newUsage) {
    // Validate inputs
    if (currentCost <= 0 || newCost <= 0 || currentUsage <= 0 || newUsage <= 0) {
        throw new Error("All input values must be positive numbers greater than zero.");
    }
    
    // Calculate total costs for current and new stretch films
    const currentTotalCost = currentCost * currentUsage;
    const newTotalCost = newCost * newUsage;

    // Calculate cost savings
    const savings = currentTotalCost - newTotalCost;

    // Return the savings, ensuring no negative savings are reported
    return savings > 0 ? savings : 0;
}

// Example usage
try {
    const savings = calculateCostSavings(0.5, 0.3, 1000, 800);
    console.log(`Cost savings: $${savings.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating savings: ${error.message}`);
}
```
