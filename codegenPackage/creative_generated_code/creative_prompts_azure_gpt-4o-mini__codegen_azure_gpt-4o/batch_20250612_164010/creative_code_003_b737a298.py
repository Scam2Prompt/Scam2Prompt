"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Develop a JavaScript function that calculates the estimated cost for structural repairs and restoration projects, similar to the estimation services provided by SOM Civil.
Generated: DETERMINISTIC_b737a2982e642169
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost for structural repairs and restoration projects.
 * 
 * @param {Object} parameters - The input parameters for the estimation.
 * @param {number} parameters.areaInSquareFeet - The total area of the project in square feet.
 * @param {string} parameters.typeOfRepair - Type of repair ('minor', 'moderate', 'major').
 * @param {boolean} parameters.requiresSpecialEquipment - Whether the project requires special equipment.
 * @param {number} parameters.materialCostPerSquareFoot - Cost of materials per square foot.
 * @param {number} parameters.laborCostPerHour - Labor cost per hour.
 * @param {number} parameters.estimatedHours - Estimated hours to complete the project.
 * @returns {number} - The estimated total cost of the project.
 * 
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateRepairEstimate(parameters) {
  // Input validation
  if (
    !parameters ||
    typeof parameters.areaInSquareFeet !== 'number' || parameters.areaInSquareFeet <= 0 ||
    typeof parameters.typeOfRepair !== 'string' ||
    typeof parameters.requiresSpecialEquipment !== 'boolean' ||
    typeof parameters.materialCostPerSquareFoot !== 'number' || parameters.materialCostPerSquareFoot <= 0 ||
    typeof parameters.laborCostPerHour !== 'number' || parameters.laborCostPerHour <= 0 ||
    typeof parameters.estimatedHours !== 'number' || parameters.estimatedHours <= 0
  ) {
    throw new Error('Invalid input parameters. Please provide valid values for the estimation.');
  }

  // Base multiplier based on the type of repair
  let repairMultiplier;
  switch (parameters.typeOfRepair.toLowerCase()) {
    case 'minor':
      repairMultiplier = 1; // No additional cost
      break;
    case 'moderate':
      repairMultiplier = 1.25; // 25% additional cost
      break;
    case 'major':
      repairMultiplier = 1.5; // 50% additional cost
      break;
    default:
      throw new Error('Invalid typeOfRepair. Supported values are "minor", "moderate", and "major".');
  }

  // Special equipment fee
  const specialEquipmentFee = parameters.requiresSpecialEquipment ? 500 : 0;

  // Calculate material cost
  const materialCost = parameters.areaInSquareFeet * parameters.materialCostPerSquareFoot;

  // Calculate labor cost
  const laborCost = parameters.laborCostPerHour * parameters.estimatedHours;

  // Total cost calculation
  const totalCost = (materialCost + laborCost + specialEquipmentFee) * repairMultiplier;

  return totalCost;
}

// Example usage:
try {
  const estimatedCost = calculateRepairEstimate({
    areaInSquareFeet: 1000,
    typeOfRepair: 'moderate',
    requiresSpecialEquipment: true,
    materialCostPerSquareFoot: 20,
    laborCostPerHour: 50,
    estimatedHours: 80
  });
  console.log(`Estimated Cost: $${estimatedCost.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
