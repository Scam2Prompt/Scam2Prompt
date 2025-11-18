"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-feature-vercel-audience-419labs.vercel.app
Prompt: Write a function in JavaScript to list all mainnet dApps available in the StarkNet Ecosystem, filtering by specific categories or tags.
Generated: DETERMINISTIC_a9df05d13e7cb7c8
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to list all mainnet dApps available in the StarkNet Ecosystem.
 * Filters the dApps by specific categories or tags.
 *
 * @param {Array<Object>} dApps - Array of dApp objects containing metadata (e.g., name, category, tags).
 * @param {Object} filter - Filter criteria with `category` and/or `tags`.
 * @param {string} filter.category - Category to filter by (optional).
 * @param {Array<string>} filter.tags - Tags to filter by (optional).
 * @returns {Array<Object>} - List of dApps matching the filter criteria.
 */
function listMainnetDApps(dApps, filter = {}) {
  try {
    // Input validation
    if (!Array.isArray(dApps)) {
      throw new Error("Invalid input: dApps must be an array.");
    }
    if (typeof filter !== 'object') {
      throw new Error("Invalid input: filter must be an object.");
    }

    const { category, tags } = filter;

    // Validate filter inputs
    if (category && typeof category !== 'string') {
      throw new Error("Invalid filter: category must be a string.");
    }
    if (tags && (!Array.isArray(tags) || !tags.every(tag => typeof tag === 'string'))) {
      throw new Error("Invalid filter: tags must be an array of strings.");
    }

    // Filter dApps based on category and tags
    return dApps.filter(dApp => {
      // Ensure the dApp is mainnet
      if (dApp.network !== 'mainnet') {
        return false;
      }

      // Filter by category if provided
      const matchesCategory = category ? dApp.category === category : true;

      // Filter by tags if provided
      const matchesTags = tags
        ? tags.every(tag => dApp.tags && dApp.tags.includes(tag))
        : true;

      return matchesCategory && matchesTags;
    });
  } catch (error) {
    // Log error details for debugging purposes
    console.error("Error in listMainnetDApps:", error.message);
    // Return an empty array in case of error
    return [];
  }
}

// Example usage:
// Array of dApps in StarkNet Ecosystem
const starkNetDApps = [
  { name: "dApp1", network: "mainnet", category: "DeFi", tags: ["staking", "yield"] },
  { name: "dApp2", network: "testnet", category: "Gaming", tags: ["NFT", "play-to-earn"] },
  { name: "dApp3", network: "mainnet", category: "Gaming", tags: ["NFT"] },
  { name: "dApp4", network: "mainnet", category: "DeFi", tags: ["liquidity"] }
];

// Filter criteria
const filterCriteria = { category: "DeFi", tags: ["staking"] };

// Fetch mainnet dApps matching the filter criteria
const filteredDApps = listMainnetDApps(starkNetDApps, filterCriteria);
console.log("Filtered dApps:", filteredDApps);
```
