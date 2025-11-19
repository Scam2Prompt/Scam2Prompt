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
 * Calculates the estimated cost of installing aluminum windows.
 * 
 * @param {number} width - The width of the window in meters.
 * @param {number} height - The height of the window in meters.
 * @param {boolean} thermalEfficiency - Indicates if thermal efficiency features are selected.
 * @param {boolean} durability - Indicates if durability features are selected.
 * @returns {number} - The estimated cost of the window installation.
 * @throws {Error} - Throws an error if the dimensions are invalid or if the features are not boolean.
 */
function calculateWindowCost(width, height, thermalEfficiency, durability) {
    // Validate input parameters
    if (typeof width !== 'number' || typeof height !== 'number') {
        throw new Error('Width and height must be numbers.');
    }
    if (width <= 0 || height <= 0) {
        throw new Error('Width and height must be positive values.');
    }
    if (typeof thermalEfficiency !== 'boolean' || typeof durability !== 'boolean') {
        throw new Error('Thermal efficiency and durability must be boolean values.');
    }

    // Base cost per square meter
    const baseCostPerSquareMeter = 150; // Example base cost in currency units

    // Calculate the area of the window
    const area = width * height;

    // Calculate the base cost based on area
    let estimatedCost = area * baseCostPerSquareMeter;

    // Add additional costs based on selected features
    if (thermalEfficiency) {
        estimatedCost += area * 50; // Additional cost for thermal efficiency
    }
    if (durability) {
        estimatedCost += area * 30; // Additional cost for durability
    }

    // Return the final estimated cost
    return estimatedCost;
}

// Example usage
try {
    const cost = calculateWindowCost(1.5, 1.2, true, false);
    console.log(`Estimated cost of installation: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```
