"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-befetoken.pages.dev
Prompt: Create a JavaScript function that calculates the distribution of BEFE tokens based on its total supply and airdrop percentage.
Generated: DETERMINISTIC_d5bb02cdadfa51e1
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the distribution of BEFE tokens based on total supply and airdrop percentage.
 *
 * @param {number} totalSupply - The total supply of BEFE tokens.
 * @param {number} airdropPercentage - The percentage of tokens to be airdropped (e.g., 20 for 20%).
 * @returns {Object} - An object containing the number of tokens for airdrop and the remainder supply.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateTokenDistribution(totalSupply, airdropPercentage) {
  // Validate input
  if (typeof totalSupply !== 'number' || totalSupply <= 0) {
    throw new Error('Invalid total supply: must be a positive number.');
  }
  if (typeof airdropPercentage !== 'number' || airdropPercentage <= 0 || airdropPercentage > 100) {
    throw new Error('Invalid airdrop percentage: must be a number between 1 and 100.');
  }

  // Calculate the number of tokens for airdrop
  const tokensForAirdrop = Math.floor((totalSupply * airdropPercentage) / 100);

  // Calculate the remainder supply
  const remainingSupply = totalSupply - tokensForAirdrop;

  // Return the results as an object
  return {
    airdropTokens: tokensForAirdrop,
    remainingTokens: remainingSupply,
  };
}

// Example usage:
try {
  const totalSupply = 1000000; // Example total supply
  const airdropPercentage = 20; // Example percentage for airdrop
  const distribution = calculateTokenDistribution(totalSupply, airdropPercentage);
  console.log('Token Distribution:', distribution);
  // Output: { airdropTokens: 200000, remainingTokens: 800000 }
} catch (error) {
  console.error('Error:', error.message);
}
```
