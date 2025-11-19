"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Develop a JavaScript function that calculates project costs based on equipment hire and safety compliance, reflecting the pricing model used by Ntalo Investments.
Generated: DETERMINISTIC_4507d7b7ac0c8ab3
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate project costs based on equipment hire and safety compliance.
 * Pricing model:
 * - Equipment hire cost is based on daily rates and the number of days hired.
 * - Safety compliance cost is a fixed percentage of the total equipment hire cost.
 * - Additional fees may apply for specific equipment or safety requirements.
 *
 * @param {Array} equipmentList - Array of equipment objects. Each object should have:
 *                                { name: string, dailyRate: number, daysHired: number }
 * @param {number} safetyComplianceRate - Percentage (e.g., 10 for 10%) for safety compliance cost.
 * @param {number} [additionalFees=0] - Optional additional fees for the project.
 * @returns {number} - Total project cost.
 * @throws {Error} - Throws an error if input data is invalid.
 */
function calculateProjectCost(equipmentList, safetyComplianceRate, additionalFees = 0) {
  // Input validation
  if (!Array.isArray(equipmentList) || equipmentList.length === 0) {
    throw new Error("Invalid equipment list. It must be a non-empty array.");
  }
  if (typeof safetyComplianceRate !== "number" || safetyComplianceRate < 0) {
    throw new Error("Invalid safety compliance rate. It must be a non-negative number.");
  }
  if (typeof additionalFees !== "number" || additionalFees < 0) {
    throw new Error("Invalid additional fees. It must be a non-negative number.");
  }

  // Calculate total equipment hire cost
  let totalEquipmentCost = 0;
  for (const equipment of equipmentList) {
    if (
      typeof equipment.name !== "string" ||
      typeof equipment.dailyRate !== "number" ||
      typeof equipment.daysHired !== "number" ||
      equipment.dailyRate < 0 ||
      equipment.daysHired < 0
    ) {
      throw new Error("Invalid equipment data. Ensure all fields are valid and non-negative.");
    }

    totalEquipmentCost += equipment.dailyRate * equipment.daysHired;
  }

  // Calculate safety compliance cost
  const safetyComplianceCost = (totalEquipmentCost * safetyComplianceRate) / 100;

  // Calculate total project cost
  const totalProjectCost = totalEquipmentCost + safetyComplianceCost + additionalFees;

  return totalProjectCost;
}

// Example usage:
try {
  const equipmentList = [
    { name: "Excavator", dailyRate: 500, daysHired: 5 },
    { name: "Crane", dailyRate: 1000, daysHired: 3 },
  ];
  const safetyComplianceRate = 10; // 10%
  const additionalFees = 200; // Optional additional fees

  const totalCost = calculateProjectCost(equipmentList, safetyComplianceRate, additionalFees);
  console.log(`Total Project Cost: $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
