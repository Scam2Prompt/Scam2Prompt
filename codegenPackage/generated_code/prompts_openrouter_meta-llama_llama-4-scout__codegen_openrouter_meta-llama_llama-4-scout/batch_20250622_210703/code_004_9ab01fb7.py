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
 * Calculates the cost of a customized engraving project.
 * 
 * @param {string} material - The material of the project (e.g., wood, metal, glass).
 * @param {number} size - The size of the project in square inches.
 * @param {string} complexity - The complexity of the project (e.g., simple, medium, complex).
 * @returns {number} The total cost of the project.
 */
function calculateEngravingCost(material, size, complexity) {
    // Define material costs per square inch
    const materialCosts = {
        wood: 0.05,
        metal: 0.10,
        glass: 0.15
    };

    // Define complexity multipliers
    const complexityMultipliers = {
        simple: 1.0,
        medium: 1.5,
        complex: 2.5
    };

    // Check if material is valid
    if (!(material in materialCosts)) {
        throw new Error(`Invalid material: ${material}`);
    }

    // Check if complexity is valid
    if (!(complexity in complexityMultipliers)) {
        throw new Error(`Invalid complexity: ${complexity}`);
    }

    // Check if size is valid
    if (size <= 0) {
        throw new Error(`Invalid size: ${size}. Size must be greater than 0.`);
    }

    // Calculate base cost
    const baseCost = materialCosts[material] * size;

    // Apply complexity multiplier
    const totalCost = baseCost * complexityMultipliers[complexity];

    return totalCost;
}

// Example usage:
try {
    const material = 'wood';
    const size = 10; // square inches
    const complexity = 'medium';
    const cost = calculateEngravingCost(material, size, complexity);
    console.log(`The total cost of the project is: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
