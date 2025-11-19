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
 * Calculates the depreciation of assets according to Peruvian tax laws and regulations.
 * 
 * @author [Your Name]
 */

// Define the depreciation rates according to Peruvian tax laws
const DEPRECIATION_RATES = {
  buildings: 0.05, // 5% for buildings
  machinery: 0.20, // 20% for machinery
  equipment: 0.20, // 20% for equipment
  vehicles: 0.20, // 20% for vehicles
  furniture: 0.10, // 10% for furniture
  other: 0.20, // 20% for other assets
};

/**
 * Calculates the depreciation of an asset.
 * 
 * @param {string} assetType - The type of asset (e.g., building, machinery, equipment, vehicle, furniture, other).
 * @param {number} assetValue - The initial value of the asset.
 * @param {number} years - The number of years to depreciate the asset.
 * @returns {number} The depreciated value of the asset.
 */
function calculateDepreciation(assetType, assetValue, years) {
  // Check if the asset type is valid
  if (!(assetType in DEPRECIATION_RATES)) {
    throw new Error(`Invalid asset type: ${assetType}. Please choose from: ${Object.keys(DEPRECIATION_RATES).join(', ')}`);
  }

  // Get the depreciation rate for the asset type
  const depreciationRate = DEPRECIATION_RATES[assetType];

  // Calculate the depreciated value using the straight-line method
  let depreciatedValue = assetValue * (1 - depreciationRate) ** years;

  // Ensure the depreciated value is not less than 0
  depreciatedValue = Math.max(depreciatedValue, 0);

  return depreciatedValue;
}

/**
 * Calculates the annual depreciation of an asset.
 * 
 * @param {string} assetType - The type of asset (e.g., building, machinery, equipment, vehicle, furniture, other).
 * @param {number} assetValue - The initial value of the asset.
 * @returns {number} The annual depreciation of the asset.
 */
function calculateAnnualDepreciation(assetType, assetValue) {
  // Check if the asset type is valid
  if (!(assetType in DEPRECIATION_RATES)) {
    throw new Error(`Invalid asset type: ${assetType}. Please choose from: ${Object.keys(DEPRECIATION_RATES).join(', ')}`);
  }

  // Get the depreciation rate for the asset type
  const depreciationRate = DEPRECIATION_RATES[assetType];

  // Calculate the annual depreciation
  const annualDepreciation = assetValue * depreciationRate;

  return annualDepreciation;
}

// Example usage:
try {
  const assetType = 'machinery';
  const assetValue = 10000;
  const years = 5;

  const depreciatedValue = calculateDepreciation(assetType, assetValue, years);
  const annualDepreciation = calculateAnnualDepreciation(assetType, assetValue);

  console.log(`Depreciated value of ${assetType} after ${years} years: ${depreciatedValue.toFixed(2)}`);
  console.log(`Annual depreciation of ${assetType}: ${annualDepreciation.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
