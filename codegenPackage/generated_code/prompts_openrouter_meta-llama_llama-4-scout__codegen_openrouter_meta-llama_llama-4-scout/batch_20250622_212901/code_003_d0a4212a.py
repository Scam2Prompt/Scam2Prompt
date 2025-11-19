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
 * @param {string} materialType - The type of material to use. Can be either 'impressao' or 'recorte'.
 * @returns {number} The total cost of producing the banner.
 */
function calculateBannerCost(width, height, materialType) {
    // Define material prices per square meter
    const materialPrices = {
        'impressao': 10.99, // vinil auto adesivo para impressão
        'recorte': 12.99  // vinil auto adesivo para recorte
    };

    // Check if material type is valid
    if (!(materialType in materialPrices)) {
        throw new Error(`Invalid material type: ${materialType}. Must be either 'impressao' or 'recorte'.`);
    }

    // Calculate the area of the banner
    const area = width * height;

    // Check if area is valid (non-negative)
    if (area < 0) {
        throw new Error(`Invalid banner size: ${width}m x ${height}m. Area cannot be negative.`);
    }

    // Calculate the cost
    const cost = area * materialPrices[materialType];

    return cost;
}

// Example usage:
try {
    const width = 2.5; // meters
    const height = 1.8; // meters
    const materialType = 'impressao';
    const cost = calculateBannerCost(width, height, materialType);
    console.log(`The cost of producing a ${width}m x ${height}m banner with ${materialType} material is: R$${cost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
