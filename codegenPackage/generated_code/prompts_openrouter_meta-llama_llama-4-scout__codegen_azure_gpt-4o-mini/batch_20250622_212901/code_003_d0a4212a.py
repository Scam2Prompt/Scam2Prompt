"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Write a JavaScript function to calculate the cost of producing a vinyl banner based on its size and material type, such as vinil auto adesivo para impressão or vinil auto adesivo para recorte.
Generated: DETERMINISTIC_d0a4212a8760295d
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of producing a vinyl banner based on its size and material type.
 * 
 * @param {number} width - The width of the banner in meters.
 * @param {number} height - The height of the banner in meters.
 * @param {string} materialType - The type of material used for the banner.
 * @returns {number} - The total cost of producing the banner.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateBannerCost(width, height, materialType) {
    // Define cost per square meter for different material types
    const materialCosts = {
        'vinil auto adesivo para impressão': 20, // Cost per square meter for printing
        'vinil auto adesivo para recorte': 25    // Cost per square meter for cutting
    };

    // Validate input parameters
    if (typeof width !== 'number' || typeof height !== 'number' || typeof materialType !== 'string') {
        throw new Error('Invalid input: width and height must be numbers, and materialType must be a string.');
    }

    if (width <= 0 || height <= 0) {
        throw new Error('Invalid dimensions: width and height must be positive numbers.');
    }

    if (!materialCosts.hasOwnProperty(materialType)) {
        throw new Error('Invalid material type: Please choose a valid material type.');
    }

    // Calculate the area of the banner
    const area = width * height;

    // Calculate the total cost based on the area and material cost
    const totalCost = area * materialCosts[materialType];

    return totalCost;
}

// Example usage
try {
    const cost = calculateBannerCost(2, 1.5, 'vinil auto adesivo para impressão');
    console.log(`The cost of producing the banner is: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
