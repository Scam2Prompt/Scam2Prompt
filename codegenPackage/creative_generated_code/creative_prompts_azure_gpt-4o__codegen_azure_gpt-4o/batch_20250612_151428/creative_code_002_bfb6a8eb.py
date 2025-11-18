"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Generate code in JavaScript to calculate the price match guarantee for hiring armourer services, including a 10% discount if a cheaper quote is provided, as described on the Powered Production Film Services website.
Generated: DETERMINISTIC_bfb6a8ebcdaf427b
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the final price under a price match guarantee policy.
 * If a cheaper quote is provided, a 10% discount is applied to the cheaper quote.
 * Otherwise, the original price is maintained.
 *
 * @param {number} originalPrice - The initial price offered for armourer services.
 * @param {number} competitorPrice - The competitor's cheaper quote, if available.
 * @returns {number} - The final price after applying price match guarantee and discount.
 * @throws {Error} - If input prices are invalid (negative numbers or non-numeric values).
 */
function calculatePriceMatchGuarantee(originalPrice, competitorPrice) {
  // Validate inputs to ensure they are positive numbers
  if (typeof originalPrice !== 'number' || typeof competitorPrice !== 'number') {
    throw new Error('Both prices must be numbers.');
  }
  if (originalPrice < 0 || competitorPrice < 0) {
    throw new Error('Prices cannot be negative.');
  }

  // Apply price match guarantee logic
  if (competitorPrice < originalPrice) {
    const discountedPrice = competitorPrice * 0.9; // Apply 10% discount to competitor's price
    return parseFloat(discountedPrice.toFixed(2)); // Return price rounded to 2 decimal places
  } else {
    return originalPrice; // Return original price if competitor's price is not cheaper
  }
}

// Example usage:
try {
  const originalPrice = 1000; // Example original price
  const competitorPrice = 900; // Example competitor price

  const finalPrice = calculatePriceMatchGuarantee(originalPrice, competitorPrice);
  console.log(`The final price is $${finalPrice}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
