"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Create a JavaScript function to calculate the cost of a custom window order, taking into account factors like material (aluminium, PVC, or bois), size, and type (e.g., fenêtre aluminium, porte de garage)."
Generated: DETERMINISTIC_ce89ae09660292eb
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of a custom window order.
 * @param {string} material - The material of the window (e.g., 'aluminium', 'PVC', 'bois').
 * @param {string} type - The type of the window (e.g., 'fenêtre aluminium', 'porte de garage').
 * @param {number} width - The width of the window in centimeters.
 * @param {number} height - The height of the window in centimeters.
 * @returns {number} - The total cost of the custom window order.
 * @throws {Error} - Throws an error if invalid inputs are provided.
 */
function calculateWindowCost(material, type, width, height) {
  // Validate inputs
  if (typeof material !== 'string' || typeof type !== 'string') {
    throw new Error('Material and type must be strings.');
  }
  if (typeof width !== 'number' || typeof height !== 'number' || width <= 0 || height <= 0) {
    throw new Error('Width and height must be positive numbers.');
  }

  // Base price per square centimeter for each material
  const materialPrices = {
    aluminium: 0.05, // Price per cm²
    PVC: 0.04,       // Price per cm²
    bois: 0.06       // Price per cm²
  };

  // Additional cost multipliers for different types
  const typeMultipliers = {
    'fenêtre aluminium': 1.2,
    'porte de garage': 1.5
  };

  // Check if material and type are valid
  if (!materialPrices[material]) {
    throw new Error(`Invalid material: ${material}. Valid options are 'aluminium', 'PVC', 'bois'.`);
  }
  if (!typeMultipliers[type]) {
    throw new Error(`Invalid type: ${type}. Valid options are 'fenêtre aluminium', 'porte de garage'.`);
  }

  // Calculate the area of the window
  const area = width * height; // in cm²

  // Calculate the base cost based on material
  const baseCost = area * materialPrices[material];

  // Apply the type multiplier
  const totalCost = baseCost * typeMultipliers[type];

  // Return the final cost rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
  const cost = calculateWindowCost('aluminium', 'fenêtre aluminium', 120, 150);
  console.log(`The total cost is: €${cost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
