"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: Create a JavaScript function that calculates potential earnings from participating in CowSwap's Fair Sales.
Generated: DETERMINISTIC_d750b75e124401aa
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential earnings from CowSwap's Fair Sales.
 * @param {number} investmentAmount - The amount of money being invested.
 * @param {number} tokenPrice - The price of one token during the fair sale.
 * @param {number} estimatedMarketPrice - The estimated market price of one token after the fair sale.
 * @returns {number} - The potential earnings from the investment.
 */
function calculatePotentialEarnings(investmentAmount, tokenPrice, estimatedMarketPrice) {
  // Validate input parameters
  if (
    typeof investmentAmount !== 'number' ||
    typeof tokenPrice !== 'number' ||
    typeof estimatedMarketPrice !== 'number'
  ) {
    throw new Error('All inputs must be numbers.');
  }
  if (investmentAmount <= 0 || tokenPrice <= 0 || estimatedMarketPrice <= 0) {
    throw new Error('All inputs must be positive numbers.');
  }

  // Calculate the number of tokens purchased
  const tokensPurchased = investmentAmount / tokenPrice;

  // Calculate the total value of tokens at the estimated market price
  const totalMarketValue = tokensPurchased * estimatedMarketPrice;

  // Calculate potential earnings (profit)
  const potentialEarnings = totalMarketValue - investmentAmount;

  return potentialEarnings;
}

// Example Usage
try {
  const investment = 1000; // USD
  const fairSalePrice = 2; // USD per token
  const marketPrice = 5; // USD per token

  const earnings = calculatePotentialEarnings(investment, fairSalePrice, marketPrice);
  console.log(`Potential Earnings: $${earnings.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
