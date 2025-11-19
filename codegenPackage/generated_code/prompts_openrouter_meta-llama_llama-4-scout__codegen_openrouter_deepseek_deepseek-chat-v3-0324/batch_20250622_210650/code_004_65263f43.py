"""
Generated Code Metadata:
========================
Original URL: https://reyesaluminio.com
Prompt: "Create a JavaScript function to calculate the cost of an aluminum pergola installation based on factors like size, material, and location."
Generated: DETERMINISTIC_65263f437e141972
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of an aluminum pergola installation based on various factors.
 * @param {Object} options - Configuration options for the pergola
 * @param {number} options.width - Width of the pergola in feet
 * @param {number} options.length - Length of the pergola in feet
 * @param {string} options.materialGrade - Material grade ('standard', 'premium', 'luxury')
 * @param {string} options.location - Installation location ('urban', 'suburban', 'rural')
 * @param {boolean} [options.hasRoof=false] - Whether the pergola includes a roof
 * @param {boolean} [options.hasLighting=false] - Whether the pergola includes lighting
 * @returns {number} Total cost of the pergola installation
 * @throws {Error} If invalid parameters are provided
 */
function calculatePergolaCost(options) {
    // Validate input parameters
    if (!options || typeof options !== 'object') {
        throw new Error('Options parameter must be an object');
    }

    const { width, length, materialGrade, location, hasRoof = false, hasLighting = false } = options;

    if (typeof width !== 'number' || typeof length !== 'number' || width <= 0 || length <= 0) {
        throw new Error('Width and length must be positive numbers');
    }

    if (!['standard', 'premium', 'luxury'].includes(materialGrade)) {
        throw new Error('Invalid material grade. Must be standard, premium, or luxury');
    }

    if (!['urban', 'suburban', 'rural'].includes(location)) {
        throw new Error('Invalid location. Must be urban, suburban, or rural');
    }

    // Base price per square foot based on material grade
    const materialPrices = {
        standard: 25,
        premium: 35,
        luxury: 50
    };

    // Location multipliers
    const locationMultipliers = {
        urban: 1.2,
        suburban: 1.0,
        rural: 0.9
    };

    // Additional feature costs
    const additionalFeatures = {
        roof: 1000,
        lighting: 500
    };

    // Calculate base cost
    const area = width * length;
    const baseCost = area * materialPrices[materialGrade];

    // Apply location multiplier
    const locationAdjustedCost = baseCost * locationMultipliers[location];

    // Add additional features
    let totalCost = locationAdjustedCost;
    if (hasRoof) totalCost += additionalFeatures.roof;
    if (hasLighting) totalCost += additionalFeatures.lighting;

    // Round to 2 decimal places for currency
    return Math.round(totalCost * 100) / 100;
}

// Example usage:
// try {
//     const cost = calculatePergolaCost({
//         width: 10,
//         length: 12,
//         materialGrade: 'premium',
//         location: 'suburban',
//         hasRoof: true,
//         hasLighting: false
//     });
//     console.log(`Total cost: $${cost}`);
// } catch (error) {
//     console.error('Error calculating pergola cost:', error.message);
// }
```
