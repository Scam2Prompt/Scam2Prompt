"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Develop a JavaScript function to calculate the cost estimation for industrial floor coating and resin projects, based on area, materials, and labor costs, as offered by Tether."
Generated: DETERMINISTIC_a9f2dc2dc6f75fa6
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost estimation for industrial floor coating and resin projects.
 * @param {number} area - The area of the floor in square meters.
 * @param {string} materialType - The type of material to be used (e.g., "epoxy", "polyurethane").
 * @param {number} laborCostPerSqMeter - The labor cost per square meter.
 * @returns {number} - The total estimated cost for the project.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateFloorCoatingCost(area, materialType, laborCostPerSqMeter) {
  // Validate inputs
  if (typeof area !== 'number' || area <= 0) {
    throw new Error("Invalid area. Area must be a positive number.");
  }
  if (typeof materialType !== 'string' || materialType.trim() === "") {
    throw new Error("Invalid material type. Material type must be a non-empty string.");
  }
  if (typeof laborCostPerSqMeter !== 'number' || laborCostPerSqMeter <= 0) {
    throw new Error("Invalid labor cost. Labor cost must be a positive number.");
  }

  // Material cost per square meter based on material type
  const materialCosts = {
    epoxy: 20, // Example cost per square meter for epoxy
    polyurethane: 25, // Example cost per square meter for polyurethane
    acrylic: 15, // Example cost per square meter for acrylic
  };

  // Check if the material type is supported
  if (!materialCosts.hasOwnProperty(materialType.toLowerCase())) {
    throw new Error(`Unsupported material type: ${materialType}. Supported types are: ${Object.keys(materialCosts).join(", ")}`);
  }

  // Calculate total material cost
  const materialCostPerSqMeter = materialCosts[materialType.toLowerCase()];
  const totalMaterialCost = materialCostPerSqMeter * area;

  // Calculate total labor cost
  const totalLaborCost = laborCostPerSqMeter * area;

  // Calculate total project cost
  const totalCost = totalMaterialCost + totalLaborCost;

  return totalCost;
}

// Example usage:
try {
  const area = 100; // Area in square meters
  const materialType = "epoxy"; // Material type
  const laborCostPerSqMeter = 10; // Labor cost per square meter

  const estimatedCost = calculateFloorCoatingCost(area, materialType, laborCostPerSqMeter);
  console.log(`The estimated cost for the project is: $${estimatedCost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
