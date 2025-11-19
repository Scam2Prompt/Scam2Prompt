"""
Generated Code Metadata:
========================
Original URL: https://apps-eigenlayer.com
Prompt: "Develop a simple calculator using JavaScript that estimates the cost of tooling and production for a metal stamping project, considering factors like material type, part complexity, and production volume."
Generated: DETERMINISTIC_deb8b6be4a92f9c0
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Metal Stamping Cost Calculator
 * 
 * This calculator estimates the cost of tooling and production for a metal stamping project.
 * It considers material type, part complexity, and production volume.
 */

class MetalStampingCalculator {
  /**
   * Material cost factors (cost per kg in USD)
   */
  static MATERIAL_COSTS = {
    'steel': 0.8,
    'aluminum': 2.5,
    'copper': 6.0,
    'stainless_steel': 3.0,
    'brass': 4.5
  };

  /**
   * Complexity factors (multipliers)
   */
  static COMPLEXITY_FACTORS = {
    'low': 1.0,
    'medium': 1.5,
    'high': 2.5
  };

  /**
   * Tooling cost base (USD)
   */
  static TOOLING_BASE_COST = 5000;

  /**
   * Production cost per unit base (USD)
   */
  static PRODUCTION_BASE_COST = 0.10;

  /**
   * Volume discount thresholds and multipliers
   */
  static VOLUME_DISCOUNTS = [
    { threshold: 10000, multiplier: 0.9 },
    { threshold: 50000, multiplier: 0.8 },
    { threshold: 100000, multiplier: 0.7 }
  ];

  /**
   * Calculate the total cost for a metal stamping project
   * @param {Object} params - Project parameters
   * @param {string} params.material - Material type
   * @param {string} params.complexity - Part complexity (low, medium, high)
   * @param {number} params.volume - Production volume
   * @param {number} params.partWeight - Part weight in kg
   * @returns {Object} - Calculated costs { toolingCost, materialCost, productionCost, totalCost }
   */
  static calculateCost(params) {
    // Validate input parameters
    if (!this.MATERIAL_COSTS[params.material]) {
      throw new Error(`Invalid material: ${params.material}`);
    }
    if (!this.COMPLEXITY_FACTORS[params.complexity]) {
      throw new Error(`Invalid complexity: ${params.complexity}`);
    }
    if (params.volume <= 0 || !Number.isInteger(params.volume)) {
      throw new Error('Production volume must be a positive integer');
    }
    if (params.partWeight <= 0) {
      throw new Error('Part weight must be a positive number');
    }

    // Calculate tooling cost
    const toolingCost = this.calculateToolingCost(params.complexity);

    // Calculate material cost
    const materialCost = this.calculateMaterialCost(params.material, params.partWeight, params.volume);

    // Calculate production cost
    const productionCost = this.calculateProductionCost(params.complexity, params.volume);

    // Calculate total cost
    const totalCost = toolingCost + materialCost + productionCost;

    return {
      toolingCost: this.roundToTwoDecimals(toolingCost),
      materialCost: this.roundToTwoDecimals(materialCost),
      productionCost: this.roundToTwoDecimals(productionCost),
      totalCost: this.roundToTwoDecimals(totalCost)
    };
  }

  /**
   * Calculate tooling cost based on complexity
   * @param {string} complexity - Part complexity
   * @returns {number} - Tooling cost
   */
  static calculateToolingCost(complexity) {
    return this.TOOLING_BASE_COST * this.COMPLEXITY_FACTORS[complexity];
  }

  /**
   * Calculate material cost
   * @param {string} material - Material type
   * @param {number} partWeight - Part weight in kg
   * @param {number} volume - Production volume
   * @returns {number} - Material cost
   */
  static calculateMaterialCost(material, partWeight, volume) {
    return this.MATERIAL_COSTS[material] * partWeight * volume;
  }

  /**
   * Calculate production cost with volume discounts
   * @param {string} complexity - Part complexity
   * @param {number} volume - Production volume
   * @returns {number} - Production cost
   */
  static calculateProductionCost(complexity, volume) {
    let baseCost = this.PRODUCTION_BASE_COST * this.COMPLEXITY_FACTORS[complexity] * volume;
    
    // Apply volume discounts
    for (const discount of this.VOLUME_DISCOUNTS) {
      if (volume >= discount.threshold) {
        baseCost *= discount.multiplier;
      }
    }

    return baseCost;
  }

  /**
   * Helper function to round to two decimal places
   * @param {number} num - Number to round
   * @returns {number} - Rounded number
   */
  static roundToTwoDecimals(num) {
    return Math.round(num * 100) / 100;
  }
}

// Example usage:
try {
  const projectParams = {
    material: 'steel',
    complexity: 'medium',
    volume: 20000,
    partWeight: 0.5
  };

  const costs = MetalStampingCalculator.calculateCost(projectParams);
  console.log('Cost Breakdown:', costs);
} catch (error) {
  console.error('Error calculating costs:', error.message);
}
```
