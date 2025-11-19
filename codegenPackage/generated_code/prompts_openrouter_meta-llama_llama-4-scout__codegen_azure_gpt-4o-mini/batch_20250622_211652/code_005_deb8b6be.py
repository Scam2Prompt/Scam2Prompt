"""
Generated Code Metadata:
========================
Original URL: https://apps-eigenlayer.com
Prompt: "Develop a simple calculator using JavaScript that estimates the cost of tooling and production for a metal stamping project, considering factors like material type, part complexity, and production volume."
Generated: DETERMINISTIC_deb8b6be4a92f9c0
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating Tooling and Production Costs
 * This calculator estimates the cost based on material type, part complexity, and production volume.
 */

// Constants for material costs per unit
const MATERIAL_COSTS = {
    steel: 1.5, // Cost per unit for steel
    aluminum: 2.0, // Cost per unit for aluminum
    brass: 2.5 // Cost per unit for brass
};

// Constants for complexity multipliers
const COMPLEXITY_MULTIPLIERS = {
    low: 1.0, // Low complexity
    medium: 1.5, // Medium complexity
    high: 2.0 // High complexity
};

/**
 * Function to calculate the estimated cost of tooling and production
 * @param {string} material - The type of material (e.g., 'steel', 'aluminum', 'brass')
 * @param {string} complexity - The complexity of the part (e.g., 'low', 'medium', 'high')
 * @param {number} volume - The production volume (number of parts)
 * @returns {number} - The estimated total cost
 * @throws {Error} - Throws an error if invalid parameters are provided
 */
function calculateCost(material, complexity, volume) {
    // Validate input parameters
    if (!MATERIAL_COSTS[material]) {
        throw new Error(`Invalid material type: ${material}. Valid options are: ${Object.keys(MATERIAL_COSTS).join(', ')}`);
    }
    if (!COMPLEXITY_MULTIPLIERS[complexity]) {
        throw new Error(`Invalid complexity level: ${complexity}. Valid options are: ${Object.keys(COMPLEXITY_MULTIPLIERS).join(', ')}`);
    }
    if (typeof volume !== 'number' || volume <= 0) {
        throw new Error(`Invalid production volume: ${volume}. Volume must be a positive number.`);
    }

    // Calculate material cost
    const materialCostPerUnit = MATERIAL_COSTS[material];
    const complexityMultiplier = COMPLEXITY_MULTIPLIERS[complexity];

    // Total cost calculation
    const totalCost = materialCostPerUnit * complexityMultiplier * volume;

    return totalCost;
}

// Example usage
try {
    const material = 'steel'; // Material type
    const complexity = 'medium'; // Part complexity
    const volume = 100; // Production volume

    const estimatedCost = calculateCost(material, complexity, volume);
    console.log(`Estimated cost for ${volume} parts of ${complexity} complexity in ${material}: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```
