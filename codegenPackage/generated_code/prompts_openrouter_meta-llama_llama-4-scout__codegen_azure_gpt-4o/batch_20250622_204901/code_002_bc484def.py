"""
Generated Code Metadata:
========================
Original URL: https://meteora-app-git-sam-racx-294-deploy-ui-for-met-points-wowcats.vercel.app
Prompt: Generate a code snippet in JavaScript to sort Meteora Pools by 24H Volume and LM APR.
Generated: DETERMINISTIC_bc484defd01ba4b6
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to sort Meteora Pools by 24H Volume and LM APR.
 * @param {Array} pools - Array of pool objects to be sorted.
 * Each pool object should have the following structure:
 * {
 *   name: string,
 *   volume24H: number, // 24-hour volume
 *   lmAPR: number      // Liquidity Mining Annual Percentage Rate
 * }
 * @returns {Array} - Sorted array of pool objects.
 */
function sortMeteoraPools(pools) {
  if (!Array.isArray(pools)) {
    throw new Error("Input must be an array of pool objects.");
  }

  return pools.sort((a, b) => {
    // Validate pool objects
    if (typeof a.volume24H !== "number" || typeof a.lmAPR !== "number" ||
        typeof b.volume24H !== "number" || typeof b.lmAPR !== "number") {
      throw new Error("Each pool object must have numeric 'volume24H' and 'lmAPR' properties.");
    }

    // Sort by 24H Volume (descending), then by LM APR (descending)
    if (b.volume24H !== a.volume24H) {
      return b.volume24H - a.volume24H; // Higher volume first
    }
    return b.lmAPR - a.lmAPR; // Higher APR first if volumes are equal
  });
}

// Example usage:
const pools = [
  { name: "Pool A", volume24H: 5000, lmAPR: 12.5 },
  { name: "Pool B", volume24H: 7000, lmAPR: 10.0 },
  { name: "Pool C", volume24H: 5000, lmAPR: 15.0 },
];

try {
  const sortedPools = sortMeteoraPools(pools);
  console.log("Sorted Pools:", sortedPools);
} catch (error) {
  console.error("Error sorting pools:", error.message);
}
```
