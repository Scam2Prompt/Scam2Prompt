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
 * Calculate the estimated cost of installing aluminum windows based on dimensions 
 * and selected features.
 *
 * @param {number} width - The width of the window in meters.
 * @param {number} height - The height of the window in meters.
 * @param {boolean} thermalEfficiency - Whether thermal efficiency is selected.
 * @param {boolean} durability - Whether durability upgrade is selected.
 * @returns {number} - The estimated cost of installing the aluminum window.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateAluminumWindowCost(width, height, thermalEfficiency, durability) {
    // Validate input parameters
    if (typeof width !== 'number' || width <= 0) {
        throw new Error('Invalid width: Width must be a positive number.');
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error('Invalid height: Height must be a positive number.');
    }
    if (typeof thermalEfficiency !== 'boolean') {
        throw new Error('Invalid thermal efficiency: Must be a boolean.');
    }
    if (typeof durability !== 'boolean') {
        throw new Error('Invalid durability: Must be a boolean.');
    }

    // Base cost per square meter
    const BASE_COST_PER_SQ_M = 200;

    // Features cost multipliers
    const THERMAL_EFFICIENCY_MULTIPLIER = 1.25;
    const DURABILITY_MULTIPLIER = 1.15;

    // Calculate the area of the window
    const area = width * height;

    // Calculate the base cost
    let totalCost = area * BASE_COST_PER_SQ_M;

    // Apply feature cost multipliers if selected
    if (thermalEfficiency) {
        totalCost *= THERMAL_EFFICIENCY_MULTIPLIER;
    }
    if (durability) {
        totalCost *= DURABILITY_MULTIPLIER;
    }

    // Return the final estimated cost, rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
    const width = 1.5; // in meters
    const height = 2.0; // in meters
    const thermalEfficiency = true; // selected
    const durability = false; // not selected

    const estimatedCost = calculateAluminumWindowCost(width, height, thermalEfficiency, durability);
    console.log(`Estimated cost: $${estimatedCost}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```
