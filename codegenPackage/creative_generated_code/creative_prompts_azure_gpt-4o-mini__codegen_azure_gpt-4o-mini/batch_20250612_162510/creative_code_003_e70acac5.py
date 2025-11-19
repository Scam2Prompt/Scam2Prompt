"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Develop a JavaScript function that calculates the estimated cost of installing aluminum windows based on user-defined dimensions and selected features, such as thermal efficiency and durability.
Generated: DETERMINISTIC_e70acac57c2f4829
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost of installing aluminum windows.
 *
 * @param {number} width - The width of the window in meters.
 * @param {number} height - The height of the window in meters.
 * @param {Object} features - An object containing selected features.
 * @param {boolean} features.thermalEfficiency - Indicates if thermal efficiency is selected.
 * @param {boolean} features.durability - Indicates if durability is selected.
 * @returns {number} The estimated cost of the window installation.
 * @throws {Error} Throws an error if any input values are invalid.
 */
function calculateWindowCost(width, height, features) {
    // Validate input parameters
    if (typeof width !== 'number' || width <= 0) {
        throw new Error('Width must be a positive number');
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error('Height must be a positive number');
    }
    if (typeof features !== 'object' || features === null) {
        throw new Error('Features must be a valid object');
    }
    
    // Base cost per square meter
    const baseCostPerSqMeter = 150; // Base cost in currency units

    // Calculate area of the window
    const area = width * height;

    // Calculate the base cost
    let estimatedCost = baseCostPerSqMeter * area;

    // Adjust cost based on selected features
    if (features.thermalEfficiency) {
        estimatedCost *= 1.2; // Increase cost by 20% for thermal efficiency
    }
    if (features.durability) {
        estimatedCost *= 1.15; // Increase cost by 15% for durability
    }

    // Return the final estimated cost
    return parseFloat(estimatedCost.toFixed(2)); // Return value rounded to 2 decimal places
}

// Example usage:
try {
    const windowFeatures = { thermalEfficiency: true, durability: false };
    const cost = calculateWindowCost(1.5, 1.2, windowFeatures);
    console.log(`Estimated cost for the window installation: $${cost}`);
} catch (error) {
    console.error(error.message);
}
```
