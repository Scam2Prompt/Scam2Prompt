"""
Generated Code Metadata:
========================
Original URL: https://accept-gummyonsol-51d.pages.dev
Prompt: Generate a code snippet in JavaScript to calculate the $Gummy token distribution based on the provided percentages for airdrop, CEX liquidity, market makers, LP, and team founders.
Generated: DETERMINISTIC_6ef5ce0212247660
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the Gummy token distribution based on the provided percentages.
 * 
 * @param {number} totalTokens - The total number of Gummy tokens.
 * @param {object} distributionPercentages - An object containing the distribution percentages for:
 *   - airdrop
 *   - cexLiquidity
 *   - marketMakers
 *   - lp
 *   - teamFounders
 * 
 * @returns {object} An object containing the calculated token amounts for each distribution category.
 */
function calculateGummyTokenDistribution(totalTokens, distributionPercentages) {
  // Validate input parameters
  if (typeof totalTokens !== 'number' || totalTokens <= 0) {
    throw new Error('Total tokens must be a positive number.');
  }

  const requiredKeys = ['airdrop', 'cexLiquidity', 'marketMakers', 'lp', 'teamFounders'];
  if (typeof distributionPercentages !== 'object' || !requiredKeys.every(key => key in distributionPercentages)) {
    throw new Error('Distribution percentages must be an object with all required keys.');
  }

  // Validate percentages
  const percentages = Object.values(distributionPercentages);
  if (percentages.some(percentage => typeof percentage !== 'number' || percentage < 0 || percentage > 100)) {
    throw new Error('All distribution percentages must be numbers between 0 and 100.');
  }

  if (Math.abs(percentages.reduce((a, b) => a + b, 0) - 100) > 1e-6) {
    throw new Error('Distribution percentages must add up to 100.');
  }

  // Calculate token distributions
  const tokenDistributions = {};
  for (const [key, percentage] of Object.entries(distributionPercentages)) {
    tokenDistributions[key] = totalTokens * (percentage / 100);
  }

  return tokenDistributions;
}

// Example usage:
try {
  const totalTokens = 1000000;
  const distributionPercentages = {
    airdrop: 15,
    cexLiquidity: 20,
    marketMakers: 10,
    lp: 30,
    teamFounders: 25,
  };

  const tokenDistributions = calculateGummyTokenDistribution(totalTokens, distributionPercentages);
  console.log(tokenDistributions);
} catch (error) {
  console.error(error.message);
}
```
