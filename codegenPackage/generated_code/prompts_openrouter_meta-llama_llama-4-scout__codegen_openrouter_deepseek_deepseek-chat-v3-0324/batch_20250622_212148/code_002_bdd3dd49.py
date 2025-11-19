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
 * Estimates cost based on repair type and area size
 */
class CarpetRepairCalculator {
  /**
   * Repair types and their cost per square meter
   * @type {Object}
   */
  static REPAIR_TYPES = {
    SEAMING: { name: 'Seaming', costPerSqm: 25 },
    RESTRETCHING: { name: 'Restretching', costPerSqm: 30 },
    WEAVING: { name: 'Weaving', costPerSqm: 45 },
    FRAYING: { name: 'Fraying Repair', costPerSqm: 35 }
  };

  /**
   * Minimum service charge for any repair
   * @type {number}
   */
  static MINIMUM_CHARGE = 50;

  /**
   * Calculate repair cost based on type and area
   * @param {string} repairType - Type of repair (key from REPAIR_TYPES)
   * @param {number} areaSqm - Area in square meters
   * @returns {number} Calculated cost
   * @throws {Error} If invalid parameters are provided
   */
  static calculateCost(repairType, areaSqm) {
    // Validate inputs
    if (!this.REPAIR_TYPES[repairType]) {
      throw new Error(`Invalid repair type. Valid types are: ${Object.keys(this.REPAIR_TYPES).join(', ')}`);
    }

    if (typeof areaSqm !== 'number' || areaSqm <= 0) {
      throw new Error('Area must be a positive number');
    }

    // Calculate cost
    const repairInfo = this.REPAIR_TYPES[repairType];
    const calculatedCost = repairInfo.costPerSqm * areaSqm;
    
    // Apply minimum charge if calculated cost is lower
    return Math.max(calculatedCost, this.MINIMUM_CHARGE);
  }

  /**
   * Get formatted cost estimate with details
   * @param {string} repairType - Type of repair
   * @param {number} areaSqm - Area in square meters
   * @returns {Object} Formatted result with cost and details
   */
  static getEstimate(repairType, areaSqm) {
    try {
      const cost = this.calculateCost(repairType, areaSqm);
      const repairInfo = this.REPAIR_TYPES[repairType];
      
      return {
        repairType: repairInfo.name,
        areaSqm: areaSqm,
        costPerSqm: repairInfo.costPerSqm,
        totalCost: cost,
        minimumChargeApplied: cost === this.MINIMUM_CHARGE && (repairInfo.costPerSqm * areaSqm) < this.MINIMUM_CHARGE
      };
    } catch (error) {
      return {
        error: error.message
      };
    }
  }
}

// Example usage:
// const estimate = CarpetRepairCalculator.getEstimate('SEAMING', 2);
// console.log(estimate);
```
