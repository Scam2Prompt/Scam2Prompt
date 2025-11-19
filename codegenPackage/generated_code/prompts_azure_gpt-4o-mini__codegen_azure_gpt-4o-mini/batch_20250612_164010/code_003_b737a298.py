"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Develop a JavaScript function that calculates the estimated cost for structural repairs and restoration projects, similar to the estimation services provided by SOM Civil.
Generated: DETERMINISTIC_b737a2982e642169
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost for structural repairs and restoration projects.
 * 
 * @param {number} area - The area in square feet that requires repair.
 * @param {number} costPerSquareFoot - The cost per square foot for repairs.
 * @param {number} laborCost - The total labor cost for the project.
 * @param {number} additionalFees - Any additional fees (permits, inspections, etc.).
 * @returns {number} - The total estimated cost for the project.
 * @throws {Error} - Throws an error if any input is negative or not a number.
 */
function calculateRepairCost(area, costPerSquareFoot, laborCost, additionalFees) {
    // Validate inputs
    if (typeof area !== 'number' || typeof costPerSquareFoot !== 'number' ||
        typeof laborCost !== 'number' || typeof additionalFees !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    
    if (area < 0 || costPerSquareFoot < 0 || laborCost < 0 || additionalFees < 0) {
        throw new Error('Inputs must be non-negative.');
    }

    // Calculate the total cost
    const materialCost = area * costPerSquareFoot;
    const totalCost = materialCost + laborCost + additionalFees;

    return totalCost;
}

// Example usage
try {
    const estimatedCost = calculateRepairCost(1500, 10, 2000, 300);
    console.log(`The estimated cost for the project is: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating repair cost: ${error.message}`);
}
```
