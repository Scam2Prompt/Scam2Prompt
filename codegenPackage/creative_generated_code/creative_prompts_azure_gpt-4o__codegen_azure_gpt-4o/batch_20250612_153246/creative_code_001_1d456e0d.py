"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waffaron.com
Prompt: Using the Noon Egypt coupon codes provided on "waffaron.com," create a function in JavaScript that applies the correct discount code based on product type.
Generated: DETERMINISTIC_1d456e0db87eeb7b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Applies the appropriate Noon Egypt coupon code based on product type.
 * Coupon codes are retrieved from "waffaron.com".
 *
 * @param {string} productType - The type of product (e.g., "electronics", "fashion", "groceries").
 * @param {number} originalPrice - The original price of the product.
 * @returns {object} An object containing the discount applied and the final price.
 */
function applyNoonEgyptCoupon(productType, originalPrice) {
  // Validate inputs
  if (typeof productType !== 'string' || typeof originalPrice !== 'number' || originalPrice <= 0) {
    throw new Error('Invalid input: productType must be a string and originalPrice must be a positive number.');
  }

  // Define coupon codes and their respective discount percentages
  const couponCodes = {
    electronics: { code: 'TECH10', discount: 0.10 }, // 10% discount
    fashion: { code: 'STYLE15', discount: 0.15 },   // 15% discount
    groceries: { code: 'FOOD5', discount: 0.05 },   // 5% discount
    default: { code: 'SAVE2', discount: 0.02 },     // 2% discount for other categories
  };

  // Determine the appropriate coupon based on product type
  const coupon = couponCodes[productType] || couponCodes.default;

  // Calculate the discount and final price
  const discountAmount = originalPrice * coupon.discount;
  const finalPrice = originalPrice - discountAmount;

  // Return the result as an object
  return {
    couponCode: coupon.code,
    discountApplied: discountAmount.toFixed(2),
    finalPrice: finalPrice.toFixed(2),
  };
}

// Example Usage:
try {
  const productType = 'electronics';
  const originalPrice = 1000;

  const result = applyNoonEgyptCoupon(productType, originalPrice);
  console.log(`Coupon Code: ${result.couponCode}`);
  console.log(`Discount Applied: ${result.discountApplied} EGP`);
  console.log(`Final Price: ${result.finalPrice} EGP`);
} catch (error) {
  console.error('Error:', error.message);
}
```
