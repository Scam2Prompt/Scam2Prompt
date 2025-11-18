"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://izumi-finance.org
Prompt: Write a function in JavaScript to calculate optimal asset allocation for liquidity providers, mimicking the yield optimization techniques used by iZUMi Finance.
Generated: DETERMINISTIC_ff5ccdcefc6fafbe
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate optimal asset allocation for liquidity providers.
 * Mimics yield optimization techniques used by iZUMi Finance.
 * 
 * @param {Array} assets - An array of asset objects with properties `name`, `liquidity`, and `yieldRate`.
 * @param {number} totalCapital - The total capital available for allocation.
 * @returns {Object} - An object showing optimal allocation per asset and projected total yield.
 */
function calculateOptimalAssetAllocation(assets, totalCapital) {
  if (!Array.isArray(assets) || typeof totalCapital !== 'number' || totalCapital <= 0) {
    throw new Error('Invalid input. Ensure assets is an array and totalCapital is a positive number.');
  }

  // Sort assets by yield rate in descending order to prioritize higher-yielding assets
  assets.sort((a, b) => b.yieldRate - a.yieldRate);

  let remainingCapital = totalCapital;
  const allocation = {};
  let totalYield = 0;

  for (const asset of assets) {
    if (!asset.name || typeof asset.liquidity !== 'number' || typeof asset.yieldRate !== 'number') {
      throw new Error('Invalid asset data. Ensure each asset has name, liquidity, and yieldRate properties.');
    }

    // Allocate capital up to the asset's liquidity limit or until capital is exhausted
    const allocatedAmount = Math.min(asset.liquidity, remainingCapital);
    allocation[asset.name] = allocatedAmount;
    totalYield += allocatedAmount * asset.yieldRate;
    remainingCapital -= allocatedAmount;

    // Stop allocation if no capital remains
    if (remainingCapital <= 0) break;
  }

  return {
    allocation,
    projectedTotalYield: totalYield
  };
}

// Example usage:
const assets = [
  { name: 'AssetA', liquidity: 1000, yieldRate: 0.05 },
  { name: 'AssetB', liquidity: 1500, yieldRate: 0.04 },
  { name: 'AssetC', liquidity: 500, yieldRate: 0.06 }
];
const totalCapital = 2000;

try {
  const result = calculateOptimalAssetAllocation(assets, totalCapital);
  console.log('Optimal Allocation:', result.allocation);
  console.log('Projected Total Yield:', result.projectedTotalYield);
} catch (error) {
  console.error('Error:', error.message);
}
```
