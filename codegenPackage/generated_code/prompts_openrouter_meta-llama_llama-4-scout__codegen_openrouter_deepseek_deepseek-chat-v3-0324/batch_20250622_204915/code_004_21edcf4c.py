"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Create a JavaScript function to estimate the cost of a civil engineering project, including materials, labor, and equipment costs, based on SOM Civil Engineers' pricing models."
Generated: DETERMINISTIC_21edcf4c155b78ae
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Estimates the cost of a civil engineering project based on SOM Civil Engineers' pricing models.
 * @param {Object} projectDetails - Project details including materials, labor, and equipment.
 * @param {number} projectDetails.area - Area of the project in square meters.
 * @param {string} projectDetails.complexity - Complexity level ('simple', 'medium', 'complex').
 * @param {number} projectDetails.duration - Project duration in months.
 * @param {Object} [options] - Optional parameters.
 * @param {number} [options.materialCostFactor=1.0] - Multiplier for material costs.
 * @param {number} [options.laborCostFactor=1.0] - Multiplier for labor costs.
 * @param {number} [options.equipmentCostFactor=1.0] - Multiplier for equipment costs.
 * @returns {Object} - Estimated costs breakdown and total.
 * @throws {Error} - If invalid input is provided.
 */
function estimateProjectCost(projectDetails, options = {}) {
    // Validate input
    if (!projectDetails || typeof projectDetails !== 'object') {
        throw new Error('Project details must be provided as an object');
    }

    const { area, complexity, duration } = projectDetails;
    if (typeof area !== 'number' || area <= 0) {
        throw new Error('Area must be a positive number');
    }
    if (!['simple', 'medium', 'complex'].includes(complexity)) {
        throw new Error('Complexity must be one of: simple, medium, complex');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Duration must be a positive number');
    }

    // Set default options
    const {
        materialCostFactor = 1.0,
        laborCostFactor = 1.0,
        equipmentCostFactor = 1.0
    } = options;

    // Base cost rates (per sqm) from SOM Civil Engineers' pricing models
    const BASE_MATERIAL_COST = 150; // USD per sqm
    const BASE_LABOR_COST = 100;    // USD per sqm
    const BASE_EQUIPMENT_COST = 50; // USD per sqm

    // Complexity multipliers
    const complexityMultipliers = {
        simple: 1.0,
        medium: 1.5,
        complex: 2.0
    };

    // Duration adjustment factor (longer projects may have reduced equipment costs)
    const durationAdjustment = duration > 12 ? 0.9 : 1.0;

    // Calculate costs
    const materialCost = area * BASE_MATERIAL_COST * complexityMultipliers[complexity] * materialCostFactor;
    const laborCost = area * BASE_LABOR_COST * complexityMultipliers[complexity] * laborCostFactor;
    const equipmentCost = area * BASE_EQUIPMENT_COST * complexityMultipliers[complexity] * equipmentCostFactor * durationAdjustment;

    const totalCost = materialCost + laborCost + equipmentCost;

    return {
        materialCost: parseFloat(materialCost.toFixed(2)),
        laborCost: parseFloat(laborCost.toFixed(2)),
        equipmentCost: parseFloat(equipmentCost.toFixed(2)),
        totalCost: parseFloat(totalCost.toFixed(2)),
        costPerSqm: parseFloat((totalCost / area).toFixed(2))
    };
}

// Example usage:
// try {
//     const project = {
//         area: 1000,
//         complexity: 'medium',
//         duration: 6
//     };
//     const estimate = estimateProjectCost(project, { laborCostFactor: 1.2 });
//     console.log(estimate);
// } catch (error) {
//     console.error('Error estimating project cost:', error.message);
// }
```
