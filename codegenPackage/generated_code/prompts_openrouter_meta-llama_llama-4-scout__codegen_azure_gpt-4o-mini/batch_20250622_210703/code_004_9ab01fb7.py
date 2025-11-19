"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write a JavaScript function to calculate the cost of a customized engraving project based on material, size, and complexity.
Generated: DETERMINISTIC_9ab01fb7088a70df
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of a customized engraving project based on material, size, and complexity.
 * 
 * @param {string} material - The material type for the engraving (e.g., 'wood', 'metal', 'glass').
 * @param {number} size - The size of the engraving in square inches.
 * @param {string} complexity - The complexity level of the engraving (e.g., 'simple', 'medium', 'complex').
 * @returns {number} - The total cost of the engraving project.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateEngravingCost(material, size, complexity) {
    // Define base costs for materials
    const materialCosts = {
        wood: 5,
        metal: 10,
        glass: 15
    };

    // Define complexity multipliers
    const complexityMultipliers = {
        simple: 1,
        medium: 1.5,
        complex: 2
    };

    // Validate input parameters
    if (!materialCosts[material]) {
        throw new Error(`Invalid material: ${material}. Valid options are: ${Object.keys(materialCosts).join(', ')}`);
    }
    if (typeof size !== 'number' || size <= 0) {
        throw new Error('Size must be a positive number.');
    }
    if (!complexityMultipliers[complexity]) {
        throw new Error(`Invalid complexity: ${complexity}. Valid options are: ${Object.keys(complexityMultipliers).join(', ')}`);
    }

    // Calculate the base cost based on material
    const baseCost = materialCosts[material];

    // Calculate the total cost
    const totalCost = baseCost * size * complexityMultipliers[complexity];

    return totalCost;
}

// Example usage
try {
    const cost = calculateEngravingCost('metal', 10, 'medium');
    console.log(`The total cost of the engraving project is: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
