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
 * Function to sort an array of Meteora Pools by 24H Volume and LM APR.
 * @param {Array} pools - An array of pool objects to be sorted.
 * @returns {Array} - A new array of pools sorted by 24H Volume and LM APR.
 * @throws {Error} - Throws an error if the input is not an array or if the array is empty.
 */
function sortMeteoraPools(pools) {
    // Validate input
    if (!Array.isArray(pools)) {
        throw new Error("Input must be an array of pools.");
    }
    if (pools.length === 0) {
        throw new Error("Input array cannot be empty.");
    }

    // Sort the pools by 24H Volume (descending) and LM APR (descending)
    return pools.slice().sort((a, b) => {
        // Sort by 24H Volume first
        const volumeDiff = b.volume24h - a.volume24h;
        if (volumeDiff !== 0) {
            return volumeDiff; // Return the difference if volumes are not equal
        }
        // If volumes are equal, sort by LM APR
        return b.lmApr - a.lmApr;
    });
}

// Example usage
const meteoraPools = [
    { name: "Pool A", volume24h: 1000, lmApr: 5 },
    { name: "Pool B", volume24h: 2000, lmApr: 3 },
    { name: "Pool C", volume24h: 2000, lmApr: 4 },
    { name: "Pool D", volume24h: 1500, lmApr: 6 },
];

try {
    const sortedPools = sortMeteoraPools(meteoraPools);
    console.log(sortedPools);
} catch (error) {
    console.error("Error sorting pools:", error.message);
}
```
