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
 * Function to calculate $Gummy token distribution based on provided percentages.
 * @param {number} totalSupply - The total supply of $Gummy tokens.
 * @param {object} percentages - An object containing the distribution percentages.
 * @returns {object} - An object with the calculated token distribution.
 * @throws {Error} - Throws an error if percentages do not add up to 100 or if inputs are invalid.
 */
function calculateTokenDistribution(totalSupply, percentages) {
  // Validate inputs
  if (typeof totalSupply !== 'number' || totalSupply <= 0) {
    throw new Error("Invalid total supply. Must be a positive number.");
  }

  if (typeof percentages !== 'object' || percentages === null) {
    throw new Error("Invalid percentages. Must be a non-null object.");
  }

  const { airdrop, cexLiquidity, marketMakers, lp, teamFounders } = percentages;

  // Ensure all percentages are numbers and add up to 100
  const totalPercentage = airdrop + cexLiquidity + marketMakers + lp + teamFounders;
  if (
    [airdrop, cexLiquidity, marketMakers, lp, teamFounders].some(
      (value) => typeof value !== 'number' || value < 0
    )
  ) {
    throw new Error("All percentage values must be non-negative numbers.");
  }

  if (totalPercentage !== 100) {
    throw new Error("Percentages must add up to 100.");
  }

  // Calculate token distribution
  const distribution = {
    airdrop: (totalSupply * airdrop) / 100,
    cexLiquidity: (totalSupply * cexLiquidity) / 100,
    marketMakers: (totalSupply * marketMakers) / 100,
    lp: (totalSupply * lp) / 100,
    teamFounders: (totalSupply * teamFounders) / 100,
  };

  return distribution;
}

// Example usage:
try {
  const totalSupply = 1000000; // Total supply of $Gummy tokens
  const percentages = {
    airdrop: 20,        // 20% for airdrop
    cexLiquidity: 30,   // 30% for CEX liquidity
    marketMakers: 25,   // 25% for market makers
    lp: 15,             // 15% for liquidity pool
    teamFounders: 10,   // 10% for team founders
  };

  const distribution = calculateTokenDistribution(totalSupply, percentages);
  console.log("Token Distribution:", distribution);
} catch (error) {
  console.error("Error calculating token distribution:", error.message);
}
```
