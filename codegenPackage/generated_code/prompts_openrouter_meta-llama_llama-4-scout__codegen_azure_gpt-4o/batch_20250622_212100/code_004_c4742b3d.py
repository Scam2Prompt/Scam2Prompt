"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: "Write a JavaScript function to implement a discount calculator for Móveis Campo Largo's products, applying a 10% discount for purchases made online."
Generated: DETERMINISTIC_c4742b3daf167416
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Discount Calculator for Móveis Campo Largo's products.
 * Applies a 10% discount for purchases made online.
 *
 * @param {number} originalPrice - The original price of the product.
 * @param {boolean} isOnlinePurchase - Indicates if the purchase is made online.
 * @returns {number} - The final price after applying the discount (if applicable).
 * @throws {Error} - Throws an error if the original price is invalid.
 */
function calculateDiscount(originalPrice, isOnlinePurchase) {
  // Validate the original price
  if (typeof originalPrice !== 'number' || originalPrice < 0) {
    throw new Error('Invalid original price. It must be a positive number.');
  }

  // Validate the isOnlinePurchase flag
  if (typeof isOnlinePurchase !== 'boolean') {
    throw new Error('Invalid isOnlinePurchase flag. It must be a boolean value.');
  }

  // Apply a 10% discount for online purchases
  const discountRate = 0.10;
  const finalPrice = isOnlinePurchase
    ? originalPrice * (1 - discountRate)
    : originalPrice;

  // Return the final price rounded to two decimal places
  return parseFloat(finalPrice.toFixed(2));
}

// Example usage:
try {
  const originalPrice = 100.0; // Example original price
  const isOnlinePurchase = true; // Example purchase type
  const finalPrice = calculateDiscount(originalPrice, isOnlinePurchase);
  console.log(`Final Price: $${finalPrice}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
