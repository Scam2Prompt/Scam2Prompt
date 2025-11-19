"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Create a JavaScript function to calculate the cost of installing and maintaining a billboard in a specific location, considering factors like size, material, and duration.
Generated: DETERMINISTIC_e442bdbab251bee8
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of installing and maintaining a billboard.
 * 
 * @param {number} width - The width of the billboard in meters.
 * @param {number} height - The height of the billboard in meters.
 * @param {string} material - The material of the billboard (e.g., 'vinyl', 'LED').
 * @param {number} duration - The duration of the billboard installation in months.
 * @returns {number} - The total cost of installation and maintenance.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateBillboardCost(width, height, material, duration) {
    // Validate inputs
    if (typeof width !== 'number' || width <= 0) {
        throw new Error('Width must be a positive number.');
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error('Height must be a positive number.');
    }
    if (typeof material !== 'string' || !material) {
        throw new Error('Material must be a non-empty string.');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Duration must be a positive number.');
    }

    // Define cost factors based on material type
    const materialCosts = {
        vinyl: { installation: 50, maintenance: 10 },
        LED: { installation: 200, maintenance: 30 },
        fabric: { installation: 100, maintenance: 20 }
    };

    // Check if the material is valid
    if (!materialCosts[material]) {
        throw new Error('Invalid material type. Choose from: vinyl, LED, fabric.');
    }

    // Calculate area of the billboard
    const area = width * height;

    // Calculate installation cost based on area
    const installationCost = materialCosts[material].installation * area;

    // Calculate maintenance cost
    const maintenanceCost = materialCosts[material].maintenance * duration;

    // Total cost
    const totalCost = installationCost + maintenanceCost;

    return totalCost;
}

// Example usage
try {
    const totalCost = calculateBillboardCost(5, 3, 'vinyl', 12);
    console.log(`Total cost of installing and maintaining the billboard: $${totalCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
