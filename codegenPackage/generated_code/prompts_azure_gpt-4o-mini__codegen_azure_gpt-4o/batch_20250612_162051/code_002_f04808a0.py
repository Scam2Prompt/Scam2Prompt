"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Create a JavaScript function that calculates the budget for a construction project, considering the unique aspects of project management highlighted by TWM Associates.
Generated: DETERMINISTIC_f04808a04e143861
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the budget for a construction project.
 * 
 * @param {Object} projectDetails - An object containing details about the project.
 * @param {number} projectDetails.materialCost - Total cost of materials.
 * @param {number} projectDetails.laborCost - Total cost of labor.
 * @param {number} projectDetails.equipmentCost - Total cost of equipment.
 * @param {number} projectDetails.contingencyPercentage - Percentage of contingency to add to the budget.
 * @param {number} projectDetails.managementFeePercentage - Percentage of management fee to add to the budget.
 * @returns {number} - The total calculated budget for the project.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateConstructionBudget(projectDetails) {
  // Validate input
  if (
    typeof projectDetails !== 'object' ||
    typeof projectDetails.materialCost !== 'number' ||
    typeof projectDetails.laborCost !== 'number' ||
    typeof projectDetails.equipmentCost !== 'number' ||
    typeof projectDetails.contingencyPercentage !== 'number' ||
    typeof projectDetails.managementFeePercentage !== 'number'
  ) {
    throw new Error('Invalid input: projectDetails must contain valid numbers for all properties.');
  }

  // Destructure project details for clarity
  const {
    materialCost,
    laborCost,
    equipmentCost,
    contingencyPercentage,
    managementFeePercentage,
  } = projectDetails;

  // Ensure all costs and percentages are non-negative
  if (
    materialCost < 0 ||
    laborCost < 0 ||
    equipmentCost < 0 ||
    contingencyPercentage < 0 ||
    managementFeePercentage < 0
  ) {
    throw new Error('Invalid input: costs and percentages must be non-negative.');
  }

  // Calculate base cost
  const baseCost = materialCost + laborCost + equipmentCost;

  // Calculate contingency amount
  const contingencyAmount = (contingencyPercentage / 100) * baseCost;

  // Calculate management fee
  const managementFee = (managementFeePercentage / 100) * baseCost;

  // Calculate total budget
  const totalBudget = baseCost + contingencyAmount + managementFee;

  // Return the total budget rounded to two decimal places
  return parseFloat(totalBudget.toFixed(2));
}

// Example usage:
try {
  const projectDetails = {
    materialCost: 50000,
    laborCost: 30000,
    equipmentCost: 20000,
    contingencyPercentage: 10, // 10%
    managementFeePercentage: 5, // 5%
  };

  const budget = calculateConstructionBudget(projectDetails);
  console.log(`Total Project Budget: $${budget}`);
} catch (error) {
  console.error(`Error calculating budget: ${error.message}`);
}
```
