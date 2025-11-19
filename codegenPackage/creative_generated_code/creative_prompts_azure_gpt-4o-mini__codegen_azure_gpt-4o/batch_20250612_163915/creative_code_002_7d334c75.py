"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minkycoin-claim.pages.dev
Prompt: Create a JavaScript function that calculates the total supply and tax rate for a meme coin like $MINKY, ensuring it reflects the unique characteristics mentioned on the site.
Generated: DETERMINISTIC_7d334c753f252405
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total supply and tax rate for a meme coin.
 * 
 * @param {number} baseSupply - The base supply of the coin (e.g., starting supply).
 * @param {number} mintRate - The percentage rate at which new coins are minted (e.g., 5% = 0.05).
 * @param {number} burnRate - The percentage rate at which coins are burned (e.g., 3% = 0.03).
 * @param {number} taxRate - The percentage tax rate on transactions (e.g., 2% = 0.02).
 * 
 * @returns {Object} An object containing the total supply and effective tax rate.
 */
function calculateMemeCoinStatistics(baseSupply, mintRate, burnRate, taxRate) {
  // Input validation for required parameters
  if (
    typeof baseSupply !== 'number' || baseSupply <= 0 ||
    typeof mintRate !== 'number' || mintRate < 0 ||
    typeof burnRate !== 'number' || burnRate < 0 ||
    typeof taxRate !== 'number' || taxRate < 0
  ) {
    throw new Error('Invalid input: all parameters must be positive numbers.');
  }

  // Calculating minted and burned amounts
  const mintedCoins = baseSupply * mintRate;
  const burnedCoins = baseSupply * burnRate;

  // Calculating the total supply after minting and burning
  const totalSupply = baseSupply + mintedCoins - burnedCoins;

  // Ensuring the tax rate is represented properly
  const effectiveTaxRate = taxRate;

  // Returning the results in an object
  return {
    totalSupply: totalSupply, // Total supply of the meme coin
    effectiveTaxRate: effectiveTaxRate // Effective tax rate for the coin
  };
}

// Example usage:
try {
  const baseSupply = 1000000; // Example base supply: 1,000,000 coins
  const mintRate = 0.05; // Mint rate: 5%
  const burnRate = 0.03; // Burn rate: 3%
  const taxRate = 0.02; // Tax rate: 2%

  const statistics = calculateMemeCoinStatistics(baseSupply, mintRate, burnRate, taxRate);
  console.log('Meme Coin Statistics:', statistics);
} catch (error) {
  console.error('Error calculating meme coin statistics:', error.message);
}
```
