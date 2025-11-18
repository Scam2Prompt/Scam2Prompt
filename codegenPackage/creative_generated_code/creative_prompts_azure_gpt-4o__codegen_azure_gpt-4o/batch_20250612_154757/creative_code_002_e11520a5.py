"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbull.io
Prompt: Develop a function in JavaScript to calculate the weighted Bitcoin airdrop amount for $BTCBULL holders based on their Community Sale purchase, as outlined on the BTC Bull site.
Generated: DETERMINISTIC_e11520a566e7ddc2
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate weighted Bitcoin airdrop amount for $BTCBULL holders.
 * 
 * @param {number} purchaseAmount - The amount of $BTCBULL tokens purchased during the Community Sale.
 * @param {number} totalSale - The total amount of $BTCBULL tokens sold during the Community Sale.
 * @param {number} totalAirdrop - The total amount of Bitcoin allocated for the airdrop.
 * @returns {number} - The weighted Bitcoin airdrop amount for the holder.
 * 
 * Usage:
 *   const airdropAmount = calculateAirdrop(500, 10000, 2);
 *   console.log(airdropAmount); // Output: 0.1 (BTC)
 */
function calculateAirdrop(purchaseAmount, totalSale, totalAirdrop) {
  try {
    // Input validation
    if (typeof purchaseAmount !== 'number' || purchaseAmount < 0) {
      throw new Error('Purchase amount must be a positive number.');
    }
    if (typeof totalSale !== 'number' || totalSale <= 0) {
      throw new Error('Total sale amount must be a positive number greater than zero.');
    }
    if (typeof totalAirdrop !== 'number' || totalAirdrop <= 0) {
      throw new Error('Total airdrop amount must be a positive number greater than zero.');
    }

    // Calculate weighted airdrop amount
    const airdropAmount = (purchaseAmount / totalSale) * totalAirdrop;

    // Return the result rounded to 8 decimal places (standard for Bitcoin)
    return parseFloat(airdropAmount.toFixed(8));
  } catch (error) {
    // Log the error and return 0 as a fallback
    console.error(`Error calculating airdrop: ${error.message}`);
    return 0;
  }
}

// Example usage:
const exampleAirdrop = calculateAirdrop(500, 10000, 2);
console.log(`Weighted Bitcoin Airdrop Amount: ${exampleAirdrop} BTC`);
```
