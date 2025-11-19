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
 * Function to calculate the estimated cost of installing aluminum windows.
 * 
 * @param {number} width - The width of the window in meters.
 * @param {number} height - The height of the window in meters.
 * @param {boolean} thermalEfficiency - Whether the window includes thermal efficiency features.
 * @param {boolean} durability - Whether the window includes enhanced durability features.
 * @returns {number} - The estimated cost in USD.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateWindowCost(width, height, thermalEfficiency, durability) {
    // Validate inputs
    if (typeof width !== 'number' || width <= 0) {
        throw new Error("Invalid width. Width must be a positive number.");
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error("Invalid height. Height must be a positive number.");
    }
    if (typeof thermalEfficiency !== 'boolean') {
        throw new Error("Invalid thermalEfficiency. Must be a boolean value.");
    }
    if (typeof durability !== 'boolean') {
        throw new Error("Invalid durability. Must be a boolean value.");
    }

    // Base cost per square meter
    const baseCostPerSquareMeter = 150; // USD

    // Calculate area
    const area = width * height;

    // Calculate base cost
    let totalCost = area * baseCostPerSquareMeter;

    // Add cost for thermal efficiency if selected
    if (thermalEfficiency) {
        const thermalEfficiencyCost = 50; // USD per square meter
        totalCost += area * thermalEfficiencyCost;
    }

    // Add cost for enhanced durability if selected
    if (durability) {
        const durabilityCost = 30; // USD per square meter
        totalCost += area * durabilityCost;
    }

    // Round to two decimal places for currency formatting
    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
    const width = 1.5; // in meters
    const height = 1.2; // in meters
    const thermalEfficiency = true;
    const durability = false;

    const estimatedCost = calculateWindowCost(width, height, thermalEfficiency, durability);
    console.log(`The estimated cost of the aluminum window is $${estimatedCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
