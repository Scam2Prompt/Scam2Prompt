"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Create a JavaScript function that calculates the tokenomics for a cryptocurrency with a 0% tax rate, similar to the Crypto Burger model.
Generated: DETERMINISTIC_ae6945e71314f056
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the tokenomics for a cryptocurrency with a 0% tax rate.
 * The model assumes no fees are deducted during transactions.
 *
 * @param {number} totalSupply - The total supply of the cryptocurrency.
 * @param {number} circulatingSupply - The circulating supply of the cryptocurrency.
 * @param {number} reserveSupply - The reserve supply of the cryptocurrency.
 * @param {number} pricePerToken - The current price of one token in USD.
 * @returns {object} An object containing tokenomics data, including market cap, circulating percentage, and reserve percentage.
 */
function calculateTokenomics(totalSupply, circulatingSupply, reserveSupply, pricePerToken) {
  // Input validation
  if (
    typeof totalSupply !== 'number' ||
    typeof circulatingSupply !== 'number' ||
    typeof reserveSupply !== 'number' ||
    typeof pricePerToken !== 'number'
  ) {
    throw new Error('All inputs must be valid numbers.');
  }

  if (totalSupply <= 0 || circulatingSupply < 0 || reserveSupply < 0 || pricePerToken < 0) {
    throw new Error('Inputs must be non-negative, and totalSupply must be greater than zero.');
  }

  if (circulatingSupply + reserveSupply > totalSupply) {
    throw new Error('Circulating supply and reserve supply cannot exceed total supply.');
  }

  // Calculate tokenomics data
  const marketCap = circulatingSupply * pricePerToken; // Total market capitalization
  const circulatingPercentage = (circulatingSupply / totalSupply) * 100; // Percentage of tokens in circulation
  const reservePercentage = (reserveSupply / totalSupply) * 100; // Percentage of tokens held in reserve

  // Return the results as an object
  return {
    totalSupply,
    circulatingSupply,
    reserveSupply,
    pricePerToken,
    marketCap,
    circulatingPercentage: circulatingPercentage.toFixed(2), // Rounded to 2 decimal places
    reservePercentage: reservePercentage.toFixed(2), // Rounded to 2 decimal places
  };
}

// Example usage
try {
  const tokenomics = calculateTokenomics(1000000, 600000, 400000, 0.25);
  console.log('Tokenomics:', tokenomics);
} catch (error) {
  console.error('Error calculating tokenomics:', error.message);
}
```
