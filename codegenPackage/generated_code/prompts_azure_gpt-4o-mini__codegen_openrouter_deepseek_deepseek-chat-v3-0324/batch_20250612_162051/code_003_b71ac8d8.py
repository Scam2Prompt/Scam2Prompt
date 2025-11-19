"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Create a function in JavaScript that calculates the cost of insulation services based on the materials and areas specified in the services provided by the company.
Generated: DETERMINISTIC_b71ac8d84f579b8f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of insulation services based on materials and areas.
 * 
 * @param {Object} options - The options for the insulation service.
 * @param {string} options.material - The type of insulation material ('fiberglass', 'cellulose', 'foam', 'mineral').
 * @param {number} options.area - The area to be insulated in square feet.
 * @param {boolean} [options.includeInstallation=true] - Whether installation is included (default: true).
 * @returns {number} The total cost of the insulation service.
 * @throws {Error} If invalid material or non-positive area is provided.
 */
function calculateInsulationCost(options) {
    const { material, area, includeInstallation = true } = options;

    // Validate input
    if (!material || typeof material !== 'string') {
        throw new Error('Invalid material: must be a non-empty string');
    }
    if (typeof area !== 'number' || area <= 0) {
        throw new Error('Invalid area: must be a positive number');
    }

    // Material cost per square foot
    const materialCosts = {
        fiberglass: 0.50,
        cellulose: 0.75,
        foam: 1.25,
        mineral: 0.60
    };

    // Installation cost per square foot
    const installationCost = 0.30;

    // Check if material is valid
    const materialCost = materialCosts[material.toLowerCase()];
    if (materialCost === undefined) {
        throw new Error(`Invalid material: ${material}. Must be one of: ${Object.keys(materialCosts).join(', ')}`);
    }

    // Calculate total cost
    let totalCost = area * materialCost;
    if (includeInstallation) {
        totalCost += area * installationCost;
    }

    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
// try {
//     const cost = calculateInsulationCost({
//         material: 'fiberglass',
//         area: 1000,
//         includeInstallation: true
//     });
//     console.log(`Total cost: $${cost}`);
// } catch (error) {
//     console.error(error.message);
// }
```
