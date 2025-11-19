"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cakco.com
Prompt: Create a JavaScript function to implement a discount feature for bags on an online store, inspired by the sales promotions mentioned on Cakco.com.
Generated: DETERMINISTIC_9499b98ea8a9ac6c
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the discounted price of a bag based on promotion rules.
 *
 * @param {number} originalPrice - The original price of the bag.
 * @param {number} discountPercentage - The discount percentage to be applied (0-100).
 * @returns {number} - The final price of the bag after applying the discount.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateDiscountedPrice(originalPrice, discountPercentage) {
  // Validate input
  if (typeof originalPrice !== 'number' || originalPrice <= 0) {
    throw new Error("Invalid original price. It must be a positive number.");
  }
  if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 100) {
    throw new Error("Invalid discount percentage. It must be a number between 0 and 100.");
  }

  // Calculate the discount amount
  const discountAmount = (originalPrice * discountPercentage) / 100;

  // Compute the final price
  const finalPrice = originalPrice - discountAmount;

  // Ensure final price is not negative
  if (finalPrice < 0) {
    throw new Error("Final price cannot be negative.");
  }

  return parseFloat(finalPrice.toFixed(2)); // Round to two decimal places for currency formatting
}

/**
 * Example usage of calculateDiscountedPrice function.
 * Uncomment the lines below to test the function.
 */

// try {
//   const originalPrice = 100; // $100
//   const discountPercentage = 20; // 20% discount
//   const discountedPrice = calculateDiscountedPrice(originalPrice, discountPercentage);
//   console.log(`Discounted Price: $${discountedPrice}`); // Expected output: Discounted Price: $80.00
// } catch (error) {
//   console.error(error.message);
// }
```
