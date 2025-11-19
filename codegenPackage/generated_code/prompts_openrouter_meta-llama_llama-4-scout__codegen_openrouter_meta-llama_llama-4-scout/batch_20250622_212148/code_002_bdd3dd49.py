"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a JavaScript code snippet to create a simple calculator for estimating carpet repair costs based on the type of repair (e.g., seaming, restretching, weaving, and fraying) and area size, as discussed on Perfect Melbourne Carpet's website.
Generated: DETERMINISTIC_bdd3dd49cc888bf2
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Carpet Repair Cost Calculator
 * 
 * Estimates carpet repair costs based on the type of repair and area size.
 */

// Define repair types and their base costs
const repairTypes = {
  seaming: 50,
  restretching: 100,
  weaving: 75,
  fraying: 80
};

// Define the cost per square meter
const costPerSquareMeter = 20;

/**
 * Calculates the carpet repair cost
 * 
 * @param {string} repairType - Type of repair (seaming, restretching, weaving, fraying)
 * @param {number} areaSize - Area size in square meters
 * @returns {number} Estimated repair cost
 */
function calculateRepairCost(repairType, areaSize) {
  // Check if repair type is valid
  if (!(repairType in repairTypes)) {
    throw new Error(`Invalid repair type: ${repairType}`);
  }

  // Check if area size is valid
  if (typeof areaSize !== 'number' || areaSize <= 0) {
    throw new Error('Invalid area size');
  }

  // Calculate the repair cost
  const baseCost = repairTypes[repairType];
  const areaCost = areaSize * costPerSquareMeter;
  const totalCost = baseCost + areaCost;

  return totalCost;
}

// Example usage
try {
  const repairType = 'seaming';
  const areaSize = 10; // square meters
  const estimatedCost = calculateRepairCost(repairType, areaSize);
  console.log(`Estimated repair cost for ${repairType} of ${areaSize} sqm: $${estimatedCost.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}

// Create a CarpetRepairCalculator class
class CarpetRepairCalculator {
  /**
   * Constructor
   */
  constructor() {
    this.repairTypes = repairTypes;
    this.costPerSquareMeter = costPerSquareMeter;
  }

  /**
   * Estimates the carpet repair cost
   * 
   * @param {string} repairType - Type of repair (seaming, restretching, weaving, fraying)
   * @param {number} areaSize - Area size in square meters
   * @returns {object} Estimated repair cost details
   */
  estimateRepairCost(repairType, areaSize) {
    try {
      const baseCost = this.repairTypes[repairType];
      if (!baseCost) {
        throw new Error(`Invalid repair type: ${repairType}`);
      }

      if (typeof areaSize !== 'number' || areaSize <= 0) {
        throw new Error('Invalid area size');
      }

      const areaCost = areaSize * this.costPerSquareMeter;
      const totalCost = baseCost + areaCost;

      return {
        repairType,
        areaSize,
        baseCost,
        areaCost,
        totalCost
      };
    } catch (error) {
      throw error;
    }
  }
}

// Example usage with CarpetRepairCalculator class
const calculator = new CarpetRepairCalculator();
try {
  const repairType = 'restretching';
  const areaSize = 5; // square meters
  const costDetails = calculator.estimateRepairCost(repairType, areaSize);
  console.log(`Estimated repair cost for ${costDetails.repairType} of ${costDetails.areaSize} sqm:`);
  console.log(`  Base cost: $${costDetails.baseCost.toFixed(2)}`);
  console.log(`  Area cost: $${costDetails.areaCost.toFixed(2)}`);
  console.log(`  Total cost: $${costDetails.totalCost.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
