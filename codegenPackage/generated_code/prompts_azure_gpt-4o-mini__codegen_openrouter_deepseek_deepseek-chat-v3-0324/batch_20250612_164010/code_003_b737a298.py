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
 * @param {Object} projectDetails - The details of the project.
 * @param {number} projectDetails.area - The area of the structure in square meters.
 * @param {string} projectDetails.materialType - The type of material ('concrete', 'steel', 'wood', 'masonry').
 * @param {string} projectDetails.damageLevel - The level of damage ('low', 'medium', 'high', 'severe').
 * @param {number} [projectDetails.laborCostPerHour=50] - The labor cost per hour (default: 50).
 * @param {number} [projectDetails.overheadPercentage=15] - The overhead percentage (default: 15).
 * @returns {Object} An object containing the estimated cost breakdown and total cost.
 * @throws {Error} If required parameters are missing or invalid.
 */
function calculateRepairEstimate(projectDetails) {
    // Validate required parameters
    if (!projectDetails || typeof projectDetails !== 'object') {
        throw new Error('Project details must be provided as an object.');
    }

    const { area, materialType, damageLevel, laborCostPerHour = 50, overheadPercentage = 15 } = projectDetails;

    if (typeof area !== 'number' || area <= 0) {
        throw new Error('Area must be a positive number.');
    }

    const validMaterialTypes = ['concrete', 'steel', 'wood', 'masonry'];
    if (!validMaterialTypes.includes(materialType)) {
        throw new Error(`Invalid material type. Must be one of: ${validMaterialTypes.join(', ')}`);
    }

    const validDamageLevels = ['low', 'medium', 'high', 'severe'];
    if (!validDamageLevels.includes(damageLevel)) {
        throw new Error(`Invalid damage level. Must be one of: ${validDamageLevels.join(', ')}`);
    }

    if (typeof laborCostPerHour !== 'number' || laborCostPerHour <= 0) {
        throw new Error('Labor cost per hour must be a positive number.');
    }

    if (typeof overheadPercentage !== 'number' || overheadPercentage < 0) {
        throw new Error('Overhead percentage must be a non-negative number.');
    }

    // Material cost per square meter based on type
    const materialCosts = {
        concrete: 100,
        steel: 150,
        wood: 80,
        masonry: 70
    };

    // Damage multipliers
    const damageMultipliers = {
        low: 1.0,
        medium: 1.5,
        high: 2.0,
        severe: 3.0
    };

    // Calculate material cost
    const baseMaterialCost = materialCosts[materialType] * area;
    const damageAdjustedMaterialCost = baseMaterialCost * damageMultipliers[damageLevel];

    // Calculate labor cost (estimated hours based on area and damage level)
    const laborHours = area * (damageMultipliers[damageLevel] * 0.5);
    const laborCost = laborHours * laborCostPerHour;

    // Calculate overhead cost
    const subtotal = damageAdjustedMaterialCost + laborCost;
    const overheadCost = subtotal * (overheadPercentage / 100);

    // Calculate total cost
    const totalCost = subtotal + overheadCost;

    return {
        materialCost: parseFloat(damageAdjustedMaterialCost.toFixed(2)),
        laborCost: parseFloat(laborCost.toFixed(2)),
        overheadCost: parseFloat(overheadCost.toFixed(2)),
        totalCost: parseFloat(totalCost.toFixed(2)),
        breakdown: {
            area,
            materialType,
            damageLevel,
            laborHours: parseFloat(laborHours.toFixed(2)),
            laborCostPerHour,
            overheadPercentage
        }
    };
}

// Example usage:
// try {
//     const estimate = calculateRepairEstimate({
//         area: 200,
//         materialType: 'concrete',
//         damageLevel: 'medium',
//         laborCostPerHour: 60,
//         overheadPercentage: 20
//     });
//     console.log(estimate);
// } catch (error) {
//     console.error('Error calculating estimate:', error.message);
// }
```
