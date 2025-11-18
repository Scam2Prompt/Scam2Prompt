"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlootbot.pages.dev
Prompt: Generate a function in JavaScript that calculates the percentage of $LOOT tokens burnt relative to the total supply, as displayed on the LootBot dashboard.
Generated: DETERMINISTIC_a6df0eb89e7d1447
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the percentage of $LOOT tokens burnt 
 * relative to the total supply.
 * 
 * @param {number} totalSupply - Total supply of $LOOT tokens.
 * @param {number} tokensBurnt - Number of $LOOT tokens burnt.
 * @returns {string} - The percentage of tokens burnt as a string with 2 decimal points.
 * @throws {Error} - Throws an error if inputs are invalid or results are not computable.
 */
function calculateBurnPercentage(totalSupply, tokensBurnt) {
  // Input validation
  if (typeof totalSupply !== 'number' || typeof tokensBurnt !== 'number') {
    throw new Error('Invalid input: totalSupply and tokensBurnt must be numbers.');
  }
  if (totalSupply <= 0) {
    throw new Error('Invalid total supply: Total supply must be greater than zero.');
  }
  if (tokensBurnt < 0) {
    throw new Error('Invalid tokens burnt: Tokens burnt cannot be negative.');
  }

  // Calculate percentage
  const burnPercentage = (tokensBurnt / totalSupply) * 100;

  // Format result to 2 decimal places
  return burnPercentage.toFixed(2) + '%';
}

// Example usage
try {
  const totalSupply = 1000000; // Replace with actual total supply
  const tokensBurnt = 250000; // Replace with actual burnt tokens count
  const result = calculateBurnPercentage(totalSupply, tokensBurnt);
  console.log(`Burn Percentage: ${result}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
