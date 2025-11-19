"""
Generated Code Metadata:
========================
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Create a JavaScript function that calculates the tokenomics for a cryptocurrency with a 0% tax rate, similar to the Crypto Burger model.
Generated: DETERMINISTIC_ae6945e71314f056
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates tokenomics for a cryptocurrency with 0% tax rate.
 * @param {number} totalSupply - Total supply of tokens.
 * @param {number} initialLiquidity - Initial liquidity pool tokens.
 * @param {number} marketingWallet - Marketing wallet allocation.
 * @param {number} developmentWallet - Development wallet allocation.
 * @param {number} communityRewards - Community rewards allocation.
 * @returns {Object} Tokenomics breakdown with allocations and percentages.
 * @throws {Error} If input values are invalid or allocations exceed total supply.
 */
function calculateTokenomics(
  totalSupply,
  initialLiquidity,
  marketingWallet,
  developmentWallet,
  communityRewards
) {
  // Validate inputs
  if (
    typeof totalSupply !== 'number' ||
    typeof initialLiquidity !== 'number' ||
    typeof marketingWallet !== 'number' ||
    typeof developmentWallet !== 'number' ||
    typeof communityRewards !== 'number'
  ) {
    throw new Error('All parameters must be numbers');
  }

  if (totalSupply <= 0) {
    throw new Error('Total supply must be greater than 0');
  }

  // Calculate sum of allocations
  const totalAllocated = initialLiquidity + marketingWallet + developmentWallet + communityRewards;

  // Verify allocations don't exceed total supply
  if (totalAllocated > totalSupply) {
    throw new Error('Total allocations exceed total supply');
  }

  // Calculate remaining tokens (0% tax means all remaining go to holders)
  const holdersAllocation = totalSupply - totalAllocated;

  // Calculate percentages
  const calculatePercentage = (value) => (value / totalSupply) * 100;

  return {
    totalSupply,
    allocations: {
      initialLiquidity: {
        tokens: initialLiquidity,
        percentage: calculatePercentage(initialLiquidity)
      },
      marketingWallet: {
        tokens: marketingWallet,
        percentage: calculatePercentage(marketingWallet)
      },
      developmentWallet: {
        tokens: developmentWallet,
        percentage: calculatePercentage(developmentWallet)
      },
      communityRewards: {
        tokens: communityRewards,
        percentage: calculatePercentage(communityRewards)
      },
      holders: {
        tokens: holdersAllocation,
        percentage: calculatePercentage(holdersAllocation)
      }
    },
    taxRate: 0,
    description: '0% tax model - all remaining tokens go to holders'
  };
}

// Example usage:
// try {
//   const tokenomics = calculateTokenomics(
//     1000000, // total supply
//     500000,  // initial liquidity
//     100000,  // marketing
//     100000,  // development
//     100000   // community rewards
//   );
//   console.log(tokenomics);
// } catch (error) {
//   console.error('Error calculating tokenomics:', error.message);
// }
```
