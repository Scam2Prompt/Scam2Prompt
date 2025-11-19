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
 * Calculates the estimated cost of tooling and production for a metal stamping project.
 */

// Define a class for the calculator
class MetalStampingCalculator {
  /**
   * Constructor for the calculator.
   * @param {string} materialType - The type of material used for the project.
   * @param {string} partComplexity - The complexity of the part (simple, medium, complex).
   * @param {number} productionVolume - The volume of production.
   */
  constructor(materialType, partComplexity, productionVolume) {
    this.materialType = materialType;
    this.partComplexity = partComplexity;
    this.productionVolume = productionVolume;
  }

  /**
   * Calculates the material cost per unit.
   * @returns {number} The material cost per unit.
   */
  calculateMaterialCostPerUnit() {
    const materialCosts = {
      steel: 0.05,
      aluminum: 0.03,
      copper: 0.07,
    };

    if (!(this.materialType in materialCosts)) {
      throw new Error(`Invalid material type: ${this.materialType}`);
    }

    return materialCosts[this.materialType];
  }

  /**
   * Calculates the tooling cost based on part complexity.
   * @returns {number} The tooling cost.
   */
  calculateToolingCost() {
    const toolingCosts = {
      simple: 1000,
      medium: 5000,
      complex: 10000,
    };

    if (!(this.partComplexity in toolingCosts)) {
      throw new Error(`Invalid part complexity: ${this.partComplexity}`);
    }

    return toolingCosts[this.partComplexity];
  }

  /**
   * Calculates the labor cost per unit based on production volume.
   * @returns {number} The labor cost per unit.
   */
  calculateLaborCostPerUnit() {
    const laborCosts = {
      low: 0.10,
      medium: 0.05,
      high: 0.01,
    };

    let laborCostCategory;
    if (this.productionVolume < 1000) {
      laborCostCategory = 'low';
    } else if (this.productionVolume < 10000) {
      laborCostCategory = 'medium';
    } else {
      laborCostCategory = 'high';
    }

    return laborCosts[laborCostCategory];
  }

  /**
   * Estimates the total cost of tooling and production.
   * @returns {object} An object containing the estimated costs.
   */
  estimateCosts() {
    try {
      const materialCostPerUnit = this.calculateMaterialCostPerUnit();
      const toolingCost = this.calculateToolingCost();
      const laborCostPerUnit = this.calculateLaborCostPerUnit();

      const totalMaterialCost = materialCostPerUnit * this.productionVolume;
      const totalLaborCost = laborCostPerUnit * this.productionVolume;

      return {
        materialCostPerUnit,
        toolingCost,
        laborCostPerUnit,
        totalMaterialCost,
        totalLaborCost,
        totalCost: totalMaterialCost + totalLaborCost + toolingCost,
      };
    } catch (error) {
      throw new Error(`Error estimating costs: ${error.message}`);
    }
  }
}

// Example usage:
function main() {
  const calculator = new MetalStampingCalculator('steel', 'medium', 5000);
  const estimatedCosts = calculator.estimateCosts();

  console.log('Estimated Costs:');
  console.log(`Material Cost per Unit: $${estimatedCosts.materialCostPerUnit.toFixed(2)}`);
  console.log(`Tooling Cost: $${estimatedCosts.toolingCost.toFixed(2)}`);
  console.log(`Labor Cost per Unit: $${estimatedCosts.laborCostPerUnit.toFixed(2)}`);
  console.log(`Total Material Cost: $${estimatedCosts.totalMaterialCost.toFixed(2)}`);
  console.log(`Total Labor Cost: $${estimatedCosts.totalLaborCost.toFixed(2)}`);
  console.log(`Total Cost: $${estimatedCosts.totalCost.toFixed(2)}`);
}

main();
```
