"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Develop a simple calculator in JavaScript to determine the depreciation of assets according to Peruvian tax laws and regulations."
Generated: DETERMINISTIC_44a36de3f2cda031
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Depreciation Calculator for Peruvian Tax Laws
 * 
 * This calculator determines the depreciation of assets based on Peruvian tax regulations.
 * Peruvian tax law typically uses the straight-line depreciation method.
 * 
 * Assumptions:
 * - The user provides the asset's initial value, useful life (in years), and salvage value.
 * - The calculator computes annual depreciation and total depreciation over the useful life.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

class DepreciationCalculator {
  /**
   * Calculate annual depreciation using the straight-line method.
   * @param {number} initialValue - The initial value of the asset.
   * @param {number} salvageValue - The residual value of the asset at the end of its useful life.
   * @param {number} usefulLife - The useful life of the asset in years.
   * @returns {number} - Annual depreciation amount.
   */
  static calculateAnnualDepreciation(initialValue, salvageValue, usefulLife) {
    if (usefulLife <= 0) {
      throw new Error("Useful life must be greater than zero.");
    }
    return (initialValue - salvageValue) / usefulLife;
  }

  /**
   * Calculate total depreciation over the useful life of the asset.
   * @param {number} initialValue - The initial value of the asset.
   * @param {number} salvageValue - The residual value of the asset at the end of its useful life.
   * @returns {number} - Total depreciation amount.
   */
  static calculateTotalDepreciation(initialValue, salvageValue) {
    if (initialValue < salvageValue) {
      throw new Error("Initial value must be greater than or equal to salvage value.");
    }
    return initialValue - salvageValue;
  }
}

// Example usage
try {
  const initialValue = 10000; // Asset's initial value in Peruvian Soles (PEN)
  const salvageValue = 1000; // Residual value in Peruvian Soles (PEN)
  const usefulLife = 5; // Useful life in years

  const annualDepreciation = DepreciationCalculator.calculateAnnualDepreciation(
    initialValue,
    salvageValue,
    usefulLife
  );
  const totalDepreciation = DepreciationCalculator.calculateTotalDepreciation(
    initialValue,
    salvageValue
  );

  console.log(`Annual Depreciation: PEN ${annualDepreciation.toFixed(2)}`);
  console.log(`Total Depreciation: PEN ${totalDepreciation.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
