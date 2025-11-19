"""
Generated Code Metadata:
========================
Original URL: https://filterwale.com
Prompt: Develop a function in JavaScript to calculate the discounted price of a Fleetguard Lube Oil Filter LF 9028 with a given discount percentage.
Generated: DETERMINISTIC_8bbd05f6a1714534
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the discounted price of a Fleetguard Lube Oil Filter LF 9028.
 * @param {number} originalPrice - The original price of the filter.
 * @param {number} discountPercentage - The discount percentage to be applied.
 * @returns {number} - The discounted price after applying the discount.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateDiscountedPrice(originalPrice, discountPercentage) {
  // Validate inputs
  if (typeof originalPrice !== 'number' || originalPrice <= 0) {
    throw new Error('Invalid original price. It must be a positive number.');
  }
  if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 100) {
    throw new Error('Invalid discount percentage. It must be a number between 0 and 100.');
  }

  // Calculate the discount amount
  const discountAmount = (originalPrice * discountPercentage) / 100;

  // Calculate the final discounted price
  const discountedPrice = originalPrice - discountAmount;

  // Return the discounted price rounded to two decimal places
  return parseFloat(discountedPrice.toFixed(2));
}

// Example usage:
try {
  const originalPrice = 100; // Example original price
  const discountPercentage = 15; // Example discount percentage
  const discountedPrice = calculateDiscountedPrice(originalPrice, discountPercentage);
  console.log(`The discounted price is: $${discountedPrice}`);
} catch (error) {
  console.error(error.message);
}
```
