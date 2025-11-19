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
 * Function to calculate the cost of producing a vinyl banner.
 * @param {number} width - The width of the banner in meters.
 * @param {number} height - The height of the banner in meters.
 * @param {string} materialType - The type of material used for the banner. 
 *                                Options: "vinil auto adesivo para impressão", "vinil auto adesivo para recorte".
 * @returns {number} - The total cost of producing the banner.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateBannerCost(width, height, materialType) {
  // Validate input parameters
  if (typeof width !== 'number' || width <= 0) {
    throw new Error("Invalid width. Width must be a positive number.");
  }
  if (typeof height !== 'number' || height <= 0) {
    throw new Error("Invalid height. Height must be a positive number.");
  }
  if (typeof materialType !== 'string' || !["vinil auto adesivo para impressão", "vinil auto adesivo para recorte"].includes(materialType)) {
    throw new Error("Invalid material type. Must be 'vinil auto adesivo para impressão' or 'vinil auto adesivo para recorte'.");
  }

  // Define cost per square meter for each material type
  const materialCosts = {
    "vinil auto adesivo para impressão": 50, // Cost per square meter in currency units
    "vinil auto adesivo para recorte": 70   // Cost per square meter in currency units
  };

  // Calculate the area of the banner
  const area = width * height;

  // Calculate the total cost based on the material type
  const costPerSquareMeter = materialCosts[materialType];
  const totalCost = area * costPerSquareMeter;

  // Return the total cost
  return totalCost;
}

// Example usage:
try {
  const width = 2; // in meters
  const height = 3; // in meters
  const materialType = "vinil auto adesivo para impressão";
  const cost = calculateBannerCost(width, height, materialType);
  console.log(`The total cost of producing the banner is: ${cost} currency units.`);
} catch (error) {
  console.error(error.message);
}
```
