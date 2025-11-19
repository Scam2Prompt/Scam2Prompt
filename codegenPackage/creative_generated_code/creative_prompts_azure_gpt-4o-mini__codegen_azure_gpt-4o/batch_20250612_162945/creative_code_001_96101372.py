"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write a JavaScript function that simulates the pricing algorithm used on medebooks.shop for calculating discounts on medical courses.
Generated: DETERMINISTIC_961013721b9e4d08
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the final price of a medical course after applying discounts.
 * The pricing algorithm applies:
 * - A percentage discount (if applicable)
 * - A fixed discount amount (if applicable)
 * - Ensures the price does not drop below a minimum threshold (e.g., $20)
 *
 * @param {number} basePrice - The original price of the course.
 * @param {Object} discountOptions - An object containing discount options.
 * @param {number} discountOptions.percentage - Percentage discount to apply (e.g., 10 for 10%).
 * @param {number} discountOptions.fixedAmount - Fixed discount amount to subtract (e.g., 15 for $15 off).
 * @param {number} minimumPrice - The minimum allowable final price for the course.
 * @returns {number} - The calculated final price after applying all discounts.
 * @throws {Error} - Throws an error if basePrice or discountOptions are invalid.
 */
function calculateCoursePrice(basePrice, discountOptions, minimumPrice = 20) {
  // Input validation
  if (typeof basePrice !== 'number' || basePrice <= 0) {
    throw new Error("Invalid base price. Must be a positive number.");
  }

  if (typeof discountOptions !== 'object' || discountOptions === null) {
    throw new Error("Invalid discount options. Must be a valid object.");
  }

  const { percentage = 0, fixedAmount = 0 } = discountOptions;

  if (typeof percentage !== 'number' || percentage < 0 || percentage > 100) {
    throw new Error("Invalid percentage discount. Must be between 0 and 100.");
  }

  if (typeof fixedAmount !== 'number' || fixedAmount < 0) {
    throw new Error("Invalid fixed discount. Must be a positive number.");
  }

  if (typeof minimumPrice !== 'number' || minimumPrice <= 0) {
    throw new Error("Invalid minimum price. Must be a positive number.");
  }

  // Apply percentage discount
  let discountedPrice = basePrice - (basePrice * (percentage / 100));

  // Apply fixed amount discount
  discountedPrice -= fixedAmount;

  // Ensure the price does not drop below the minimum threshold
  discountedPrice = Math.max(discountedPrice, minimumPrice);

  // Round to 2 decimal places for currency format
  return Math.round(discountedPrice * 100) / 100;
}

// Example usage:
try {
  const basePrice = 100; // Original course price: $100
  const discounts = { percentage: 10, fixedAmount: 15 }; // 10% off and $15 off
  const minimumPrice = 20; // Minimum allowable price: $20

  const finalPrice = calculateCoursePrice(basePrice, discounts, minimumPrice);
  console.log(`Final course price: $${finalPrice}`); // Expected output: Final course price: $20
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
