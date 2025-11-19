"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Develop a JavaScript function that calculates project costs based on equipment hire and safety compliance, reflecting the pricing model used by Ntalo Investments.
Generated: DETERMINISTIC_4507d7b7ac0c8ab3
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total project cost based on equipment hire and safety compliance.
 * 
 * Pricing Model:
 * - Each equipment item has a daily hire rate.
 * - Safety compliance costs are a percentage of the total equipment hire cost.
 * 
 * @param {Array} equipment - Array of equipment objects. Each object contains:
 *                            - name: {string} Name of the equipment
 *                            - dailyRate: {number} Cost per day for hiring the equipment
 *                            - days: {number} Number of days the equipment is hired
 * @param {number} safetyComplianceRate - Percentage (as a decimal) for safety compliance cost. Example: 0.1 for 10%
 * @returns {number} The total cost of the project.
 */
function calculateProjectCost(equipment, safetyComplianceRate) {
  try {
    // Validate inputs
    if (!Array.isArray(equipment)) {
      throw new Error('Invalid input: equipment should be an array');
    }
    if (typeof safetyComplianceRate !== 'number' || safetyComplianceRate < 0 || safetyComplianceRate > 1) {
      throw new Error('Invalid input: safetyComplianceRate should be a number between 0 and 1');
    }

    // Calculate total equipment hire cost
    let totalEquipmentCost = 0;
    equipment.forEach(item => {
      if (
        typeof item.dailyRate !== 'number' ||
        typeof item.days !== 'number' ||
        item.dailyRate < 0 ||
        item.days < 0
      ) {
        throw new Error(`Invalid equipment entry: ${JSON.stringify(item)}`);
      }
      totalEquipmentCost += item.dailyRate * item.days;
    });

    // Calculate safety compliance cost
    const safetyComplianceCost = totalEquipmentCost * safetyComplianceRate;

    // Calculate total project cost
    const totalProjectCost = totalEquipmentCost + safetyComplianceCost;

    // Return the formatted total cost
    return totalProjectCost;
  } catch (error) {
    console.error(`Error calculating project cost: ${error.message}`);
    return null; // Return null if an error occurs
  }
}

/** Example Usage */
const equipmentList = [
  { name: 'Excavator', dailyRate: 500, days: 3 },
  { name: 'Dump Truck', dailyRate: 300, days: 2 },
  { name: 'Safety Harness', dailyRate: 50, days: 5 }
];

const safetyComplianceRate = 0.15; // 15% of equipment hire cost

const totalCost = calculateProjectCost(equipmentList, safetyComplianceRate);
console.log(`Total Project Cost: $${totalCost}`);
```
