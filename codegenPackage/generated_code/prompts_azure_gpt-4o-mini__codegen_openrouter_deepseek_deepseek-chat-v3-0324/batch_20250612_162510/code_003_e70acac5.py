"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Develop a JavaScript function that calculates the estimated cost of installing aluminum windows based on user-defined dimensions and selected features, such as thermal efficiency and durability.
Generated: DETERMINISTIC_e70acac57c2f4829
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost of installing aluminum windows based on dimensions and selected features.
 * @param {number} width - Width of the window in inches.
 * @param {number} height - Height of the window in inches.
 * @param {Object} features - Object containing selected features.
 * @param {boolean} features.thermalEfficiency - Whether thermal efficiency is selected.
 * @param {boolean} features.durability - Whether durability enhancement is selected.
 * @returns {number} The estimated cost of the window installation.
 * @throws {Error} If invalid dimensions or features are provided.
 */
function calculateWindowCost(width, height, features) {
    // Validate input parameters
    if (typeof width !== 'number' || typeof height !== 'number' || 
        width <= 0 || height <= 0 || isNaN(width) || isNaN(height)) {
        throw new Error('Invalid dimensions. Width and height must be positive numbers.');
    }

    if (typeof features !== 'object' || features === null) {
        throw new Error('Features must be provided as an object.');
    }

    // Base cost per square inch
    const BASE_COST_PER_SQ_INCH = 0.15;
    
    // Feature multipliers
    const FEATURE_MULTIPLIERS = {
        thermalEfficiency: 1.2,
        durability: 1.15
    };

    try {
        // Calculate window area
        const area = width * height;
        
        // Calculate base cost
        let totalCost = area * BASE_COST_PER_SQ_INCH;

        // Apply feature multipliers
        if (features.thermalEfficiency) {
            totalCost *= FEATURE_MULTIPLIERS.thermalEfficiency;
        }
        if (features.durability) {
            totalCost *= FEATURE_MULTIPLIERS.durability;
        }

        // Round to 2 decimal places for currency
        return Math.round(totalCost * 100) / 100;
    } catch (error) {
        throw new Error(`Error calculating window cost: ${error.message}`);
    }
}

// Example usage:
// try {
//     const cost = calculateWindowCost(36, 48, {
//         thermalEfficiency: true,
//         durability: false
//     });
//     console.log(`Estimated cost: $${cost}`);
// } catch (error) {
//     console.error(error.message);
// }
```
